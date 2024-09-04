## Working Memory Capacity of ChatGPT: An Empirical Study

Abstract

One Working memory is a critical aspect of both human intelligence and artificial intelligence, serving as a workspace for the temporary storage and manipulation of information. In this paper, we systematically assess the working memory capacity of ChatGPT, a large language model developed by OpenAI, by examining its performance in verbal and spatial n-back tasks under various conditions. Our experiments reveal that ChatGPT experiences significant declines in performance as n increases (which necessitates more information to be stored in working memory), suggesting a limit to the working memory capacity strikingly similar to that of humans. Furthermore, we investigate the impact of different instruction strategies on ChatGPT's performance and observe that the fundamental patterns of a capacity limit persist. From our empirical findings, we propose that n-back tasks may serve as tools for benchmarking the working memory capacity of large language models and hold potential for informing future efforts aimed at enhancing AI working memory and deepening our understanding of human working memory through AI models.


## One Introduction

The advent of large language models like ChatGPT and GPT-four has propelled the pursuit of artificial general intelligence and unveiled human-level abilities that warrant further exploration. Among these abilities is the capacity to retain contextual information while engaging in multi-turn conversations, suggesting the presence of working memory in these LLMs.

In cognitive sciences, working memory is usually defined as the ability to temporarily store and manipulate information in mind. It is widely regarded as a critical element of human intelligence, as it underlies various higher-order cognitive processes such as reasoning, problem-solving, and language comprehension.

Studies on human participants have revealed a fundamental capacity limit in working memory.

However, there has not been a consensus on why and how working memory capacity is limited.


## Among many theories, the executive attention hypothesis suggests that working memory

requires using attention to maintain or suppress information, and the constraint on working memory capacity is not really about memory storage per se, but about the capacity for controlled, sustained

Supporting evidence of the executive attention hypothesis includes results from the n-back task,

which is arguably the current gold standard measure of working memory capacity in the cognitive neuroscience literature. The n-back task, initially developed by Kirchner,

requires participants to monitor a continuous stream of stimuli, and to decide for each stimulus whether it matches the one n steps back in the stream. The participants in this task must, therefore, continuously update their mental representation of the target items while also dropping now irrelevant items from consideration. So,

37 representation of the target items while also dropping now irrelevant items from consideration. So,

some executive attention processes are required in addition to storage. Typical human performance

(measured by accuracy) as a function of n is shown in Figure two, where we used the data presented in

41 In humans, working memory capacity has proved to be closely related with fluid intelligence or general intelligence, placing working memory at the core of human intelligence.

However, in artificial intelligence, there has not been a consensus as to which metrics should be accepted as an intelligence index when evaluating and comparing cognitive abilities of LLMs. In the current

44 However, in artificial intelligence, there has not been a consensus as 45 to which metrics should be accepted as an intelligence index when 46 evaluating and comparing cognitive abilities of LLMs. In the current study, we define working memory of LLMs as an emergent ability to selectively maintain and manipulate information for ongoing cognitive processes, echoing the executive attention hypothesis in cognitive sciences. We propose that the performance of LLMs on n-back tasks can be a reliable metric for assessing their working memory capacity, which in turn might reflect the general intelligence

To demonstrate this, we used ChatGPT as a representative of LLMs, and designed two categories of the n-back task to evaluate its working memory capacity. Our results revealed strikingly consistent patterns of a capacity limit across multiple experimental conditions, hinting at possibly similar mechanisms of working memory in humans and LLMs. We believe this finding is important for both cognitive scientists and LLM

researchers, and hope that this could guide future endeavors of better understanding why human working memory capacity is limited and building more intelligent LLMs with better working memory capacity.


## Two Related Works

Working memory has long been a subject of study in human and animal cognition. Unlike long-term memory, which is stored in long-term synaptic weights in the neural system, working memory is believed to be maintained by sustained activations of neurons in prefrontal cortex.

This working mechanism bears striking resemblance to the in-context learning ability found in LLMs.

However, the investigation of working memory in LLMs remains largely unexplored. Therefore,

exploring the working memory capacity of LLMs holds great interest and significance, as it can contribute to the development of more powerful models.

Large language models have played a crucial role in achieving impressive performance across a wide range of downstream tasks. While fine-tuning has emerged as a popular approach for transferring to new tasks, it can be impractical to apply this method to extremely large models and/or

Note that both verbal and spatial tasks are compatible with these variants; we illustrate using verbal tasks without loss of generality.

showcasing the remarkable few-shot learning capabilities of large language models without requiring weight updates through gradient descent. Since its introduction, research on in-context learning in language models has garnered significant attention from both academia and industry. Previous studies have presented various approaches to leverage the in-context learning ability of language models,

including selecting labeled examples for demonstrations, meta-training with an explicit in-context learning objective, and exploring the variant of in-context learning that involves learning to follow instructions.

However, relatively less work has been done to calibrate the working memory capacity of LLMs and understand the limitation of in-context learning ability. To the best of our knowledge, this paper is the first that provides an empirical analysis from the neuroscience view that investigates the working memory ability of LLMs.


## Three Methods

We devised two categories of n-back tasks involving verbal and spatial working memory respectively, and prompted ChatGPT to complete the

88 tively, and prompted ChatGPT (using the OpenAI API, <LATEX>= ^ { \prime \prime } g p t - 3 . 5 - t u r b o ^ { \prime \prime }</LATEX> to complete the tasks in a trial-by-trial manner. For both categories, we have a base version task, and several variants derived from the base version to further test the model's performance under different conditions.


## Three point one Verbal n n-back experiments

In the base version of the verbal n-back task, for n equals one, two, three, respectively, we generated fifty blocks of letter sequences using an alphabet commonly found in the literature ("bcdfghjklnpqrstvwxyz').

Each block contained a sequence of twenty-four letters, which are presented one at a time as user input to the

API. We included eight match trials and sixteen nonmatch trials in each block. The LLM was instructed to

Ninety-six respond with M double prime on match trials and "-" on nonmatch trials. Apart from the above base version, we

Ninety-seven further explored the behavioural performance of ChatGPT with the following modifications of the Ninety-eight task presented in Figure three:

Ninety-nine. We added three quad dash six noise symbols to the input on every trial to examine the LLM's behaviour when to make it impossible to get the correct answer by simply doing string match between stimulus inputs.

One hundred two. In human behavioural studies, a common strategy to improve participants' performance is to One hundred three provide feedback after each trial. Here in the task, after the LLM provided a response One hundred four for the previous trial, we added feedback on whether its response was correct or wrong One hundred five alongside the stimulus input of the current trial.

One hundred six. Chain-of-thought (CoT) prompting has proved helpful in eliciting reasoning in LLMs. Here we instructed the LLM to think step by step when giving a response.


## One hundred eight. Three point two Spatial n-back experiments

One hundred nine. Although in its very nature, LLMs are text-based, but at least one study has demonstrated that they One hundred ten have spatial reasoning abilities. To build on this promising trail and further examine the spatial working memory of ChatGPT. In the base version of the spatial n-back task, we constructed a three by three One hundred eleven

One hundred twelve grid using ASCII characters (see Table two for detailed prompts). For n equals one, two, three respectively, we

One hundred thirteen generated fifty blocks of grid sequences each featuring a letter X in one of the nine positions. Note that

One hundred fourteen the letter X here was arbitrarily chosen to represent an occupied spatial location textually and could One hundred fifteen be substituted by any other letter or symbol. Each block contains twenty-four grids, including eight match trials

One hundred seventeen on match trials and "-" on nonmatch trials. We further explored the spatial working memory capacity

One hundred eighteen of ChatGPT with the following modifications of the task:

As in the variants of verbal N-back tasks, we also have "spatial-with-noise," "spatial-with-feedback," and "spatial-with-CoT-reasoning" versions of the task. The prompts for the the with-feedback and with-reasoning versions were basically the same as those for the corresponding verbal tasks. For the spatial-with-noise version, we added a noise character (chosen from "# dollar percent and at ") to one to three unoccupied locations in the three by three grid on every trial. This is a first step to examine the LLM's spatial working memory when it was not able to get the correct answer by simply doing string match.

To further confirm that the LLM can really reason in a spatial way rather than trivially performing some kind of string match under the hood, we further introduced two variants that specifically require abstract spatial reasoning; an model that would otherwise simply match strings would have failed. To achieve so, in these two tasks, a match is defined as when the location of the letter X is in the same row or column as the X N trials ago. The difference is whether identical locations also count as a match. We expect the version excluding identical locations to be harder for the LLM to perform.

We also explored whether the size of the grid three by three, four by four, five by five would influence the LLM's performance. To the best of our knowledge, there hasn't been human studies exploring how the number of all possible spatial locations would impact behavioral performance. In light of this, we didn't have specific assumptions for how the LLM would perform differently under these scenarios.


## Four Results

To analyse the model's performance on our experiments, we used four widely accepted performance metrics reported in numerous human behavioral studies:

Hit Rate: It is a performance measure used in various fields, including computer science, statistics,

and information retrieval. It represents the proportion of correct or successful outcomes out of the total number of targets or true positives. Mathematically, it is calculated by

Hit Rate equals Number of True Positives plus Number of False Negatives divided by Number of True Positives

False Alarm Rate: It quantifies the frequency at which a system or algorithm incorrectly identifies a negative outcome as positive. Mathematically, it is calculated by

Number of False Positives

False Alarm Rate equals Number of False Positives plus Number of True Negatives

Accuracy: It is a commonly used performance metric that measures the correctness or reliability of a system, model, or algorithm in making predictions or classifications. It represents the proportion of correct predictions or classifications out of the total number of predictions or classifications made.

Mathematically, it is calculated by

Accuracy equals Number of Correct Responses divided by Total Number of Trials

Detection Sensitivity d prime: It is a statistical measure used to assess the ability of a diagnostic test or classification model to accurately distinguish between two groups or conditions. It quantifies the extent to which the test or model can correctly identify positive cases relative to negative cases while minimizing false positives and false negatives. Mathematically, it is calculated by d prime equals Z Hit Rate minus Z False Alarm Rate where Z Hit Rate and Z False Alarm Rate represent the z-score of Hit Rate and False Alarm Rate, respectively.

In the current study, we did fifty blocks of tests for N equals one, two, three in each experiment, which allows us to calculate the standard error of mean and draw error bars to visualize the reliability of our findings.


## Four point one Verbal N-back experiments

In all versions of the task, we observed a performance pattern strikingly consistent with human participants, with the LLM's performance declining significantly when N increased from one to three five,

as shown in hit rate, accuracy, and d prime. Compared to the base version, the verbal-with-noise variant significantly made the LLM's performance worse. We observe that while chain-of-thought prompting has significantly improved the performance of the language models in verbal task variants, feedback on whether the model has performed correctly in the previous task failed to meaningfully improve performance.


## Four point two Spatial N-back experiments

In the four versions spatial tasks corresponding to the above verbal tasks, same patterns of performance were basically replicated. CoT reasoning significantly made the LLM perform better,

adding noise made the model perform worse. But in all versions of the task, ChatGPT suffered significant declines in performance as N increases.

When further evaluated whether the LLM could conduct abstract spatial reasoning. The results confirmed so. In line with our prediction, the LLM performed worse when identical locations are not defined a match, which means more abstract spatial reasoning would be required in this scenario.

Our explorations on the effect of grid size on the model performance yielded interesting results, too.

The LLM performed better when grid size was larger, especially as seen from the hit rate of d prime results in Figure eight.


## Five Discussion

We argue that our experimental results firmly point to the conclusion that ChatGPT has limited working memory capacity similar to humans. Even various prompting techniques such as the provision of feedback and the use of state-of-the-art chain-of-thought prompting may be used to improve its performance, the trend of performance decline as a function of increasing N still bears striking resemblance to human performance shown in numerous previous work. The consistent pattern of performance declines thus might be reflecting a fundamental constraint emerged from the architecture of the model, suggesting a possibility that the low-level working memory mechanism of LLMs might be similar to human working memory at least in some aspects.

In neuroscience, there are many unsolved problems on working memory, especially where and how working memory is encoded and maintained in the brain and why working memory capacity is limited. We propose that, in light of the above observation, ChatGPT and or other large language models of similar calibre could be potentially used and tested as a modeling platform for studying human working memory, just as what neuroscientists have done in recent years using other artificial neural networks. Furthermore, future efforts aimed at interpreting activity of artificial neurons in LLMs like ChatGPT would probably hold potential in informing the mechanisms of human working memory.

Our work also has some limitations. It would be important to test other LLMs on the same task we used here, to test whether they exhibit similar performance patterns and whether they have different working memory capacity. It would also be helpful to test ChatGPT on other working memory span tasks used in cognitive sciences to address the generalizability of N-back tasks as measurement tools.

Two hundred. Last but not the least, the current work opens a brand new topic in probing the cognitive abilities of LLMs: if the working memory capacity of LLMs are fundamentally limited, then why? How their architecture is related to the capacity limit? One possible explanation would be the self-attention mechanism used in the Transformer architecture. The self-attention mechanism computes a weighted sum of input elements, where each element's weight is determined by its relevance to other elements in the sequence. While this approach allows the model to focus on relevant information, it may also lead to a diffusion of information across multiple input elements, making it challenging to maintain and access specific pieces of information as N increases in N-back tasks.