## Asymmetric Student-Teacher Networks for Industrial Anomaly Detection

Abstract

Industrial defect detection is commonly addressed with anomaly detection methods where no or only incomplete data of potentially occurring defects is available. This work discovers previously unknown problems of student-teacher approaches for anomaly detection and proposes a solution, where two neural networks are trained to produce the same output for the defect-free training examples. The core assumption of student-teacher networks is that the distance between the outputs of both networks is larger for anomalies since they are absent in training. However, previous methods suffer from the similarity of student and teacher architecture, such that the distance is undesirably small for anomalies. For this reason, we propose asymmetric student-teacher networks. We train a normalizing flow for density estimation as a teacher and a conventional feed-forward network as a student to trigger large distances for anomalies: The bijectivity of the normalizing flow enforces a divergence of teacher outputs for anomalies compared to normal data. Outside the training distribution the student cannot imitate this divergence due to its fundamentally different architecture. Our asymmetric student-teacher network compensates for wrongly estimated likelihoods by a normalizing flow, which was alternatively used for anomaly detection in previous work. We show that our method produces state-of-the-art results on the two currently most relevant defect detection datasets MVTec anomaly detection and MVTec three-D-anomaly detection regarding image-level anomaly detection on RGB and three-D data.


## One. Introduction

To ensure product quality and safety standards in industrial manufacturing processes, products are traditionally inspected by humans, which is expensive and unreliable in practice. For this reason, image-based methods for automatic inspection have been developed recently using advances in deep learning. Since there are no or only very few negative examples, i.e. erroneous products, available, especially at the beginning of production, and new errors occur repeatedly during the process, traditional supervised algorithms cannot be applied to this task.

Instead, it is assumed that only data of a normal class of defect-free examples is available in training which is termed as semi-supervised anomaly detection. This work and others specialize for industrial anomaly detection. This domain differs in contrast to others that normal examples are similar to each other and to defective products. In this work, we not only show the effectiveness of our method for common RGB images but also on three-D data and their combination as shown in Figure one.

Several approaches try to solve the problem by so-called student-teacher networks. First, the teacher is trained on a pretext task to learn a semantic embedding. In a second step, the student is trained to match the output of the teacher. The motivation is that the student can only match the outputs of the teacher on normal data since it is trained only on normal data. The distance between the outputs of student and teacher is used as an indicator of an anomaly at test-time. It is assumed that this distance is larger for defective examples compared to defect-free examples. However, this is not necessarily the case in previous work, since we discovered that both teacher and student are conventional (i. e. non-injective) neural networks with similar architecture. A student with similar architecture tends to undesired generalization, such that it extrapolates similar outputs as the teacher for inputs that are out of the training distribution, which, in turn, gives an undesired low anomaly score. This effect is shown in Figure two using an explanatory experiment with one-dimensional data: If the same neural network with one hidden layer is used for student and teacher, the outputs are still similar for anomalous data in the yellow area of the upper plot. In contrast, the outputs for anomalies diverge if an M L P with three hidden layers is used as the student.

In general, it is not guaranteed that an out-of-distribution input will cause a sufficiently large change in both outputs due to the missing injectivity of common neural networks. In contrast to normalizing flows, conventional networks have no guarantee to provide out-of-distribution outputs for out-of-distribution inputs. These problems motivate us to use an asymmetric student-teacher pair: A bijective normalizing flow acts as a teacher while a conventional sequential model acts as a student. In this way, the teacher guarantees to be sensitive to changes in the input caused by anomalies. Furthermore, the usage of different architectures and thus of different sets of learnable functions enforces the effect of distant outputs for out-of-distribution samples. As a pretext task for the teacher, we optimize to transform the distribution of image features and/or depth maps to a normal distribution via maximum likelihood training which is equivalent to a density estimation. This optimization itself is used in previous work for anomaly detection by utilizing the likelihoods as an anomaly score: A low likelihood of being normal should be an indicator of anomalies. However, Le and Dinh have shown that even perfect density estimators cannot guarantee anomaly detection. For example, just reparameterizing the data would change the likelihoods of samples. Furthermore, unstable training leads to misestimated likelihoods. We show that our student-teacher distance is a better measure for anomaly detection compared to the obtained likelihoods by the teacher. The advantage to using a normalizing flow itself for anomaly detection is that a possible misestimation in likelihood can be compensated for: If a low likelihood of being normal is incorrectly assigned to normal data, this output can be predicted by the student, thus still resulting in a small anomaly score. If a high likelihood of being normal is incorrectly assigned to anomalous data, this output cannot be predicted by the student, again resulting in a high anomaly score. In this way, we combine the benefits of student-teacher networks and density estimation with normalizing flows. We further enhance the detection by a positional encoding and by masking the foreground using three-D images.

Our contributions are summarized as follows:

· Our method avoids the undesired generalization from teacher to student by having highly asymmetric networks as a student-teacher pair.

· We improve student-teacher networks by incorporating a bijective normalizing flow as a teacher.

· Our asymmetric student-teacher network outperforms the density estimation capability of the teacher by utilizing student-teacher distances.


## Two. Related Work

Two point one. Student-Teacher Networks

Originally, the motivation for having a student network that learns to regress the output of a teacher network was to distill knowledge and save model parameters. In this case, a student with clearly fewer parameters compared to the teacher almost matches the performance. Some previous work exploits the student-teacher idea for anomaly detection by using the distance between their outputs: The larger the distance, the more likely the sample is anomalous. Bergmann et al. propose an ensemble of students which are trained to regress the output of a teacher for image patches. This teacher is either a distilled version of an ImageNet-pre-trained network or trained via metric learning. The anomaly score is composed of the student uncertainty, measured by the variance of the ensemble, and the regression error. Wang et al. extend the student task by regressing a feature pyramid rather than a single output of a pre-trained network. Bergmann and Sattlegger adapt the student-teacher concept to point clouds. Local geometric descriptors are learned in a self-supervised manner to train the teacher. Xiao et al. let teachers learn to classify applied image transformations. The anomaly score is a weighted sum of the regression error and the class score entropy of an ensemble of students. By contrast, our method requires only one student and the regression error as the only criterion to detect anomalies. All of the existing work is based on identical and conventional (non-injective) networks for student and teacher, which causes undesired generalization of the student as explained in Section one.


## Two point two. Density Estimation

Anomaly detection can be viewed from a statistical perspective: By estimating the density of normal samples, anomalies are identified through a low likelihood. The concept of density estimation for anomaly detection can be simply realized by assuming a multivariate normal distribution. For example, the Mahalanobis distance of pre-extracted features can be applied as an anomaly score which is equivalent to computing the negative log likelihood of a multivariate Gaussian. However, this method is very inflexible to the training distributions, since the assumption of a Gaussian distribution is a strong simplification.

To this end, many works try to estimate the density more flexibly with a Normalizing Flow. Normalizing Flows are a family of generative models that map bijectively by construction as opposed to conventional neural networks. This property enables exact density estimation in contrast to other generative models like GANs or VAEs. Rudolph et al. make use of this concept by modeling the density of multi-scale feature vectors obtained by pre-trained networks. Subsequently, they extend this to multi-scale feature maps instead of vectors to avoid information loss caused by averaging. To handle differently sized feature maps so-called cross-convolutions are integrated. A similar approach by Gudovskiy et al. computes a density on feature maps with a conditional normalizing flow, where likelihoods are estimated on the level of local positions which act as a condition for the Normalizing Flow.

A common problem of normalizing flows is unstable training, which has a tradeoff on the flexibility of density estimation. However, even the ground truth density estimation does not provide perfect anomaly detection, since the density strongly depends on the parameterization.


## Two point three. Other Approaches

Generative Models


## Many approaches try to tackle anomaly detection based on

other generative models than normalizing flows as autoencoders or GANs. This is motivated by the inability of these models to generate anomalous data. Usually, the reconstruction error is used for anomaly scoring. Since the magnitude of this error depends highly on the size and structure of the anomaly, these methods underperform in the industrial inspection setting. The disadvantage of these methods is that the synthetic anomalies cannot imitate many real anomalies.


## Anomaly Synthesization

Some work reformulates semi-supervised anomaly detection as a supervised problem by synthetically generating anomalies. Either parts of training images or random images are patched into normal images. Synthetic masks are created to train a supervised segmentation. Traditional Approaches

In addition to deep-learning-based approaches, there are also classical approaches for anomaly detection. The one-class SVM is a max-margin method optimizing a function that assigns a higher value to high-density regions than to low-density regions. Isolation forests are based on decision trees, where a sample is considered anomalous if it can be separated from the rest of the data by a few constraints. Local Outlier Factor compares the density of a point with that of its neighbors. A comparatively low density of a point identifies anomalies. Traditional approaches usually fail in visual anomaly detection due to the high dimensionality and complexity of the data. This can be circumvented by combining them with other techniques: For example, the distance to the nearest neighbor, as first proposed by Amer and Goldstein, is used as an anomaly score after features are extracted by a pre-trained network. Alternatively point cloud features or density-based clustering can be used to characterize a points neighborhood and label it accordingly. However, the runtime is linearly related to the dataset size.


## Three. Method

Our goal is to train two models, a student model F sub S and a teacher model F sub T, such that the student learns to regress the teacher outputs on defect-free image data only. The training process is divided into two phases: First, the teacher model is optimized to transform the training distribution P sub X to a normal distribution N zero, one bijectively with a normalizing flow. Second, the student is optimized to match the teacher outputs by minimizing the distance between F sub S X and F sub T X of training samples X in set X. We apply the distance for anomaly scoring at test-time, which is further described in Section three point two.

We follow and use extracted features obtained by a pre-trained network on ImageNet instead of R G B images as direct input for our models. Such networks have been shown to be universal feature extractors whose outputs carry relevant semantics for industrial anomaly detection.

In addition to R G B data, our approach is easily extendable to multimodal inputs including three-D data. If three-D data is available, we concatenate depth maps to these features along the channels. Since the feature maps are reduced in height and width compared to the depth map resolution by a factor D, we apply pixel-unshuffling by grouping a depth image patch of D by D pixels as one pixel with D squared channels to match the dimensions of the feature maps.

Any three-D data that may be present is used to extract the foreground. This is straightforward and reasonable whenever the background is static or planar, which is the case for almost all real applications. Pixels that are in the background are ignored when optimizing the teacher and student by masking the distance and negative log likelihood loss, which are introduced in Sections three point one and three point two. If not three-D data is available, the whole image is considered as foreground. Details of the foreground extraction are given in Section four point two point one.

Similar to, we use a sinusoidal positional encoding for the spatial dimensions of the input maps as a condition for the normalizing flow F T. In this way, the occurrence of a feature is related to its position to detect anomalies such as misplaced objects. An overview of our pipeline is given in Figure three.


## Three point one. Teacher

Similar to we train a normalizing flow based on Real N V P to transform the training distribution to a normal distribution N zero, I. In contrast to previous work, we do not use the outputs to compute likelihoods and thereby obtain anomaly scores directly. Instead, we interpret this training as a pretext task to create targets for our student network.

The normalizing flow consists of multiple subsequent affine coupling blocks. Let the input X be feature maps with N feat features of size W by H. Within these blocks, the channels of the input X are split evenly along the channels into the parts X one and X two after randomly choosing a permutation that remains fixed. These parts are each concatenated with a positional encoding C as a static condition. Both are used to compute scaling and shift parameters for an affine transformation of the counterpart by having subnetworks S one and T one for each part:

Y two equals X two times S one of X one and C plus T one of X one and C

One

Y one equals X one times E S two of X two and C plus T two of X two and C,

where O is the element-wise product and concatenation. The output of one coupling block is the concatenation of Y one and Y two along the channels. Note that the number of dimensions of input and output does not change due to invertibility.

To stabilize training, we apply alpha-clamping of scalar coefficients as in and the gamma-trick as in. Using the change-of-variable formula with Z as our final output

Two a det

Two we minimize the negative log likelihood with P Z as the normal distribution N zero, I by optimizing the mean of

C I equals minus log P X X I J equals X I J minus twelve O G det A Z I J O X I J three over all foreground pixels at pixel position I, J.


## Three point two. Student

As opposed to the teacher, the student is a conventional feed-forward network that does not map injectively or surjectively. We propose a simple fully convolutional network with residual blocks which is shown in Figure four. Each residual block consists of two sequences of three by three convolutional layers, batch normalization and leaky ReLU activations. We add convolutions as the first and last layer to increase and decrease the feature dimensions.

Similarly to the teacher, the student takes image features as input which are concatenated with three-D data if available. In addition, the positional encoding C is concatenated. The output dimensions match the teacher to enable pixel-wise distance computation. We minimize the squared L two-distance between student outputs F S X and the teacher outputs F T X on training samples X in X, given the training set X, at a pixel position I, J of the output:

C I J equals one F X I J minus F T X I J squared.

Four

Averaging over all foreground pixels gives us the final loss. The distance C S is also used in testing to obtain an anomaly score on image level: Ignoring the anomaly scores of background pixels, we aggregate the pixel distances of one sample by computing either the maximum or the mean over the pixels.


## Four. Experiments

Four point one. Datasets

To demonstrate the benefits of our method on a wide range of industrial inspection scenarios, we evaluate with a diverse set of twenty-five scenarios in total, including natural objects, industrial components and textures in two-D and three-D. Table one shows an overview of the used benchmark datasets MVTec A D and MVTec three-D A D. For both datasets, the training set only contains defect-free data and the test set contains defect-free and defective examples. In addition to image-level labels, the datasets also provide pixel-level annotations about defective regions which we use to evaluate the segmentation of defects.

MVTec A D, which will be called MVT two-D in the following, is a high-resolution two-D R G B image dataset containing ten object and five texture categories. The total of seventy-three defect types in the test set appear, for example, in the form of displacements, cracks or scratches in various sizes and shapes. The images have a side length of seven hundred to one thousand twenty-four pixels.

MVTec three-D A D, to which we refer to as MVT three-D, is a very recent three-D dataset containing two-D R G B images paired with three-D scans for ten categories. These categories include deformable and non-deformable objects, partially with natural variations (e.g. peach and carrot). In addition to the defect types in MVT two-D there are also defects that are only recognizable from the depth map, such as indentations. On the other hand, there are anomalies such as discoloration that can only be perceived from the R G B data. The R G B images have a resolution of four hundred to eight hundred pixels per side, paired with rasterized three-D point clouds at the same resolution.


## Four point two. Implementation Details

Four point two point one Image Preprocessing

Following, we use the layer thirty-six output of EfficientNet B five pre-trained on ImageNet as a feature extractor. This feature extractor is not trained during training of the student and teacher networks. The images are resized to a resolution of seven hundred sixty-eight by seven hundred sixty-eight pixels resulting in feature maps of size twenty-four by twenty-four with three hundred-four channels.


## Four point two point two Three-D Preprocessing

We discard the x and y coordinates due to the low informative content and use only the depth component z in centimeters. Missing depth values are repeatedly filled by using the average value of valid pixels from an eight-connected neighborhood for three iterations. We model the background as a twoD plane by interpolating the depth of the four corner pixels. A pixel is assumed as foreground if its depth is further than seven millimeters distant from the background plane. As an input to our models, we first resize the masks to one hundred ninety-two by one hundred ninety-two pixels via bilinear downsampling and then perform pixel-unshuffling with d equals eight as described in Section three to match the feature map resolution. In order to detect anomalies at the edge of the object and fill holes of missing values, the foreground mask is dilated using a square structural element of size eight. We subtract the mean foreground depth from each depth map and set its background pixels to zero. The binary foreground mask M with ones as foreground and zeros as background is downsampled to feature map resolution to mask the loss for student and teacher. This is done by a bilinear interpolation f1 followed by a binarization where all entries greater than zero are assumed as foreground to mask the loss at position (i, j):

Cmasked [Lij if fi(M)ij greater than zero equals ten else


## Four point two point three Teacher

For the normalizing flow architecture of the teacher, we use four coupling blocks which are conditioned on a positional encoding with thirty-two channels. Each pair of internal subnetworks Si and ti is designed as one shallow convolutional network ri with one hidden layer whose output is split into the scale and shift components. Inside ri we use ReLU-Activations and a hidden channel size of one thousand twenty-four for MVTtwoD and sixty-four for MVTthreeD. We choose the alpha-clamping parameter o equals three for MVTtwoD and Q equals one point nine for MVTthreeD. The teacher networks are trained for two hundred forty epochs for MVTtwoD and seventy-two epochs for MVTthreeD, respectively, with the Adam optimizer, using author-given momentum parameters thirty-one equals zero point nine and thirty-two equals zero point nine nine nine, a learning rate of two times ten to the negative four and a weight decay of ten to the negative five.


## Four point two point four Student

For the student networks, we use nst_blocks equals four residual convolutional blocks as described in Section three point two. The Leaky-ReLU-activations use a slope of zero point two for negative values. We choose a hidden channel size of nhidden equals one thousand twenty-four for the residual block. Likewise, we take over the number of epochs and optimizer parameters from the teacher. The scores at feature map resolution are aggregated for evaluation at image level by the maximum distance if a foreground mask is available, and the average distance otherwise (RGB only).


## Four point three Evaluation Metrics

As common for anomaly detection, we evaluate the performance of our method on image-level by calculating the area under receiver operating characteristics. The ROC measures the true positive rate dependent on the false positive rate for varying thresholds of the anomaly score. Thus, it is independent of the choice of a threshold and invariant to the class balance in the test set. For measuring the segmentation of anomalies at pixel-level, we compute the AUROC on pixel level given the ground truth masks in the datasets.


## Four point four Results

Four point four point one Detection

Table two shows the AUROC of our method and previous work for detecting anomalies on the fifteen classes of MVTtwoD as well as the averages for textures, objects and all classes. We set a new state-of-the-art performance on the mean detection AUROC over all classes, improving it slightly to ninety-nine point two percent. This is mainly due to the good performance on the more challenging objects, where we outperform previous work by a comparatively large margin of zero point nine percent, except for PatchCore. The detection of anomalies on textures, which CS-Flow has already almost solved with a mean AUROC of ninety-nine point eight percent, still works very reliably at ninety-nine point three percent. Especially compared to the two student-teacher approaches, a significant improvement of six percent and three point six percent respectively is achieved. Moreover, our student-teacher distances show to be a better indicator of anomalies compared to the likelihoods of current state-of-the-art density estimators which, like our teacher, are based on normalizing flows.

Even though MVTtwoD has established itself as a standard benchmark in the past, this dataset (especially the textures) is easily solvable for recent methods, and differences are mainly in the sub-percent range, which is only a minor difference in terms of the comparatively small size of the dataset. In the following, we focus on the newer, more challenging MVTthreeD dataset where the normal data shows more variance and anomalies only partly occur in one of the two data modalities, RGB and threeD.

The results for individual classes of MVT three D grouped by data modality are given in Table three. We are able to outperform all previous methods for all data modalities regarding the average of all classes by a large margin of five point one percent for three D, five percent for R G B and seven point two percent for the combination. Facing the individual classes and data domains, we set a new state-of-the-art in twenty-one of thirty cases. Note that this data set is much more challenging when comparing the best results from previous work (ninety-nine point one percent for MVT two D vs. eighty-six point five percent AUROC for MVT three D). Nevertheless, we detect defects in seven out of ten cases for R G B plus three D at an AUROC of at least ninety-three percent, which demonstrates the robustness of our method. In contrast, the nearest-neighbor approach PatchCore, which provides comparable performance to us on MVT two D, struggles with the increased demands of the dataset and is outperformed by eleven percent on R G B. The same applies for the three D extension using FPFH despite using a foreground mask as well. Figure one shows qualitative results for the R G B plus three D case given both inputs and ground truth annotations. More examples can be found in the supplemental material. Despite the low resolution, the regions of the anomaly can still be localized well for practical purposes. Table four reports the pixel-AUROC of our method and previous work.

For the class peach in the R G B plus three D setting, the top of Figure five compares the distribution of student-teacher distances for anomalous and normal regions. The distribution of anomalous samples shows a clear shift towards larger distances. At the bottom of Figure five, the outputs of student and teacher as well as our the distance of corresponding pairs representing our anomaly score are visualized by a random orthographic two D projection. Note that visualizations made by techniques such as t-SNE or P C A are not meaningful here, since the teacher outputs (and therefore most of the student outputs) follow an isotropic standard normal distribution. Therefore, different random projections barely differ qualitatively.


## Four point four point two Ablation Studies

We demonstrate the effectiveness of our contributions and design decisions with several ablation studies. Table five compares the performance of variants of students with the teacher, which can be used as a density estimator itself for anomaly detection by using its likelihoods, given by Equation two, as anomaly score. In comparison, a symmetric student-teacher pair worsens the results by one to two percent, excepting the R G B case. However, the performance is already improved for R G B and three D plus R G B by creating the asymmetry with a deeper version of the student than the teacher by doubling the number of coupling blocks to eight. This effect is further enhanced if the architecture of the N F-teacher is replaced by a conventional feedforward network as we suggest. We also vary the depth of our student network and analyzed its relation to performance, model size and inference time in Table six. With an increasing number of residual blocks N S T underscore blocks, we observe an increasing performance which is almost saturated after four blocks. Since the remaining potential in detection performance is not in relation to the linearly increasing additional computational effort per block, we suggest to choose four blocks to have a good trade-off.

In Table seven we investigate the impact of the positional encoding and the foreground mask. For MVT three D, positional encoding improves the detection by one point four percent of our AST-pair when trained with three D data as the only input. Even though the effect is not present when combining both data modalities, we consider it generally reasonable to use the positional encoding, considering that the integration with just thirty-two additional channels does not significantly increase the computational effort.

Foreground extraction in order to mask the loss for training and anomaly score for testing is also highly effective. Since the majority of the image area often consists of background, the teacher has to spend a large part of the distribution on the background. Masking allows the teacher and student to focus on the essential structures. Moreover, noisy background scores are eliminated.


## Five. Conclusion

We discovered the generalization problem of previous student teacher pairs for A D and introduced an alternative student-teacher method that prevents this issue by using a highly different architecture for student and teacher. We were able to compensate for skewed likelihoods of a normalizing flow-based teacher, which was used directly for detection in previous work, by the additional use of a student. Future work could extend the approach to more data domains and improve the localization resolution.