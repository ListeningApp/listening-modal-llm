## 1piq-2024-08-26_19_16_04-ml.pdf

Using machine learning approaches for multi-omics data analysis: A review Parminder S. Reel, Smarti Reel, Ewan Pearson, Emanuele Trucco, Emily Jefferson.


## One. Introduction

Digital information is growing rapidly, in terms of five V's (volume, velocity, veracity, variety and value), and hence this is hailed as the big data era. Health-based big data including linked information for patients, such as their clinical data (for example gender, age, pathological and physiological history) and omics data (such as genetics, proteomics and metabolomics) has now become more widely available. Recently, such data has been used for precision (also called personalised or stratified) medicine to provide customised healthcare, i.


## ABSTRACT

With the development of modern high-throughput omic measurement platforms, it has become essential for biomedical studies to undertake an integrative (combined) approach to fully utilise these data to gain insights into biological systems. Data from various omics sources such as genetics, proteomics, and metabolomics can be integrated to unravel the intricate working of systems biology using machine learning-based predictive algorithms. Machine learning methods offer novel techniques to integrate and analyse the various omics data enabling the discovery of new biomarkers. These biomarkers have the potential to help in accurate disease prediction, patient stratification and delivery of precision medicine. This review paper explores different integrative machine learning methods which have been used to provide an in-depth understanding of biological systems during normal physiological functioning and in the presence of a disease. It provides insight and recommendations for interdisciplinary professionals who envisage employing machine learning skills in multi-omics studies.

e. providing a bespoke treatment for individuals. There has been unprecedented growth in the development of precision medicine supported by machine learning approaches and data mining tools. These techniques have also helped to discover novel omics biological markers which can identify the molecular cause of a disease.

A biomarker is a substance, structure, or process that can be measured in the human body or its products and can provide surrogate information about the presence of a disease/condition.

Genomics nineteen eighty-six.

Single nucleotide polymorphisms, Rare variants and Copy number variations.

DNA-Sequencing Sanger, Whole-genome, Whole-exome, Single-Cell DNA and targeted sequencing, Microarray.

Transcriptomics

Nineteen ninety-nine.

Messenger, Micro and Long non-coding RNA expression.

RNA-Sequencing Sanger, Single-Cell RNA and targeted sequencing, Microarray. Reverse Phase Protein Array, Liquid Chromatography - Mass Spectrometry and Mass Spectrometry.

transcriptomics,

Nineteen ninety-nine

Metabolite expression Mass Spectrometry, Liquid Chromatography - Mass Spectrometry, Gas Chromatography - Mass Spectrometry. Liquid Chromatography - Mass Spectrometry, High-performance Liquid Chromatography - Mass Spectrometry and Direct-Infusion/ Shotgun - Mass Spectrometry.

Two thousand eleven.

Molecular biomarkers are discovered by analysing the cascade of information provided by different omics. For example, the high-sensitivity C-Reactive protein test provides an accurate and quantitative risk assessment for cardiovascular disease. Biomarkers play a significant role in planning preventive measures and decisions for patients and can be classified as either diagnostic, prognostic or predictive. Diagnostic biomarkers are used for determining the presence of disease in a patient, while prognostic biomarkers provide information on the overall outcome with or without the standard treatment. Predictive biomarkers are used to identify who is at risk of an outcome. All of these biomarkers can also be used to identify which treatment will be most suitable for a given patient. For example, the Alzheimer's Disease Neuroimaging Initiative study used a combination of neuroimaging, biochemical and genetic biomarkers to discriminate early Alzheimer's patients from healthy volunteers with an accuracy of ninety-eight percent. Similarly, different forms of Parkinson's syndromes have been investigated by developing an automated tool that fuses multi-site diffusion-weighted MRI imaging biomarkers and disease rating score. Biomarkers can help identify high-risk individuals before their physiological symptoms are evident. Moreover, they also help in measuring disease progression.

In the context of precision medicine, machine learning has been used to develop diagnostic, prognostic and predictive tools from single omics data. However, machine learning may have deteriorated performance for certain single omics such as gene data due to inherent characteristics. Machine learning methods are now also being applied to multi-omics data, to investigate and interpret the relationships.

between data and phenotypes. Although ML analysis of multi-omics is still in its embryonic stage, it has already been explored for a wide range of applications, as reported in recent reviews on brain diseases, diabetes, cancers, cardiovascular disease, medical imaging, single-cell analysis in humans and plant science studies. Currently, many of the multi-omic reviews are focused on individual sub-topics. For example, designing studies, setting up workflows, choosing software tools and evaluating overfitted performance.

In contrast, this review aims at a broader focus, presenting an interdisciplinary perspective to new readers in this domain by providing a background on multi-omics and ML. It takes forward the integration terminologies introduced by Ritchie and summarizes the recent integrative state-of-the-art approaches. We aim to cover various integration methods concisely and include a recommendation flowchart enabling interdisciplinary scientists to have a quick head start in this domain.

Scope of this review: This review investigates the two primary learning strategies in ML, i.e., supervised and unsupervised, which are commonly used within the context of multi-omics integration. This review considers multi-omics integration as a process of combining different single omics. Although various ML specializations such as reinforcement, hybrid, multi-view and self-supervised learning are now emerging in generic healthcare applications, they have not yet gained enough momentum in multi-omics analysis, hence they remain beyond the scope of this review.

This paper is organized as follows. Section Two provides a short background related to multi-omics and ML. Section Three describes how ML is employed for multi-omics analysis and what are the various real-world challenges of it. In Section Four, details of different multi-omics integration approaches are presented. Section Five, published multi-omics studies using ML methods are discussed. Section Six describes a recommendation flowchart for choosing an appropriate method for multi-omics integration. Conclusions are provided in Section Seven.


## Two. Background

Two point one. Multi-omics

In living beings, genetic information in the cells flows from DNA (deoxyribonucleic acid) to the mRNA (messenger ribonucleic acid) to protein and is dictated by the central dogma of molecular biology. This flow of information is often considered analogous to a computer system which has facilitated the understanding of biological information processing.

The study of DNA, mRNA and proteins is broadly denoted as genomics, transcriptomics, and proteomics respectively. The genetic blueprint of a cell is explored using genomics, which looks at the DNA of individuals and helps us to investigate the presence or absence of certain genes.

are actively expressed and provides information about what is happening at the cellular level. Proteomics helps in characterizing the information flow happening within the cell and the organism in the form of protein pathways and their networks.

Although metabolomics, lipidomics, and glycomics do not form part of the central dogma analysis, they still provide an invaluable amount of information regarding the metabolites, lipids and glycans (synthesized by the proteome via biosynthetic pathways). These substances are the intermediate products of a cell's information flow and therefore are considered to be excellent indicators of the cell's activity. Similar to single-genome studies, metagenomics is used to sequence genetic information from environmental samples without the requirement of isolating individual species.

All measured omics data can be used as a biomarker which helps us to understand and analyse the underlying characteristics and complexities of biological systems. Table one shows some of the important omics used to study biological systems. All of them are part of the same pipeline of biological information, whose output depends on the different inputs and regulation. As shown in Table one, each of these omics can be measured using specialised high-throughput technologies, for example microarray and mass spectrometry for genomics and metabolomics respectively. The table also includes a list of recent reviews on each of these omics. High-throughput generated omics data has played a pivotal role in developing precision medicine biomarkers for diseases such as Alzheimer's, diabetes, cancer, hypertension, cardiovascular and chronic respiratory diseases. Recently, these omics have also been integrated for COVID-nineteen studies. Many other specialised omics have also emerged such as pharmacogenomics, methylomics, interactomics and radiomics.

Overall, these omics provide a complete picture of cell biology and related cellular function. This provided the impetus for the development of various software mechanisms which can offer a prediction of a particular phenotype while using the available next- generation multi-omics data. Furthermore, they can be utilised to develop materials and devices which be used for diagnostic and preventive purpose at the molecular level while targeting molecules with greater accuracy.


## Two point two. Machine learning

Classical statistical modelling has always been the de facto standard choice for health data analysis and its interpretation. In recent years, with the increasing availability of affordable computing power and high-throughput omics data and the success of artificial intelligence technology in various fields, the use of machine learning has become popular in health sciences. Machine learning can be used to mine information hidden in the experimental data. In contrast, a conventional statistics-based model is usually developed using statistical assumptions and draws an inference about a population from a given dataset.

The objective of machine learning methods is to acquire knowledge from historic or present-day data and utilise that understanding to make forecasts or choices for unidentified forthcoming data measures. To assist beginners in the machine learning domain, a glossary of learning approaches covered in this review, standard machine learning terminology and commonly used machine learning algorithms are provided. The basic foundations of machine learning and its uses have been extensively covered in the literature.

Machine learning is employed in a wide range of scenarios, where designing and programming explicit algorithms with optimal results is challenging, such as email filtering, hand-written optical character recognition, and computer vision. Also, it has been deployed for self-driving cars, cyber-security, automated assistants such as 'Siri', websites that recommend items based on the purchasing decisions of other people and novel solutions to some of the challenging problems of the real world.

Deep learning has emerged in recent years as the leading class of machine learning algorithms. It uses neural networks composed of hidden layers performing different operations to find complex representations of data. It has pushed the performance of classifiers beyond that of traditional machine learning algorithms, especially in scenarios involving large-scale datasets with high dimensionality. On the other hand, it is very computationally intensive, requiring high-throughput or high-performance hardware, and lacks explainability in feature selection, black-box approach, in the sense that it is difficult to extract from the network the features that the network has found as mainly responsible for the task, e.g. classification. However, in the context of multi- omic integration, deep learning offers an exciting opportunity.

different keyword and searching across all databases. Although the use of ML in medical science can be dated back to the nineteen seventies, more rapid growth is evident in the past ten years. Moreover, publications based on 'multi-omics integration' and 'multi-omics and machine learning' have started to emerge in the last five years and have gained popularity in the precision and computational medicine domain. Although deep learning is widely popular in other related domains, the interest has been more limited for multi-omics analysis. This is because multi-omics studies are challenging to deploy as they require specialised high-throughput omic infrastructure. This fact is reinforced by the evidence that most of the current literature employs deep learning on large-scale multi-omics datasets from open sources for cancer prognosis and anti-cancer drug response.


## Three. Challenges in multi-omics analysis using machine learning

The use of ML to analyse high-throughput generated multi-omic data poses key unique challenges. They can be summarised as follows.


## Three point one. Heterogeneity, sparsity and outliers

Multi-omic data from different high-throughput sources are usually heterogeneous. For example, transcriptomics and proteomics use different normalisation and scaling techniques before omics analysis. This leads to different dynamic ranges and data distribution. Also, some omics are more prone to generating sparse data than others. Therefore, imputation and outlier detection should be considered for each omic separately, before planning their integration.


## Three point two. Class imbalance and overfitting

In disease classification, certain disease classes are rarer than others which can cause a class imbalance in the multi-omics dataset. For example, primary hypertension is the most common form of hypertension with ninety-five percent prevalence while endocrine hypertension occurs in only five percent. The ML model trained using an imbalanced dataset may be overfitted i.e. high accuracy for training data but underperformance for unseen test data. Therefore, to classify these two types of hypertension one of the following approaches can be used: one, collect more data if possible; or two, consider using weighted or normalised metrics to measure the ML performance; or three, consider over or undersampling the under or over-represented class respectively; or four, consider synthetic sample generation for the under-represented class. Similarly, techniques such as regularisation, bagging, hyperparameter tuning and cross-validation can be used to balance bias-variance trade-off. Any of the above approaches can be used, depending on data and problem, to overcome the class imbalance and overfitting problems.


## Three point three. More features than data.

Most multi-omics datasets suffer from the classical 'curse of dimensionality' problem, i.e. having much fewer observation samples than multi-omics features. The resulting high-dimensional space often contains correlated features which are redundant and can mislead the algorithm training. The dimensional space of the data can be reduced by employing dimensionality reduction techniques such as feature extraction and feature selection. Feature extraction refers here to techniques computing a subset of representative features which summarise the original dataset and its dimensions. These features are functions of the original ones, for instance, principal component analysis, linear discriminant analysis and multidimensional scaling. On the other hand, feature selection finds a subset of the original features that maximise the accuracy of a predictive model. It can be based on prior knowledge or based on a database such as a Biofilter. Formally, feature selection methods can be classed as filter, wrapper and embedded techniques. Xu and Stańczyk provide an excellent resource for understanding and exploring the use of different dimensionality reduction techniques in the generic ML domain. Meng offers a review of these methods from the perspective of multi-omics data analysis.


## Three point four. Computation and storage cost

The use of ML for multi-omics analysis comes with computational and data storage cost. Most ML algorithms require high computation power and large volumes of storage capacity to save the logs, results and analysis. In recent years, ML models can be deployed on dedicated graphics processing units and cloud computing platforms such as Amazon EC2, Microsoft Azure and Google Cloud Platform. The related costs should be considered well in advance before planning an ML-based multi-omics workflow.


## Three point five. What algorithm works best for what conditions?

The commonly used ML algorithms have different attributes and therefore it is crucial to choose an appropriate algorithm for the multi-omics analysis. In the literature, many reviews cover the key strengths and weaknesses of different ML algorithms using single omics and multi-omics datasets. Most of them use a systematic workflow that involves simultaneous performance evaluation of different algorithms using a common dataset. Since each multi-omics dataset is unique, using a similar workflow could allow the selection of the best-suited algorithm. Later, in Section six a recommendation flowchart is proposed which can help the inter-disciplinary user to choose from available methods.

Recently, various artificial intelligence-driven automated ML platforms and tools have also emerged which can be utilised to exhaustively search for the best ML model and corresponding parameter tuning, however, they are computationally expensive.


## Three point six. Translating ML: bench to bedside

Various ML-based multi-omics publications have emerged in the past five years and some use performance metrics such as decision curve and calibration analytics to evaluate their diagnostic utility. Still, only very few have been translated into clinical practice, for example, Idx, FerriSmart and SubtleMR.

One of the key issues which hinder the clinical deployment of ML methods is transparency and explainability. A transparent and explainable ML algorithm seems essential to building trust for clinical decision making. Recently, the U S Food and Drug Administration has issued the "Artificial Intelligence/Machine Learning (AI/ML)-Based Software as a Medical Device Action Plan" to ensure deployment of ML-based products is safe for patients to better assist the health care providers. A recent in-depth analysis by Muehlematter showed most of the FDA approved and "Conformité Européenne" marked ML products are in the field of radiology. It also highlighted the key differences between U S and European policy implications around the approval of AI/ML-based devices.

All the above challenges directly impact the use of ML for multi-omics analysis. However, there are few other challenges related to multi-omics studies which are not ML related such as study design, multi-site sample collection and management, multi-site data sharing and governance, visualisation, ethical standards, and finally making the research reproducible and translational. A broader checklist of criteria is investigated by McShane while focusing on various aspects ranging from specimen requirements, predictive model development to clinical trial designing and related regulatory approvals.


## Four. Data integration methods for multi-omics

In recent years, various new data integration methods have been introduced from the modern developments in mathematical, statistical and computational sciences. For the benefit of the readers, Table five includes a summary of a few reviews which cover the breadth of multi-omics integration for generic as well as specialised domains such as oncology and toxicology. Most of these reviews have strived to introduce different categorical terminologies which enable them to group the integration methods based on different factors or parameters.

As mentioned earlier, this section adopts the categorical terminologies from Ritchie and builds upon it to summarise a complete spectrum of recent integration methods. It concisely covers them giving a clear perspective to a new interdisciplinary user. The various integration methods are classed as either 'concatenation-', 'model-' or 'transformation'-based and described below in detail.


## Four point one. Concatenation-based integration methods

Concatenation-based integration methods consider developing a model using a joint data matrix which is formed by combining multiple omics datasets. Fig. two shows the stages of concatenation-based integration. Stage one includes the raw data from three individual omics (e.g. genomics, proteomics, and metabolomics) along with the corresponding phenotypic information. Commonly, concatenation-based integration does not require any pre-processing and hence does not have a stage two. In stage three, the data from the individual omics is concatenated to form a single large matrix of multi-omics data. Finally, in stage four the joint matrix is used for supervised or unsupervised analysis. The main advantage of using concatenation-based methods is the simplicity of employing ML for analysing continuous or categorical data, once the concatenation of all individual omics is completed. These methods use all the concatenated features equally and can select the most discriminating features for a given phenotype.

The different concatenation-based integration methods can be further classed as:


## Four point one point one. Supervised learning concatenation-based methods

Different concatenation-based supervised learning methods have been used for phenotypic prediction. In scenarios where the number of features in the joint matrix are higher, different feature selection methods described in Section three can be employed during concatenation.

The concatenated multi-omics data (in the form of a joint matrix) is provided as input to different classical M L methods such as decision tree, naive Bayes, artificial neural networks, support vector machine, k-nearest neighbors, random forest and K-Star in the literature. For example, a joint matrix of multi-omics features (which included gene expression, copy number variation and mutation) was used with classical random forest and support vector machine to predict anti-cancer drug response.

Similarly, multivariate LASSO models have been investigated. Also, Boosted trees and support vector regression have been investigated for finding the longitudinal predictors of glycaemic health.

Other than classical M L algorithms, deep neural networks have also been widely used to analyse concatenated multi-omics data. They have been studied to identify robust survival sub-groups of liver cancer using RNA, miRNA and methylation data.


## Four point one point two. Unsupervised learning concatenation-based methods

Various concatenation-based unsupervised methods have been used for clustering and association analysis. Different matrix factorisation-based methods have evolved in recent years. Joint non-negative matrix factorisation was proposed to integrate multi-omics data with non-negative values. It involved decomposing the joint matrix into loadings and factors, bringing the different omics into a common basis matrix. Joint non-negative matrix factorisation is computationally slow and needs large memory allocation.

Similarly, Shen proposed iCluster framework which used principles similar to non-negative matrix factorisation but allows integration of datasets having negative values. They showed the functioning of the framework by using copy number, mRNA expression and methylation data to conduct a cancer subtype discovery in glioblastoma. This framework was also employed for a landmark study that used genomic and transcriptomic data from two thousand breast tumours and discovered novel sub-groups amongst them.

Later, the iCluster+ framework by Mo, offered a significant enhancement over the iCluster framework. The iCluster plus framework can discover patterns and combine a range of omics having binary, categorical and continuous values and was demonstrated by combining genomic data from the colorectal cancer datasets.

Another adaptation of non-negative matrix factorisation was evaluated as JIVE which captures joint variation across integrating data types and structural variation of each data type along with the residual noise. It was used to investigate gene expression and miRNA data on brain tumour samples. The sparsity problem in JIVE was improved by Joint Bayes Factor. Joint Bayes Factor used joint factor analysis to evaluate the feature space and converted it into shared and datatype-specific components.

The MoCluster proposed by Meng, used multi-block multivariate analysis for highlighting the patterns across different input omics data and then finds the joint clusters amongst them. MoCluster was validated by integrating proteomic and transcriptomic data and shows a noticeably higher clustering accuracy and lower computation cost in comparison to both Cluster and iCluster plus.

Fridley has studied the genomic effects due to the gemcitabine drug using high-throughput data from mRNA expression and SNPs. They integrated these two datasets into one large input matrix and developed a Bayesian pathway analysis that uses a stochastic search variable selection. They proposed that the Bayesian integrative model offers better performance in detecting the genomic effects in comparison to using conventional single-omics analysis. Similarly, Zhu has also explored Bayesian network to understand cell regulation in yeast using metabolomics and transcriptomics data.

Also, LRAcluster was developed to integrate high-dimensional multi-omics data and find low-dimensional manifold to identify molecular subtypes of cancer.

Recently, iClusterBayes was introduced by Mo, which is a fully Bayesian latent variable model. It overcomes the limitations of iCluster plus, in terms of statistical inference and computational speed. iClusterBayes includes a binary indicator prior for selection of variable and generalises for binary data and count data. Also, Argelaguet have developed Multi-Omics Factor Analysis which disentangles the heterogeneity shared across different omics to discover the principal source of variability. It can integrate partially overlapping datasets.


## Four point two. Model-based integration methods

Model-based integration methods create multiple intermediate models for the different omics data and then build a final model from various intermediate models. Stage One sets up the raw data from the three individual omics along with the corresponding phenotypic information. In Stage Two, individual models are developed for each of the omics which are later integrated into a joint model in Stage Three. Finally, in Stage Four the joint model is analysed. The major advantage of model-based integration methods is that they can be used for merging models based on different omic types, where each model is developed from a different patient group having the same disease information.

Model-based integration approaches facilitate the understanding of interactions amongst different omics for a certain phenotype (for example, survival in pancreatic cancer). The final multi-dimensional joint model in Stage Four can be built using an M L algorithm (such as neural networks) which uses the most relevant variables from each omics models (from Stage Three). This approach allows the analysis of the improvement in the predictive power for individual models and also finds the best discriminating features.

The different model-based integration methods can be further classed as follows.


## Four point two point one. Supervised learning model-based methods

Model-based supervised learning methods include a variety of frameworks for developing a model, such as majority-based voting, hierarchical classifiers and ensemble-based approaches (such as XGBoost and k-nearest neighbors).

Deep learning methods have also been adopted for model-based supervised learning. MOLI, multi-omics late integration, method used type-specific encoding sub-networks to learn features from somatic mutation, CNA, and gene expression data independently and then later concatenated them for predicting the response to a given drug. Lee has proposed a deep learning-based auto-encoding approach for integrating four omics to create a survival prediction model. Also, HI- DFNForest hierarchical integration deep flexible neural forest framework was developed which uses a stacked auto- encoder to learn high-level representations from three omic datasets. Later, these representations are integrated to predict cancer subtype classification. Similarly, Chaudhary has used autoencoders along with SVM for survival prediction in subgroups of hepatocellular carcinoma.

In the past years, ATHENA, Analysis Tool for Heritable and Environmental Network Associations, was developed for analysing multi- omics data. It uses grammatical evolution neural networks along with Biofilter and Random Jungle to investigate different categorical and quantitative variables and develop prediction models.

Recently, MOSAE, Multi-omics Supervised Autoencoder, was developed for pan-cancer analysis and compared with conventional ML methods such as SVM, DT, naïve Bayes, KNN, RF and AdaBoost. Similarly, Denoising autoencoder has been incorporated along with L one-penalized logistic regression for identifying ovarian cancer subtypes.


## Four point two point two. Unsupervised learning model-based methods

Various model-based unsupervised learning methods have been implemented in the past. PSDF, Patient-Specific Data Fusion, is a non-parametric Bayesian model for clustering prognostic cancer subtypes by combining gene expression and copy number variation data. It uses a two-step process and limits the integration to only two datatypes. Similarly, CONEXIC also uses a BN to integrate gene expression and copy number variation from tumour samples to identify driver mutations. On the other hand, clustering methods such as FCA, Formal Concept Analysis, consensus clustering, MDI, Multiple Dataset Integration, PINS, Perturbation clustering for data integration and disease subtyping, PINS Plus and BCC, Bayesian consensus clustering, are more flexible and allow late-stage integration of clusters.

Different network-based methods are also available for association analysis. Lemon-Tree implemented ensemble methods for reconstructing module networks which used somatic copy number alterations and gene expression in brain tumour samples. Furthermore, SNF, Similarity Network Fusion, constructs networks of samples for respective data type and then effectively fuses them into a joint network which denotes the complete range of original data. It combines mRNA expression, DNA methylation and microRNA, miRNA, expression data from cancer datasets.


## Four point three. Transformation-based integration methods

Transformation-based integration methods transform each of the omics datasets firstly into graphs or kernel matrices and then combine all of them into one before constructing a model.

Graphs provide a formal means to transform and portray relationships between different omics samples where the nodes and edges of a graph represent the subjects and their relationships, respectively. Similarly, Kernel methods enable the transformation of data from its original space into a higher dimensional feature space. These methods then explore linear decision functions in the feature space which were non-linear in the original space.

The transformation-based integrative methods can be classed as follows.


## Four point three point one. Supervised learning transformation-based methods

In the past, various transformation-based supervised learning methods have been presented. Most of them are kernel and graph-based algorithms. The kernel-based integration approaches include SDP-SVM, Semi-Definite Programming SVM, FSMKL, Multiple Kernel Learning with Feature Selection, RVM, Relevance Vector Machine and Ada-boost RVM. Moreover, fMKL-DR, fast multiple kernel learning for dimensionality reduction, has been used along with SVM for combining gene expression, miRNA expression, and DNA methylation data. Similarly, the graph-based integration approaches consist of graph-based semi-supervised learning, graph sharpening, composite network and BN.

Overall, it is evident from the literature that kernel-based algorithms have superior performance to graph-based approaches, but they usually need more time for the training phase. In contrast, graph-based approaches can disclose the relations between samples while taking less computation time.

comparison between different graph- and kernel-based integration approaches in a supervised learning context using various standardized test datasets. It highlights the better classification performance of RVM, Ada- boost RVM and SDP-SVM in comparison to semi-supervised learning, graph sharpening, composite network and BN.

Recently, MORONET, Multi-Omics gRaph convolutional NETworks, is introduced, which use graph convolutional networks taking benefit of the omics features and the associations among patients, as defined by the patient similarity networks, for better classification results.


## Four point three point two. Unsupervised learning transformation-based methods

Different transformation-based unsupervised methods have been introduced. Some of them are kernel- and graph-based methods. Lately, rMKL-LPP (regularised multiple kernel learning for Locality Preserving Projections) was implemented for clustering analysis. It used an individual kernel for each omics along with a graph embedding framework to identify biologically meaningful subgroups for five different cancer types. Similarly, PAMOGK is developed for integrating multi-omics data with pathways using graph kernel, SmSPK (smoothed shortest path graph kernel). It used somatic mutations, transcriptomics and proteomics data to find subgroups of kidney cancer.

Meta-SVM (Meta-analytic SVM) is proposed by Kim, which integrates multiple omics data and able to detect consensus genes associated with diseases across studies such as breast cancer and idiopathic pulmonary fibrosis. Recently, NEMO (NEighbor-hood based Multi-Omics clustering) is introduced which uses an inter-patient similarity matrix-based distance metric for evaluating the input omic datasets individually. These omics matrices are then combined into one matrix and then analysed using spectral-based clustering. It can work on partial data sets (no imputation needed), where measurements are only available for a subset of omics data.

Table six highlights the advantages and disadvantages of various integration methods. Table seven summarises various multi-omics integration methods based on learning type.


## Five. Application of integrative methods in multi-omics studies

The availability of high-throughput omics provides a unique opportunity to explore the complex relationships between different omics and phenotypic targets instead of mono-omics evaluation. This section describes various multi-omics studies which deployed methods investigated in the previous section. Table eight summarises different phenotypic target-based, multi-omics studies published and tabulates them across the span of seven main omics namely, genomics, transcriptomics, metabolomics, proteomics, glycomics, lipidomics and epigenomics. Genomics is further divided into gene expression, DNA methylation, somatic point mutation and copy number alteration. Similarly, transcriptomics is further classed into long non-coding RNAs and microRNAs. The various multi-omics studies are broadly grouped based on the target and the corresponding ML method used.

It is evident from Table eight that most of the multi-omics studies focus on different forms of cancer. In particular, the presence of many multi- omics studies related to breast and ovarian cancer highlights the research thrust by the scientific community in these domains.

Many intra-omics studies have successfully explored the integration of gene expression and DNA methylation. LASSO methods have been used for this particular integration by Taskesen and Lee for acute myeloid leukaemia and breast cancer respectively. LASSO has also been employed for cancer prognosis. Similarly, mRNA - miRNA integration was investigated using Neural Fuzzy Network for colorectal cancer, SVM for pancreatic cancer, and RF for cardiac tissue ageing and ovarian cancer respectively. SVM has also been used for oral squamous cell carcinoma study by integrating different transcriptomics namely mRNA, miRNA and long non-coding RNA.

Metabolomics and proteomics have been integrated using RF for analysis of prostate cancer and thyroid functioning. Similarly, metabolomics is integrated with mRNA for studying ulcerative colitis and cancer survival. On the other hand, glycomics and epigenomics have only appeared once in the multi-omics context (along with mRNA and metabolomics) and used for the study of age-related comorbidities using a graphical variant of RF.

Recently, metabolomics and proteomics have also been integrated with lipidomics to evaluate COVID-nineteen patients using Partial Least Squares Discriminant Analysis and Extra Trees.

Multi-omics studies have also been successfully conducted in plants and animals such as canine heart disease.

Overall, the different recent multi-omics studies highlight the superiority of integration methods in understanding the complexity of different diseases and uncovering the underlying abnormalities from the vastly generated multi-omics data, which is not always possible with individual omics analysis.


## Six. Recommendations

Today a plethora of multi-omic integration methods are available for both supervised and unsupervised learning as evident in the current review. This information can overwhelm interdisciplinary scientists and would require a time-consuming effort to understand the challenging mathematical and computational concepts behind them. Hence, we suggest that interdisciplinary teams working on multi-omics always include ML practitioners to assist with the choice of methods, the development of solutions, the interpretation of results and their significance and limits. Such truly interdisciplinary teams offer real opportunities for better mutual understanding of the different fields, practice and expertise necessary, leading ultimately to more robust conclusions. Also, to facilitate the method selection process, a recommendation flowchart is proposed. It shows the various decision steps required for choosing an appropriate method or family of methods for a given scenario. For example, to choose a method for integrating two omics for unsupervised learning one can choose a model-based method such as PSDF or Lemon-Tree if the two omics are gene expression and CNV, otherwise MDI or SNF can be used. Similarly, NEMO can be used in scenarios where the datasets are partially overlapping, and a transformation approach is required. Hence, it can be used for biomedical analysis, including diagnosis, prognosis and biomarker identification, by posing them as supervised or unsupervised learning problems.

Clearly, a one-size-fits-all approach is not feasible. Also,

unfortunately, the existing literature does not provide many direct comparisons between methods using the same publicly available datasets. Hence, to choose the best method which suits a given dataset and question, an empirical approach that investigates the use of different methods, guided by ML practitioners is recommended.


## Seven. Conclusions

This paper reviewed various ML approaches used for the integration of multi-omics data for analysis. A concise background of multi-omics and ML was presented. It examined the concatenation-, model- and transformation-based integration methods, employed for multi-omics data along with their advantages and disadvantages. Also, various existing multi-omics studies have been summarised. Finally, a recommendation flowchart is presented for interdisciplinary professionals to choose an appropriate method for a multi-omics dataset. Overall, this work showcases the recent findings in the multi-omics domain and signifies the key role of ML in the future of personalised healthcare.


## Disclosure

The authors have nothing to disclose.


## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.


## Acknowledgement

This project has received funding from the European Union's Horizon twenty twenty research and innovation programme under grant agreement number six three three nine eight three. Ewan Pearson and Emanuele Trucco would like to acknowledge the National Institute for Health Research global health research unit on global diabetes outcomes research at the University of Dundee for useful discussions.