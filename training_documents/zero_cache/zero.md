## Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents

Abstract

Can world knowledge learned by large language models be used to act in interactive environments? In this paper, we investigate the possibility of grounding high-level tasks, expressed in natural language (for example, "make breakfast"), to a chosen set of actionable steps (for example, "open fridge"). While prior work focused on learning from explicit step-by-step examples of how to act, we surprisingly find that if pre-trained language models are large enough and prompted appropriately, they can effectively decompose high-level tasks into mid-level plans without any further training. However, the plans produced naively by language models often cannot map precisely to admissible actions. We propose a procedure that conditions on existing demonstrations and semantically translates the plans to admissible actions. Our evaluation in the recent VirtualHome environment shows that the resulting method substantially improves executability over the language model baseline. The conducted human evaluation reveals a trade-off between executability and correctness but shows a promising sign towards extracting actionable knowledge from language models.


## Introduction One

Large language models have made impressive advances in language generation and understanding in recent years. See for a recent summary of their capabilities and impacts. Being trained on large corpora of human-produced language, these models are thought to contain a lot of information about the world - albeit in linguistic form.

We ask whether we can use such knowledge contained in language models not just for linguistic tasks, but to make goal-driven decisions that can be enacted in interactive, embodied environments. But we are not simply interested in whether we can train models on a dataset of demonstrations collected for some specific environment - we are instead interested in whether language models already contain information necessary to accomplish goals without any additional training.

More specifically, we ask whether world knowledge about how to perform high-level tasks (such as "make breakfast") can be expanded to a series of groundable actions (such as "open fridge", "grab milk", "close fridge", et cetera) that can be executed in the environment. For our investigation, we use the recently proposed VirtualHome environment. It can simulate a large variety of realistic human activities in a household environment and supports the ability to perform them via embodied actions defined with a verb-object syntax. However, due to the open-ended nature of the tasks, it is difficult to autonomously evaluate their success. We rely on human evaluation to decide whether sequences of actions meaningfully accomplish posed tasks.

We find that large GPT-three and Codex models, when prompted with a single fixed example of a task description and its associated sequence of actions, can produce very plausible action plans for the task we're interested in. Such completions reflect the information already stored in the model - no model fine-tuning is involved. Additionally, we only observe this effect in the larger models. Unfortunately, despite their semantic correctness, the produced action plans are often not executable in the environment. Produced actions may not map precisely to admissible actions, or may contain various linguistic ambiguities.

We propose several tools to improve executability of the model's outputs. First, we enumerate all admissible actions and map the model's output phrases to the most semantically-similar admissible action (we use similarity measure between sentence embeddings produced by a RoBERTa model in this work, but other choices are possible). Second, we use the model to autoregressively generate actions in a plan by conditioning past actions that have been made admissible via the technique above. Such on-the-fly correction can keep generation anchored to admissible actions. Third, we provide weak supervision to the model by prompting the model with a known task example similar to the query task. This is somewhat reminiscent of prompt tuning approaches but does not require access to gradients or internals of the model.

Using the above tools to bias model generation, we find that we improve executability of action plans from eighteen percent to seventy-nine percent (see Figure one) without any invasive modifications to model parameters or any extra gradient or internal information beyond what is returned from the model's forward pass. This is advantageous because it does not require any modifications to the model training procedure and can fit within existing model serving pipelines. However, we do find there to be some drop in correctness of the action sequences generated with the above tools (as judged by humans), indicating a promising step, but requiring more research on the topic.

To summarize, our paper's contributions are as follows:

· We show that without any training, large language models can be prompted to generate plausible goal-driven action plans, but such plans are frequently not executable in interactive environments.

We propose several tools to improve executability of the model generation without invasive probing or modifications to the model.

We conduct a human evaluation of multiple techniques and models and report on the trade-offs between executability and semantic correctness.


## Two Evaluation Framework

Simulating open-ended tasks that resemble naturalistic human activities requires an environment to support a rich set of diverse interactions, rendering most existing embodied environments unsuitable for our investigation. One exception is VirtualHome, which we evaluate on as it models complex human activities, though only in a household setting. To measure correctness of the generated action plans, for which evaluating computationally is inherently difficult for these open-ended tasks, we conduct a human evaluation similar to Puig et al. We note that since no further training is involved throughout our investigations, the observations and findings presented in this paper should also translate to similar embodied environments, likely even beyond the household domain.


## Two point one Evaluated Environment: VirtualHome

Preliminaries In VirtualHome, activities are expressed as programs. Each program consists of a sequence of textual action steps, where each step is written as: [action] (arg) (idx). Each action refers to one of the forty-two atomic actions supported in VirtualHome, such as "walk" and "open". Full list of atomic actions can be found in Appendix A point four. Different actions take in different numbers of arguments, such as "bedroom" and "fridge", that are necessary for specifying an interaction. Associated with each argument is a unique id specifying the corresponding node in the environment graph, in case of multiple instances of the same object class are present in the graph. For the sake of simplicity, we omit the id in the remaining discussions of this paper and allow automatic assignment by the environment. An example program is shown below for the task "Relax on sofa":

[WALK] (living_room) (one) [WALK] (television) (one) [FIND] (television) (one) [SWITCHON] (television) (one) [FIND] (sofa) (one) [SIT] (sofa) (one) [TURNTO] (television) (one) [WATCH] (television) (one)

Evaluated Tasks We use the ActivityPrograms knowledge base collected by Puig et al. for evaluation. It contains two thousand eight hundred twenty-one different entries annotated by Amazon Mechanical Turk workers. Each entry contains one) a high-level task name (for example, "Watch TV"), two) detailed instructions expressed in natural language to complete the task (for example, "Sit on my couch directly opposite my TV, switch on my TV with the remote control and watch"), and three) an executable program containing all necessary steps for a robotic agent (example above). We omit the use of detailed instructions two) as we desire direct extraction of executable programs three) from only high-level task names one). There are two hundred ninety-two distinct high-level tasks in the knowledge base, from which we randomly sample eighty-eight held-out tasks for evaluation. The remaining two hundred four tasks are used as demonstration set from which we are allowed.

to select as example(s) for prompting language models, or in the case of supervised fine-tuning baselines, they are used to fine-tune pre-trained language models.


## Two point two Metrics

A program that commands the agent to wander around in a household environment is highly executable but is mostly not correct. On the other hand, a program composed of natural language instructions annotated by humans is likely correct but cannot be executed, because its format is ambiguous and may lack necessary common-sense actions. We thus consider two axes for evaluation: executability and correctness.

Executability Executability measures whether an action plan can be correctly parsed and satisfies the common-sense constraints of the environment. To be correctly parsed, an action plan must be syntactically correct and contain only allowed actions and recognizable objects. To satisfy the common-sense constraints, each action step must not violate the set of its preconditions and postconditions. We report the average executability across all eighty-eight tasks and all seven VirtualHome scenes.

Correctness Unlike most embodied environments where the completion of a task can be easily judged, the ambiguous and multimodal nature of natural language task specification makes it impractical to obtain a gold-standard measurement of correctness. Therefore, we conduct human evaluations for the main methods. For the remaining analysis, we rely on a match-based metric that measures how similar a generated program is to human annotations. Specifically, we follow Puig et al. and calculate the longest common subsequence between two programs, normalized by the maximum length of the two. In the presence of multiple human-written programs for a single task, we take the maximum longest common subsequence across them. However, we note that the majority of the tasks only have one human annotation, but there are often many plausible ways to complete a certain task, making this metric imperfect at evaluation program correctness. Although correlation between the two is shown by Puig et al., we consider it only as a proxy metric in replacement of unscalable human evaluation.


## Three Method

In this section, we investigate the possibility of extracting actionable knowledge from pre-trained language models without further training. We first give an overview of the common approach to query large language models and how it may be used for embodied agents in Section three point one. Then we describe an inference-time procedure that addresses several deficiencies of the language model baseline and offers better executability in embodied environments. We break down the proposed procedure into three individual components, each discussed in Section three point two, three point three, three point four. Pseudo-code is in Algorithm one.

Since language models excel at dealing with natural language text instead of the specific format required by VirtualHome as described in Section two point one, we only expose natural language text to language models. To do this, we define a bidirectional mapping for each atomic action that converts between the natural language format and the program format. For instance, "walk to living room" is mapped to Walk to living room. Full list of the mappings is in Appendix A point four.


## Three point one Querying Language Models for Action Plans

Previous works have shown that large language models pre-trained on a colossal amount of data would internalize rich world knowledge that can be probed to perform various downstream tasks. Notably, autoregressive language models can even perform in-context learning, an ability to solve tasks using only contextual information without gradient updates. Contextual information is given as part of the input prompt and language models are asked to complete the remaining text. It often consists of natural language instructions and or a number of examples containing the desired input-output pairs.

We adopt the same approach to query language models to generate action plans for high-level tasks. Specifically, we prepend one example high-level task and its annotated action plan from the demonstration set to the query task, as shown in Figure two. To obtain text completion results, we sample from autoregressive language model using temperature sampling and nucleus sampling. We refer to this language model as Planning Language Model and the approach using this language model for plan generation as Vanilla language model, where language model is replaced by specific language model such as GPT three.

To improve the generation quality, we follow Chen et al. to sample multiple outputs for each query. However, unlike Chen et al. who investigate program synthesis and can choose the sample with highest unit test pass rate, we only consider the setting where one sample is allowed to be evaluated for each task. This is because repetitive trial-and-error is equivalent to probing the environment for privileged information, which should not be considered viable in our setting. For Vanilla language model, to choose the best action plan X star among k samples, each consisting of n i tokens, we select the sample with highest mean log probability as follows:

n i one j equals one n i log probability x, x i, less than j where zero parameterizes the Planning Language Model. one X i argmax ( P subscript O (X) equals greater than


## Three point two Admissible Action Parsing by Semantic Translation

One issue arises when naively following the above approach to generate action plans: the plan expressed in free-form language often cannot be mapped to unambiguous actionable steps and thus is not executable by a robotic agent. Many reasons can cause such failures: one) the output does not follow pre-defined mappings of any atomic action (e.g. "I first walk to the bedroom" is not of the format "walk to PLACE"), two) the output may refer to atomic action and objects using words unrecognizable by the environment (e.g. "microwave the chocolate milk" where "microwave" and "chocolate milk" cannot be mapped to precise action and object), or three) the output contains lexically ambiguous words (e.g. "open TV" should instead be "switch on TV").

Instead of developing a set of rules to transform the free-form text into admissible action steps, we propose to again leverage world knowledge learned by language models to semantically translate the action. For each admissible environment action A subscript E , we calculate its semantic distance to the predicted action phrase A hat by cosine similarity:

C left( F left( A hat right) , F left( A subscript E right) right) equals fraction numerator F left( A hat right) dot F left( A subscript E right) over denominator norm of F left( A hat right) norm of F left( A subscript E right) end fraction where F is an embedding function . (two)

To embed the output action phrase and environment actions, we use a BERT-style LM pre-trained with Sentence-BERT objective, to which we refer as Translation LM cubed. The action embedding is obtained by mean-pooling the last layer hidden states across all tokens in that action phrase. While the set of admissible actions in our environment is discrete and possible to exhaustively enumerate, sampling or projection can be employed in larger discrete or continuous action spaces.


## Three point three Autoregressive Trajectory Correction

Translating each step of the program after the entire program has been synthesized lacks consideration of achievability of individual steps and subjects to compounding errors. In practice, LLMs might output compounded instructions for a single step, even though it cannot be completed using one admissible action in the environment. To this end, we can instead interleave plan generation and action translation to allow for automatic trajectory correction. At each step, we first query Planning LM to generate K samples for a single action left( A subscript one hat, A subscript two hat, ellipsis, A subscript K hat right). For each sample A hat, we consider both its semantic soundness and its achievability in the environment. Specifically, we aim to find admissible environment action A subscript E by modifying the ranking scheme described in Equation one as follows:

argmax subscript A subscript E left bracket max subscript A hat C left( F left( A hat right), F left( A subscript E right) right) plus beta dot P subscript theta left( A hat right) right bracket where beta is a weighting coefficient . (three)

Then we append the translated environment action A subscript E to the unfinished text completion. This way all subsequent steps will be conditioned on admissible actions instead of free-form action phrases generated by Planning LM. Furthermore, we can use Translation LM to detect out-of-distribution actions, those outside the capabilities of a robot, and terminate a program early instead of mapping to a faulty action. This can be achieved by setting a threshold epsilon such that if max subscript A hat comma A subscript E C left( F left( A hat right), F left( A subscript E right) right) plus beta dot P subscript theta left( A hat right) less than epsilon at step T, the program is terminated early. Since we now sample Planning LM for individual steps instead of an entire sequence, another termination condition we consider is when greater than fifty percent of current-step samples are zero-length (excluding leading or trailing non-English text tokens).


## Three point four Dynamic Example Selection for Improved Knowledge Extraction

So far in the text, we always give the same example in the prompt for all query tasks. However, consider the task of "ordering pizza". Prompting LLMs with this task may give the assumption that the agent is initialized in front of a computer, and the LLMs may guide the agent to search for a pizza store and click "checkout my cart". Although these are reasonable and feasible in the real world, such assumption cannot always be made as these interactions may not be supported in simulated environments. In fact, the closest series of actions that human experts give in VirtualHome may be "walking to a computer", "switching on the computer", and "typing the keyboard". Without being fine-tuned on these data, LLMs would often fail at these tasks.

To provide weak supervision at inference time, we propose to select the most similar task T and its example plan E from the demonstration set to be used as the example in the prompt. Specifically, we re-use the same Translation LM introduced in Section three point two and select left( T star, E star right) whose high-level task name T star maximizes C left( F left( T right), F left( Q right) right), where Q is the query task. This approach bears resemblance to several recent works. An example is shown in Figure two where "Shave" is the most similar to the query task "Apply lotion".

FINAL METHOD Combining the various improvement discussed above, we refer to the final method as Translated LM, where LM is replaced by specific language model used such as GPT-three.


## Four Results

In this section, we first show that language models can generate sensible action plans for many high-level tasks, even without any additional training. Then we highlight its inadequacy when naively applied to embodied environments and demonstrate how this can be improved by again leveraging world knowledge learned by LLMs. Visualization of generated programs is shown in Figure three.

Sampling from LMs Pre-trained LMs are sensitive to sampling parameters and the specific example given in the prompt. For all evaluated methods, we perform hyperparameter search over various sampling parameters, and for methods using a fixed prompt example, we report metrics averaged across three randomly chosen examples. To select the best run for each method, we rank the runs by the sum of LCS and executability, each normalized by human-expert scores. Further details are in Appendix A point one.

Model Choices For Planning LM, we evaluate a representative set of causal language models. For Translation LM, we mainly use Sentence-Roberta-three hundred fifty-five M and provide relevant ablations in Section five point three. GPT-three and Codex are accessed using OpenAI API, and the remaining models are accessed through open-source packages, Hugging Face Transformers and SentenceTransformers, all without additional training (except for the fine-tuning baseline).


## Four point one Do LLMs contain actionable knowledge for high-level tasks?

We first investigate whether LLMs can generate sensible action plans expressed in free-form language. We use the approach described in Section three point one to query pre-trained LLMs. To evaluate the correctness of generated action plans, we conduct human evaluations. For each model, we ask ten human annotators to determine - by answering "Yes" or "No" - whether each task can be completed using provided action steps. To provide a reference of how humans might rate the action plans provided by other humans, we also ask annotators to rate the human-written action plans included in the VirtualHome dataset for the same set of tasks. In contrast to the free-form text output by LLMs, humans wrote the plans using a graphical programming interface that enforces strict syntax and a chosen set of atomic action vocabulary, which limit the expressivity and the completeness of their answers. More details of our human evaluation procedure can be found in Appendix A point two.

We show the human evaluation results in Figure one, where the y-axis shows correctness averaged across all tasks and all annotators. Surprisingly, when LLMs are large enough and without imposed syntactic constraints, they can generate highly realistic action plans whose correctness - as deemed by human annotators - even surpasses human-written action plans. We also observe some level of correctness for smaller models such as GPT-two. However, inspection of its produced output indicates that it often generates shorter plans by ignoring common-sense actions or by simply rephrasing the given task (e.g. the task "Go to sleep" produces only a single step "Go to bed"). These failure modes sometimes mislead human annotators to mark them correct as the annotators may ignore common-sense actions in their judgment as well, resulting in a higher correctness rate than the quality of the output shows.


## Four point two How executable are the LLM action plans?

We analyze the executability of LLM plans by evaluating them in all seven household scenes in VirtualHome. As shown in Table one, we find action plans generated naively by LLMs are generally not very executable. Although smaller models seem to have higher executability, we find that the majority of these executable plans are produced by ignoring the queried task and repeating the given example of a different task. This is validated by the fact that smaller models have lower LCS than larger models despite having high executability, showing that this failure mode is prevalent among smaller models. In contrast, larger models do not suffer severely from this failure mode. Yet as a result of being more expressive, their generated programs are substantially less executable.


## Four point three Can LLM action plans be made executable by proposed procedure?

We evaluate the effectiveness of our proposed procedure of action translation. We first create a bank of all allowed forty-seven thousand five hundred twenty-two action steps in the environment, including all possible combinations of atomic actions and allowed arguments or objects. Then we use an off-the-shelf Sentence-Roberta as Translation LM to create embeddings for actions and output text. For better computational efficiency, we pre-compute the embeddings for all allowed actions, leaving minor computation overhead for our procedure over the baseline methods at inference time. As shown in Table one, executability of generated programs is significantly improved. Furthermore, we also observe improved LCS because the translated action steps precisely follow the program syntax and thus are more similar to the plans produced by human experts. Sample output is shown in Figure one and a larger random subset of generated samples can be found in Appendix A point five.

To validate their correctness, we again perform human evaluations using the same procedure from Section four point one. Results are shown in Table one. We find that despite being more similar to human-written plans as they follow strict syntax, the programs are deemed less correct by humans compared to their vanilla counterparts. By examining the output, we observe two main sources of errors. First, we find Translation LM is poor at mapping compounded instructions to a succinct admissible action, e.g. "brush teeth with toothbrush and toothpaste". Second, we find that the generated programs are sometimes terminated too early. This is partly due to the imperfect expressivity of the environment;

certain necessary actions or objects are not implemented to fully achieve some tasks, so Translation LM cannot map to a sufficiently similar action. This is also reflected by our human evaluation results of the programs written by other humans, as only seventy percent of the programs are considered complete.


## Five Analysis and Discussions

Five point one Ablation of design decisions

We perform ablation studies for the three components of our proposed procedure, described in Section three point two, three point three, and three point four respectively. As shown in Table two, leaving out any of the three components would all lead to decreased performance in both executability and LCS. An exception is Translated GPT-three without Trajectory Correction, where we observe a slight improvement in LCS at the expense of a considerable drop in executability. Among the three proposed components, leaving out action translation leads to the most significant executability drop, showing the importance of action translation in extracting executable action plans from LLMs.


## Five point two. Are the generated action plans grounded in the environment?

Since successful execution of correct action plans directly measures grounding, we calculate the percentage of generated action plans that are both correct and executable. We deem an action plan to be correct if seventy percent or more human annotators decide it is correct. Human-written plans are one hundred percent executable, of which sixty-five point nine one percent are deemed correct. Results for LMs are shown in Figure Four.

Although smaller LMs such as GPT-Two can generate highly executable action plans as shown in Table One, these executable plans mostly are not correct, as they often repeat the given example or do not contain all necessary steps. Increasing model parameters can lead to some improvement in generating plans that are both executable and correct, yet it scales poorly with the parameter count. In the meantime, action translation offers a promising way towards grounding actionable knowledge by producing executable and correct plans, though a large gap remains to be closed to reach human-level performance, sixty-five point nine one percent.


## Five point three. Effect of Different Translation LMs

In this section, we study the effect of using different Translation LM. We compare two size variants of Sentence BERT and Sentence RoBERTa trained on the STS benchmark and a baseline using averaged Glo Ve embeddings. Results are shown in Table Three. Notably, we do not observe significant differences in executability and LCS across different variants of BERT and RoBERTa. We hypothesize that this is because any language models trained on reasonably large datasets should be capable of the single-step action phrase translation considered in this work. However, simply using average Glo Ve embeddings would lead to significantly reduced performance.


## Five point four. Can LLMs generate actionable programs by following step-by-step instructions?

Prior works often focus on translating step-by-step instructions into executable programs. Specifically, instead of only providing a high-level task name, how-to instructions are also provided, as shown in Figure Five. Although this setting is easier as it does not require rich prior knowledge, how-to instructions can help resolve much ambiguity of exactly how to perform a high-level task when multiple solutions are possible. To investigate whether pre-trained LLMs are capable of doing this without additional training, we include these instructions in the prompt and evaluate LLMs with the proposed procedure. We compare to a supervised baseline from VirtualHome that trains an LSTM from scratch on human-annotated data. Since the code to train the baseline is not publicly released and a different train/test split is likely used, we only show results reported in Puig et al. as a crude reference. We also cannot compare executability as it is not reported. Results are shown in Table Four. Surprisingly, without being fine-tuned on any domain data, Translated Codex/GPT-Three can attain LCS close to supervised methods while generating highly executable programs.


## Five point five. Analysis of program length

Shorter programs have a natural advantage of being more executable as they need to satisfy less pre/post-conditions, albeit being prone to incompleteness. To validate the proposed approach does not simply generate very short programs, we calculate the average program length across the eighty-eight evaluated tasks. Results are shown in Table Five. Mirroring the observations made in Section Four point one and Section Four point two, we find smaller LMs such as GPT-Two tend to generate shorter programs than larger models do while frequently repeating the given executable example. In contrast, larger models like Codex and GPT-Three can generate more expressive programs with high realism, yet consequently, they often suffer from executability. We show proposed procedure can find appropriate balance and is capable of generating programs that are highly executable while maintaining reasonable expressiveness as measured by program length.


## Six. Related Works

Large-scale natural language modeling has witnessed rapid advances since the inception of the Transformer architecture. It has been shown by recent works that large language models pre-trained on large unstructured text corpus not only can perform strongly on various down-stream NLP tasks but the learned representations can also be used to model relations of entities, retrieve matching visual features, synthesize code from docstrings, solve math problems, and even as valuable priors when applied to diverse tasks from different modalities. Notably, by pre-training on large-scale data, these models can also internalize an implicit knowledge base containing rich information about the world from which factual answers (e.g. "Dante was born in PLACE") can be extracted. Compared to prior works in single-step knowledge extraction, we aim to extract sequential action plans to complete open-ended human activities while satisfying various constraints of an interactive environment.

Many prior works have looked into grounding natural language in embodied environments. A series of them parse language instructions into formal logic or rely mainly on lexical analysis to resolve various linguistic ambiguities for embodied agents. However, they often require many hand-designed rules or scale inadequately to more complex tasks and environments. Recently, many efforts have been put into creating more realistic environments with the goal to further advances in this area. At the same time, by leveraging the better representation power of neural architectures, a number of works have looked into creating instruction-following agents that can perform manipulation, navigation, or both. Recent works also use language as hierarchical abstractions to plan actions using imitation learning and to guide exploration in reinforcement learning.

Notably, many prior works do not leverage full-blown pre-trained LLMs; most investigate smaller LMs that require considerable domain-specific data for fine-tuning to obtain reasonable performance. Perhaps more importantly, few works have evaluated LLMs in an embodiment setting that realizes the full potential of the actionable knowledge these models already contain by pre-training on large-scale unstructured text: the tasks evaluated are often generated from a handful of templates, which do not resemble the highly diverse activities that humans perform in daily lives. The development of VirtualHome environment enables such possibility. However, relevant works rely on human-annotated data and perform supervised training from scratch. Due to the lack of rich world knowledge, these models can only generate action plans given detailed instructions of how to act or video demonstrations. Concurrent work by Li et al. validates similar hypothesis that

LMs contain rich actionable knowledge. They fine-tune GPT-Two with demonstrations to incorporate environment context and to predict actions in VirtualHome, and evaluate on tasks that are generated from pre-defined predicates. In contrast, we investigate existing knowledge in LLMs without any additional training and evaluate on human activity tasks expressed in free-form language.


## Seven. Conclusion, Limitations and Future Work

In this work, we investigate actionable knowledge already contained in pre-trained LLMs without any additional training. We present several techniques to extract this knowledge to perform common-sense grounding by planning actions for complex human activities.

Despite promising findings, there remain several limitations of this work which we discuss as follows:

Drop in Correctness Although our approach can significantly improve executability of the generated plans, we observe a considerable drop in correctness. In addition to the errors caused by the proposed action translation, this is partially attributed to the limited expressivity of VirtualHome, as it may not support all necessary actions to fully complete all evaluated tasks (correctness is judged by humans). This is also reflected by that Vanilla LMs can even surpass human-written plans, which are restricted by environment expressivity.

Mid-Level Grounding Instead of grounding the LLM generation to low-level actions by using downstream data from a specific environment, we focus on high-level to mid-level grounding such that we evaluate raw knowledge of LLMs as closely and broadly as possible. Hence, we only consider the most prominent challenge in mid-level grounding that the generated plans must satisfy all common-sense constraints characterized by executability metric. As a result, we assume there is a low-level controller that can execute these mid-level actions such as "grab cup", and we do not investigate the usefulness of LLMs for low-level sensorimotor behavior grounding. To perform sensorimotor grounding, such as navigation and interaction mask prediction, domain-specific data and fine-tuning are likely required.

Ignorant of Environment Context We do not incorporate observation context or feedback into our models. To some extent, we approach LLMs in the same way as how VirtualHome asks human annotators to write action plans for a given human activity by imagination, in which case humans similarly do not observe environment context. Similar to human-written plans, we assume the plans generated by LMs only refer to one instance of each object class. As a result, successful plan generation for tasks like "stack two plates on the right side of a cup" is not possible.

Evaluation Protocol We measure quality of plans by a combination of executability and correctness instead of one straightforward metric. To the best of our knowledge, there isn't a known way to computationally assess the semantic correctness of the plans due to the tasks' open-ended and multi-modal nature. Prior work also adopt similar combination of metrics. We report two metrics individually to shine light on the deficiencies of existing LLMs which we hope could provide insights for future works. To provide a holistic view, we report results by combining two metrics in Section five point two.

We believe addressing each of these shortcoming will lead to exciting future directions. We also hope these findings can inspire future investigations into using pre-trained LMs for goal-driven decision-making problems and grounding the learned knowledge in embodied environments.

For each evaluated method, we perform grid search over the following hyperparameters:

For methods that use fixed example across evaluated tasks, we search over the following three randomly chosen examples:

Human evaluations are conducted on Amazon Mechanical Turk. For each method, we generate action plans for all eighty-eight high-level tasks. To account for the expressivity of the VirtualHome environment, we include action plans written by human experts from the VirtualHome dataset as references in our human evaluations. The evaluations are conducted in the form of questionnaires containing all action plans whose order is randomly shuffled and whose corresponding methods are unknown to the annotators. Human annotators are required to answer all the questions in the questionnaire. For each question, the annotators need to answer either "Yes" or "No" indicating if they believe the action plan completes the task. For each method, we report correctness percentage averaged across ten participated human annotators and all eighty-eight tasks. We further report the standard error of the mean across human annotators. Screenshot can be found in Figure six.

The evaluated tasks are part of the ActivityPrograms dataset collected by Puig et al.. Some of the task names may contain misspelling(s).

One. Apply lotion

Two. Arrange folders

Three. Breakfast

Four. Browse internet

Five. Brush teeth

Six. Change clothes

Seven. Change sheets and pillow cases

Eight. Collect napkin rings

Nine. Complete surveys on amazon turk

Ten. Compute

Eleven. Decorate it

Twelve. Do homework

Thirteen. Do work

Fourteen. Draft home

Fifteen. Draw picture

Sixteen. Dry soap bottles


## Seventeen. Dust

Eighteen. Eat cereal


## Nineteen. Eat cheese Twenty. Eat snacks and drink tea

Twenty-one. Empty dishwasher and fill dishwasher


## Twenty-two. Entertain

Twenty-three. Feed me


## Twenty-four. Find dictionary

Twenty-five. Fix snack


## Twenty-six. Get glass of milk

Twenty-seven. Give milk to cat


## Twenty-eight. Go to sleep

Twenty-nine. Grab things


## Thirty. Hand washing

Thirty-one. Hang keys


## Thirty-two. Hang pictures

Thirty-three. Iron shirt


## Thirty-four. Keep cats inside while door is open

Thirty-five. Keep cats out of room


## Thirty-six. Leave home

Thirty-seven. Listen to music


## Thirty-eight. Look at mirror

Thirty-nine. Look at painting


## Forty. Make bed

Forty-one. Make popcorn


## Forty-two. Organize closet

Forty-three. Organize pantry


## Forty-four. Paint ceiling

Forty-five. Pay bills


## Forty-six. Pick up toys

Forty-seven. Play musical chairs


## Forty-eight. Prepare pot of boiling water

Forty-nine. Push all chairs in


## Fifty. Push in desk chair

Fifty-one. Put alarm clock in bed- room


## Fifty-two. Put away groceries

Fifty-three. Put away toys


## Fifty-four. Put clothes away

Fifty-five. Put mail in mail orga- nizer


## Fifty-six. Put on your shoes

Fifty-seven. Put out flowers


## Fifty-eight. Put up decoration

Fifty-nine. Read


## Sixty. Read newspaper

Twenty


## Sixty-one. Read on sofa

Sixty-two. Read to child


## Sixty-three. Read yourself to sleep

Sixty-four. Receive credit card


## Sixty-five. Restock

Sixty-six. Scrubbing living room tile floor is once week activity for me


## Sixty-seven. Style hair

Sixty-eight. Switch on lamp


## Sixty-nine. Take jacket off

Seventy. Take shoes off


## Seventy-one. Tale off shoes

Seventy-two. Throw away paper


## Seventy-three. Try yourself off

Seventy-four. Turn off TV


## Seventy-five. Turn on TV with re- mote

Seventy-six. Turn on radio


## Seventy-seven. Type up document

Seventy-eight. Unload various items from pockets and place them in bowl on table


## Seventy-nine. Use laptop

Eighty. Vacuum


## Eighty-one. Walk to room

Eighty-two. Wash dirty dishes


## Eighty-three. Wash face

Eighty-four. Wash monitor


## Eighty-five. Wash teeth

Eighty-six. Watch horror movie


## Eighty-seven. Wipe down sink

Eighty-eight. Write book


## A.4 Natural Language Templates for All Atomic Actions

VirtualHome requires action steps specified in a specific format, yet language models are trained to deal with mostly natural language. We thus define a natural language template for each atomic action and only expose the converted natural language text in all operations involving language models, i.e. autoregressive generation and action translation. After we obtain an entire generated program expressed in natural language, such as those in Figure One and Figure Two, we then convert each action step to the VirtualHome syntax. Full list of the atomic actions and their natural language templates can be found below.


## A.5 Random Samples of Action Plans

Human

Task: Go to sleep Step One: Walk to bedroom Step Two: Walk to bed

Step Three: Find bed Step Four: Turn to bed

Step Five: Look at bed

Step Six: Sit on bed Step Seven: Sleep

Task: Browse internet Step One: Walk to home office Step Two: Walk to chair Step Three: Find chair Step Four: Sit on chair Step Five: Find computer Step Six: Switch on computer Step Seven: Turn to computer Step Eight: Look at computer

Step Nine: Find keyboard Step Ten: Type on keyboard

Task: Wash teeth Step One: Stand up Step Two: Walk to bathroom Step Three: Walk to sink Step Four: Find sink Step Five: Turn to sink Step Six: Look at sink Step Seven: Find teeth

Step Eight: Wash teeth

Step One: Walk to bathroom Step Two: Walk to tooth paste Step Three: Find tooth paste Step Four: Grab tooth paste Step Five: Find toothbrush Step Six: Put toothpaste on tooth- brush Step Seven: Put toothbrush in mouth Step Eight: Brush teeth


## Task: Brush teeth

Step Six: Grab toothbrush

Task: Vacuum Step One: Walk to home office Step Two: Walk to computer Step Three: Find vacuum cleaner Step Four: Switch on vacuum cleaner Step Five: Switch off vacuum cleaner


## Vanilla GPT3-One hundred seventy-five B

Task: Go to sleep Step One: Walk to bedroom Step Two: Walk to bed Step Three: Find pajamas Step Four: Put on pajamas Step Five: Find slippers Step Six: Put on slippers Step Seven: Get in bed Step Eight: Sleep Task: Browse internet Step One: Walk to home office Step Two: Walk to computer Step Three: Find computer Step Four: Grab computer Step Five: Find chair Step Six: Sit on chair

Step Seven: Browse internet Task: Wash teeth Step One: Walk to bathroom Step Two: Walk to sink Step Three: Turn on faucet Step Four: Grab toothbrush Step Five: Put toothpaste on tooth- brush Step Six: Put toothbrush in mouth Step Seven: Brush teeth Step Eight: Rinse mouth out with wa- ter Step Nine: Turn off faucet Step Ten: Walk back to bedroom


## Task: Brush teeth Step One: Walk to bathroom Step Two: Walk to sink

Step Three: Turn on water Step Four: Grab toothbrush


## Task: Vacuum Step One: Walk to home office Step Two: Walk to vacuum Step Three: Find vacuum Step Four: Grab vacuum

Step Five: Find chair Step Six: Sit on chair

Step Seven: Vacuum


## Translated GPT3-One hundred seventy-five B (Ours)

Task: Go to sleep Step One: Walk to bedroom Step Two: Walk to bed Step Three: Lie on bed Step Four: Sleep

Task: Browse internet Step One: Walk to home office Step Two: Walk to desk Step Three: Find chair Step Four: Sit on chair Step Five: Find computer Step Six: Switch on computer Step Seven: Find mouse Step Eight: Grab mouse Step Nine: Turn to computer Step Ten: Point at computer

Task: Wash teeth Step One: Walk to bathroom Step Two: Walk to sink Step Three: Find faucet Step Four: Switch on faucet

Step Five: Walk to toothbrush Step Six: Grab toothbrush


## Task: Brush teeth Step One: Find toothbrush Step Two: Turn to toothbrush Step Three: Point at toothbrush Step Four: Wash toothbrush

Task: Vacuum

Step One: Walk to home office Step Two: Walk to dresser Step Three: Open dresser

Step Four: Find vacuum cleaner Step Five: Grab vacuum cleaner Step Six: Pull vacuum cleaner Step Seven: Plug in vacuum cleaner Step Eight: Switch on vacuum cleaner


## Task: Pick up toys Step One: Walk to bedroom Step Two: Walk to toy Step Three: Find toy Step Four: Grab toy

Step Five: Walk to filing cabinet

Step Six: Open filing cabinet

Step Seven: Put toy on filing cabinet Step Eight: Find toy Step Nine: Grab toy

Step Ten: Walk to filing cabinet Step Eleven: Put toy on filing cabinet Step Twelve: Find toy

Step Thirteen: Grab toy

Step Fourteen: Walk to filing cabinet Step Fifteen: Put toy on filing cabinet Step Sixteen: Close filing cabinet


## Task: Decorate it

Step One: Walk to home office Step Two: Walk to centerpiece Step Three: Find centerpiece Step Four: Grab centerpiece

Step Five: Walk to table Step Six: Put centerpiece on table Step Seven: Find drawing Step Eight: Grab drawing Step Nine: Find wall Step Ten: Turn to wall

Step Eleven: Put drawing on wall Step Twelve: Find drawing Step Thirteen: Grab drawing

Step Fourteen: Turn to wall Step Fifteen: Put drawing on wall


## Task: Put away groceries Step One: Walk to dining room Step Two: Walk to freezer

Step Three: Find freezer Step Four: Open freezer

Step Five: Find food Step Six: Grab food

Step Seven: Put food in freezer

Step Eight: Close freezer

Task: Pick up toys Step One: Walk to living room Step Two: Walk to toy box Step Three: Find toy box Step Four: Grab toy box Step Five: Find chair Step Six: Sit on chair Step Seven: Pick up toys

Task: Decorate it Step One: Walk to home office Step Two: Walk to novel Step Three: Find novel Step Four: Grab novel Step Five: Find chair Step Six: Sit on chair Step Seven: Read novel

Step Eight: Decorate it

Task: Put away groceries Step One: Walk to kitchen Step Two: Walk to refrigerator Step Three: Open refrigerator Step Four: Grab milk and eggs Step Five: Close refrigerator Step Six: Walk to counter

Step Seven: Put milk and eggs on counter Step Eight: Walk to cabinet Step Nine: Open cabinet Step Ten: Put away milk and eggs Step Eleven: Close cabinet

Step Twelve: Walk to refrigerator Step Thirteen: Grab orange juice and bread Step Fourteen: Close refrigerator

Task: Pick up toys Step One: Find toy Step Two: Turn to toy Step Three: Point at toy Step Four: Wash toy

Task: Decorate it Step One: Walk to table Step Two: Walk to centerpiece Step Three: Look at centerpiece Step Four: Grab centerpiece Step Five: Point at centerpiece

Task: Put away groceries Step One: Walk to kitchen Step Two: Walk to fridge Step Three: Open fridge Step Four: Put food in fridge Step Five: Close fridge

Step Six: Walk to dining room Step Seven: Walk to livingroom Step Eight: Walk to bedroom Step Nine: Walk to bathroom

Task: Draw picture Step One: Walk to home office Step Two: Walk to chair Step Three: Find chair Step Four: Sit on chair Step Five: Find desk Step Six: Open desk Step Seven: Find check Step Eight: Grab check Step Nine: Put check on desk Step Ten: Find pencil Step Eleven: Grab pencil Step Twelve: Close desk


## Task: Entertain

Step One: Walk to home office Step Two: Walk to cheese

Step Three: Find cheese

Step Four: Find food Step Three: Find remote

Step Five: Find couch

Step Six: Sit on couch

Step Seven: Find wine glass Step Six: Sit on chair

Step Eight: Grab wine glass Step Nine: Drink wine glass

Task: Type up document Step One: Walk to home office Step Two: Walk to chair Step Three: Find chair Step Four: Sit on chair Step Five: Find computer Step Six: Switch on computer Step Seven: Turn to computer Step Eight: Look at computer Step Nine: Find check Step Ten: Grab check Step Eleven: Read check Step Twelve: Find coffee cup Step Thirteen: Grab coffee cup Step Fourteen: Drink coffee cup Step Fifteen: Put back coffee cup

Step Sixteen: Find keyboard Step Seventeen: Type on keyboard


## Task: Put on your shoes Step One: Walk to home office Step Two: Walk to shoes Step Three: Find shoes Step Four: Grab shoes

Step Five: Find chair Step Five: Find chair Step Six: Sit on chair Step Six: Sit on chair

Step Seven: Find feet both Step Eight: Put shoes on feet both

Task: Draw picture Step One: Walk to home office Step Two: Walk to pencils Step Three: Find pencils Step Four: Grab pencils Step Five: Find paper Step Six: Sit on chair

Step Seven: Draw picture


## Task: Entertain

Step One: Walk to living room

Step Two: Walk to entertainment center

Step Four: Grab remote

Step Five: Find chair

Step Seven: Entertain self Task: Type up document Step One: Walk to home office Step Two: Walk to keyboard Step Three: Find keyboard Step Four: Grab keyboard Step Five: Find chair Step Six: Sit on chair

Step Seven: Type document


## Task: Put on your shoes Step One: Walk to home office Step Two: Walk to shoes Step Three: Find shoes Step Four: Grab shoes

Step Seven: Put on shoes


## Task: Draw picture Step One: Walk to home office Step Two: Walk to wall

Step Three: Walk to drawing Step Four: Find drawing Step Five: Turn to drawing Step Six: Look at drawing Step Seven: Touch drawing Step Eight: Pull drawing Step Nine: Push drawing


## Task: Entertain Step One: Walk to livingroom Step Two: Walk to couch Step Three: Find couch Step Four: Sit on couch

Task: Type up document Step One: Walk to home office Step Two: Walk to computer Step Three: Find computer

Step Four: Switch on computer Step Five: Find chair Step Six: Sit on chair Step Seven: Turn to computer Step Eight: Look at computer Step Nine: Find keyboard Step Ten: Grab keyboard Step Eleven: Type on keyboard Step Twelve: Stand up Step Thirteen: Find printer

Step Fourteen: Switch on printer Step Fifteen: Find printing paper


## Task: Put on your shoes Step One: Find shoes Step Two: Turn to shoes Step Three: Point at shoes

Step Four: Wash shoes

Task: Watch horror movie Step One: Walk to home office Step Two: Walk to remote control Step Three: Find remote control Step Four: Grab remote control

Step Five: Find couch

Step Six: Sit on couch Step Seven: Find television Step Eight: Switch on television Step Nine: Turn to television Step Ten: Watch television

Task: Turn on radio Step One: Walk to home office Step Two: Walk to stereo Step Three: Find stereo Step Four: Find electrical outlet Step Five: Turn to electrical outlet Step Six: Plug in stereo

Step Seven: Switch on electrical outlet Step Eight: Switch on stereo


## Task: Look at mirror Step One: Walk to bathroom Step Two: Walk to mirror Step Three: Find mirror Step Four: Turn to mirror

Step Five: Look at mirror


## Task: Leave home

Step One: Walk to home office Step Two: Walk to shoes

Step Three: Find shoes

Step Four: Grab shoes

Step Five: Put on shoes


## Task: Walk to room Step One: Walk to home office Step Two: Walk to home office

Task: Watch horror movie Step One: Walk to home office Step Two: Walk to horror movie Step Three: Find horror movie Step Four: Grab horror movie Step Five: Find chair Step Six: Sit on chair

Step Seven: Watch horror movie


## Task: Turn on radio Step One: Walk to home office Step Two: Walk to radio Step Three: Find radio Step Four: Grab radio

Step Five: Find chair

Step Six: Sit on chair

Step Seven: Turn on radio Task: Look at mirror Step One: Walk to bathroom Step Two: Walk to mirror Step Three: Look in mirror

Task: Leave home Step One: Walk to front door Step Two: Open front door Step Three: Walk to car Step Four: Open car door Step Five: Get in car Step Six: Close car door Step Seven: Drive to work

Task: Walk to room Step One: Walk to home office Step Two: Walk to novel Step Three: Find novel Step Four: Grab novel Step Five: Find chair Step Six: Sit on chair Step Seven: Read novel


## Task: Watch horror movie Step One: Find television Step Two: Switch on television Step Three: Find cd player

Step Four: Switch on CD player Step Five: Switch off CD player Step Six: Find remote control

Step Seven: Switch on remote control Step Eight: Switch off remote control

Task: Turn on radio Step One: Walk to home office Step Two: Walk to chair Step Three: Find chair Step Four: Sit on chair

Step Five: Find remote control Step Six: Grab remote control Step Seven: Find radio Step Eight: Point at radio Step Nine: Switch on radio Step Ten: Put back remote control

Task: Look at mirror Step One: Walk to bedroom Step Two: Walk to mirror Step Three: Find mirror Step Four: Turn to mirror Step Five: Look at mirror Step Six: Find face Step Seven: Turn to face Step Eight: Look at face Step Nine: Find hair Step Ten: Turn to hair Step Eleven: Look at hair Step Twelve: Find dress Step Thirteen: Turn to dress Step Fourteen: Look at dress

Task: Leave home Step One: Find shoes Step Two: Grab shoes Step Three: Put on shoes

Task: Walk to room Step One: Walk to dining room Step Two: Walk to living room Step Three: Walk to bedroom

Task: Hang pictures Step One: Walk to bedroom Step Two: Walk to drawing Step Three: Find drawing Step Four: Grab drawing Step Five: Find wall Step Six: Put drawing on wall Step Seven: Turn to drawing Step Eight: Look at drawing Step Nine: Find drawing Step Ten: Grab drawing Step Eleven: Put drawing on wall Step Twelve: Turn to drawing Step Thirteen: Look at drawing

Task: Wipe down sink

Step One: Walk to dining room Step Two: Walk to rag Step Three: Find rag Step Four: Grab rag Step Five: Walk to sink

Step Six: Wipe sink

Step Seven: Put back rag Step Eight: Wash hands Task: Take shoes off Step One: Walk to home office Step Two: Walk to shoes Step Three: Find shoes Step Four: Grab shoes

Task: Take shoes off Step One: Walk to home office Step Two: Walk to shoes Step Three: Find shoes Step Four: Find shoes Step Five: Take off shoes Step Six: Find dresser Step Seven: Open dresser Step Eight: Grab shoes

Step Nine: Put shoes in dresser Step Ten: Close dresser

Task: Give milk to cat Step One: Walk to home office Step Two: Walk to cat Step Three: Find cat Step Four: Turn to cat Step Five: Point at cat Step Six: Pull cat Step Seven: Find milk

Step Eight: Grab milk Step Nine: Find plate Step Ten: Pour milk into plate Step Eleven: Touch cat Step Twelve: Scrub cat

Task: Hang pictures Step One: Walk to home office Step Two: Walk to box of pictures Step Three: Find box of pictures Step Four: Grab box of pictures Step Five: Walk to wall Step Six: Hang pictures on wall

Task: Wipe down sink Step One: Walk to kitchen Step Two: Walk to sink Step Three: Grab sponge Step Four: Wipe down sink

Step Five: Rinse sponge Step Six: Put sponge away Step Seven: Pour cleaning solution into sink Step Eight: Find faucet Step Nine: Switch on faucet Step Ten: Scrub sink Step Eleven: Wash sink Task: Take shoes off Step One: Walk to home office Step Two: Walk to shoes Step Three: Find shoes

Step Five: Find chair Step Six: Sit on chair

Step Seven: Take shoes off

Task: Give milk to cat Step One: Walk to kitchen Step Two: Walk to fridge Step Three: Open fridge Step Four: Grab milk Step Five: Walk to cat Step Six: Pour milk into bowl Step Seven: Put bowl on floor

Step Eight: Walk away from cat

Task: Hang pictures Step One: Walk to home office Step Two: Walk to table Step Three: Find keys Step Four: Grab keys Step Five: Walk to wall Step Six: Find hanger Step Seven: Put keys on hanger

Task: Wipe down sink Step One: Walk to bathroom Step Two: Walk to cleaning solution Step Three: Find cleaning solution Step Four: Grab cleaning solution Step Five: Find sink

Task: Give milk to cat Step One: Find cat Step Two: Touch cat Step Three: Open fridge Step Four: Touch milk Step Five: Pour milk into bowl

Task: Grab things Step One: Walk to novel Step Two: Turn to novel Step Three: Grab novel

Task: Use laptop Step One: Walk to home office Step Two: Walk to couch Step Three: Find couch Step Four: Sit on couch Step Five: Find laptop Step Six: Switch on laptop Step Seven: Turn to laptop Step Eight: Look at laptop

Step Nine: Find keyboard Step Ten: Type on keyboard Step Eleven: Turn to keyboard Step Twelve: Look at keyboard Step Thirteen: Type on keyboard

Step Fourteen: Turn to laptop Step Fifteen: Look at laptop

Task: Organize pantry Step One: Walk to dining room Step Two: Walk to pantry Step Three: Find food Step Four: Grab food Step Five: Turn to food Step Six: Look at food Step Seven: Find garbage can Step Eight: Put food on garbage can Step Nine: Find vegetable

Step Ten: Grab vegetable Step Eleven: Turn to vegetable Step Twelve: Look at vegetable Step Thirteen: Put vegetable on garbage can Step Fourteen: Find dry pasta Step Fifteen: Grab dry pasta Step Sixteen: Turn to dry pasta Step Seventeen: Look at dry pasta Step Eighteen: Put back dry pasta Step Nineteen: Find food

Step Twenty: Turn to food Step Twenty-One: Look at food Step Twenty-Two: Push food Step Twenty-Three: Find noodles Step Twenty-Four: Grab noodles Step Twenty-Five: Turn to noodles Step Twenty-Six: Look at noodles Step Twenty-Seven: Put back noodles

Task: Grab things Step one: Walk to home office Step two: Walk to novel Step three: Find novel Step four: Grab novel Step five: Find chair Step six: Sit on chair Step seven: Read novel Step eight: Grab things Task: Use laptop Step one: Walk to home office Step two: Walk to laptop Step three: Find laptop Step four: Grab laptop Step five: Find chair Step six: Sit on chair Step seven: Use laptop

Task: Organize pantry Step one: Walk to kitchen Step two: Walk to pantry Step three: Find pantry Step four: Grab pantry Step five: Find chair Step six: Sit on chair Step seven: Organize pantry

Task: Grab things Step one: Find toy Step two: Turn to toy Step three: Point at toy Step four: Wash toy

Task: Use laptop Step one: Walk to home office Step two: Walk to chair Step three: Find chair Step four: Sit on chair Step five: Find laptop Step six: Switch on laptop Step seven: Find mouse Step eight: Grab mouse Step nine: Find mousepad Step ten: Put mouse on mousepad Step eleven: Turn to laptop Step twelve: Point at laptop

Task: Organize pantry Step one: Walk to pantry Step two: Find pantry

Task: Change clothes Step one: Walk to bedroom Step two: Walk to dresser Step three: Open dresser Step four: Find dress Step five: Grab dress Step six: Put on dress

Step seven: Close dresser

Task: Put up decoration Step one: Walk to home office Step two: Walk to drawing Step three: Find drawing Step four: Find centerpiece Step five: Grab centerpiece Step six: Walk to wall Step seven: Grab drawing Step eight: Put drawing on wall Step nine: Find centerpiece Step ten: Grab centerpiece Step eleven: Walk to table Step twelve: Put centerpiece on table

Task: Make bed

Step one: Walk to bedroom Step two: Walk to bed Step three: Find sheets

Step four: Grab sheets

Step five: Pull sheets

Task: Scrubbing living room tile floor is once week activity for me Step one: Find mop Step two: Turn to mop Step three: Point at mop

Step four: Wash mop Step five: Turn to mop Step six: Look at mop

Task: Read yourself to sleep Step one: Walk to bedroom Step two: Walk to novel Step three: Find novel Step four: Grab novel Step five: Find bed Step six: Sit on bed

Step seven: Find bookmark Step eight: Grab bookmark Step nine: Read novel Step ten: Put bookmark on novel Step eleven: Sleep

Task: Change clothes Step one: Walk to bedroom Step two: Walk to closet Step three: Find clothes Step four: Grab clothes Step five: Find chair Step six: Sit on chair Step seven: Change clothes

Task: Put up decoration Step one: Walk to home office Step two: Walk to decoration Step three: Find decoration Step four: Grab decoration Step five: Find chair Step six: Sit on chair Step seven: Put up decoration

Task: Make bed Step one: Walk to bedroom Step two: Walk to bed Step three: Find sheets Step four: Find blanket Step five: Find pillow Step six: Put sheets on bed Step seven: Put blanket on bed Step eight: Put pillow on bed

Task: Scrubbing living room tile floor is once week activity for me Step one: Walk to living room Step two: Walk to tile floor Step three: Find scrub brush Step four: Grab scrub brush Step five: Scrub tile floor Step six: Put down scrub brush Step seven: Walk to kitchen

Task: Read yourself to sleep Step one: Walk to bedroom Step two: Walk to bed Step three: Find book Step four: Grab book Step five: Find chair Step six: Sit on chair Step seven: Read book Step eight: Sleep

Task: Change clothes Step one: Walk to bedroom Step two: Walk to dresser Step three: Find dresser Step four: Open dresser Step five: Find pants Step six: Grab pants Step seven: Put on pants Step eight: Find shirt Step nine: Grab shirt Step ten: Put on shirt Step eleven: Close dresser

Task: Put up decoration Step one: Walk to living room Step two: Walk to table

Task: Make bed Step one: Stand up Step two: Find sheets Step three: Find blanket Step four: Find pillow

Step five: Find comforter Step six: Find bed

Task: Scrubbing living room tile floor is once week activity for me Step one: Walk to living room Step two: Walk to mop Step three: Find mop Step four: Grab mop Step five: Walk to bathroom Step six: Find bucket Step seven: Switch on faucet

Task: Read yourself to sleep Step one: Walk to bedroom Step two: Walk to bed Step three: Lie on bed Step four: Sleep Step five: Read book

Task: Hand washing Step one: Walk to bathroom Step two: Walk to sink Step three: Find faucet Step four: Switch on faucet

Step five: Find soap Step six: Grab soap Step seven: Find hands both Step eight: Scrub hands both Step nine: Put back soap Step ten: Wash hands both Step eleven: Switch off faucet Step twelve: Find towel Step thirteen: Grab towel Step fourteen: Wipe hands both

Task: Throw away paper Step one: Walk to home office Step two: Walk to desk Step three: Find desk Step four: Turn to desk Step five: Find chair Step six: Sit on chair Step seven: Find check Step eight: Grab check Step nine: Squeeze check Step ten: Stand up

Step eleven: Walk to trashcan Step twelve: Put check on trashcan

Task: Take off shoes

Step one: Walk to home office Step two: Walk to shoes

Step three: Find shoes

Step four: Find shoes

Step five: Take off shoes Step six: Grab shoes

Step seven: Find mat Step eight: Put shoes on mat

Task: Hang keys

Step one: Walk to bedroom Step two: Walk to dresser Step three: Find purse Step four: Grab purse Step five: Open purse Step six: Find keys Step seven: Grab keys Step eight: Find bowl Step nine: Put keys on bowl Step ten: Close purse Step eleven: Put back purse

Task: Hand washing Step one: Walk to bathroom Step two: Walk to sink Step three: Turn on faucet Step four: Grab soap Step five: Wash hands Step six: Rinse hands Step seven: Dry hands

Task: Throw away paper Step one: Walk to home office Step two: Walk to wastebasket Step three: Find wastebasket Step four: Grab wastebasket

Step five: Walk to desk

Step six: Drop paper in wastebasket

Task: Take off shoes Step one: Walk to home office Step two: Walk to novel Step three: Find novel Step four: Grab novel

Step five: Find chair

Step six: Sit on chair

Step seven: Read novel Task: Hang keys Step one: Walk to home office Step two: Walk to key hook Step three: Find key hook Step four: Grab key hook Step five: Find keys

Step six: Hang keys on key hook Step seven: Walk to front door

Step eight: Leave house

Task: Hand washing Step one: Walk to bathroom Step two: Walk to sink Step three: Find faucet Step four: Turn to faucet Step five: Find hands both Step six: Wash hands both

Task: Throw away paper Step one: Walk to home office Step two: Walk to table Step three: Find table Step four: Turn to table Step five: Find paper Step six: Grab paper Step seven: Walk to trashcan Step eight: Open trashcan Step nine: Put paper on trashcan Step ten: Close trashcan


## Task: Take off shoes Step one: Walk to home office Step two: Walk to shoes Step three: Find shoes

Task: Hang keys Step one: Walk to home office Step two: Walk to table Step three: Find keys Step four: Grab keys

Step five: Walk to wall

Step six: Find hanger Step seven: Put keys on hanger


## Task: Make popcorn Step one: Walk to dining room Step two: Walk to food Step three: Find food Step four: Grab food

Step five: Walk to microwave Step six: Turn to microwave Step seven: Open microwave Step eight: Put food in microwave Step nine: Close microwave

Step ten: Switch on microwave


## Task: Receive credit card

Step one: Walk to home office Step two: Walk to envelope Step three: Find envelope

Step four: Grab envelope Step five: Walk to home office Step six: Walk to scissors

Step seven: Find scissors Step eight: Open envelope Step nine: Find credit card

Step ten: Grab credit card


## Task: Read to child

Step one: Walk to bedroom Step two: Walk to child Step three: Find child Step four: Greet child

Step five: Walk to filing cabinet Step six: Open filing cabinet Step seven: Find novel

Step eight: Grab novel

Step nine: Walk to chair Step ten: Pull chair Step eleven: Sit on chair Step twelve: Turn to novel Step thirteen: Look at novel Step fourteen: Turn to novel Step fifteen: Point at novel Step sixteen: Turn to novel

Step seventeen: Point at novel Step eighteen: Read novel Step nineteen: Read novel

Step twenty: Read novel

Task: Make popcorn Step one: Walk to kitchen Step two: Walk to microwave Step three: Open microwave Step four: Put bag of popcorn in microwave Step five: Close microwave Step six: Push buttons on microwave Step seven: Wait for popcorn to pop Step eight: Get bowl out of cupboard Step nine: Get butter out of fridge Step ten: Get salt out of cupboard Step eleven: Pour popcorn into bowl Step twelve: Add butter and salt to bowl Step thirteen:

Task: Receive credit card Step one: Walk to mailbox Step two: Open mailbox Step three: Grab credit card Step four: Walk to home office Step five: Walk to desk

Step six: Put credit card on desk Step seven: Sit at desk

Step eight: Look at credit card


## Task: Read to child Step one: Walk to home office Step two: Walk to novel Step three: Find novel Step four: Grab novel

Step five: Find chair

Step six: Sit on chair

Step seven: Read novel


## Task: Make popcorn Step one: Walk to kitchen Step two: Walk to microwave Step three: Find microwave Step four: Open microwave

Task: Receive credit card Step one: Walk to home office Step two: Walk to cabinet Step three: Find cabinet Step four: Open cabinet


## Task: Read to child Step one: Walk to child Step two: Read book

Task: Eat cheese Step one: Walk to dining room Step two: Walk to freezer Step three: Open freezer Step four: Find cheese Step five: Grab cheese

Step six: Eat cheese

Task: Unload various items from pockets and place them in bowl on table Step one: Walk to home office Step two: Walk to table Step three: Find bowl Step four: Grab bowl Step five: Put bowl on table Step six: Find pants Step seven: Find bills Step eight: Grab bills

Step nine: Find phone Step ten: Grab phone


## Task: Switch on lamp

Step one: Walk to bedroom Step two: Walk to floor lamp Step three: Find floor lamp

Step four: Switch on floor lamp

Task: Take jacket off Step one: Walk to bedroom Step two: Walk to jacket Step three: Find jacket Step four: Find jacket Step five: Take off jacket Step six: Find dresser Step seven: Open dresser

Step eight: Close dresser

Task: Eat cheese Step one: Walk to kitchen Step two: Walk to refrigerator Step three: Open refrigerator Step four: Grab cheese Step five: Eat cheese

Task: Unload various items from pockets and place them in bowl on table Step one: Walk to home office Step two: Walk to bowl on table Step three: Find bowl on table Step four: Grab bowl on table Step five: Unload various items from pockets and place them in bowl on table Task: Switch on lamp Step one: Walk to lamp Step two: Switch on lamp Step three: Walk to chair Step four: Sit on chair Step five: Read book Task: Take jacket off Step one: Walk to home office Step two: Walk to jacket Step three: Find jacket Step four: Grab jacket Step five: Find chair Step six: Sit on chair Step seven: Take jacket off

Task: Eat cheese Step one: Walk to dining room Step two: Walk to table Step three: Find table Step four: Turn to table Step five: Find chair Step six: Sit on chair Step seven: Find food Step eight: Grab food Step nine: Find plate Step ten: Put food on plate

Task: Unload various items from pockets and place them in bowl on table Step one: Find bowl Step two: Turn to bowl Step three: Point at bowl Step four: Wash bowl

Task: Switch on lamp. Step One: Walk to bedroom. Step Two: Walk to floor lamp. Step Three: Find floor lamp. Step Four: Turn to floor lamp. Step Five: Switch on floor lamp. Step Six: Find bed. Step Seven: Lie on bed. Task: Take jacket off. Step One: Walk to home office. Step Two: Walk to jacket. Step Three: Find jacket.