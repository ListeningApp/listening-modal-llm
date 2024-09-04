## Chapter twenty. Data Assimilation

Data assimilation is a powerful methodology for incorporating data into a mathematical model in a way that is consistent with physical processes. In this chapter we present a Bayesian approach to data assimilation, discuss the Kalman filter algorithm for data assimilation for linear processes and linear data models in the presence of Gaussian noise, and describe a simple version of the ensemble Kalman filter, which relies on stochastic simulation.


## Twenty point one. Data Assimilation and Climate

To predict the state of the climate system at any future time or to recreate its past, we must necessarily rely on mathematical models and numerical simulations. Throughout this book, we have encountered several types of models, some of them conceptual and others closer to the "real" world of physics, chemistry, and biology. Most of these models are process models-models that are described by systems of equations that determine the state variables (also called process variables) and their evolution in time. In data assimilation, one links such process models with data models-models of observational data of these same state variables, together with their uncertainties. The idea is that, by making it consistent with the available observations, a process model becomes better at predicting future states of the system. Data assimilation is an essential technique in any scientific discipline that is data-rich and for which well-founded predictive mathematical models exist. The technique originated in engineering and has found widespread application in many other disciplines, most notably in weather prediction, where it has extended the ability to predict weather more or less accurately from hours to days. Not only does the technique generate estimates of the state of the weather system, but it also produces an assessment of the uncertainties in the prediction, often in the form of probability distributions for process variables or parameters.

A typical example of a data model is the record of SSTs obtained with a drifting instrument that periodically reports local measurements. The record contains information about the temperature at the location of the instrument (but not anywhere else). The


## Chapter twenty. Data Assimilation

record may have gaps for times when the instrument is shut down, and there may be uncertainties regarding the drifter's location and due to limited accuracy of the thermometer. Any data model contains an element of randomness.

Data assimilation can be applied to estimate process variables at a certain time using all available observational data, including those made at a later time (reanalysis or smoothing mode), or to estimate the present state using past and present observations (analysis or filtering mode), or to estimate process variables that are inaccessible to observations, such as future states or states between measurements (forecasting or predicting mode). In any of these modes, problems can be approached with a variety of techniques, including optimization methods, which attempt to find the best fit of a parameterized process model to a given set of data; maximum likelihood methods, which work in a similar spirit but have more detailed statistical models for the uncertainties in the process; and Bayesian methods.


## Twenty point two. Example

The following example illustrates the application of data assimilation methodology to reanalysis, filtering, and forecasting.

Consider a process with four real-valued state variables, {X; : i equals one, ..., four}. The state variables are related by the process model

X sub i plus one equals a X sub i plus {;, i equals one, two, three, (Equation twenty point one)

where a is a known positive constant and the random process error terms 5, are either identically zero or have a standard normal distribution, §; ~ N(0, one). The convention is to use upper-case letters X, Y, Z, etc., for random quantities and the corresponding lower-case letters x, y, z, etc., for their realizations. Random error terms are indicated by Greek letters.

The data model consists of two observations, {Y; : i equals two, three}, and is related to the process model through the identities

Y sub i equals X sub one plus {; i equals two, three, (Equation twenty point two)

where the random observational error terms {; are independent and identically distributed with a standard normal distribution. The entire model is shown schematically in Figure twenty point one. The problem of estimating X sub one from the observations Y sub two and Y sub three is a reanalysis problem, estimating X sub two from Y sub two or X sub three from Y sub two and Y sub three is a filtering problem, and estimating X sub four from Y sub two and Y sub three is a forecasting problem.

X sub one minus X sub two minus X sub three minus X sub four plus Y sub two Y sub three


## Twenty point two point one. Variational Approach

We first demonstrate a variational approach. If the process error terms §; are all zero, we minimize the cost function J,

J(x sub two, x sub three; )23/3) equals (x sub two minus two) squared plus (x sub three minus y sub three) squared.

(Equation twenty point three)


## Twenty point two. Example

Because of the process model relation x sub { three } equals alpha x sub { two }, J reduces to a function J sub { zero } of x sub { two } alone,

J ( x sub { two } , alpha x sub { two } ; y sub { two } , y sub { three } ) equals J sub { zero } ( x sub { two } ; y sub { two } , y sub { three } ) equals ( x sub { two } minus y sub { two } ) squared plus ( alpha x sub { two } minus y sub { three } ) squared. (Equation twenty point four)

This function reaches its minimum at X sub two star equals left parenthesis Y sub two plus alpha Y sub three right parenthesis divided by left parenthesis one plus alpha squared right parenthesis, so X sub two star is the reanalysis value of X sub two. The corresponding filtering value of X sub three is X sub three star equals alpha X sub two star, the forecast value of X sub four is X sub four star equals alpha X sub three star equals alpha squared X sub two star, and the reanalysis value of X sub one is X sub one star equals alpha to the power of negative one X sub two star. We obtain the same values if we use the process model relation X sub three equals alpha X sub two to eliminate X sub two from the cost function twenty point three and minimize with respect to

X sub three. These solutions do not give any uncertainty estimates confidence sets for the reanalysis and filtering values. In this case, such estimates can be inferred from the data model twenty point two and the explicit form of the solution. However, in the general case, the reanalysis and filtering values are obtained numerically and uncertainty estimates are not immediately available. If the process error terms five do not vanish, the cost function must be extended with additional terms. We refer the reader to for a more detailed discussion of the variational approach and its relation to the probabilistic approaches discussed in the next sections.


## Twenty point two point two. Maximum Likelihood Approach

Next we demonstrate a maximum likelihood approach to the same example. Assume that the process error variables Xi sub j are random and have standard normal distributions. Assume for the moment that X sub one has a fixed but unknown value X sub one, which we wish to estimate from the observations Y sub two and Y sub three. This is therefore a reanalysis problem. Probability theory shows that

Y sub two is distributed as N left parenthesis alpha X sub one, one plus tau squared right parenthesis, Y sub three is distributed as N left parenthesis alpha squared X sub one, one plus tau squared plus alpha squared right parenthesis, cov Y sub two, Y sub three equals alpha. The joint distribution of left parenthesis Y sub two, Y sub three right parenthesis is Gaussian with density f sub Y sub two, Y sub three left parenthesis Y sub two, Y sub three right parenthesis proportional to exp left parenthesis negative one divided by two left parenthesis Y sub two minus alpha X sub one, Y sub three minus alpha squared X sub one right parenthesis Sigma to the power of negative one left parenthesis Y sub two minus alpha X sub one, Y sub three minus alpha squared X sub one right parenthesis transpose, twenty point five where Sigma is the covariance matrix,

Sigma equals left parenthesis one plus tau squared, alpha, alpha, one plus tau squared plus alpha squared right parenthesis. The proportionality constant implied in Equation twenty point five does not depend on the unknown parameter X sub one. If Y sub two and Y sub three are actual observational data, the maximization of the expression on the right-hand side of Equation twenty point five leads to the maximum likelihood estimate

X hat sub one equals alpha left parenthesis one plus tau squared right parenthesis Y sub two plus alpha squared tau squared Y sub three divided by alpha squared plus alpha squared tau squared plus tau to the power of four, twenty point six

The reanalysis estimate X hat sub one is a linear combination of the observations Y sub two and Y sub three. If zero less than alpha less than one, Y sub two has the larger weight. If, furthermore, the observation errors Zeta sub i have very small standard deviations left parenthesis tau much less than one right parenthesis, the weight for Y sub three is very small, so the reanalysis estimate depends mainly on the observation that was made right after the unknown state. One can show that the expectation of X hat sub one equals X sub one, so the estimate is unbiased, and it is not hard to show that X hat sub one has a normal distribution and to find its variance.

Approaches to estimating X sub two left parenthesis reanalysis right parenthesis and X sub three filtering from observations using the maximum likelihood method are discussed in the exercises. We next introduce a general Bayesian approach to data assimilation and then return to this example.


## Twenty point three - Bayesian Approach

Chapter Twenty. Data Assimilation

The contemporary approach to analysis and forecasting problems is based on Bayes' rule. This rule was first formulated by the English mathematician and Presbyterian minister Thomas Bayes, seventeen hundred one to seventeen sixty-one. It yields estimates that are asymptotically correct and does not require an appeal to the law of large numbers, which would make little sense in the climate context. To simplify the following presentation, we assume that all state variables and data are finite-dimensional vectors-a reasonable assumption for data but a substantial simplification for state variables.

Suppose we are interested in estimating a vector X of process variables with a known or assumed P D F F X. The distribution may come from long-term observations or from another forecast model and is referred to as the prior distribution on X. The data model uses a vector Y of observations of the components of X, which may also include other random effects. We assume that for each possible realization x of X, the conditional distribution F Y given X of Y given x is known. This is essentially the data model.

Now, suppose that the observation of Y at a particular instance results in the value y. The goal is to incorporate this value in the distribution of X by constructing the conditional distribution F X given Y of X given y. This conditional distribution is referred to as the posterior distribution on X. To find its formula, we note that the joint probability density F X Y of process variables and observations can be expressed in two ways,

Twenty point seven

The prior distribution F X is assumed to be known, as is the data model F Y given X; the posterior distribution F X given Y is sought, and the distribution of the observations F Y is unknown. After dividing both expressions by F Y of y, we obtain Bayes' rule,

F X given Y of x equals F Y given X of y times F X of x over F Y of y.

Twenty point eight

Note that both sides depend on x and y. The quantity y is given as an observation; therefore the denominator on the right-hand side is fixed, although unknown. The entire equation has the form

F X of x is proportional to F X given X of y times F X of x, twenty point nine,

where the implied proportionality constant depending on F Y makes the term on the left a P D F. The constant can be found and equality established by computing an integral, either with analytical techniques or with numerical simulations.

In the case of Gaussian random variables, all integrations that would be required in equation twenty point nine can, however, be replaced by matrix algebra, as the following lemma shows.

Lemma Twenty point one. Let X and Y be Gaussian random variables such that X follows normal distribution with mean U and covariance P and Y given X follows normal distribution of H X and R, where H is a matrix. Then X given Y follows normal distribution with mean U star equals U plus K Y minus H U and covariance P star equals I minus K H P, where K is the gain matrix,

K equals P H transpose times R plus H P H transpose inverse. Twenty point ten.

Proof. According to equation twenty point nine, the conditional probability density F X given Y satisfies

F X given Y of x is proportional to exponent of negative open parenthesis x minus H y transpose R inverse x minus H y minus y minus U transpose P inverse y minus U. Twenty point eleven.


## Twenty point four. Sequential Data Assimilation

Completing the square, we obtain a Gaussian distribution,

F sub X given script Y of x is proportional to exponent of negative one half open parenthesis x minus mu star transpose P star inverse x minus mu star. Twenty point twelve,

with mu star equals script E of X given y equals open parenthesis P inverse plus H transpose R inverse H close parenthesis inverse open parenthesis P inverse mu plus R inverse H transpose y close parenthesis equals mu plus K open parenthesis y minus H mu close parenthesis, P star equals variance of X given y equals open parenthesis P inverse plus H transpose R inverse H close parenthesis inverse equals I minus K H P. We leave the details of these calculations to the reader.

The distribution F sub X given script Y given in the lemma is the posterior distribution. Its covariance matrix P star does not depend on the value y. The lemma tells us that P star equals P minus C, where C is a symmetric positive semidefinite matrix. In this sense, the posterior variance is smaller than the prior variance, and we have reduced uncertainty by using the data. The lemma also shows that the mean of the posterior distribution is the prior mean updated by the gain applied to the difference between the observed Y and its mean value H mu. Recall that the difference between an observed quantity and its temporal mean is called "anomaly" in climate science, so this concept arises naturally in Bayesian data assimilation.


## Twenty point three point one . Example: Bayesian Approach

We return to the example introduced in Section Twenty point two. Assume that X sub one follows normal distribution with mean mu zero, variance sigma squared, where mu zero and sigma squared are known. Then the column vector X equals X sub one to X sub four of process variables has a multivariate normal distribution X follows normal distribution with mean vector mu equals open parenthesis omega zero, alpha mu zero, alpha squared mu zero, alpha cubed mu zero close parenthesis transpose and a suitable covariance matrix Sigma. This is the prior distribution F sub X on X. It does not use any observations. Explicitly,

F of x is proportional to exp of negative one half of x minus mu transpose sigma inverse x minus mu. The column vector Y equals Y two, Y three transpose of observations and the vector X of process variables are related by the equation Y tilde equals H X plus zeta two xi three transpose, where H equals zero one zero, zero zero one. Given a particular realization of the process variables, Y then has a multivariate normal distribution, Y given x follows N of H x, tau squared I, where I is the two by two identity matrix. All quantities can be computed from the gain matrix K, which will also be derived in the exercises.

It is instructive to compare the standard deviations of the prior and posterior distributions for X one (reanalysis) and for X three (filtering). These quantities are computed in Exercise four. It turns out that var of X one given y is less than var of X one which equals sigma squared and var of X three given y is less than var of X three which equals sigma squared alpha to the fourth plus alpha squared plus one, as expected. However, var of X one given y cannot be made arbitrarily small, even if z is small, while var of X three given y equals O of tau squared. Details are in the exercises.


## Twenty point four - Sequential Data Assimilation

We now focus on reanalysis, filtering, and forecasting for time-dependent processes. The data arrive as a time series-a sequence of realizations of a discrete-time stochastic process.

Suppose the process variables are X of k, k equals zero, one, and the observations are Y of k, k equals one, two, and so on. A starting value X of zero for the process variables is allowed to incorporate a background state for which no observations are available. We use the notation X of zero to N for a sequence of X of k: k equals zero, one, through N of vector-valued random variables and x of zero to N for a sequence of its realizations, and similarly for Y. We are interested in estimating X of n, given Y of one to N (reanalysis), or given Y of one to n (filtering), or given Y of one to n minus one (forecasting).


## Chapter Twenty - Data Assimilation

Joint P D F s (also called probability mass functions) and conditional P D F s are identified by suitable indices. For example, f of x from zero to n, Y from one to n of x from zero to n, y from one to n is the joint density function of the process variables X of zero, through X of n and observations Y of one, through Y of n, and f of x from two to n given Y from one to n minus one which is x from two to n is the conditional P D F for X from two, through X of n given observations y from one, through y of n minus one. The latter is a function of y from one to n minus one and x from two to n. Since observations arrive sequentially, one can try to find forecast and filter estimates also sequentially.


## Twenty point four point one - Filtering and Forecasting for Markov Chains

Definition Twenty point one. A discrete-time stochastic process X(Zero : N) has the Markov property if its pdfs satisfy f X(n:N)|x(Zero:n-1)(X(n: N)) = f X(n:N)|x(n-1)(X(n:N)), n equals One, and so on, N, for all X(n : N). A discrete-time stochastic process that has the Markov property is called a Markov chain.

Intuitively, the Markov property says that, to predict future observations X(n : N) of the stochastic process, it is sufficient to know the immediate past X(n-1). Additional knowledge of the more distant past X(Zero : n-2) does not change the predictions of the future. An induction argument shows that the joint distribution of X(Zero : n) can then be written as a product of conditional distributions,

f X(Zero:n)(X(Zero: n) = f X(Zero)(X(Zero))] [f X()|X(j-1)(X(j)), n equals one, two, and so on j equals one n

The functions f X(i)|X(j-1)(X(j)) are called transition probabilities of the Markov chain. We shall also assume throughout that f X(one:n)x(:)(y(one : n) equals f X()|X(j)(y(j), n equals one, two, and so on j equals one n

This identity implies that, given the sequence of process variables X(Zero : n), the observations Y(one : n) are independent of one another and their distributions do not depend on X(Zero). In particular, it follows that given X(i), the observation Y(i) is independent of all other observations Y(j) (j does not equal i).

We can now formulate a basic algorithm for filtering and forecasting of Markov chains.


## Algorithm Twenty point one (Filtering and prediction). Given

(i) a prior distribution f X(Zero)

(ii) transition probabilities f X(i)X(i-1) (i equals one, and so on N) for the process variables, and

(iii) conditional distributions f y(i)|X(i) (i equals one, and so on N) for the observations, the following algorithm gives the filtering distributions f X(i)y(one:i) and forecasting distributions f X(one)y(one:one-1):

Step one. Set f X(one)y(one)(X(one)) x f X(one)|X(one)(y(one))f X(one)(X(one)),

f X(one)(X(one) equals f X(one)X()(X(one)f X()(X(Zero)dX(Zero),

where the proportionality constant is chosen such that a pdf with respect to X(one) is generated.


## Twenty point five. Kalman Filtering

Step Two. Suppose i belongs to the set two , three , and so on N and the filtering pdf of X at i minus one given y from one to i minus one is given. Set f of X at i given y from one to i minus one of x at i is equal to the integral of f of X at i given x at i minus one of x at i times f of X at i minus one given y from one to i minus one of x at i minus one d x at i minus one , f of X at i given y from one to i of x at i is proportional to f of Y at i given x at i of y at i times f of X at i given y from one to i minus one of x at i , where the proportionality constant is chosen such that a pdf with respect to x at i is generated.

The correctness of this algorithm can be proved with induction. Step one is just the law of total probability to obtain f of X at one and Bayes' rule to obtain f of X at one given y at one . For the induction step, the formula for the forecasting distribution is again just the law of total probability, and the filtering distribution can be obtained from

F sub X of I given Y of one to I of X of I equals F sub X of I given Y of I Y of one to I minus one of X of I is proportional to F sub Y of I given X of I Y of one to I minus one of Y of I of X of I equals F sub Y of I given X of I of Y of I F sub X of I given Y of one to I minus one of X of I. The last equation follows because the observations Y of I were assumed to be independent of the other observations conditioned on the X of I in Equation twenty point fifteen.

Once the filtering distributions are known, the reanalysis distributions F sub X of I given Y of one to N of X of I can be obtained recursively for

I equals N, N minus one, down to zero. Algorithm twenty point two, Reanalysis. Given one, transition probabilities F sub X of I given X of I minus one of I equals one, down to N for the process variables and two, filtering distributions

F sub X of I given Y of one to I of I equals one, down to N, the following algorithm gives the reanalysis distributions

F sub X of I given Y of one to N: Step one. If I equals N, the filtering distribution and the reanalysis distribution coincide.

Step two. Suppose I in one, two, down to N minus one and the reanalysis pdf F sub X of I plus one given Y of one to N is given. Set

F sub X of I given X of I plus one, Y of one to I of X of I is proportional to F sub X of I plus one given X of I of X of I plus one F sub X of I given Y of one to I of X of I, F sub X of I given Y of one to N of X of I equals integral F sub X of I given X of I plus one, Y of one to I of X of I F sub X of I plus one given Y of one to N of X of I plus one D X of I plus one, where the proportionality constant is chosen such that a pdf with respect to X of I is generated.

The correctness of this algorithm is proved with backwards induction.

Algorithms twenty point one and twenty point two provide a general framework for reanalysis, filtering, and forecasting. However, they are usually impossible to implement, due to multiple difficulties. For general process models, it is often not possible to obtain all the required transition probabilities, even in very simple cases. In the case of a process described by differential equations, a closed form solution would be required, followed by a complicated change of variables. Even if the transition probabilities were known, each step would require the computation of many integrals, one given explicitly in the algorithm and another to determine the proportionality constants. These integrations are usually impossible to do in closed form, and in the case of five or more state space dimensions they are also difficult to do numerically.


## Twenty point five. Kalman Filtering

If the prior distribution on X of zero is Gaussian, if the process is described by linear equations, and if the data model is also Gaussian with means that depend linearly on the pro-

Downloaded August thirty twenty-three to one three one point two one two point two five zero point one zero three. Redistribution subject to SIAM license or copyright; see https://epubs.siam.org/terms-privacy


## Chapter twenty. Data Assimilation

cess variables, then all probability distributions in the reanalysis and filtering algorithms are also Gaussian, and all integrations reduce to matrix manipulations. The result is the famous Kalman filtering algorithm, first proposed by the Hungarian-American engineer and mathematician Rudolf (Rudy) Emil Kalman.

Assume that the process variables X of I in R of N form a linear process model,

X of I equals M sub I X of I minus one plus xi sub I, I equals one through N,

with X of zero follows N of mu, Sigma. The more general process model X of I equals M sub I X of I minus one plus b of I plus xi sub I can be reduced to Equation twenty point sixteen. Assume, furthermore, that the data variables Y of I in R of M are linearly related to the process variables,

Y of I equals H sub I X of I plus zeta sub I, I equals one through N.

The M sub I and H sub I are matrices of suitable dimensions, and the xi sub I in R of N and zeta sub I in R of M are random variables, independent of each other and of X of zero, distributed as xi sub I follows N of zero, Q sub I and zeta sub I follows N of zero, R sub I. The assumptions cover the case where the dimension m sub I of the Ith observation Y of I depends on I or where some of the Y of I are absent.

Then the theory of multivariate normal distributions implies that the X of I and Y of I are also Gaussian, as are all conditional variables. In particular, X of one follows N of M sub one mu, Q sub one plus M sub one Sigma M sub one transposed. It is therefore sufficient to describe the means and covariance matrices of these variables. We use the following abbreviations:

mu sub I given I minus one equals E of X of I given Y of one to I minus one, Sigma sub I given I minus one equals VAR of X of I given Y of one to I minus one, mu sub I given I equals E of X of I given Y of one to I, Sigma sub I given I equals VAR of X of I given Y of one to I, mu sub I equals E of X of I given Y of one to N, Sigma sub I equals VAR of X of I given Y of one to N, with the convention mu sub zero one zero equals mu, mu sub one zero equals six X of one equals M sub one u and, similarly, Sigma sub O of zero equals Sigma, Sigma sub one given zero equals Q sub one plus M sub one Sigma M sub one transposed. The quantities u are conditional means and the quantities sum conditional covariance matrices. The subscript I given I minus one refers to a forecasting quantity, the subscript I given to a filtering quantity to estimate the current state based on current and past observations, and the simple subscript I to a reanalysis quantity to estimate a past state from all available data. The goal is to obtain recursions for all these quantities. Straightforward computations show that mu sub I given I minus one equals M sub I M sub I minus one given I minus one, Sigma sub I given I minus one equals Q sub I plus M sub I Sigma sub I minus one given I minus one M sub I transposed, I equals one through N.

As expected, the forecasting distribution does not depend on new data.

Next, we use induction, applying Lemma twenty point one with X equals X of i given Y of one to i minus one and Y equals Y of i given y of one to i minus one. The data model has the property that Y of i is independent of Y of k for k less than i, so Y of i given y of one to i minus one equals Y of i. According to Lemma twenty point one,

mu sub i given i equals mu sub i given i minus one plus K sub i times y of i minus H sub i mu sub i given i minus one, equation twenty point nineteen,

where the Kalman gain matrix

K sub i is given by K sub i equals Sigma sub i given i minus one H sub i transposed times H sub i transposed Sigma sub i given i minus one H sub i plus R sub i inverse, equation twenty point twenty,

provided the matrix inverses all exist. The term y of i minus H sub i mu sub i given i minus one is called the innovation and is conceptually similar to an anomaly in climate science. Also from Lemma twenty point one, the filtering covariance matrix is

Sigma sub i given i equals I minus K sub i H sub i Sigma sub i given i minus one, equation twenty point twenty-one.


## Twenty point six. Numerical Example

The Kalman filter algorithm is obtained by alternating the forecasting and filtering step, just as in the general Algorithm twenty point one.

Algorithm twenty point three, Kalman filter. Given

(i) a prior distribution

X of zero follows a normal distribution with mean mu and covariance Sigma, (ii) the process model equation twenty point sixteen, and (iii) the linear data model twenty point seventeen,

the following algorithm gives the forecasting distributions f sub X of i given y of one to i minus one and filtering distributions f sub X of i given y of i. Step one. The forecasting and filtering distributions of X of one are given by X of one follows a normal distribution with mean mu sub one given zero and covariance Sigma sub one given zero, X of one given y of one follows a normal distribution with mean mu sub one given one and covariance Sigma sub one given one. Step two. Suppose i is in the set two, three, up to N and the filtering distribution at time step i minus one is known, X of i minus one given y of one to i minus one follows a normal distribution with mean mu sub i minus one given i minus one and covariance Sigma sub i minus one given i minus one. Then the forecasting and filtering distributions at time step i are given by

X of i given y of one to i minus one follows a normal distribution with mean mu sub i given i minus one and covariance Sigma sub i given i minus one, X of i given y of i follows a normal distribution with mean mu sub i given i and covariance Sigma sub i given i, where Mu sub i given i minus one, mu sub i given i, K sub i, Sigma sub i given i minus one, and Sigma sub i given i are computed from equations twenty point eighteen, twenty point nineteen, and twenty point twenty-one.

The data influence only the forecasting and filtering means but not the variance matrices which, in principle, can all be computed in advance. In practical applications, the problem of computing or estimating the covariance matrices becomes important. For those I for which no observations are available, the filtering distribution and the forecasting distribution agree.

The basic reanalysis Algorithm twenty point two can also be rewritten in terms of matrix operations for this situation.


## Twenty point six - Numerical Example

The following numerical example illustrates the results of Kalman filtering and reanalysis. The example uses the one-dimensional process model X subscript I equals alpha X subscript i minus one plus Xi subscript I for I equals one to thirty where alpha equals zero point eight and xi subscript I is distributed normally with mean zero and variance q squared where q equals zero point four. The value X subscript zero is drawn from a standard normal distribution. A typical sequence is plotted in black in Figure twenty point two. The data model is y subscript I equals b subscript I x subscript I plus zeta subscript I where zeta subscript I is distributed normally with mean zero and variance r squared where r equals zero point one. h subscript I equals zero point one for I from eleven to twenty, and equals one for I from one to ten and from twenty-one to thirty. The data model is set up so that for I from eleven to twenty, there is a period of "low observability." Figure twenty point two shows a single realization of the true process, the filtering estimates, and the reanalysis estimates. It is clear that these estimates are not the same. As expected, all estimates are much closer to the true values where b subscript I equals one. Figure twenty point three shows computed standard deviations, bold lines, for the forecasting estimates x subscript i for i minus one in black, filtering estimates x subscript i for i in blue, and reanalysis estimates x subscript i for N in red, together with their negative values. Forecasting standard deviations are always larger than


## Chapter twenty. Data Assimilation

Errors


## Twenty point seven. Extensions

filtering standard deviations which, in turn, are larger than reanalysis standard deviations. During the interval of low observability (I equals eleven to twenty), all these standard deviations are larger. Also plotted in the same figure, thin lines, are the forecasting errors x subscript I minus x sub i for i minus one in black, filtering errors x subscript I minus x sub i for i in blue, and reanalysis errors x subscript I minus x sub i for N in red for a single realization.


## Twenty point seven. Extensions

The Kalman filter and reanalysis algorithms have theoretical and practical limitations if the error distributions are not Gaussian or if the process model is nonlinear. In the latter case, even Gaussian errors typically become immediately non-Gaussian, and biases, systematic errors, appear. Another practical difficulty arises because in weather forecasting or climate science temporal and spatial features may lead to state variables with millions of components, with error covariance matrices with ten to the power of twelve or more entries.


## Twenty point seven point one - Extended Kalman Filter

Nonlinear process and data models are often handled by linearization. The resulting algorithm is known as the extended Kalman filter. In essence, it uses the nonlinear process model without noise terms to compute the forecasting estimate and uses linearization about the most recent filtering estimate to compute the forecasting covariance and the gain matrix. The filtering estimate and its covariance are then computed from these quantities more or less in the same way as in Algorithm twenty point three. This approach works well in engineering applications with a modest number of process variables but quickly becomes infeasible in high-dimensional situations. Variational methods for data assimilation that were mentioned earlier can avoid these difficulties but do not readily produce an assessment of errors.


## Twenty point seven point two - Ensemble Kalman Filter

The ensemble Kalman filter, introduced in the nineteen nineties, uses stochastic simulation techniques known as Monte Carlo methods. The archetypical use for a Monte Carlo approach is the computation of an expected value of a random variable X with density fx of x. Formally, the definition is the integral of F of x times fx of x with respect to x, where the integral is over the space in which X takes its values. Numerical computation of the integral is essentially impossible if the dimension of X exceeds ten or so. In a Monte Carlo approach, one draws m independent random samples x of one to m from the distribution of X and approximates the expected value,

F of x of i.

By the law of large numbers, the right-hand side converges almost surely to the correct expected value as m approaches zero, and the speed of convergence can be determined, it is always slow.

For a simple version of EnKf, we assume a nonlinear process model,

the equation twenty point twenty-three.

Where the M are functions from the range of the X of i to itself. All other assumptions are left unchanged-the model errors are Gaussian, there is a linear data model,


## Chapter twenty. Data Assimilation

and the background state is Gaussian, X of zero is distributed normally with mean u and variance sigma squared. Suppose we are given an estimate of the filtering mean at i minus one, an estimate of the filtering covariance matrix at this time step, and an estimate of the distribution of X of i minus one given y of one to i minus one. For the simulation, draw m independent samples x of i minus one given i minus one, j equals one to m, from this distribution, propagate them forward with the process, and add simulated model errors n distributed normally with mean zero and covariance Q that have the same distribution as the model errors at this time step. The result is an ensemble of simulated forecasts,

X of i given i minus one equals M of X of I given i minus one plus n, j equals one to m.

The forecasting estimate is now computed as the sample mean of this ensemble,

and the sample covariance matrix provides an estimate of the forecasting covariance matrix. Next, compute the gain matrix, just as in equation twenty point twenty, but with the estimated covariance,

and the sample covariance matrix provides an estimate Žili-1 of the forecasting covari- ance matrix. Next, compute the gain matrix, just as in (20.20) but with the estimated covariance,

R equals the product of S and the transpose of H times the inverse of the sum of the product of H, S, and the transpose of H and R.

To compute a filtering estimate, the ensemble of forecasts is adjusted using an innovation term and gain matrix as in Equation twenty point nineteen. There is only one observation y(i) available, but it turns out that using it unchanged for all innovations in the ensemble tends to underestimate the variability of the filtering distribution. Hence, the innovation term y(i)-Hi Mili-one in the ordinary Kalman filter is replaced by an innovation ensemble y(i) plus e minus H;x, where the perturbations e; are simulated observation errors with the same distribution as the errors in the data model. One can therefore compute an ensemble of simulated filtering states,

Ex minus one plus R; y(i) plus e; minus H[-].

This ensemble is used to produce estimates &j ; of the filtering mean and 2 ;; of the filtering covariance matrix. One then uses N( *¡ , [i) as an estimate of the filtering distribution at time step i, and the algorithm has completed a step. There is also a reanalysis version of this method.

If the process model is actually linear, such that Equation twenty point twenty-three reduces to Equation twenty point sixteen, then the ensemble Kalman forecasting and filtering estimates converge in the limit of large ensemble size to those of the ordinary Kalman filter algorithm. However, if the M; are nonlinear, then the forecasting and filtering distributions become non-Gaussian, and there will be biases from the ensemble approach that do not disappear with large ensemble size. These biases must be assessed or possibly corrected separately.


## Twenty point eight. Data Assimilation for the Lorenz System

If the space of process variables is high-dimensional one zero to the power of six or one zero to the power of eight is not uncommon, the ensemble approach successfully avoids the problem of high-dimensional integration and the manipulation of huge covariance matrices. However, typically the ensemble size is much smaller, perhaps m equals zero one zero to the power of two. Then the sample covariance matrices have rank at most m and cannot possibly give all covariances correctly. On the other hand, in such situations the process vector X(i) may describe physical quantities at different locations across a region or around the globe. Then one often multiplies sum from i to i minus one or sum from i to i elementwise with a "cut-off" matrix C whose entries are small far from the diagonal (for component pairs that have little to do with each other). This trick eliminates spurious large correlations at distant locations and at the same time tends to restore full rank to the estimated covariance matrices. Care must be taken to avoid destroying teleconnections.

The EnKf is now widely used. Many versions have been developed, and the literature has grown quite large.


## Twenty point eight. Data Assimilation for the Lorenz System

To illustrate the EnKf technique, we apply the algorithm to the Lorenz model seven point one with the fixed parameter values sigma equals ten, beta equals eight divided by three, and rho equals twenty-eight. The attractor is shown in Figure seven point two.

Let X equals (x, y, z): t maps to x(t) equals (x(t), y(t), z(t)) be the solution of the Lorenz system (seven point one) which satisfies the initial data x(0) equals (x(0), y(0), z(0)) in R cubed. The process model associated with the Lorenz equations is the map

Script M maps set of real numbers cubed to set of real numbers cubed defined by script M of X sub zero equals X of one in set of real numbers cubed, X sub zero in set of real numbers cubed.

There is no closed formula for script M, so script M must be computed numerically by solving the system of differential equations for each

X sub zero Figure twenty point four shows the x-component of a trajectory for zero less than or equal to T less than or equal to six for initial data x sub zero equals negative seven point three, y sub zero equals negative eleven point five, z sub zero equals seventeen point eight. This trajectory switches from one "sheet" of the attractor to the other near T equals two. Also shown in Figure twenty point four are the x-components of ten trajectories from a solution ensemble with initial data X sub zero prime equals X sub zero plus Xi sub one, Xi sub two, Xi sub three, where the Xi sub i are normal random variables, as well as the ensemble mean computed by averaging one thousand trajectories of this ensemble. For T greater than one point five or so, the ensemble mean is seen to differ dramatically from the true solution. The specific reason in this case is that trajectories from the ensemble switch from one leaf of the attractor to the other at times that can be very different from T equals two. Essentially, if the initial data are known only up to random errors that have standard normal distributions, then the true trajectory becomes unpredictable for T greater than one point five or so. Averaging over many ensemble trajectories does not eliminate this bias. This situation is typical for nonlinear systems of differential equations; for linear systems, the ensemble mean always equals the true trajectory.

Figure twenty point five again shows the x-component of the true trajectory, together with the corresponding results of the EnKf, for an ensemble of size fifty. The data model is given by Equation twenty point seventeen, with H equals matrix with rows one and one and zero, zero and one and one. Therefore, only a two-dimensional projection of the true trajectory, corrupted by random noise, is observed at each time. The error terms zeta sub i are standard normal. Each assimilated trajectory starts at a filtering state at T equals i, red circle, and ends at a forecasting state at T equals i plus one, green circle. Evidently, the assimilation process is only partially successful in approximating the correct trajectory. For example, on the intervals one point five less than T less than two and four point five less than T less than five, the assimilated trajectories are not even qualitatively correct. Nevertheless, it is remarkable that a significant portion of the true trajectory is recreated correctly over the entire interval of interest.


## Chapter twenty. Data Assimilation

Twenty point nine. Concluding Remarks


## Twenty point nine. Concluding Remarks

Data assimilation has been very important for weather prediction, where it has extended both the range and reliability of forecasts. In the best-case scenario, there is a correct dynamical model with sufficiently high resolution and a well-designed observational network that can provide accurate data. In the next-best-case scenario, there may be a somewhat deficient dynamical model, but the observational network is still good enough to provide adequate data. Then it is still possible to obtain estimates in agreement with nature, as long as dynamical model errors are recognized and incorporated adequately.

In climate science, data assimilation has been used since the late nineteen eighties. It is having an increasingly significant impact, since it allows improved and faster estimation of both internal and external parameters. Parameter estimation is particularly promising in the biogeochemistry of the climate system, where it is often difficult to measure rates directly in situ. Realistic dynamical models and feasible measurements of quantities such as concentration fields of plankton, in combination with advanced data assimilation techniques, can lead to surprisingly realistic estimates of these rates.

Data assimilation techniques have been applied to create reliable uniform background data for the past, reanalysis, and to obtain information about unobservable quantities such as ocean upwelling and chemical reaction rates in the ocean. A typical example is described, where an EnKf approach is used to reconstruct the ocean climate for the period nineteen fifty-eight to two thousand one.

Interestingly, there are specific problems with heterogeneous data sources associated with all reanalysis exercises for ocean circulation for the twentieth century. Since about nineteen eighty, satellites with circumpolar orbits have provided reliable records of planet-wide uniformly distributed ocean measurements. But prior to about nineteen eighty, observations came mainly from shipboard observations that were concentrated along major shipping routes. There are also other more subtle trends in the data collection efforts that are known to introduce spurious trends during data assimilation. For example, the typical height at which shipboard anemometers are mounted has increased since the middle of the last century, leading to biased results for wind strengths and patterns. In the past, when data assimilation was used mainly for weather prediction, such slow trends did not matter.

Ridgwell et al. describe a similar project for biogeochemistry data. Here, an EnKf is employed in an iterative fashion to obtain steady-state information about geochemical parameters such as uptake rates and concentrations of phosphate and calcium carbonate in the ocean at preindustrial times.

The EnKf is known to run into problems when the underlying process model is highly nonlinear and has many unstable equilibria. Other methods have been proposed for such situations. For example, Apte, Jones, and Stuart develop a Bayesian approach to address data assimilation questions coming from drifting buoys, which are known to have trajectories that are very sensitive to changes in the initial data.


## Twenty point ten. Exercises

One. Consider a physical process in which real-valued state variables X sub i comma i equals one comma two comma and so on, are generated according to the rule X sub i plus one equals F of X sub i, where F is a given real-valued function. The states are observed according to the data model Y sub i equals X sub i plus epsilon sub i, where the epsilon sub i are independent random variables with an N zero comma sigma squared-distribution.

(i) Assume that observations Y one, Y two, and so on, up to Y sub N are available and that you want to estimate X one. Describe in general terms how a cost function should be set up whose minimum is expected to give an estimate for X one.

Sigma circ equals Q plus M of open parenthesis Sigma circ minus Sigma circ H transpose of open parenthesis H Sigma circ H transpose plus R close parenthesis inverse H Sigma circ close parenthesis M transpose,


## Chapter twenty. Data Assimilation

(ii) Consider the special case F of open parenthesis X close parenthesis equals four X open parenthesis one minus X close parenthesis. Begin with the case N equals three, sigma equals zero point one, X one equals zero point two. Construct this cost function for several realizations of the Y sub i and plot it, using a computer. Is the minimum of the cost function where you expect it to be?

(iii) Repeat part (ii) with a larger sigma, for example sigma equals zero point five. Repeat with the previous sigma and a larger N, for example N equals six. Describe your observations. Does it help to have more observations available?

The cost function may have multiple local minima, which can lead to serious numerical difficulties.

Two. Consider the process model equation twenty point one together with the data model equation twenty point two. Derive the joint distribution of Y sub two, Y sub three as a function of the unknown parameter X sub two and use it to obtain the maximum likelihood estimate X hat sub two. Interpret your result in the case where tau is much less than one. Three. Consider again the process model equation twenty point one together with the data model equation twenty point two. Derive the joint distribution of Y sub two, Y sub three as a function of the unknown parameter X sub three and use it to obtain the maximum likelihood estimate X hat sub three. Interpret your result in the case where tau is much less than one. One. Use

X sub two equals alpha inverse of open parenthesis X sub three minus xi sub two close parenthesis. Four. Consider the process model equation twenty point one and assume that

X sub one follows N of omega sub zero comma sigma squared. (i) Compute the covariance matrix Sigma of the random vector

X equals open parenthesis X sub one, and so on, up to X sub four close parenthesis transpose. (ii) Compute the gain matrix K from the definition equation twenty point ten.

(iii) Show that var of open parenthesis X sub one given y close parenthesis equals the fraction sigma squared of tau to the fourth power plus open parenthesis alpha squared plus two close parenthesis tau squared plus one over tau to the fourth power plus open parenthesis alpha squared plus one close parenthesis sigma squared alpha squared plus alpha squared plus two close parenthesis tau squared plus alpha squared sigma squared plus one and var of open parenthesis X sub three given y close parenthesis equals the fraction tau squared alpha squared sigma squared plus open parenthesis sigma squared alpha to the fourth power plus alpha squared plus one close parenthesis tau squared plus one over tau to the fourth power plus open parenthesis alpha squared plus one close parenthesis sigma squared alpha squared plus alpha squared plus two close parenthesis tau squared plus alpha squared sigma squared plus one. Five. Consider the general process model X of open parenthesis i close parenthesis equals M sub i X of open parenthesis i minus one close parenthesis plus b of open parenthesis i close parenthesis plus xi sub i, i equals one to N, where X of open parenthesis i close parenthesis, b of open parenthesis i close parenthesis, xi sub i belong to the reals to the power of n and M sub i are n by n matrices. Define X bar of open parenthesis i close parenthesis by

Bar X of zero equals zero; bar X of I equals M sub i bar X of i minus one plus B of i, I equals one to N.

and set \widetilde X of i equals X of i minus bar X of i. Show that the \widetilde X of i satisfy the recursion.

Six. Use the MATLAB code for the Lorenz equations given in Section C point one to explore the behavior of the ensemble mean of the Lorenz equations for other initial data X sub zero. Can you find initial data such that the ensemble mean stays close to the correct solution for an interval of length

T equals five? Seven. Consider the linear process model together with the data model, and assume that all matrices are independent of i, so M sub i equals M, H sub i equals H, Q sub i equals Q, and R sub i equals R for all i. Assume that the forecasting covariates matrices Sigma sub i given i minus one converge to a limit Sigma sub c. Derive the equation


## Twenty point ten. Exercises

and derive similar equations for the limits of the matrices Zili and K. The above equation is known as a matrix Riccati equation. It reduces to an ordinary quadratic equation if the dimension of the state space is one.