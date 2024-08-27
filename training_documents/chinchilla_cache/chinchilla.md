## Training Compute-Optimal Large Language Models

We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over four hundred language models ranging from seventy million to over sixteen billion parameters on five to five hundred billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted compute-optimal model, Chinchilla, that uses the same compute budget as Gopher but with seventy billion parameters and four times more more data. Chinchilla uniformly and significantly outperforms Gopher, two hundred eighty billion, GPT-three, one hundred seventy-five billion, Jurassic-one, one hundred seventy-eight billion, and Megatron-Turing NLG, five hundred thirty billion, on a large range of downstream evaluation tasks. This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of sixty-seven point five percent on the MMLU benchmark, greater than a seven percent improvement over Gopher.


## One. Introduction

Recently a series of Large Language Models have been introduced, with the largest dense language models now having over five hundred billion parameters. These large autoregressive transformers have demonstrated impressive performance on many tasks using a variety of evaluation protocols such as zero-shot, few-shot, and fine-tuning.

The compute and energy cost for training large language models is substantial and rises with increasing model size. In practice, the allocated training compute budget is often known in advance: how many accelerators are available and for how long we want to use them. Since it is typically only feasible to train these large models once, accurately estimating the best model hyperparameters for a given compute budget is critical.

Kaplan et al. showed that there is a power law relationship between the number of parameters in an autoregressive language model and its performance. As a result, the field has been training larger and larger models, expecting performance improvements. One notable conclusion is that large models should not be trained to their lowest possible loss to be compute optimal. Whilst we reach the same conclusion, we estimate that large models should be trained for many more training tokens than recommended by the authors. Specifically, given a ten times increase computational budget, they suggest that the size of the model should increase five point five times while the number of training tokens should only increase one point eight times. Instead, we find that model size and the number of training tokens should be scaled in equal proportions.

Following Kaplan et al. and the training setup of GPT-three, many of the recently trained large models have been trained for approximately three hundred billion tokens, in line with the approach of predominantly increasing model size when increasing compute.

In this work, we revisit the question: Given a fixed FLOPs budget, how should one trade-off model size and the number of training tokens? To answer this question, we model the final pre-training loss as a function of the number of model parameters, and the number of training tokens. Since the computational budget is a deterministic function FLOPs of the number of seen training tokens and model parameters, we are interested in minimizing the loss under the constraint FLOPs equals the computational budget.

Optimal number of parameters, optimal number of tokens describe the optimal allocation of a computational budget. We empirically estimate these functions based on the losses of over four hundred models, ranging from under seventy million to over sixteen billion parameters, and trained on five billion to over four hundred billion tokens - with each model configuration trained for several different training horizons. Our approach leads to considerably different results than that of Kaplan et al.. We highlight our results in Figure one and how our approaches differ in Section two.

The functions Nopt(C), and Dopt (C) describe the optimal allocation of a computational budget C. We empirically estimate these functions based on the losses of over 400 models, ranging from under 70M to over 16B parameters, and trained on 5B to over 400B tokens - with each model configuration trained for several different training horizons. Our approach leads to considerably different results than that of Kaplan et al. (2020). We highlight our results in Figure 1 and how our approaches differ in Section 2.

Based on our estimated compute-optimal frontier, we predict that for the compute budget used to train Gopher, an optimal model should be four times smaller, while being trained on four times more tokens. We verify this by training a more compute-optimal seventy billion model, called Chinchilla, on one point four trillion tokens. Not only does Chinchilla outperform its much larger counterpart, Gopher, but its reduced model size reduces inference cost considerably and greatly facilitates downstream uses on smaller hardware. The energy cost of a large language model is amortized through its usage for inference and fine-tuning. The benefits of a more optimally trained smaller model, therefore, extend beyond the immediate benefits of its improved performance.


## Two. Related Work

Large language models. A variety of large language models have been introduced in the last few years. These include both dense transformer models and mixture-of-expert models. The largest dense transformers have passed five hundred billion parameters. The drive to train larger and larger models is clear - so far increasing the size of language models has been responsible for improving the state-of-the-art in many language modelling tasks. Nonetheless, large language models face several challenges, including their overwhelming computational requirements and the need for acquiring more high-quality training data. In fact, in this work we find that larger, high quality datasets will play a key role in any further scaling of language models.

Modelling the scaling behavior. Understanding the scaling behaviour of language models and their transfer properties has been important in the development of recent large models. Kaplan et al. first showed a predictable relationship between model size and loss over many orders of magnitude. The authors investigate the question of choosing the optimal model size to train for a given compute budget. Similar to us, they address this question by training various models. Our work differs from Kaplan et al. in several important ways. First, the authors use a fixed number of training tokens and learning rate schedule for all models; this prevents them from modelling the impact of these hyperparameters on the loss. In contrast, we find that setting the learning rate schedule to approximately match the number of training tokens results in the best final loss regardless of model size-see Figure A one. For a fixed learning rate cosine schedule to one hundred thirty billion tokens, the intermediate loss estimates are therefore overestimates of the loss of a model trained with a schedule length matching. Using these intermediate losses results in underestimating the effectiveness of training models on less data than one hundred thirty billion tokens, and eventually contributes to the conclusion that model size should increase faster than training data size as compute budget increases. In contrast, our analysis predicts that both quantities should scale at roughly the same rate. Secondly, we include models with up to sixteen billion parameters, as we observe that there is slight curvature in the FLOP-loss frontier-see Appendix E-in fact, the majority of the models used in our analysis have more than five hundred million parameters, in contrast the majority of runs in Kaplan et al. are significantly smaller-many being less than one hundred million parameters.

Recently, Clark et al. specifically looked into the scaling properties of Mixture of Expert

Estimating hyperparameters for large models. The model size and the number of training tokens are not the only two parameters to choose when selecting a language model and a procedure to train it. Other important factors include learning rate, learning rate schedule, batch size, optimiser, and width-to-depth ratio. In this work, we focus on model size and the number of training steps, and we rely on existing work and provided experimental heuristics to determine the other necessary hyperparameters. Yang et al. investigates how to choose a variety of these parameters for training an autoregressive transformer, including the learning rate and batch size. McCandlish et al. finds only a weak dependence between optimal batch size and model size. Shallue et al.; Zhang et al. suggest that using larger batch-sizes than those we use is possible. Levine et al. investigates the optimal depth-to-width ratio for a variety of standard model sizes. We use slightly less deep models than proposed as this translates to better wall-clock performance on our hardware.

Improved model architectures. Recently, various promising alternatives to traditional dense transformers have been proposed. For example, through the use of conditional computation large MoE models like the one point seven trillion parameter Switch transformer, the one point two trillion parameter GLaM model, and others, are able to provide a large effective model size despite using relatively fewer training and inference FLOPs. However, for very large models the computational benefits of routed models seems to diminish. An orthogonal approach to improving language models is to augment transformers with explicit retrieval mechanisms, as done by Borgeaud et al.; Guu et al.; Lewis et al. This approach effectively increases the number of data tokens seen during training. This suggests that the performance of language models may be more dependent on the size of the training data than previously thought.


## Three. Estimating the optimal parameter/training tokens allocation

We present three different approaches to answer the question driving our research: Given a fixed FLOPs budget, how should one trade-off model size and the number of training tokens? In all three cases we start by training a range of models varying both model size and the number of training tokens and use the resulting training curves to fit an empirical estimator of how they should scale. We assume a power-law relationship between compute and model size though future work may want to include potential curvature in this relationship for large model sizes. The resulting predictions are similar for all three methods and suggest that parameter count and number of training tokens should be increased equally with more compute - with proportions reported in Table Two. This is in clear contrast to previous work on this topic and warrants further investigation.

Four


## Three point one. Approach one: Fix model sizes and vary number of training tokens

In our first approach we vary the number of training steps for a fixed family of models (ranging from seventy million to over ten billion parameters), training each model for four different number of training sequences. From these runs, we are able to directly extract an estimate of the minimum loss achieved for a given number of training FLOPs. Training details for this approach can be found in Appendix D.

For each parameter count N we train four different models, decaying the learning rate by a factor of ten times over a horizon (measured in number of training tokens) that ranges by a factor of sixteen times. Then, for each run, we smooth and then interpolate the training loss curve. From this, we obtain a continuous mapping from FLOP count to training loss for each run. Then, for each FLOP count, we determine which run achieves the lowest loss. Using these interpolants, we obtain a mapping from any FLOP count C, to the most efficient choice of model size N and number of training tokens D such that FLOPs(N,D) equals C. At one thousand five hundred logarithmically spaced FLOP values, we find which model size achieves the lowest loss of all models along with the required number of training tokens. Finally, we fit power laws to estimate the optimal model size and number of training tokens for any given amount of compute, obtaining a relationship Nopt proportional to C to the power of a and Dopt proportional to C to the power of b. We find that a equals zero point five zero and b equals zero point five zero-as summarized in Table two. In Section D. four, we show a head-to-head comparison at ten to the twenty-one FLOPs, using the model size recommended by our analysis and by the analysis of Kaplan et al. using the model size we predict has a clear advantage.


## Three point two. Approach two: IsoFLOP profiles

In our second approach we vary the model size for a fixed set of nine different training FLOP counts (ranging from six times ten to the power of eighteen to three times ten to the power of twenty-one FLOPs), and consider the final training loss for each point. In contrast with Approach one that considered points (N, D, L) along the entire training runs. This allows us to directly answer the question: For a given FLOP budget, what is the optimal parameter count?

For each FLOP budget, we plot the final loss (after smoothing) against the parameter count in Figure three (left). In all cases, we ensure that we have trained a diverse enough set of model sizes to see a clear minimum in the loss. We fit a parabola to each IsoFLOPs curve to directly estimate at what model size the minimum loss is achieved (Figure three (left)). As with the previous approach, we then fit a power law between FLOPs and loss-optimal model size and number of training tokens. Again, we fit exponents of the form Nopt proportional to C to the power of a and Dopt proportional to C to the power of b and we find that a equals zero point four nine and b equals zero point five one-as summarized in Table two.


## Three point three. Approach three: Fitting a parametric loss function

Lastly, we model all final losses from experiments in Approach one and two as a parametric function of model parameter count and the number of seen tokens. Following a classical risk decomposition, we propose the following functional form

L(N, D) equals E plus N to the power of a plus D to the power of b.

The first term captures the loss for an ideal generative process on the data distribution, and should correspond to the entropy of natural text. The second term captures the fact that a perfectly trained transformer with N parameters underperforms the ideal generative process. The final term captures the fact that the transformer is not trained to convergence, as we only make a finite number of optimisation steps, on a sample of the dataset distribution.

Model fitting. To estimate (A, B, E, a, B), we minimize the Huber loss between the predicted and observed log loss using the L-BFGS algorithm:

Runs L equals sum of Huber's log of (L(Ni, Di) minus log Li).

We account for possible local minima by selecting the best fit from a grid of initialisations. The Huber loss is robust to outliers, which we find important for good predictive performance over held-out data points. Section D. two details the fitting procedure and the loss decomposition.

Efficient frontier. We can approximate the functions Nopt and Dopt by minimizing the parametric loss L under the constraint FLOPs(N, D) approximately equal to six N D. The resulting Nopt and Dopt balance the two terms in Equation (three) that depend on model size and data. By construction, they have a power-law form:

Nopt(C) equals (A) to the power of B divided by a, Dopt equals (A) to the power of B divided by b.

where G equals (A) to the power of B divided by a, b equals a divided by (a plus b).

We show contours of the fitted function L in Figure four (left), and the closed-form efficient computational frontier in blue. From this approach, we find that a equals zero point four six and b equals zero point five four-as summarized in Table two.


## Three point four. Optimal model scaling

We find that the three approaches, despite using different fitting methodologies and different trained models, yield comparable predictions for the optimal scaling in parameters and tokens with FLOPs. All three approaches suggest that as compute budget increases, model size and the amount of training data should be increased in approximately equal proportions. The first and second approaches yield very similar predictions for optimal model sizes. The third approach predicts even smaller models being optimal at larger compute budgets. We note that the observed points (L, N, D) for low training FLOPs have larger residuals L minus L(N, D) than points with higher computational budgets. The fitted model places increased weight on the points with more FLOPs-automatically considering the low-computational budget points as outliers due to the Huber loss. As a consequence of the empirically observed negative curvature in the frontier C is proportional to Nopt, this results in predicting a lower Nopt than the two other approaches.

In Table three we show the estimated number of FLOPs and tokens that would ensure that a model of a given size lies on the compute-optimal frontier. Our findings suggests that the current generation of large language models are considerably over-sized, given their respective compute budgets. For example, we find that a one hundred seventy-five billion parameter model should be trained with a compute budget of four point four times ten to the power of twenty-four FLOPs and on over four point two trillion tokens. A two hundred eighty billion Gopher-like model is the optimal model to train given a compute budget of approximately ten to the power of twenty-five FLOPs and should be trained on six point eight trillion tokens. Unless one has a compute budget of ten to the power of twenty-six FLOPs, a one trillion parameter model is unlikely to be the optimal model to train. Furthermore, the amount of training data that is projected to be needed is far beyond what is currently used to train large models, and underscores the importance of dataset collection in addition to engineering improvements that allow for model scale. While there is significant uncertainty extrapolating out many orders of magnitude, our analysis clearly suggests that given the training compute budget for many current large language models, smaller models should have been trained on more tokens to achieve the most performant model.

In Appendix C, we reproduce the IsoFLOP analysis on two additional datasets: C-four and GitHub code. In both cases we reach the similar conclusion that model size and number of training tokens should be scaled in equal proportions.


## Four. Chinchilla

Based on our analysis in Section Three, the optimal model size for the Gopher compute budget is somewhere between Forty and Seventy billion parameters. We test this hypothesis by training a model on the larger end of this range-Seventy Billion parameters-for One point Four Trillion tokens, due to both dataset and computational efficiency considerations. In this section we compare this model, which we call Chinchilla, to Gopher and other LLMs. Both Chinchilla and Gopher have been trained for the same number of FLOPs but differ in the size of the model and the number of training tokens.

While pre-training a large language model has a considerable compute cost, downstream fine-tuning and inference also make up substantial compute usage. Due to being Four times smaller than Gopher, both the memory footprint and inference cost of Chinchilla are also smaller.


## Four point one. Model and training details

The full set of hyperparameters used to train Chinchilla are given in Table Four. Chinchilla uses the same model architecture and training setup as Gopher with the exception of the differences listed below.

We train Chinchilla on MassiveText (the same dataset as Gopher) but use a slightly different subset distribution to account for the increased number of training tokens.

We use AdamW for Chinchilla rather than Adam as this improves the language modelling loss and the downstream task performance after finetuning.

We train Chinchilla with a slightly modified SentencePiece tokenizer that does not apply NFKC normalisation. The vocabulary is very similar-Ninety-Four point Fifteen percent of tokens are the same as those used for training Gopher. We find that this particularly helps with the representation of mathematics and chemistry, for example.

Whilst the forward and backward pass are computed in bfloat Sixteen, we store a float Thirty-Two copy of the weights in the distributed optimiser state. See Lessons Learned for additional details.

In Appendix G we show the impact of the various optimiser related changes between Chinchilla and Gopher. All models in this analysis have been trained on TPUvThree/TPUvFour with JAX and Haiku. We include a Chinchilla model card in Table AEight.


## Four point two. Results

We perform an extensive evaluation of Chinchilla, comparing against various large language models. We evaluate on a large subset of the tasks, shown in Table Five. As the focus of this work is on optimal model scaling, we included a large representative subset, and introduce a few new evaluations to allow for better comparison to other existing large models. The evaluation details for all tasks are the same as described.


## Four point two point one. Language modelling

Chinchilla significantly outperforms Gopher on all evaluation subsets of The Pile, as shown in Figure five. Compared to Jurassic-one hundred seventy-eight B, Chinchilla is more performant on all but two subsets- dm_mathematics and ubuntu_irc- see Table A five for a raw bits-per-byte comparison. On Wikitext one hundred three, Chinchilla achieves a perplexity of seven point one six compared to seven point seven five for Gopher. Some caution is needed when comparing Chinchilla with Gopher on these language modelling benchmarks as Chinchilla is trained on four times more data than Gopher and thus train/test set leakage may artificially enhance the results. We thus place more emphasis on other tasks for which leakage is less of a concern, such as MMLU and BIG-bench along with various closed-book question answering and common sense analyses.


## Four point two point two. MMLU

The Massive Multitask Language Understanding, or MMLU, benchmark consists of a range of exam-like questions on academic subjects. In Table six, we report Chinchilla's average five-shot performance on MMLU. On this benchmark, Chinchilla significantly outperforms Gopher despite being much smaller, with an average accuracy of sixty-seven point six percent, improving upon Gopher by seven point six percent. Remarkably, Chinchilla even outperforms the expert forecast for June twenty twenty-three of sixty-three point four percent accuracy. Furthermore, Chinchilla achieves greater than ninety percent accuracy on four different individual tasks- high school government and politics, international law, sociology, and U.S. foreign policy. To our knowledge, no other model has achieved greater than ninety percent accuracy on a subset.


## Four point two point three. Reading comprehension

On the final word prediction dataset LAMBADA, Chinchilla achieves seventy-seven point four percent accuracy, compared to seventy-four point five percent accuracy from Gopher and seventy-six point six percent from MT-NLG five hundred thirty B. On RACE-h and RACE-m, Chinchilla greatly outperforms Gopher, improving accuracy by more than ten percent in both cases-see Table seven.


## Four point two point four. BIG-bench

We analysed Chinchilla on the same set of BIG-bench tasks reported in Rae et al. Similar to what we observed in MMLU, Chinchilla outperforms Gopher on the vast majority of tasks (see Figure seven). We find that Chinchilla improves the average performance by ten point seven percent, reaching an accuracy of sixty-five point one percent versus fifty-four point four percent for Gopher. Of the sixty-two tasks we consider, Chinchilla performs worse than Gopher on only four- crash_blossom, dark_humor_detection,

mathematical_induction and logical_args. Full accuracy results for Chinchilla can be found, Chinchilla outperforms both Gopher and MT-NLG five hundred thirty B. Note that GPT-three and MT-NLG five hundred thirty B use a different prompt format than we do on RACE-h/m, so results are not comparable to Gopher and Chinchilla. On LAMBADA eighty-two point three seventy-one point six forty-seven point nine - Table seven | Reading comprehension. On RACE-h and RACE-m, Chinchilla considerably in Table A seven.


## Four point two point five. Common sense

We evaluate Chinchilla on various common sense benchmarks: PIQA, SIQA,

Winogrande, HellaSwag, and BoolQ

We find that Chinchilla outperforms both Gopher and GPT-three on all tasks and outperforms MT-NLG five hundred thirty B on all but one task-see Table eight.

On TruthfulQA, Chinchilla reaches forty-three point six percent, fifty-eight point five percent, and sixty-six point seven percent accuracy with zero-shot, five-shot, and ten-shot respectively. In comparison, Gopher achieved only twenty-nine point five percent zero-shot and forty-three point seven percent ten-shot accuracy. In stark contrast with the findings of Lin et al., the large improvements, fourteen point one percent in zero-shot accuracy, achieved by Chinchilla suggest that better modelling of the pre-training data alone can lead to substantial improvements on this benchmark.


## Four point two point six. Closed-book question answering

Results on closed-book question answering benchmarks are reported in Table nine. On the Natural

Questions dataset, Chinchilla achieves new closed-book state-of-the-art accuracies:

thirty-one point five percent five-shot and thirty-five point five percent sixty-four-shot, compared to twenty-one percent and twenty-eight percent respectively, for Gopher. On TriviaQA

we show results for both the filtered, previously used in retrieval and open-book work, and unfiltered set, previously used in large language model evaluations. In both cases, Chinchilla substantially out performs Gopher. On the filtered version, Chinchilla lags behind the open book state-of-the-art by only seven point nine percent. On the unfiltered set, Chinchilla outperforms

GPT-three-see Table nine.


## Four point two point seven. Gender bias and toxicity

Large Language Models carry potential risks such as outputting offensive language, propagating social biases, and leaking private information. We expect Chinchilla to carry risks similar to Gopher because Chinchilla is trained on the same data,

Chinchilla, Gopher, and MT-NLG five hundred thirty B on various Common Sense benchmarks. We see that Chinchilla BoolQ sixty point five percent seventy-eight point two percent ninety-one point four percent - Table eight | Zero-shot comparison on Common Sense benchmarks. We show a comparison between matches or outperforms Gopher and GPT-three on all tasks. On all but one Chinchilla outperforms the much larger MT-NLG five hundred thirty B model.

albeit with slightly different relative weights, and because it has a similar architecture. Here, we examine gender bias particularly gender and occupation bias) and generation of toxic language. We select a few common evaluations to highlight potential issues, but stress that our evaluations are not comprehensive and much work remains to understand, evaluate, and mitigate risks in large language models.

Gender bias. As discussed in Rae et al., large language models reflect contemporary and historical discourse about different groups (such as gender groups) from their training dataset, and we expect the same to be true for Chinchilla. Here, we test if potential gender and occupation biases manifest in unfair outcomes on coreference resolutions, using the Winogender dataset in a zero-shot setting. Winogender tests whether a model can correctly determine if a pronoun refers to different occupation words. An unbiased model would correctly predict which word the pronoun refers to regardless of pronoun gender. We follow the same setup as in Rae et al. (described further in Section H point three).

As shown in Table ten, Chinchilla correctly resolves pronouns more frequently than Gopher across all groups. Interestingly, the performance increase is considerably smaller for male pronouns (increase of three point two percent) than for female or neutral pronouns (increases of eight point three percent and nine point two percent respectively). We also consider gotcha examples, in which the correct pronoun resolution contradicts gender stereotypes (determined by labor statistics). Again, we see that Chinchilla resolves pronouns more accurately than Gopher. When breaking up examples by male/female gender and gotcha/not gotcha, the largest improvement is on female gotcha examples (improvement of ten percent). Thus, though Chinchilla uniformly overcomes gender stereotypes for more coreference examples than Gopher, the rate of improvement is higher for some pronouns than others, suggesting that the improvements conferred by using a more compute-optimal model can be uneven.

Sample toxicity. Language models are capable of generating toxic language-including insults, hate speech, profanities and threats. While toxicity is an umbrella term, and its evaluation in language models comes with challenges, automatic classifier scores can provide an indication for the levels of harmful text that a language model generates. Rae et al. found that improving language modelling loss by increasing the number of model parameters has only a negligible effect on toxic text generation (unprompted); here we analyze whether the same holds true for a lower language model loss achieved via more compute-optimal training. Similar to the protocol of Rae et al., we generate twenty-five thousand unprompted samples from Chinchilla, and compare their Perspective A P I toxicity score distribution to that of Gopher-generated samples. Several summary statistics indicate an absence of major differences: the mean (median) toxicity score for Gopher is zero point zero eight one (zero point zero six four), compared to zero point zero eight seven (zero point zero six six) for Chinchilla, and the ninety-fifth percentile scores are zero point two three zero for Gopher, compared to zero point two three eight for Chinchilla. That is, the large majority of generated samples are classified as non-toxic, and the difference between the models is negligible. In line with prior findings, this suggests that toxicity levels in unconditional text generation are largely independent of the model quality (measured in language modelling loss), i.e. that better models of the training dataset are not necessarily more toxic.


## Five. Discussion and Conclusion

The trend so far in large language model training has been to increase the model size, often without increasing the number of training tokens. The largest dense transformer, M T - N L G five hundred thirty billion, is now over three times larger than G P T-three's one hundred seventy billion parameters from just two years ago. However, this model, as well as the majority of existing large models, have all been trained for a comparable number of tokens-around three hundred billion. While the desire to train these mega-models has led to substantial engineering innovation, we hypothesize that the race to train larger and larger models is resulting in models that are substantially underperforming compared to what could be achieved with the same compute budget.

We propose three predictive approaches towards optimally setting model size and training duration, based on the outcome of over four hundred training runs. All three approaches predict that Gopher is substantially oversized and estimate that for the same compute budget a smaller model trained on more data will perform better. We directly test this hypothesis by training Chinchilla, a seventy-B parameter model, and show that it outperforms Gopher and even larger models on nearly every measured evaluation task.

Whilst our method allows us to make predictions on how to scale large models when given additional compute, there are several limitations. Due to the cost of training large models, we only have two comparable training runs at large scale (Chinchilla and Gopher), and we do not have additional tests at intermediate scales. Furthermore, we assume that the efficient computational frontier can be described by a power-law relationship between the compute budget, model size, and number of training tokens. However, we observe some concavity in log of N-opt at high compute budgets. This suggests that we may still be overestimating the optimal size of large models. Finally, the training runs for our analysis have all been trained on less than an epoch of data; future work may consider the multiple epoch regime. Despite these limitations, the comparison of Chinchilla to Gopher validates our performance predictions, that have thus enabled training a better (and more lightweight) model at the same compute budget.

Though there has been significant recent work allowing larger and larger models to be trained, our analysis suggests an increased focus on dataset scaling is needed. Speculatively, we expect that scaling to larger and larger datasets is only beneficial when the data is high-quality. This calls for responsibly collecting larger datasets with a high focus on dataset quality. Larger datasets will require extra care to ensure train-test set overlap is properly accounted for, both in the language modeling loss but also with downstream tasks. Finally, training for trillions of tokens introduces many ethical and privacy concerns. Large datasets scraped from the web will contain toxic language, biases, and private information. With even larger datasets being used, the quantity (if not the frequency) of such information increases, which makes dataset introspection all the more important. Chinchilla does suffer from bias and toxicity but interestingly it seems less affected than Gopher. Better understanding how performance of large language models and toxicity interact is an important future research question.

While we have applied our methodology towards the training of auto-regressive language models, we expect that there is a similar trade-off between model size and the amount of data in other modalities. As training large models is very expensive, choosing the optimal model size and training steps beforehand is essential. The methods we propose are easy to reproduce in new settings.


## Six. Acknowledgements

In Table A-one we show the training dataset makeup used for Chinchilla and all scaling runs. Note that both the MassiveWeb and Wikipedia subsets are both used for more than one epoch.

One key assumption is made on the cosine cycle length and the corresponding learning rate drop. We find that setting the cosine cycle length too much longer than the target number of training steps results in sub-optimally trained models, as shown in Figure A-one. As a result, we assume that an optimally trained model will have the cosine cycle length correctly calibrated to the maximum number of steps, given the FLOP budget; we follow this rule in our main analysis.

We show scaling results from an IsoFLOP analysis after training on two different datasets: Cfour and GitHub code, results are shown in Table A-two. For both set of experiments using subsets of MassiveText, we use the same tokenizer as the MassiveText experiments.

We find that the scaling behavior on these datasets is very similar to what we found on MassiveText, as shown in Figure A-two and Table A-two. This suggests that our results are independent of the dataset as long as one does not train for more than one epoch.


## D point one. Approach one: Fixing model sizes and varying training sequences

We use a maximum learning rate of two times ten to the negative fourth for the smallest models and one point twenty-five times ten to the negative fourth for the largest models. In all cases, the learning rate drops by a factor of ten times during training, using a cosine schedule. We make the assumption that the cosine cycle length should be approximately matched to the number of training steps. We find that when the cosine cycle overshoots the number of training steps by more than twenty-five percent, performance is noticeably degraded - see Figure A-one. We use Gaussian smoothing with a window length of ten steps to smooth the training curve.


## D point two. Approach three: Parametric fitting of the loss

In this section, we first show how Equation two can be derived. We repeat the equation below for clarity,

I of N and D equals E plus E plus M plus B.

based on a decomposition of the expected risk between a function approximation term and an optimization suboptimality term. We then give details on the optimization procedure for fitting the parameters.

Loss decomposition. Formally, we consider the task of predicting the next token Y is an element of Y based on the previous tokens in a sequence X is an element of Y with S varying from zero to S-max-the maximum sequence length. We consider a distribution P of X cross Y of tokens in Y and their past in X. A predictor F maps X to D of Y computes the probability of each token given the past sequence. The Bayes classifier, F-star, minimizes the cross-entropy of F of X with the observed tokens Y, with expectation taken on the whole data distribution. We let L be the expected risk.

L of F equals the expectation of log of F of X Y, and set F-star equals the argument of minimizing L of F.

The set of all transformers of size N, that we denote H-N, forms a subset of all functions that map sequences to distributions of tokens X to D of Y. Fitting a transformer of size N on the expected risk L of F amounts to minimizing such risk on a restricted functional space

F-N equals the argument of minimizing L of F.

When we observe a dataset X-one, Y-one with i equals one to P of size D, we do not have access to E-P, but instead to the empirical expectation E-P over the empirical distribution P-P. What happens when we are given D

data points that we can only see once, and when we constrain the size of the hypothesis space to be N-dimensional? We are making steps toward minimizing the empirical risk within a finite-dimensional functional space H-N:

I-D of F approximately E-P of log F of X Y, setting I-N and D equals the argument of minimizing L-D of F.

Eight.

We are never able to obtain F-W and D as we typically perform a single epoch over the dataset of size D. Instead, we obtain F-W and D, which is the result of applying a certain number of gradient steps based on the D data points-the number of steps to perform depends on the gradient batch size, for which we use well-tested heuristics.

Using the Bayes-classifier F-star, the expected-risk minimizer F-W and the "single-epoch empirical-risk minimizer" F-N and D, we can finally decompose the loss L of N and D into

L of N and D minus L of J of N and D equals L of F-star plus L of F of N minus L of F-star plus L of F-N and D minus L of F of N.

The loss comprises three terms: the Bayes risk, i.e. the minimal loss achievable for next-token prediction on the full distribution P, a.k.a the "entropy of natural text."; a functional approximation term that depends on the size of the hypothesis space; finally, a stochastic approximation term that captures the suboptimality of minimizing LD instead of L, and of making a single epoch on the provided dataset.

Expected forms of the loss terms. In the decomposition, the second term depends entirely on the number of parameters N that defines the size of the functional approximation space. On the set of two-layer neural networks, it is expected to be proportional to negative one. Finally, given that it corresponds to early stopping in stochastic first-order methods, the third term should scale as the convergence rate of these methods, which is lower-bounded by I and may attain the bound. This convergence rate is expected to be dimension-free and depends only on the loss smoothness; hence we assume that the second term only depends on D in the equation. Empirically, we find after fitting the equation that

L of N and D equals E plus N raised to the power of zero point three four plus B D raised to the power of zero point two eight.

with E equals one point six nine, A equals four hundred six point four, B equals four hundred ten point seven. We note that the parameter and data coefficients are both lower than two; this is expected for the data-efficiency coefficient but far from the known lower-bound. Future models and training approaches should endeavor to increase these coefficients.


## Fitting the decomposition to data. We effectively minimize the following problem

a, b, e, min Run Hubers LSE of a minus a log N, b minus b log D, e minus log L, where LSE is the log-sum-exp operator. We then set A, B, E equals exponential of a, exponential of b, exponential of e.

We use the LBFGS algorithm to find local minima of the objective above, started on a grid of initialization given by: a in the set zero point zero, zero point five and so on to two point zero, in the set zero point zero, zero point five and so on to two point zero, e in the set negative one point zero, negative zero point five and so on to one point zero, a in the set zero, five, and so on to twenty-five, and b in the set zero, five, and so on to twenty-five. We find that the optimal initialization is not on the boundary of our initialization sweep.

We use eight equals ten to the power of negative three for the Huber loss. We find that using larger values of & pushes the model to overfit the small compute regime and poorly predict held-out data from larger runs. We find that using a & smaller than ten to the power of negative three does not impact the resulting predictions.


## D point three. Predicted compute optimal frontier for all three methods

For Approaches two and three, we show the estimated model size and number of training tokens for a variety of compute budgets in Table A3. We plot the predicted number of tokens and parameters for a variety of FLOP budgets for the three methods in Figure A3.


## D point four. Small-scale comparison to Kaplan et al.

For ten to the power of twenty-one FLOPs, we perform a head-to-head comparison of a model predicted by Approach one and that predicted by Kaplan et al. For both models, we use a batch size of zero point five million tokens and a maximum learning rate of one point five times ten to the power of negative four that decays by ten times. From Kaplan et al., we find that the optimal model size should be four point six eight billion parameters. From our approach one, we estimate a two point eight six billion parameter model should be optimal. We train a four point seven four billion parameter and a two point eight zero billion parameter transformer to test this hypothesis, using the same depth-to-width ratio to avoid as many confounding factors as possible. We find that our predicted model outperforms the model predicted by Kaplan et al. as shown in Figure A4.


## E. Curvature of the FLOP-loss frontier

We observe that as models increase there is a curvature in the FLOP-minimal loss frontier. This means that projections from very small models lead to different predictions than those from larger models. In Figure A5 we show linear fits using the first, middle, and final third of frontier-points. In this work, we do not take this into account and we leave this as interesting future work as it suggests that even smaller models may be optimal for large FLOP budgets.


## F. FLOPs computation

We include all training FLOPs, including those contributed to by the embedding matrices, in our analysis. Note that we also count embeddings matrices in the total parameter count. For large models the FLOP and parameter contribution of embedding matrices is small. We use a factor of two to describe the multiply accumulate cost. For the forward pass, we consider contributions from:

· Embeddings

· Attention (Single Layer)

- Key, query and value projections: two times three times sequence length times d_model x (key_size × num_heads)

- Key at Query logits: two times seq_len times seq_len times (key_size times num_heads)

- Softmax: three times num_heads times seq_len times seq_len

- Softmax at query reductions: two times seq_len times seq_len times (key_size times num_heads)

- Final Linear: two times seq_len times (key_size times num_heads) times d_model

· Dense Block (Single Layer)

- two times seq_len times (d_model times ffw_size plus d_model times ffw_size)

· Final Logits

- two times seq_len times d_model times vocab_size

· Total forward pass FLOPs: embeddings plus number_layers times (total_attention plus dense_block) plus logits

As in Kaplan et al. we assume that the backward pass has twice the FLOPs of the forward pass. We show a comparison between our calculation and that using the common approximation C equals sixDN where C is FLOPs, D is the number of training tokens, and N is the number of parameters in Table A4. We find the differences in FLOP calculation to be very small and they do not impact our analysis. Compared to the results presented in Rae et al., we use a slightly more accurate calculation giving a slightly different value (six point three times ten to the power of twenty-three compared to five point seven six times ten to the power of twenty-three).


## G. Other differences between Chinchilla and Gopher

Beyond differences in model size and number of training tokens, there are some additional minor differences between Chinchilla and Gopher. Specifically, Gopher was trained with Adam whereas Chinchilla was trained with AdamW. Furthermore, as discussed in Lessons Learned in Rae et al., Chinchilla stored a higher-precision copy of the weights in the sharded optimizer state.

We show comparisons of models trained with Adam and AdamW in Figure A6 and Figure A7. We find that, independent of the learning rate schedule, AdamW trained models outperform models trained with Adam. In Figure A6 we show a comparison of a six hundred eighty million parameter model trained with and without the higher precision copy of the weights and with Adam or AdamW for comparison.


## H. Results

H point one. The Pile


## H point two. MMLU

In Table A6 we show the performance of Chinchilla and Gopher on each subset of MMLU.


## H point three. Winogender Setup

We follow the same setup as in Rae et al. To test coreference resolution in Chinchilla, we input a sentence which includes a pronoun reference, then measure the probability of the model completing the sentence "Pronoun refers to the" with different sentence roles ("librarian" and "child" in this example). Each example is annotated with the correct pronoun resolution (the pronoun corresponds to the librarian in this example). Each sentence is tested with a female, male, and gender-neutral pronoun. An unbiased model would correctly predict which word the pronoun refers to regardless of pronoun gender.


## H point four. BIG-bench

I. Model Card

We present the Chinchilla model card in Table A8, following the framework presented by Mitchell et al.

Primary Intended Users DeepMind researchers. We will not make this model available publicly.


## Datasets

We did not investigate intersectional biases.


## Intersectional Results

J. List of trained models

In Table A9 we list the model size and configuration of all models used in this study. Many models have been trained multiple times, for a different number of training steps.