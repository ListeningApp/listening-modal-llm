## StyleTTS: A Style-Based Generative Model for Natural and Diverse Text-to-Speech Synthesis

Abstract-Text-to-Speech has recently seen great progress in synthesizing high-quality speech owing to the rapid development of parallel TTS systems. Yet producing speech with naturalistic prosodic variations, speaking styles, and emotional tones remains challenging. In addition, many existing parallel TTS models often struggle with identifying optimal monotonic alignments since speech and duration generation typically occur independently. Here, we propose StyleTTS, a style-based generative model for parallel TTS that can synthesize diverse speech with natural prosody from a reference speech utterance. Using our novel Transferable Monotonic Aligner and duration-invariant data augmentation, StyleTTS significantly outperforms other baseline models on both single and multi-speaker datasets in subjective tests of speech naturalness and synthesized speaker similarity. Through self-supervised learning, StyleTTS can generate speech with the same emotional and prosodic tone as the reference speech without needing explicit labels for these categories. In addition, when trained with a large number of speakers, our model can perform zero-shot speaker adaptation. The source code and audio samples can be found on our demo page at https://styletts.github.io/.


## I. INTRODUCTION

Text-to-speech, also known as speech synthesis, has made significant strides with the advent of deep learning, producing increasingly human-like synthetic speech. However, synthesizing expressive speech that captures the full range of prosodic, temporal, and spectral features, also known as paralinguistic information, remains a challenge. A single piece of text can be spoken in various ways, influenced by context, emotional tone, and a speaker's unique linguistic habits. Hence, TTS is fundamentally a one-to-many mapping problem requiring innovative approaches.

While several strategies have been proposed to address this, including methods based on variational inference, flow-based modeling, controlling pitch, duration and energy, and using external prosody encoder, the production of synthesized speech still falls short of real human speech. In particular, accurately modeling and incorporating different speakers' speaking styles and emotional tones poses a significant challenge.

Many attempts have been made to integrate style information into TTS models. These approaches are predominantly based on autoregressive models such as Tacotron. Non-autoregressive parallel TTS models, such as FastSpeech and Glow-TTS, however, have several advantages over autoregressive models. These models generate speech in parallel, enabling fast speech synthesis, and they are also more robust to longer and out-of-distribution utterances. Moreover, because phoneme duration, pitch, and energy are predicted independently from speech, models such as FastSpeech2 and

FastPitch allow fully controllable speech synthesis. At the same time, these models have limitations. They predominantly concentrate on speech synthesis from a single target speaker and often achieve multi-speaker extensions by concatenating speaker embeddings with the encoder output. Models that explore speech styles also incorporate styles by concatenating style vectors and phoneme embeddings as input to the decoder. This approach may not capture the temporal variation of acoustic features in the target speech effectively. In contrast, the domain of style transfer introduces styles through conditional normalization methods like adaptive instance normalization. This technique has proven effective in neural style transfer, generative modeling, and neural image editing. Application of these methods in speech synthesis has not been extensively explored yet, restricted primarily to voice conversion and speaker adaptation.

The structure of parallel TTS models allows for the entire speech to be synthesized, presenting an opportunity to leverage the powerful AdaIN module for integrating generalized styles in diverse speech synthesis. Recent state-of-the-art models mostly employ the non-autoregressive parallel framework for TTS, but because they do not directly align the input text and speech like autoregressive models do, an external aligner such as the Montreal Forced Aligner that is pre-trained on a large dataset is often required. Since the external aligner is not trained on the TTS data and objectives, the alignments are not optimally suited for the TTS task. Although training internal aligners alleviates some generalization problems, overfitting can occur as the aligners are trained on a smaller TTS dataset with only a mel-reconstruction loss.

Here, we introduce StyleTTS, a model that addresses the aforementioned challenges of incorporating diverse speaking styles and learning a reliable monotonic aligner. StyleTTS incorporates style-based generative modeling into a parallel TTS framework to enable natural and expressive speech synthesis. It leverages AdaIN to integrate style vectors derived from reference audio, capturing the full spectrum of a speaker's stylistic features. This allows our model to synthesize speech that emulates the prosodic patterns and emotional tones in the reference audio. With various reference audios, we can synthesize the same text in different speaking styles, effectively realizing the one-to-many mapping that many TTS systems find challenging. In addition, our model employs a novel Transferable Monotonic Aligner to find the optimal text alignment, aided by a novel duration-invariant data augmentation scheme to produce naturalistic prosody robust to potentially suboptimal duration predictions. Our model's design is robust against the generalization problems of external aligners and overfitting problems that can be caused by internal aligners.

This paper presents the following novel contributions: (i) the introduction of the Transferable Monotonic Aligner, a new transfer learning scheme that refines pre-trained text aligners for TTS tasks, (ii) a duration-invariant data augmentation method for improving prosody prediction, and (iii) a parallel TTS model that incorporates generalized speech styles for natural and expressive speech synthesis. Together, these contributions pave the way for advanced TTS technologies enhancing human-computer interactions.


## II. METHODS

A. Proposed Framework

Given T the input phonemes and X an arbitrary reference mel-spectrogram, our goal is to train a system that generates the mel-spectrogram that corresponds to the speech of T and reflects the generalized speech styles of X. Generalized speech styles are defined as any characteristics in the reference audio X except the phonetic content, including but not limited to prosodic pattern, lexical stress, formants transition, speaking rate, and speaker identity. Our framework consists of eight modules that can be divided into three major categories: (i) speech generation modules that include the text encoder, style encoder, and decoder, (ii) TTS prediction modules that include the duration and prosody predictor, and (iii) utility modules only used during training that include the discriminator, text aligner, and pitch extractor. An overview of our framework is provided in Figure one. We detail each of the modules below.

Text Encoder. The text encoder transforms the phonemes into a hidden representation H text equals T of T. It consists of a three-layer CNN followed by a bidirectional LSTM.

Text Aligner. The text aligner A generates an alignment dalign between mel-spectrograms and phonemes. We train a text aligner A alongside the decoder G during the reconstruction phase. Modeled after the decoder of Tacotron two with attention, A is initially trained on an automatic speech recognition task using the LibriSpeech corpus and then fine-tuned concurrently with our decoder. We call an aligner with this setup a Transferable Monotonic Aligner.

Style Encoder. Given an input mel-spectrogram X, our encoder derives a style vector s equals E of X. With various reference audios, E can generate diverse style representations, allowing the decoder G to create speech that mirrors the style s of a reference audio X. E consists of four residual blocks followed by an averaging pooling layer along the time axis.

Pitch Extractor. As in FastPitch, we extract pitch F zero directly in Hertz without further processing, providing a more straightforward representation and allowing enhanced control of speech pitch. Instead of using the acoustic periodicity detection method employed in FastPitch to estimate the ground truth pitch, we train a pitch extractor F end-to-end with our decoder G for a more accurate estimation. Our pitch extractor F is a JDC network, pre-trained on LibriSpeech with ground truth F zero estimated using YIN. This extractor is fine-tuned with the decoder to predict pitch p X equals F of X for the reconstruction of X.

Decoder. Our decoder G is trained to reconstruct the input mel-spectrogram X, represented by c equals G of h text. dalign, s, p X, ne. Here, h text. dalign is aligned hidden representation of phonemes, s equals E of s is the style vector of X, p X is pitch contour of X, and ne is energy represented by the log norm of X per frame. The decoder is comprised of seven residual blocks with AdaIN, defined as follows:

AdaIN of c, s equals La of s times c minus mu of c over sigma of c plus Lu of s.

where c is a single channel of the feature maps, s is the style vector, u of dot and o of dot denote the channel mean and standard deviation and Lo and Lu are learned linear projections for computing the adaptive gain and bias using the style vector s. The use of AdaIN is one of the major differences between our model and other TTS models with style encoders. The advantages of AdaIN for diverse speech synthesis are further discussed in Appendix A-B.

To prevent dilution of import features, we concatenate the pitch p X, energy ne, and residual phoneme features h res and deliver them to subsequent residual blocks after AdaIN. This process is further detailed in Table, and its effectiveness is discussed in Section four-D.

Discriminator. We include a discriminator D to facilitate training of our decoder for better sound quality. The discriminator shares the same architecture as our style encoder.

Duration Predictor. Our duration predictor consists of a three-layer bidirectional LSTM R with adaptive layer normalization module followed by a linear projection L, where instance normalization is replaced by layer normalization in equation one. We use adaptive layer normalization because R takes discrete tokens similar to those in NLP applications, where layer normalization is preferred. R is shared with the prosody predictor P through h prosody equals R of h text as input to P.

Prosody Predictor. Our prosody predictor P predicts both the pitch p X and energy ne with given text and style vector. The aligned shared representation h prosody of at is processed through a shared bidirectional LSTM layer to generate h prosody, which is then fed into two sets of three residual blocks with AdaIN and a linear projection layer, one for the pitch output and another for the energy output.

B. Training Objectives

Our model training process is divided into two stages to allow the integration of duration-invariant prosody data augmentation, a key contribution of our work. During the first stage, the model learns to reconstruct the mel-spectrogram from the text, pitch, energy, and style. The second stage fixes all modules except the duration and prosody predictors, which are trained to predict the duration, pitch, and energy from the given text. One First Stage Objectives:

Mel reconstruction. Given a mel-spectrogram X belonging to X prime and its corresponding text t belonging to T, we train our decoder under the L one reconstruction loss

C mel equals expectation of X, t absolute value X minus G of h text dot align, s, p X, ne.

a Mel-spectrogram reconstruction where h text equals T of t is the encoded phoneme representation, align equals A of X, t is the attention alignment from the text aligner, s equals E of X is the style vector of X, p X equals F of X is the pitch F zero of X and ne is the energy of X. For end-to-end training with the decoder and the text aligner, we apply a novel fifty percent-fifty percent strategy: half the time, we use the raw attention output as the alignment, which allows gradient backpropagation through the text aligner; for the other half, we use the non-differentiable monotonic version of alignment through dynamic programming algorithms to train the decoder for generating intelligible speech from monotonic hard alignment during inference. This innovative approach effectively fine-tunes the pre-trained text aligner to produce the optimal alignments for speech reconstruction, thus enhancing the sample quality of generated speech. The effectiveness of this strategy is analyzed in section four-D.

TMA objectives. We fine-tune our text aligner with the original sequence-to-sequence automatic speech recognition objectives L s two s to ensure that correct attention alignment is kept during the end-to-end training:

L s two s equals expectation of X, t sum from i equals one to N cross-entropy of t i, t i.

where N is the number of phonemes in t, ti is the i-th phoneme token of t, ti is the i-th predicted phoneme token, and CE(.) is the cross-entropy loss function.

Since this alignment is not necessarily monotonic, we use a simple L one loss Lmono that forces the soft attention alignment to be close to its non-differentiable monotonic version:

Lmono equals Ex,t absolute value of @align minus @hard absolute value one , where @align equals A(x, t) is the attention alignment and @hard is the monotonic hard alignment obtained through dynamic programming algorithms.


## Duration and prosody prediction

Adversarial objectives. We employ two adversarial loss functions, the original cross-entropy loss function Lady for adversarial training and the additional feature-matching loss Lfm, to improve the sound quality of the reconstructed mel-spectrogram:

Lady equals Ex,t log D(x) plus log (one minus D(x)) ,

T divided by N summation absolute value D prime of x minus D prime of x absolute value one ,

Lfm equals Ex,t where & is the reconstructed mel-spectrogram by G, T is the total number of layers in D and D prime denotes the output feature map of l-th layer with N number of features. The feature matching loss can be seen as a reconstruction loss of hidden layer features of real and generated speech as judged by the discriminator.

First stage full objectives. Our full objective functions in the first stage can be summarized as follows with hyperparameters As25, Amono, dadv and Afm:

min max Lmel plus As25 Ls2s plus Amono Lmono

G,A,E,F,T D

plus Xadv Lady plus Afm Lfm


## Second Stage Objectives:

Duration prediction. We employ the L one loss to train our duration predictor

Ldur equals Ed absolute value d minus dpred absolute value one where d is the ground truth duration obtained by summing Calign along the mel frame axis. dpred equals L(R(htext, s)) is the predicted duration under the style vector s.

Prosody prediction. We train our prosody predictor via a unique data augmentation scheme. Since the duration predictor is trained separately from other modules (using only duration), the duration predictions it produces may not always be optimal or compatible with the prosody predictor. To make the prosody predictor more robust to these potentially suboptimal duration predictions, we augment the data to introduce prosody invariance over the duration.

More specifically, instead of using the ground truth alignment, pitch, and energy of the original mel-spectrogram, we first apply a one-D bilinear interpolation to stretch or compress the mel-spectrogram in time to obtain the augmented sample. As a result, the speech speed changes, yet the pitch and energy curves remain consistent. Accordingly, the prosody predictor learns to maintain pitch and energy prediction invariance, regardless of the duration of speech. This approach helps mitigate issues with unnatural prosody when the predicted duration is incorrect.


## We use Lf zero and Ln, which are F zero and energy reconstruction loss, respectively:

Co equals Epa absolute value Pa minus Pp (S (htext, S) @ align ) absolute value ,

Ln equals Ex absolute value na minus Pn (S (htext, S) @align ) absolute value ,

where p, n and @align are the pitch, energy and alignment of the augmented dataset. Pp denotes the pitch output from the prosody predictor, and Pn denotes the energy output.

Decoder reconstruction. Lastly, we aim to ensure that the predicted pitch and energy can be effectively used by the decoder. Given that the mel-spectrogram is stretched or compressed during data augmentation, using them as the ground truth may lead to unwanted artifacts in the predicted prosody. Instead, we train the prosody predictor to produce pitch and energy predictions that can effectively reconstruct the decoder's outputs.

Lde equals E,t absolute value minus G (htext @align, s, p, i) absolute value , where equals G (htext @align, s, p, absolute value x absolute value) is the reconstruction of , p equals Pp (S (htext, S) @align) the predicted pitch and equals Pn (S (htext, S) @align) the predicted energy.

Second stage full objectives. Our full objective functions in the second stage can be summarized as follows with hyperparameters Adur, Afo, and An:

min Lde plus Adur duration plus AfO F zero plus AnCn


## Three. EXPERIMENTS

A. Datasets

We conducted experiments on three datasets. We trained a single-speaker model on the LJSpeech dataset. The LJSpeech dataset consists of thirteen thousand one hundred short audio clips with a total duration of approximately twenty-four hours. We used the same split as VITS where the training set contains twelve thousand five hundred samples, the validation set one hundred samples and the test set five hundred samples. We also trained a multi-speaker model on the LibriTTS dataset. The LibriTTS train-clean-four hundred sixty subset consists of approximately two hundred forty-five hours of audio from one thousand one hundred fifty-one speakers. We removed utterances with a duration longer than thirty seconds and shorter than one second. We randomly split the train-clean-four hundred sixty subset into a training (ninety-eight percent), a validation (one percent), and a test (one percent) set and use the test set for evaluation. We also used the VCTK dataset to show that our model is capable of zero-shot speaker adaptation. We used the same training and test speaker split as in VCTK, where eighty-eight speakers were used for training and the rest twenty were used for testing.

In addition, we trained a multi-speaker model on the emotional speech dataset (ESD) to demonstrate the capacity to synthesize speech with diverse prosodic patterns. ESD consists of ten Chinese and ten English speakers reading the same four hundred short sentences in five different emotions. We trained our model on ten English speakers with all five emotions. We upsampled training audios to twenty-four kilohertz to match the LibriTTS dataset. We converted text sequences into phoneme sequences using an open-source tool. We extracted mel-spectrograms with a FFT size of two thousand forty-eight, hop size of three hundred, and window length of twelve hundred in eighty mel bins using TorchAudio.


## B. Training

For both stages, we trained all models for two hundred epochs using the AdamW optimizer with beta one equals zero, beta two equals zero point ninety-nine, weight decay equals ten to the power of negative four, learning rate gamma equals ten to the power of negative four and batch size of sixty-four samples. We set s2s equals zero point two, dadv equals one, mono equals five, f m equals zero point two, Adur equals one, AfO equals zero point one, and An equals one. This setting of hyperparameters makes sure that all loss values are on the same scale and that the training is not sensitive to these hyperparameters. The scale factor ranges from zero point seventy-five to one point twenty-five for data augmentation. We randomly divided the mel-spectrograms into segments of the shortest length in the batch. The training was conducted on a single NVIDIA A forty GPU.


## C. Evaluations

We performed two subjective evaluations: mean opinion score of naturalness to measure the naturalness of synthesized speech, and mean opinion score of similarity to evaluate the similarity between synthesized speech and reference for the multi-speaker model. We recruited native English speakers located in the United States to participate in the evaluations on Amazon Mechanical Turk. In every experiment, we randomly selected one hundred text samples from the test set. For each text, we synthesized speech using our model and the baseline models and included the ground truth for comparison. The baseline models include Tacotron two, FastSpeech two, and VITS. For zero-shot speaker adaptation experiments, we compared our model with StyleSpeech and YourTTS. All baseline models are pre-trained and publicly available. The generated mel-spectrograms were converted into waveforms using the Hifi-GAN vocoder for all models. Each set of speech was rated by ten raters on a scale from one to five with zero point five point increments. For a fair comparison, we downsampled our synthesized audio into twenty-two kilohertz to match those from baseline models. We used random references when synthesizing speech for the single-speaker and zero-shot speaker adaptation experiments. For multi-speaker models, because our training did not require speaker labels, for a fair comparison with other models that use explicit speaker embeddings during training, we averaged the style vectors computed using all samples in the training set from the same speaker as the reference style.

When evaluating each set, we randomly permuted the order of the models and instructed the subjects to listen and rate them without telling them the model labels. It is similar to multiple stimuli with hidden reference and anchor, allowing the subjects to compare subtle differences among models. We used the ground truth as hidden attention checkers: raters were dropped from analysis if the mean opinion score of the ground truth was not ranked top two among all the models.

We also conducted objective evaluations using ASR metrics. We evaluated the robustness of the models to different lengths of text input. We created four test sets with text length L less than ten, ten less than or equal to L less than fifty, fifty less than or equal to L less than one hundred, and one hundred less than or equal to L, respectively. Each set contains one hundred texts sampled from the WSJ zero dataset. We calculated the word error rate of the synthesized speech from both single-speaker and multi-speaker models using a pre-trained ASR model from ESPnet. To measure the inference speed, we computed the real-time factor,

which denotes the time in seconds needed for the model to synthesize a one-second waveform. Real-time factor was measured on a server with one NVIDIA twenty eighty Ti GPU and a batch size of one. In addition, we conducted the same analysis on the correlations of acoustic features associated with emotions between reference and synthesized speech using four multi-speaker models. Since there is no style in FastSpeech two and VITS, we used a pre-trained X-vector model from Kaldi to extract the speaker embedding as the reference vector.


## Four. Results

A. Model Performance.

Tables one, two, and three showcase the results of human subjective evaluations on the LJSpeech and LibriTTS datasets. When assessed for naturalness and similarity, StyleTTS clearly outperforms other models, demonstrating its superior performance under both single-speaker, multi-speaker, and zero-shot settings. Our models are more robust compared to other models, especially for long input texts. Since we do not use generative flows that require inverse Jacobian computation, our model is faster than VITS, even though it was not trained end-to-end like VITS.

We do note that our evaluation results differ from those reported in the baseline models, particularly for VITS. The VITS model has been reported to yield results very close to the ground truth. However, in our evaluation, VITS was found not to reach ground truth levels of performance. The primary factor leading to this discrepancy is the difference in evaluation methods. In VITS experiments, the traditional Mean Opinion Score evaluation was used, where raters evaluated each module individually without any reference. The use of a reference point in our MUSHRA-like evaluation provides an anchor for rating, particularly the ground truth as the reference, which potentially lowers the scores of other models. A similar discrepancy has been reported in a very recent study that examines the effects of evaluation methods on the mean opinion score results, and our evaluation of VITS is comparable to other studies that have tried to reproduce it on both LJSpeech and LibriTTS datasets.


## B. Visualization of Style Vectors

To verify that our model can learn meaningful style representations, we projected the style vectors extracted from reference audios into a two-dimensional plane for visualization using t-SNE. We selected fifty samples of each emotion from a single speaker in ESD and projected the style vectors of each audio into the two-dimensional space. It can be seen in Figure two a that our style vector distinctively encodes the emotional tones of reference sentences even though the training does not use emotion labels. We also computed the style vectors using speech samples from the same speaker with our single-speaker model. This model is only trained on the LJSpeech dataset and therefore has never seen the selected speaker from ESD during training. Nevertheless, in Figure two b, we see that our model can still clearly capture the emotional tones of the sentences, indicating that even when the reference audio is from a speaker different from the single speaker seen during training, it still can synthesize speech with the correct emotional tones. This shows that our model can implicitly extract emotions from an unlabeled dataset in a self-supervised manner. Lastly, we show projected style vectors from ten unseen VCTK speakers each with fifty samples in Figure two c. Different speakers are perfectly separated from each other in the two-dimensional projection. This indicates that our model can learn speaker identities without explicit speaker labels and hence perform zero-shot speaker adaptation.


## C. Style-Enabled Diverse Speech Synthesis

To show that the learned style vectors indeed enable diverse speech synthesis, we provide an example of synthesized speech with two different reference audios using our single-speaker model trained on the LJSpeech dataset in Figure three. It can be seen clearly that the synthesized speech captures various aspects of the reference speech, including the pitch, prosody, pauses, and formant transitions. To systematically quantify this effect, we drew six scatter plots showing the correlations between synthesized and reference speech in acoustic features traditionally used for speech emotion recognition. The six features are pitch mean, pitch standard deviation, energy mean, energy standard deviation, harmonics-to-noise ratio, and speaking rate. All six features demonstrate a significant correlation between the synthesized and reference speech with the correlation coefficients all above zero point six. Our model also outperforms other models on multi-speaker datasets in acoustic feature correlations. The results indicate that multiple aspects of the synthesized speech are matched to the reference, allowing flexible control over synthesized speech simply by selecting appropriate reference audios. Since our models also allow fully controllable pitch, energy, and duration, our approach is among the most flexible models in terms of controllability for speech synthesis.


## D. Ablation Study

We further conduct an ablation study to verify the effectiveness of each component in our model with experiments of subjective human evaluation. We instructed the subjects to compare our single-speaker model to those with one component ablated. We converted the ratings into comparative mean opinion scores by taking the difference between the mean opinion scores of the baseline and ablated models. The results are shown in table seven, and more details are in Appendix A.

The leftmost table shows the results related to the proposed Transferable Monotonic Aligner training. When training consists of one hundred percent hard alignments so that no gradient is back-propagated to the parameters of the text aligner, the rated mean opinion score is decreased by negative zero point two six. This is due to the covariate shift between the pre-training data and text-to-speech data. An example of bad alignment of the pre-trained external aligner is shown in Figure five. This shows that fine-tuning the aligner is effective in improving the quality of synthesized speech. However, when using zero percent hard alignment, one hundred percent soft attention alignment, the model gets overfitted to reconstruct speech with soft alignment and is unable to produce audible speech using hard alignment during inference, negative two point nine eight comparative mean opinion score. We also see that both Transferable Monotonic Aligner objectives, equations three and four, are important for high-quality speech synthesis.

The table in the middle shows the effects of removing various training techniques and components. Using an external pitch extractor, such as acoustic-based methods, decreases the mean opinion score by negative zero point one one. This is likely caused by the acoustic-based pitch extraction method sometimes failing to extract the correct F-zero curve, and fine-tuning the pitch extractor along with the decoder makes the model learn better pitch representation. Without a pre-trained text aligner, the rated mean opinion score is decreased by negative zero point three nine. This indicates that our transfer learning is helpful for mitigating overfitting problems when training internal aligners with a relatively small dataset. Removing our novel duration-invariant data augmentation also lowers the performance. Lastly, training without discriminators significantly affects the perceived sound quality.

The rightmost table shows architecture changes by removing the residual features and replacing the AdaIN components in the decoder and predictor with instance normalization, AdaLN, and simple feature concatenation. Their effects on style reflection are also shown in Table eight. Removing the residual features in the decoder decreases both naturalness and correlations between synthesized and reference speech. Layer normalization is also worse than instance normalization for both metrics. Concatenating styles in place of AdaIN dramatically decreases the correlations and lowers rated naturalness, confirming our observation that all previous methods that use concatenation to incorporate style information are not as effective as AdaIN due to the lack of temporal modulations. Lastly, we see that replacing AdaIN with instance normalization does not significantly affect the rated naturalness,

suggesting that the improved naturalness is not due to the introduction of styles but our novel technical improvements including Transferable Monotonic Aligner, data augmentation, use of instance normalization, pitch extractor, and residual features. Nevertheless, styles enable diverse speech synthesis which models without styles cannot do.


## V. CONCLUSIONS

We introduced StyleTTS, a novel natural and diverse text-to-speech synthesis approach. Our research takes a distinctive step forward in leveraging the strengths of parallel text-to-speech systems with several novel constitutions that include a unique transferable monotonic aligner training while integrating style information via AdaIN. We demonstrated that this method can effectively reflect stylistic features from reference audio. Moreover, the style vectors from our model encode a rich set of information present in the reference audio, including pitch, energy, speaking rates, formant transitions, and speaker identities. This allows easy control of the synthesized speech's prosodic patterns and emotional tones by choosing an appropriate reference style while benefiting from robust and fast speech synthesis of parallel text-to-speech systems. Collectively, they enable natural speech synthesis with diverse speech styles that go beyond what was achieved in previous text-to-speech systems.

Our contribution lies not only in the theoretical underpinnings but also in its practical applicability. Our approach empowers various new applications, including movie dubbing, book narration, unsupervised speech emotion recognition, personalized speech generation, and any-to-any voice conversion. Our source code and pre-trained models are publicly available to assist research in this area further.


## VI. ACKNOWLEDGMENTS

In this section, we describe the detailed settings of each condition in Table seven and provide more discussions of the results in Table seven and Table eight.


## A. TMA-related

There are three Transferable Monotonic Aligner related innovations in this work: the decoder is trained with hard monotonic alignment and soft attention in a fifty percent to fifty percent manner and two TMA objectives functions. The fifty percent to fifty percent training is motivated by the fact that the monotonic alignment search proposed is not differentiable, and the soft attention alignment does not necessarily provide correct alignments for duration prediction in the second stage of training. This fifty percent to fifty percent split is arbitrary and can be changed to anything from ten percent to ninety percent to ninety percent to ten percent, depending on the dataset and the application. When the ratio is one hundred percent to zero percent, it becomes the case where the external aligners are not fine-tuned like in most parallel TTS systems such as FastSpeech, while when the ratio is zero percent to one hundred percent, it becomes the case we fine-tune the aligner with only soft attention such as in Cotatron for voice conversion applications. We find that training with external aligners hundred percent hard, no fine-tuning decreases the naturalness of the synthesized speech because bad alignments can happen due to covariate shifts between the training dataset LibriSpeech and testing dataset LJSpeech as in the case of Montreal Forced Aligner. One example is given in the leftmost figure in Figure five. On the other hand, if we only fine-tune the decoder with soft alignment, the decoder will overfit on the soft alignment and be unable to synthesize audible speech from hard alignment because the soft alignments are not either zero or one and the precise numerical values of alignments are used by the decoder to generate speech.

Another notable case is when we do not use a pre-trained text aligner such as in the case of VITS. This case makes MOS even lower than the case of no fine-tuning, suggesting that overfitting on a smaller dataset can be more detrimental than failure in generalization on the TTS dataset for some samples. The figure in the middle in Figure five shows an alignment with gaps and no background noises. This indicates overfitting of the text aligner to the smaller dataset for the mel-spectrogram reconstruction objective. However, since our goal is to synthesize the speech from predicted alignment, overfitting to speech reconstruction can be harmful to natural speech synthesis during inference.

In addition to the fifty percent to fifty percent training, we also introduced two TMA objectives Ls2s and Lmono. This is motivated by the fact that Ls2s learns correct alignments for S2S-ASR but not necessarily monotonic while non-differentiable monotonic alignments obtained through dynamic programming algorithms proposed do not necessarily produce correct alignments. By combining Ls2s and Lmono, we can learn an aligner that produces both correct and monotonic alignments.


## B. AdaIN, AdaLN, and Concatenation

As shown in Table seven and Table eight, AdaIN outperforms AdaLN and simple concatenation for both naturalness and style reflection. Here we describe our intuitions behind these results.

Concatenation vs. AdaIN. When we concatenate the style vector to each frame of the encoded phonetic representations, we create a representation hstyle equals Thtext s . When the hstyle is passed to the next convolution layer whose parameter is W, we get hstyle equals W equals

equals

Htext equals Htext times Wtext plus S times Wstyle

Htext equals Htext times Wtext plus Concat Htext S

where Wtext and Wstyle are block matrix notation of the corresponding weights for Hstyle and S and Concat Htext S equals S times Wstyle denotes the concatenation operation as a function of input Htext and style vector S. This Concat function is almost like AdaIN in equation one where Lu of S equals Wstyle except we do not have the temporal modulation term La of S. The modulation term is very important in style transfer, and some works argue that modulation alone is enough for diverse style representations. In contrast, concatenation only provides the addition term Lu but no modulation term La. Intuitively, the modulation term can determine the variance of the pitch and energy, for example, and therefore without such a term, correlations for pitch and energy standard deviation are much lower than AdaIN and AdaLN as shown in Table eight.

AdaLN versus AdaIN. Generative models for speech synthesis learn to generate mel-spectrograms, which is essentially a one-D feature map with eighty channels. Each channel in the mel-spectrogram represents a single frequency range. When we apply AdaIN, we learn a distribution with a style-specific mean and variance for each channel, compared to AdaLN, where a single mean and variance are learned for the entire feature map. This inherent difference between feature distributions makes AdaIN more expressive in terms of style reflection than AdaLN.


## C. Pitch Extractor

Acoustic methods for pitch estimation sometimes fail because of the presence of non-stationary speech intervals and sensitivity of hyper-parameters as discussed in the original papers that propose these methods. A neural network trained with ground truth from these methods, however, can leverage the problems of failed pitch estimation because the failed pitch estimation can be regarded as noises in the training set, so it does not affect the generalization of the pitch extractor network. Moreover, since the pitch extractor is fine-tuned along with the decoder, there is no ground truth for the pitch beside the sole objective that the decoder needs to use extracted pitch information to reconstruct the speech. This fine-tuning allows better pitch representations beyond the original F zero in Hertz, but it also allows flexible pitch control as we can still recognize the pitch curves and edit them later when needed during inference.

In the multi-speaker experiments, we used pre-trained Fast- speech two twelve, VITS thirteen, and HiFiGAN fourteen from ESPnet. We used pre-trained VITS from ESPnet instead of the official repository because we need the model to be trained on the LibriTTS dataset; however, the official models were trained on the LJSpeech or VCTK dataset.

Similar to the single-talker experiment, we launched five batches on AMT when we tested the multi-talker models on the LibriTTS dataset. Forty-eight out of fifty-eight subjects were qualified. We launched three batches with batch sizes thirty-three, thirty-three, thirty-four, respectively, when we tested the multi-talker models on the VCTK dataset. Twenty-eight out of thirty subjects were qualified.

Since our text encoder, text aligner, pitch extractor, and decoder are trained in a speaker-agnostic manner, our decoder can reconstruct speech from any aligned phonemes, pitch, energy, and reference speakers. Therefore, our model can perform any-to-any voice conversion by extracting the alignment, pitch, and energy from an input mel-spectrogram and generating speech using a style vector of reference audio from an arbitrary target speaker. Our voice conversion scheme is transcription-guided, similar to Mellotron and Cotatron. We provide one example in Figure six with both source and target speaker unseen from the LJSpeech and VCTK datasets. We refer our readers to our demo page for more examples.

In this section, we provide detailed model architectures of StyleTTS, which consists of eight modules. Since we use the same text encoder as in Tacotron two, very similar architecture to the decoder of Tacotron two for text aligner and the same architecture as the JDC network for pitch extractor, we leave the readers to the above references for detailed descriptions of these modules. Here, we only provide detailed architectures for the other five modules. All activation functions used are leaky ReLU with a negative slope of zero point two. We apply spectral normalization to all trainable parameters in style encoder and discriminator and weight normalization to those in decoder because they are shown to be beneficial for adversarial training.

Decoder (Table nine). Our decoder takes four inputs: the aligned phoneme representation, the pitch F zero, the energy, and the style code. It consists of seven one-D residual blocks along with three sub-modules for processing the input F zero, energy, and residual of the phoneme representation. The normalization consists of both instance normalization and adaptive instance normalization. We concatenate the processed F zero, energy, and residual of phonemes with the output from each residual block as the input to the next block for the first three blocks.

Style Encoder and Discriminator (Table ten). Our style encoder and discriminator share the same architecture, which consists of four two-D residual blocks. The dimension of the style vector is set to one hundred twenty-eight. We use learned weights for pooling through a dilated convolution layer with a kernel size of three times three. We apply an adaptive average pooling along the time axis of the feature map to make the output independent of the size of the input mel-spectrogram.

Duration and Prosody Predictors (Table eleven). The duration predictor and prosody predictors are trained together in the second stage of training. There is a shared three-layer bidirectional LSTM between the duration predictor and prosody predictor named text feature encoder, each followed by an adaptive layer normalization. AdaLN is similar to AdaIN where the gain and bias are predicted from the style vector S. However, unlike AdaIN which normalizes each channel independently, AdaLN normalizes the entire feature map. The style vector S is also concatenated with the output to every token from each LSTM layer as the input to the next LSTM layer. Lastly, we have a final bidirectional LSTM and a linear projection L that maps Hprosody into the predicted duration.

The hidden representation Hprosody is dotted with the alignment dalign and sent to the prosody decoder. The prosody encoder consists of one bidirectional LSTM and two sets of three residual blocks with AdaIN followed by a linear projection, one for predicting the F zero and another for predicting the energy, respectively.