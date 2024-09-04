import os
import time
from pathlib import Path

import modal
from fastapi.responses import StreamingResponse

from .common import VOLUME_CONFIG, Colors, app, vllm_image

INFERENCE_GPU_CONFIG = os.environ.get('INFERENCE_GPU_CONFIG', 'a10g:2')
if len(INFERENCE_GPU_CONFIG.split(':')) <= 1:
    N_INFERENCE_GPUS = int(os.environ.get('N_INFERENCE_GPUS', 2))
    INFERENCE_GPU_CONFIG = f'{INFERENCE_GPU_CONFIG}:{N_INFERENCE_GPUS}'
else:
    N_INFERENCE_GPUS = int(INFERENCE_GPU_CONFIG.split(':')[-1])


with vllm_image.imports():
    import yaml
    from vllm.engine.arg_utils import AsyncEngineArgs
    from vllm.engine.async_llm_engine import AsyncLLMEngine
    from vllm.sampling_params import SamplingParams
    from vllm.utils import random_uuid


def get_model_path_from_run(path: Path) -> Path:
    with (path / 'config.yml').open() as f:
        return path / yaml.safe_load(f.read())['output_dir'] / 'merged'  # type: ignore [no-any-return]


@app.cls(
    gpu=INFERENCE_GPU_CONFIG,
    image=vllm_image,
    volumes=VOLUME_CONFIG,
    allow_concurrent_inputs=30,
    keep_warm=0,  # Number of containers to keep running at all times
    container_idle_timeout=60,  # Keep containers alive for this many extra seconds TODO: set to 5
)
class Inference:
    def __init__(self, run_name: str = '', run_dir: str = '/runs') -> None:
        self.run_name = run_name
        self.run_dir = run_dir

    @modal.enter()
    def _on_container_start(self):
        if self.run_name:
            path = Path(self.run_dir) / self.run_name
            VOLUME_CONFIG[self.run_dir].reload()
            model_path = get_model_path_from_run(path)
        else:
            # Pick the last run automatically
            run_paths = list(Path(self.run_dir).iterdir())
            for path in sorted(run_paths, reverse=True):
                model_path = get_model_path_from_run(path)
                if model_path.exists():
                    break

        print(
            Colors.GREEN,
            Colors.BOLD,
            f'🧠: Initializing vLLM engine for model at {model_path}',
            Colors.END,
            sep='',
        )

        engine_args = AsyncEngineArgs(
            model=model_path,
            gpu_memory_utilization=0.95,
            tensor_parallel_size=N_INFERENCE_GPUS,
            disable_custom_all_reduce=True,  # brittle as of v0.5.0
        )
        self.engine = AsyncLLMEngine.from_engine_args(engine_args)

    async def _stream(
        self,
        input: str,
        *,
        frequency_penalty: float | None,
        repetition_penalty: float | None,
        temperature: float | None,
    ):
        if not input:
            return

        tokenizer = await self.engine.get_tokenizer()
        prompt = tokenizer.apply_chat_template(
            conversation=[{'role': 'user', 'content': input}],
            add_generation_prompt=True,
            tokenize=False,
        )

        # Set default values
        # https://openrouter.ai/models/meta-llama/llama-3.1-8b-instruct/parameters
        frequency_penalty = frequency_penalty if frequency_penalty is not None else 0.0
        repetition_penalty = repetition_penalty if repetition_penalty is not None else 1.0
        temperature = temperature if temperature is not None else 1.0

        sampling_params = SamplingParams(
            frequency_penalty=frequency_penalty,  # Penalty including the generated text so far (-2 to 2)
            repetition_penalty=repetition_penalty,  # Penalty including the prompt and generated text so far (0 to 2)
            temperature=temperature,  # Randomness of the sampling. Lower values make the model more deterministic.
            max_tokens=4095,
        )
        request_id = random_uuid()
        results_generator = self.engine.generate(inputs=prompt, sampling_params=sampling_params, request_id=request_id)

        t0 = time.time()
        index, tokens = 0, 0
        async for request_output in results_generator:
            if request_output.outputs[0].text and '\ufffd' == request_output.outputs[0].text[-1]:
                continue
            yield request_output.outputs[0].text[index:]
            index = len(request_output.outputs[0].text)

            # Token accounting
            new_tokens = len(request_output.outputs[0].token_ids)
            tokens = new_tokens

        throughput = tokens / (time.time() - t0)
        print(
            Colors.GREEN,
            Colors.BOLD,
            f'🧠: Effective throughput of {throughput:.2f} tok/s',
            Colors.END,
            sep='',
        )

    @modal.method()
    async def completion(
        self,
        input: str,
        *,
        frequency_penalty: float | None,
        repetition_penalty: float | None,
        temperature: float | None,
    ):
        async for text in self._stream(
            input,
            frequency_penalty=frequency_penalty,
            repetition_penalty=repetition_penalty,
            temperature=temperature,
        ):
            yield text

    @modal.method()
    async def non_streaming(
        self,
        input: str,
        *,
        frequency_penalty: float | None,
        repetition_penalty: float | None,
        temperature: float | None,
    ):
        output = [
            text
            async for text in self._stream(
                input,
                frequency_penalty=frequency_penalty,
                repetition_penalty=repetition_penalty,
                temperature=temperature,
            )
        ]
        return ''.join(output)

    @modal.web_endpoint()
    async def web(
        self,
        input: str,
        *,
        frequency_penalty: float | None,
        repetition_penalty: float | None,
        temperature: float | None,
    ):
        return StreamingResponse(
            self._stream(
                input,
                frequency_penalty=frequency_penalty,
                repetition_penalty=repetition_penalty,
                temperature=temperature,
            ),
            media_type='text/event-stream',
        )

    @modal.exit()
    def stop_engine(self):
        if N_INFERENCE_GPUS > 1:
            import ray

            ray.shutdown()

        # access private attribute to ensure graceful termination
        self.engine._background_loop_unshielded.cancel()


@app.local_entrypoint()
def inference_main(
    run_name: str = '',
    prompt: str = '',
    frequency_penalty: float | None = None,
    repetition_penalty: float | None = None,
    temperature: float | None = None,
):
    if not prompt:
        prompt = input('PROMPT:\n')

    response = ''
    for chunk in Inference(run_name).completion.remote_gen(
        prompt,
        frequency_penalty=frequency_penalty,
        repetition_penalty=repetition_penalty,
        temperature=temperature,
    ):
        response += chunk  # not streaming to avoid mixing with server logs

    print('\nINPUT:\n')
    print(Colors.BLUE, '\n'.join(prompt.split('\\n')), Colors.END, sep='')
    print('\nOUTPUT:\n')
    print(Colors.BLUE, response, Colors.END, sep='')
