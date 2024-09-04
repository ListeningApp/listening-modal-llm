"""
This script will convert the training documents into a format that can be used to fine tune a model.
Specifically, this reads from ./training_documents and writes to ./data/labels.jsonl and ./data/updates.jsonl.

EXAMPLE USAGE:
    poetry run python src/prepare_training_data.py
"""

import json
import logging
import os
from typing import Literal, TypedDict

log = logging.getLogger()

# The system instruction and user prompt are separated by three newlines in the source *.prompt.txt files
SYSTEM_USER_MSG_SEPARATOR = '\n\n\n'


class _LlmCompletionMessage(TypedDict):
    """
    A single LLM message, either from the user or the model, in OpenAI format.
    """

    role: Literal['system', 'user', 'assistant']
    content: str


class LlmCompletion(TypedDict):
    """
    A conversation between a user and the model in OpenAI format.
    """

    messages: list[_LlmCompletionMessage]


def prepare_training_data() -> None:
    """
    Parse the LLM prompts and chat completions from the `training_documents` directory and export it in JSONL format
    suitable for fine-tuning a model. https://docs.openpipe.ai/features/uploading-data
    """
    label_chats: list[LlmCompletion] = []  # Store each of the prompt-completion pairs in chat format
    update_chats: list[LlmCompletion] = []

    # For each cache directory
    for cache_dirname in os.listdir('training_documents'):
        if not cache_dirname.endswith('_cache') or not os.path.isdir(f'training_documents/{cache_dirname}'):
            continue  # Skip non-cache directories

        document_name = cache_dirname[:-6]  # Name of source pdf, without the extension
        log.info(f'Parsing training data: {document_name}')

        # For each file in the cache directory
        for cache_filename in os.listdir(f'training_documents//{cache_dirname}'):
            cache_filepath = f'training_documents/{cache_dirname}/{cache_filename}'

            # Handle label prompts
            if cache_filename.startswith(f'{document_name}.llm.label') and cache_filename.endswith('.prompt.txt'):
                try:
                    label_chat = _handle_prompt(cache_filepath)
                    label_chats.append(label_chat)
                except ValueError as e:
                    log.error(f'Failed to parse label chat in {cache_filename}: {e}')

            # Handle update prompts
            elif cache_filename.startswith(f'{document_name}.llm.update') and cache_filename.endswith('.prompt.txt'):
                try:
                    update_chat = _handle_prompt(cache_filepath)
                    update_chats.append(update_chat)
                except ValueError as e:
                    log.error(f'Failed to parse update chat in {cache_filename}: {e}')

    log.info('Exporting training data')

    # Export the the label chats in JSONL format
    with open('data/labels.jsonl', 'w') as labels_file:
        for label_chat in label_chats:
            chat_json = json.dumps(label_chat)
            labels_file.write(f'{chat_json}\n')

    # Export the the update chats in JSONL format
    with open('data/updates.jsonl', 'w') as updates_file:
        for update_chat in update_chats:
            chat_json = json.dumps(update_chat)
            updates_file.write(f'{chat_json}\n')

    log.info('Success')


def _handle_prompt(path_to_prompt_file: str) -> LlmCompletion:
    """
    Given a path to a prompt file from the traning data, return an LlmChat dict with the prompt and completion messages.
    Raises ValueError if the prompt or completion is empty.
    """
    completion = LlmCompletion(messages=[])

    # Get the example prompt for this chat
    with open(path_to_prompt_file) as prompt_file:
        raw_prompt = prompt_file.read().strip()  # Includes both the system instruction and the user input
        system_end_idx = raw_prompt.index(SYSTEM_USER_MSG_SEPARATOR) + len(SYSTEM_USER_MSG_SEPARATOR)
        system_text = raw_prompt[:system_end_idx].strip()  # System instruction for this prompt
        user_text = raw_prompt[system_end_idx:].strip()  # User input for this prompt
        system_msg = _LlmCompletionMessage(role='system', content=system_text)
        user_msg = _LlmCompletionMessage(role='user', content=user_text)
        completion['messages'].extend([system_msg, user_msg])

        # Empty prompts are not allowed in training data
        if not raw_prompt:
            raise ValueError(f'Chat prompt is empty: {path_to_prompt_file}')

    # Get the path to the completion json for this prompt
    completion_filepath = path_to_prompt_file.replace('.prompt.txt', '.json')

    # Get the completion response for this chat
    with open(completion_filepath) as completion_file:
        completion_dict = json.load(completion_file)
        raw_response: str = completion_dict['choices'][0]['message']['content']
        clean_response = raw_response.strip().strip('`\n').strip()
        output_msg = _LlmCompletionMessage(role='assistant', content=clean_response)
        completion['messages'].append(output_msg)  # Add the completion response to the chat

        # Empty completions are not allowed in training data
        if not clean_response:
            raise ValueError(f'Chat completion is empty: {completion_filepath}')

    # Format the prompt and response as an example chat for training
    return completion


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    prepare_training_data()
