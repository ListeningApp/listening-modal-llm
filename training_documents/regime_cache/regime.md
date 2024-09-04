## EXTENDING THE REGIME OF LINEAR RESPONSE WITH SYNTHETIC FORCINGS

One. Introduction. Statistical physics provides a formulation to study the macroscopic properties of interacting particle systems based on the behavior of their microscopic constituents. Its numerical realization, known as "molecular dynamics", has played an essential role in science for the past seventy years. One of the major aims of molecular dynamics is to compute macroscopic quantities or thermodynamic properties, typically given by averages of basic dynamical variables, which allows to obtain quantitative information on a system. Molecular dynamics can be thought of as a numerical microscope, as it bridges the gap between theoretical and experimental work, playing an important part across (essentially) all of science.

One particular interest in molecular dynamics is the computation of transport coefficients, such as the mobility, thermal conductivity and shear viscosity. At the macroscopic level, transport coefficients relate an external forcing acting on the system (i.e. a perturbation on the equilibrium dynamics) to an average response expressed through some steady-state flux (of energy, momentum, charged particles etc). From a mathematical perspective, this can be done by introducing a reference dynamics which models systems at equilibrium, and perturbing it by some external forcing of magnitude N in the set of real numbers mimicking the driving exerted on the system to create some flux. This corresponds to the so-called nonequilibrium molecular dynamics.

To realize this in molecular dynamics simulations, we consider general perturbed dynamics of the form dX equals (b of X plus nF of X) dt plus sigma of X dW sub t,

where F is the external forcing and n in the set of real numbers its magnitude, and W sub t a standard Brownian motion. In general, it is observed that the response E of n of R of the system, given by the steady-state average of a physical observable R of interest which has average zero for unperturbed dynamics (n equal zero), is proportional to the magnitude of the forcing for small values of the forcing. This corresponds to the linear response regime; see Figure one. When this is the case, the linear response p sub one is computed as

P sub one equals limit as n approaches zero of E of n of R divided by E of zero of R.

(One point one)

By definition, transport coefficients are the proportionality constants p sub one relating the response E of n of R to the forcing for n small. One typical example is the case where the force F is constant and the configuration space is a torus. Such a forcing is considered to compute the mobility of particles in the system, which we discuss in more detail in Section Two point two point three. Another example is the case where F has components in one direction only, whose magnitude depends on the position in another direction. Such forcings can be used to estimate the shear viscosity through the so-called sinusoidal transverse force method.

In practice, steady-state averages involved in the linear response are computed as ergodic averages over a very long trajectory of the system, obtained as a realization of the stochastic differential equation (SDE) (Two point four). Although there are several such ways of computing these steady-state averages, it is typically done in one of two ways: either based on (i) equilibrium techniques based on Green-Kubo formulae, which are integrated autocorrelation functions; or (ii) nonequilibrium steady-state methods where the limit (One point one) is numerically estimated. Both numerical methods have advantages and drawbacks, and are constantly undergoing algorithmic advances. In this work, however, we focus exclusively on the nonequilibrium approach.

In the NEMD approach, a standard estimator to compute the linear response (One point one) is

(One point two) I of n,t equals integral from zero to t of R of X ds,

where the fixed value of n not equal to zero should be small enough in absolute value in order for the nonlinear part of the response to be negligible. Although there are various sources of error associated with the estimator (One point two), as made precise in Section Two point three, the variance associated with (One point two) is the main issue. In particular, in the context of computing transport coefficients, the large signal-to-noise ratio leads to a very large statistical error, as we are averaging very small linear responses. The estimator (One point two), for instance, has asymptotic variance of order big O of t to the negative one times n to the negative two, much larger than the usual asymptotic variance of order big O of t to the negative one associated with its equilibrium averages counterpart, as the linear regime is only valid for n less than one. This motivates the interest of variance reduction techniques, which are used to decrease the statistical error in the estimated averages. Examples of standard variance reduction techniques for Monte Carlo simulations are antithetic variables, stratification, control variate methods and importance sampling.

One of the main challenges with computing nonequilibrium steady-state averages, however, is that traditional equilibrium variance reduction techniques cannot be used the same way. Although many practitioners of molecular dynamics realize that the computation of transport coefficients is a difficult numerical issue, there were only a handful


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

of attempts to develop dedicated variance reduction techniques. Many practitioners still use direct, brute force numerical methods based on a time integration of the dynamics.

In order to reduce the statistical error of order one divided by (n squared t), one idea is to extend the regime of linear response, which consequently allows to use larger values of n. One approach for doing so is to use synthetic forcings. Such forcings, as presented in this work, were introduced by Evans and Morriss (synthetic fields, in their terminology) with the purpose to produce a mechanical analog of a thermal transport process. This notion was originally used by Gillan and Dixon, then abstracted and extended by Evans and Morriss. The name synthetic is used to denote that the external fields under consideration do not exist in nature.

The key idea behind synthetic forcings is that there are infinitely many forcings which lead to the same transport coefficient. This flexibility should be used to develop better numerical methods for the computation of transport coefficients. In theory, one can add an extra forcing to the physical perturbation of the system, as long as this extra forcing preserves the invariant measure of the reference system, which in turn preserves the linear response. We call the resulting perturbation a synthetic forcing, as it has no physical representation; it is a mathematical device used to simplify the problem at hand.

The aim is to find synthetic perturbations allowing to reduce the nonlinear part of the response as much as possible (see Figure one) in order to consider larger values of n. In this article, we present a mathematical framework for choosing and quantifying the quality of synthetic forcings, in the context of linear response theory, and discuss various possible choices for them. We illustrate the analysis with numerical results in low dimensional systems.

This work is organized as follows. We present in Section two a review of linear response theory and associated computational techniques, and state technical results which make precise some error estimates, in particular bounds on the asymptotic variance of time averages such as equation one point two. We then introduce the notion of synthetic forcings in Section three, where we also give examples and discuss them in more detail. We next demonstrate the possibly dramatic benefits in terms of statistical error with some numerical results in low dimensions in Section four, namely one and two-dimensional overdamped Langevin dynamics, and one-dimensional Langevin dynamics. We finally discuss in Section five the extensions and perspectives of this approach.

Two. Linear response and associated computational techniques. In this section, we review linear response theory and the computational techniques allowing to compute transport coefficients. The framework we consider is that of stochastic dynamics, ergodic for the Boltzmann-Gibbs measure, which are perturbed by external forcings.

We start in Section two point one by setting up the framework for general time-homogeneous stochastic differential equations, and the specific dynamics we consider, namely nonequilibrium overdamped Langevin and Langevin dynamics. We then review in Section two point two linear response theory, the definition of transport coefficients and discuss the associated standard numerical techniques to estimate these coefficients. We finally present the numerical analysis of nonequilibrium molecular dynamics in Section two point three.

Two point one. Reference dynamics and perturbation. We start by describing in Section two point one point one the general setting for linear response theory for a general stochastic differential equation. We introduce in particular some assumptions on the dynamics which will be used in the analysis throughout this paper. We next describe the dynamics and their nonequilibrium perturbations for overdamped Langevin and Langevin dynamics in Sections two point one point two and two point one point three, respectively.


## Two point one point one. General setting.

Reference dynamics. Consider a general time-homogeneous stochastic differential equation defined on the state-space X, where X is typically the full space R to the power of n or a bounded domain with periodic boundary conditions T to the power of n, with T equals R over Z the one-dimensional torus:

equation two point one d X t equals b of X t d t plus sigma of X t d W t,

for a given initial condition x naught in X, a standard Brownian motion W t in R to the power of m, and where b maps X to R to the power of n and sigma maps X to R to the power of n by m are assumed to be such that there exists a unique solution to equation two point one. A simple setting is to assume that b and sigma are C infinity, hence locally Lipschitz, which is used to prove existence and uniqueness of the solution. The stochastic differential equation two point one is associated with the following infinitesimal generator equation two point two L naught equals b transpose V plus one half sigma sigma transpose V squared,

where : denotes the Frobenius inner product, and V squared is the Hessian operator. More explicitly, for some given C infinity test function psi maps R d to R, the operator L naught acts as

L naught psi equals summation i equals one to d b i partial derivative psi partial derivative x i plus one half summation i equals one to d summation j equals one to d summation k equals one to m sigma i k sigma j k second partial derivative psi partial derivative x i partial derivative x j.

We assume that the dynamics equation two point one has a unique invariant probability measure with a density with respect to the Lebesgue measure denoted by pi of x. This density satisfies


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

the stationary Fokker-Planck equation equation two point three L naught pi equals zero,

where L naught denotes the L two-adjoint of the operator L naught, acting as

L naught star pi equals negative divergence of b pi plus one half summation i equals one to d summation j equals one to d second partial derivative pi sigma sigma transpose i j.

Perturbation of the reference dynamics. We next consider a perturbation of the reference dynamics equation two point one, obtained by adding to the drift field b some smooth nongradient forcing F maps X to R to the power of n of magnitude eta in R:

equation two point four d x eta equals b of X eta plus eta F of X eta d t plus sigma of X eta d W t.

The generator of equation two point four is denoted by L eta equals L naught plus eta L phys, where L phys is the generator associated with the physical perturbation:

L phys equals F transpose V.


## We assume that b, sigma and F are such that the following assumption holds.

ASSUMPTION ONE Uniqueness of the invariant measure. The dynamics equation two point four admits a unique invariant probability measure for any eta in R, with a smooth density pi eta with respect to the Lebesgue measure. Moreover, trajectorial ergodicity holds: for any observable psi in L one of P eta, and any initial condition X eta,

expectation eta of psi equals integral psi of x pi eta of x d x equals limit as T approaches infinity of one over T integral zero to T psi of X eta t d t almost surely.

Note that pi eta solves the Fokker-Planck equation

Note that Un solves the Fokker-Planck equation

L naught plus eta L phys pi eta equals zero.

Sufficient conditions for Assumption One to hold are discussed after Assumption Two below. Although pi eta can be shown to uniquely exist, its analytical expression is generally not known. Note that in the case eta equals zero, the dynamics equation two point four reduces to the reference dynamics equation two point one.

We need to make precise some estimates on the evolution semigroup associated with equation two point four for the analysis presented in Section two point three. We consider to this end weighted spaces of bounded functions. To define them, we first introduce a family of Lyapunov functions denoted by K n sub eta in natural numbers, with K n maps X to open interval one to positive infinity such that

K sub n less than or equal to K sub n plus one.

The associated weighted B infinity spaces are

B infinity equals the set of measurable psi such that the weighted norm psi weighted B infinity equals the supremum of K n of x times psi of x is finite,

and m depending on the order of derivation. Denoting by partial derivative to the power of k equals partial derivative sub x sub one to the power of k sub one times to partial derivative sub x sub d to the power of k sub d.

<LATEX>k = (k_{1}, \ldots, k_{d}) in N^{d}</LATEX>, <LATEX>\mathscr{S} = \{ \varphi \in C^{∞}(\mathcal{X}) | for all k in N^{d}, \exists n in N, \partial^{k} \varphi \in B_{n}^{∞} \}</LATEX>. When <LATEX>\mathcal{X}</LATEX> is bounded, it is possible to choose <LATEX>\mathcal{K}_{n} = 1</LATEX> for all <LATEX>n \geqslant 0</LATEX>, in which case <LATEX>\mathscr{S} = C^{∞}(\mathcal{X})</LATEX>. For unbounded spaces, a typical choice is <LATEX>\mathcal{K}_{n} = 1 + |x|^{n}</LATEX>, in which case the functions <LATEX>\varphi \in \mathscr{S}</LATEX> and their derivatives grow at most polynomially. We also consider the subspace <LATEX>\mathscr{S}_{0} = \Pi_{0} \mathscr{S}</LATEX> of functions with average zero with respect to <LATEX>\psi_{0}</LATEX>, where <LATEX>\Pi_{n}</LATEX> for <LATEX>\eta \in \mathbb{R}</LATEX> denotes the projection operator

<LATEX>\Pi_{\eta} \varphi = \varphi - \int_{\mathcal{X}} \varphi \psi_{\eta}</LATEX>. We denote by <LATEX>\|\cdot\|_{\mathcal{B}(E)}</LATEX> the operator norm on the Banach space <LATEX>\mathcal{B}(E)</LATEX> of bounded linear operators on a Banach space <LATEX>E</LATEX>, defined by

<LATEX>\| \mathcal{A} \|_{\mathcal{B}(E)} = \sup_{g \in E \setminus \{ 0 \}} \frac{\| \mathcal{A} g \|_{E}}{\| g \|_{E}}</LATEX>. Before we state the next assumption, we let <LATEX>\mathcal{A}^{*}</LATEX> denote the adjoint of <LATEX>\mathcal{A}</LATEX> on the space <LATEX>L^{2}(\psi_{0})</LATEX>. More explicitly, for any test functions <LATEX>\varphi</LATEX>, phi in <LATEX>C^{∞}</LATEX> with compact support,

<LATEX>\int_{\mathcal{X}} (\mathcal{A} \varphi) \phi \psi_{0} = \int_{\mathcal{X}} \varphi (\mathcal{A}^{*} \phi) \psi_{0}</LATEX>. The action of these operators can be found via integration by parts. In particular, for <LATEX>\psi_{0}(x)</LATEX> a probability density proportional to <LATEX>\mathrm{e}^{- \beta U(x)}</LATEX>, an integration by parts shows that <LATEX>\partial_{x_{i}}^{*} = - \partial_{x_{i}} + \beta \partial_{x_{i}} U</LATEX>. In addition, note that <LATEX>\nabla_{x}^{*} \nabla_{x} = \sum_{i=1}^{d} \partial_{x_{i}}^{*} \partial_{x_{i}}</LATEX> .

Note that the Fokker-Planck equation two point three, written in terms of the <LATEX>L^{2}</LATEX> adjoint, can also be written with the <LATEX>L^{2}(\psi_{0})</LATEX> as <LATEX>\mathcal{L}_{0}^{*} 1 = 0</LATEX>. We make the following assumption on the Lyapunov functions.

Assumption two (Lyapunov estimates). The space <LATEX>\mathscr{S}</LATEX> is dense in <LATEX>L^{2}(\psi_{\eta})</LATEX> for any <LATEX>\eta \in \mathbb{R}</LATEX>. For any <LATEX>n \in \mathbb{N}</LATEX>, the <LATEX>L^{2}(\psi_{\eta})</LATEX> norms of the Lyapunov functions are uniformly bounded on compact sets <LATEX>\eta</LATEX>: for any <LATEX>\eta_{*} > 0</LATEX>, there exists a constant <LATEX>C_{n,n_{*}} < +∞</LATEX> such that equation two point five

For all eta less than or equal to eta star, the norm of script K sub n with respect to L squared of psi sub eta is less than or equal to C sub n eta star. Moreover, negative script L sub eta is invertible on Pi sub eta B sub n to the power of infinity, and the inverse generator is bounded uniformly on compact sets of eta: (two point six)

For all eta less than or equal to eta star, the norm of negative script L sub eta to the negative one with respect to script B of Pi sub eta B sub n to the power of infinity is less than or equal to K sub n eta star. Additionally,

(two point seven)

For all eta less than or equal to eta star, for all n greater than or equal to one, the supremum over t in the set of positive real numbers of the norm of e to the power of t script L sub eta script K sub n with respect to B sub n to the power of infinity is less than or equal to M sub n eta star less than positive infinity, We finally assume that for any n, n prime in the set of natural numbers, there exists m in the set of natural numbers such that script K sub n script K sub n prime in B sub m to the power of infinity. The estimates (two point five) through (two point seven) are usually obtained from Lyapunov conditions of the form

(two point eight)


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

for some a sub n n greater than zero and b sub n eta in the set of real numbers. After integration against psi sub eta, and making use of the invariance of psi sub eta by the dynamics,

Zero equals the integral over the set X script L sub eta script K sub n psi sub eta less than or equal to negative a sub n eta the integral over the set X script K sub n psi sub eta plus b sub n eta, so that

One less than or equal to the integral over the set X script K sub n psi sub eta less than or equal to the fraction b sub n eta divided by a sub n eta. The condition (two point five) then follows from the last statement of Assumption two since, for any n greater than or equal to one, there exists C sub n greater than zero and m greater than or equal to one such that one less than or equal to script K sub n squared less than or equal to C sub n script K sub m. Condition (two point eight) also implies the existence of an invariant probability measure for any eta in the set of real numbers when a minorization condition holds. The minorization condition typically follows from a controllability argument and hypoellipticity conditions, see for instance. As for Assumption one, trajectorial ergodicity holds when the generator script L sub eta is either elliptic or hypoelliptic, and there exists an invariant probability measure with positive density with respect to the Lebesgue measure.

We need an assumption in our analysis on the generator script L sub zero of the reference dynamics, which will be useful when stating some technical results later on.

ASSUMPTION THREE (Stability of smooth functions by inverse operators). The space script S is stable by the generator script L sub zero, and script L sub zero and script L sub zero star are invertible on script S sub zero. This means that, for any phi in script S sub zero, there exists a unique solution Psi in script S sub zero to the Poisson equation

Negative script L sub zero Psi equals phi. The generator of the perturbation should also satisfy the next assumption.

ASSUMPTION four (Stability of smooth functions by the perturbation operator). The generator Script L tilde sub phys of the perturbation is such that Script S is stable by Script L tilde sub phys, and

Script L tilde sub phys star Script S subset Script S sub zero. Assumption four is easily seen to be satisfied for perturbations Script L tilde sub phys of the form F transposed nabla when F has components in Script S, which is assumed here and for the remainder of this work. A simple computation based on integrations by parts shows that Script L tilde sub phys star Script S subset Script S sub zero when Script L tilde sub phys one equals zero. Indeed, for varphi in Script S, using the definition of the

L squared left paren psi sub zero right paren, (two point nine)

integral from Script X Script L tilde sub phys star varphi psi sub zero equals integral from Script X varphi left paren Script L tilde sub phys one right paren psi sub zero equals zero. One function of particular interest in the range of Script L tilde sub phys star is the conjugate response function

(two point ten)

S equals Script L tilde sub phys star one, which we introduce here as it will be useful later. Note that the expression for S comes from the generator Script L tilde sub phys of the perturbation, and not the observable R. Let us emphasize that beyond the case of physical forcings F transposed nabla, Assumption four will be needed for more general operators in Section three.

Assumptions one through four are natural for overdamped Langevin and Langevin dynamics, which we present in the next two sections.

Two point one point two. Overdamped Langevin dynamics. One typical dynamics used in molecular dynamics is overdamped Langevin dynamics, which evolves only the positions Q of the system.

Reference dynamics. Mathematically, the overdamped Langevin dynamics corresponds to the following S D E with nondegenerate noise:

beta squared d W t,

(two point eleven) d Q t equals negative gradient V left paren Q t right paren d t plus V

where beta is greater than zero is proportional to the inverse temperature, and V is a smooth potential. The generator associated with (two point eleven) is given by

(two point twelve) L sub zero equals negative gradient transposed V plus negative A,

with L squared X-adjoint

C h equals divergence V V plus B A.

The dynamics (two point eleven) admits the Gibbs measure with density forty four minus two zero negative BV of a, two Z equals one x by x e to the power of negative BV of I d Q less than positive infinity as its unique invariant probability measure. It can indeed be checked that L sub zero V equals zero, so that yo is a stationary solution to the Fokker-Planck equation. Here and in the remainder of this work, we assume that e to the power of negative B V is an element of L one X. Note that the generator (two point twelve) is self-adjoint on the Hilbert space L squared zero, as L sub zero equals negative B to the power of negative one V star V.


## Nonequilibrium perturbation. The perturbed overdamped Langevin dynamics corresponding to (two point four) reads

(two point thirteen) d Q f equals negative gradient V of Q plus n F of Q d t plus V beta

It has generator C n equals L sub zero plus n e phys, where C phys equals F transposed V. Recall that F is assumed to be nongradient, so that in general there is no explicit expression for the invariant probability measure of (two point thirteen) when such a measure exists.

Remark two point one. One of the only cases where a closed form for y is known is the one-dimensional case for overdamped Langevin dynamics, where the associated Fokker-Planck equation is directly solvable, as discussed for instance in, which generalizes the computations of Section two point five.

Conditions for assumptions to be satisfied. We now discuss the conditions under which Assumptions one through four are satisfied for the perturbed overdamped Langevin dynamics (two point thirteen), which correspond to standard results in the literature.

If the space X is compact, then it is trivial to satisfy the Lyapunov condition (two point eight) by choosing K n equals one. In the case of unbounded spaces, a typical choice is K n equals one plus absolute value of Q, with the condition that there exist A greater than zero and B an element of R such that

(two point fourteen) Q transposed V V of q is greater than or equal to A absolute value of q squared minus B.

Condition (two point fourteen) is satisfied for potentials V of Q that behave as absolute value of q to the power of k for k greater than or equal to two at infinity. This ensures that the dynamics returns to some compact region around the origin.


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

Assumption one can be shown to hold using Lyapunov techniques and a minorization condition. It can thus be shown that the dynamics (two point thirteen) has a unique invariant probability measure with positive density with respect to the Lebesgue measure, and therefore that trajectorial ergodicity holds.

Assumptions two and three hold under some conditions on the potential V, which include (two point fourteen); see for a precise discussion.

. Lastly, Assumption Four is trivially satisfied, as widetilde cal L sub p h y s equals F superscript T nabla sub Q leaves scr S stable when F is in scr S, and widetilde cal L sub p h y s superscript star scr S subset scr S sub zero in view of.

Two point one point three. Langevin dynamics. Another dynamics of interest used in molecular dynamics is Langevin dynamics, which can be seen as a Hamiltonian dynamics perturbed by an Ornstein-Uhlenbeck process on the momenta. Mathematically, it corresponds to an SDE with degenerate noise, as the noise acts on the momenta only (i.e. the diffusion matrix does not have full rank).

Reference dynamics. At equilibrium, Langevin dynamics evolves positions Q and momenta P according to the SDE.

left backslash left brace back slash begin right curly brace right curly brace d Q sub t equals M inverse P sub t d t comma amp backslash backslash d P sub t equals negative nabla V left parenthesis Q sub t right parenthesis d t minus Gamma M inverse P sub t d t plus square root of fraction two Gamma over Beta d W sub t comma amp backslash backslash right brace right period (two point fifteen)

where Gamma greater than zero is the friction coefficient and M is in real superscript d times d is a positive definite matrix, called the mass matrix. The state-space cal X is either torus superscript d times real superscript d or the full space.

real superscript d times real superscript d. The infinitesimal generator associated with (two point fifteen) is the following degenerate elliptic operator.

cal L sub zero equals cal L sub h a m plus Gamma cal L sub F D, where cal L sub h a m is the generator of the Hamiltonian part of the dynamics, and cal L sub F D is the generator of the fluctuation-dissipation part, i.e. the Gaussian process on the momenta, also known as the Ornstein-Uhlenbeck process.

(two point sixteen)

cal L sub h a m equals P superscript T M inverse nabla sub Q minus nabla V superscript T nabla sub P, quad cal L sub F D equals negative P superscript T M inverse nabla sub P plus Beta inverse Delta sub P. The L squared left parenthesis cal X right parenthesis (X)-adjoint of cal L sub zero acts.

cal L sub zero star psi equals negative cal L sub h a m psi plus Gamma div sub P left parenthesis M inverse P psi plus Beta inverse nabla sub P psi right parenthesis. A simple computation shows that the dynamics (two point fifteen) admits the Boltzmann-Gibbs distribution as an invariant probability measure, which is in fact unique. The density of this measure satisfies the stationary Fokker-Planck equation cal L sub zero star psi sub zero equals zero, where.

psi sub zero left parenthesis Q right parenthesis equals fraction one over Z exp superscript negative Beta H left parenthesis Q comma P right parenthesis, quad Z equals integral sub cal X exp superscript negative Beta H left parenthesis Q comma P right parenthesis d Q d P. Overdamped Langevin dynamics can be obtained from Langevin dynamics in two limiting cases: in the high friction limit Gamma tends to positive infinity, upon rescaling time as Gamma t or in the small mass limit m tends to zero.

Nonequilibrium perturbation. We also consider the case where the dynamics (two point fifteen) is perturbed by a nongradient force F colon cal X right arrow real superscript d of magnitude eta is in real numbers. The resulting nonequilibrium Langevin dynamics reads.

integral d Q sub t superscript eta equals M inverse P sub t superscript eta d t left backslash left brace back slash begin right curly brace right curly brace d Q sub t superscript eta equals M inverse P sub t superscript eta d t comma amp backslash backslash d P sub t superscript eta equals left parenthesis negative nabla V left parenthesis Q sub t superscript eta right parenthesis plus eta F left parenthesis Q sub t superscript eta right parenthesis right parenthesis d t minus Gamma M inverse P sub t superscript eta d t plus square root of fraction two Gamma over Beta d W sub t comma amp backslash backslash right brace right period (two point eighteen)

It has generator cal L sub eta equals cal L sub zero plus eta widetilde cal L sub p h y s with tilde script L sub P H Y S equals F transpose nabla sub P. Conditions for assumptions to be satisfied. We now discuss the conditions under which Assumptions one through four are satisfied for the perturbed Langevin dynamics, which correspond here as well to standard results in the literature.

For Langevin dynamics, the momentum space is always unbounded, so the choice for the Lyapunov function to satisfy the condition depends on the position space. For compact position spaces, it suffices to choose script K sub n left parenthesis P right parenthesis equals one plus absolute value of P superscript n. For unbounded position spaces, there are various possible choices. One possibility is to consider script K sub n left parenthesis Q, P right parenthesis equals left parenthesis one plus H left parenthesis Q, P right parenthesis minus V sub minus plus the fraction of gamma over two P transpose M inverse Q plus the fraction of gamma squared over four Q transpose M inverse Q right parenthesis superscript n, under the following conditions: the potential energy function V is bounded from below by V sub minus greater than negative infinity, and there exist A, B greater than zero and C in the reals such that

Q transpose M inverse nabla V left parenthesis Q right parenthesis is greater than or equal to A V left parenthesis Q right parenthesis plus B Q transpose M inverse Q plus C. The existence of an invariant probability measure in Assumption one can be shown using Lyapunov techniques when a minorization condition holds. It can be shown that the dynamics has a unique invariant measure, as psi sub zero has positive density with respect to the Lebesgue measure. Thus, since the generator script L sub eta is hypoelliptic, it follows that trajectorial ergodicity holds.

Assumption two holds as discussed.

Assumption three holds under some conditions on the potential V, which include see for a precise discussion.

Lastly, Assumption four is trivially satisfied, as tilde script L sub P H Y S equals F transpose nabla sub P is stable by script S, and tilde script L sub P H Y S one equals zero recall the discussion around.

Two point two. Transport coefficients and their numerical approximations. We discuss in this section how to compute transport coefficients such as the mobility, thermal conductivity and shear viscosity, in the context of linear response theory. We outline in Section two point two point one the theoretical framework of linear response theory, discuss regularity and well-posedness conditions, and state some technical results. We then discuss standard numerical techniques for computing transport coefficients in Section two point two point two. We finally discuss the paradigmatic example of mobility in Section two point two point three, which is the running example we use to theoretically illustrate our framework.

Two point two point one. Linear response theory. The linear response rho sub one of a given observable R is defined as the proportionality constant between the average response script E sub eta left parenthesis R right parenthesis and


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

the magnitude of the perturbation eta in the limit eta approaches zero, provided this limit makes sense:

rho sub one equals the limit as eta approaches zero of one over eta times the integral over script X of R psi sub eta minus the integral over script X of R psi sub zero equals the limit as eta approaches zero of the expectation sub eta of R minus the expectation sub zero of R over eta. We typically consider observables for which the expectation sub zero of R equals zero. Linear response characterizes, in powers of eta, the modification of psi sub n with respect to the canonical measure. It is expected that psi sub eta is a modification of order eta of psi sub zero, with dominant order eta for eta small. Rigorously proving this statement requires some regularity results. Let us first motivate the form of psi sub eta for eta small. We rewrite this function as psi sub eta equals f sub eta psi sub zero, with f sub eta a perturbation of the constant function one:

f sub eta equals one plus eta fraktur f sub one plus eta squared fraktur f sub two and so on. In this context, the Fokker-Planck equation left paren script L sub zero plus eta tilde script L sub phys right paren dagger psi sub eta equals zero can be reformulated, by the definition of the L squared left paren psi sub zero right paren adjoint, as left paren script L sub zero plus eta tilde script L sub phys right paren star f sub eta equals zero. By identifying terms with the same powers of eta in left paren two dot twenty-two right paren, we obtain, for terms of order eta, the following Poisson equation:

script L sub zero star fraktur f sub one equals negative tilde script L sub phys star one. The solution fraktur f sub one to left paren two dot twenty-three right paren is well-defined in view of Assumptions three and four. Using the conjugate response function S defined in left paren two dot ten right paren, we can then write fraktur f sub one equals negative left paren script L sub zero inverse right paren star S. Similarly, higher order terms are obtained by identifying terms of order eta superscript k in left paren two dot twenty-two right paren, leading to the recursive definition for all k greater than or equal to one, quad fraktur f sub k plus one equals left paren negative script L sub zero inverse right paren star tilde script L sub phys star fraktur f sub k. It can be shown inductively that the expression left paren two dot twenty-five right paren is also well-defined, as tilde script L sub phys star and left paren script L sub zero inverse right paren star stabilize script S. In particular, the expansion left paren two dot twenty-one right paren allows us to write the linear response left paren two dot twenty right paren in terms of the first-order perturbation of the invariant measure of the reference dynamics when the expectation sub zero of R equals zero colon left paren two dot twenty-six right paren rho sub one equals the limit as eta approaches zero of the expectation sub eta of R over eta equals the integral over script X of R fraktur f sub one psi sub zero. In order to rigorously prove that psi sub eta is of the form f sub n psi sub zero with f sub eta as above, we consider Lemma two point two, which generalizes Remark twenty-nine, five point five to expansions of arbitrary order k. LEMMA two point two. Suppose that Assumptions one through four hold true. Fix eta sub star greater than zero and varphi in script S. For any k greater than or equal to two, there exists M in the set of positive real numbers (which depends on eta sub star, k and varphi) such that the integral over X of phi psi sub eta equals the integral over X of phi times one plus eta fraktur F sub one plus et cetera plus eta to the power of k minus one fraktur F sub k minus one psi sub zero plus eta to the power of k script R sub eta phi k, with the absolute value of script R sub eta phi k less than or equal to M for all

Remark two point three. This expansion can be given a meaning as a converging infinite expansion at the level of operators when widetilde L p h y s is Lo-bounded, and L zero and its inverse are restricted to Pi zero L two left parenthesis psi zero right parenthesis. However, the perturbation we consider in Section three will be quite general and it cannot be assumed that the perturbation operator is L zero-bounded.

Proof. It is sufficient to prove the result for varphi in script S zero, as we can replace varphi by varphi plus C for some constant C, since F k has average zero with respect to psi zero for any k. Using the definition of fraktur f k, a straightforward computation gives, for phi in script S,

integral from mathcal X left parenthesis mathcal L subscript eta phi right parenthesis left parenthesis one plus eta fraktur f one plus dots plus eta to the power of k minus one fraktur f k minus one right parenthesis psi zero equals eta to the power of k integral from mathcal X left parenthesis widetilde mathcal L p h y s phi right parenthesis fraktur f k minus one psi zero. Note that all functions which appear in the above integrals are in script S, so that their integrals with respect to psi zero are well defined. One would like at this stage to replace phi by mathcal L subscript eta to the power of negative one Pi subscript eta varphi, which would already give the result. However, this would require controlling the integrability of derivatives of mathcal L subscript eta to the power of negative one Pi subscript eta varphi, which does not follow from our assumptions. We therefore consider an operator Q eta, k, defined on script S zero, which approximates mathcal L subscript eta to the power of negative one in some sense. Replacing phi by Q eta, k varphi leads to integral from mathcal X mathcal L eta Q eta, k varphi psi eta equals zero equals integral from mathcal X mathcal L eta Q eta, k varphi left parenthesis one plus eta fraktur f one plus dots plus eta to the power of k minus one fraktur f k minus one right parenthesis psi zero minus eta to the power of k integral from mathcal V left parenthesis widetilde mathcal L p h y s Q eta, k varphi right parenthesis fraktur f k minus one psi zero.

In order to construct Q n, k, we start from the following formal identity:

left parenthesis mathcal L zero plus eta widetilde mathcal L p h y s right parenthesis to the power of negative one equals mathcal L zero to the power of negative one left parenthesis one plus eta widetilde mathcal L p h y s mathcal L zero to the power of negative one right parenthesis to the power of negative one equals mathcal L zero to the power of negative one left parenthesis one minus eta widetilde mathcal L p h y s mathcal L zero to the power of negative one plus dots plus left parenthesis negative eta right parenthesis to the power of k left parenthesis widetilde mathcal L p h y s mathcal L zero to the power of negative one right parenthesis to the power of k plus dots right parenthesis. The previous expansion suggests to introduce an approximate inverse operator, obtained by truncating the formal infinite expansion at order O left parenthesis eta to the power of k right parenthesis. It is moreover sufficient to construct a pseudo-inverse on script S zero, which amounts to restricting all the operators using Pi zero on the left and on the right. We therefore introduce

Two point twenty-nine

Q sub eta comma k equals Pi sub zero curly L sub zero to the power of negative one Pi sub zero plus sum from n equals one to k minus one left parenthesis negative eta right parenthesis to the power of n Pi sub zero curly L sub zero to the power of negative one Pi sub zero left parenthesis tilde curly L sub phys Pi sub zero curly L sub zero to the power of negative one Pi sub zero right parenthesis to the power of n. This operator is well-defined by Assumptions three and four, as it consists of finite compositions of operators leaving invariant, so that Q sub eta comma k maps script S to script S sub zero. Note that, by construction,

curly L sub eta Q sub eta comma k equals Pi sub zero plus left parenthesis negative one right parenthesis to the power of k minus one eta to the power of k left parenthesis tilde curly L sub phys Pi sub zero curly L sub zero to the power of negative one Pi sub zero right parenthesis to the power of k. Equation two point two eight then becomes two point three zero


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

where the remainder is given by script R sub eta comma varphi comma k equals left parenthesis negative one right parenthesis to the power of k integral over script X left parenthesis tilde curly L sub phys Pi sub zero curly L sub zero to the power of negative one Pi sub zero right parenthesis to the power of k varphi psi sub eta plus integral over script X left parenthesis left parenthesis negative one right parenthesis to the power of k minus one left bracket left parenthesis tilde curly L sub phys Pi sub zero curly L sub zero to the power of negative one Pi sub zero right parenthesis to the power of k varphi right bracket left parenthesis one plus dots plus eta to the power of k minus one fraktur f sub k minus one right parenthesis minus left parenthesis tilde curly L sub phys Q sub eta comma k varphi right parenthesis fraktur f sub k minus one right parenthesis psi sub zero. two point three one Equation two point three zero is the desired result two point two seven, since Pi sub zero varphi equals varphi for varphi element of script S sub zero. It remains at this stage to show that the remainder term script R sub eta comma varphi comma k is uniformly bounded. We introduce, for notational convenience, the operator curly A equals tilde curly L sub phys Pi sub zero curly L sub zero to the power of negative one Pi sub zero. Since varphi element of script S, it holds that curly A to the power of k varphi element of script S by Assumptions three and four. By Assumption two, there exists m sub k element of mathbb N such that for all absolute value eta less than or equal to eta sub star, absolute value integral over script X curly A to the power of k minus one varphi psi sub eta less than or equal to norm curly A to the power of k minus one varphi norm sub B sub m sub k to the power of infinity integral over script X curly K sub m sub k psi sub eta less than or equal to norm curly A to the power of k minus one varphi norm sub B sub m sub k to the power of infinity norm curly K sub m sub k norm sub L squared left parenthesis psi sub eta right parenthesis. two point three two

The latter quantity is uniformly bounded in eta in view of two point five, with a bound depending only on eta star, varphi and k.

A similar uniform bound can be found for the second integral in two point thirty-one, since all the functions which appear in the integral belong to some space B sub m sub k superscript infinity, upon possibly increasing m sub k. Indeed, since fraktur f sub i element of script S for any one less than or equal to i less than or equal to k minus one, there exist m sub k prime greater than or equal to one such that absolute value of eta fraktur f sub one plus cdots plus eta superscript k minus one fraktur f sub k minus one absolute value is less than or equal to left parenthesis absolute value eta double vertical bar fraktur f sub one double vertical bar sub B sub m sub k prime superscript infinity plus cdots absolute value eta superscript k minus one double vertical bar fraktur f sub k minus one double vertical bar sub B sub m sub k prime superscript infinity right parenthesis script K sub m sub k prime, where the prefactor of script K sub m sub one, is uniformly bounded for absolute value eta is less than or equal to eta star, so the second term i n left parenthesis two point thirty-one right parenthesis i is uniformly bounded in eta by some constant depending only on eta star, varphi a n d k n. Lastly, since Q sub eta comma k element of script S, then tilde script L sub phys Q sub eta comma k varphi element of script S, so there exists m sub k double prime greater than or equal to one such that two point thirty-three absolute value integral sub script X left parenthesis tilde script L sub phys Q sub eta comma k varphi right parenthesis fraktur f sub one psi sub zero absolute value is less than or equal to double vertical bar tilde script L sub phys Q sub eta comma k varphi double vertical bar sub B sub m sub k double prime superscript infinity double vertical bar fraktur f sub one double vertical bar sub B sub m sub k double prime superscript infinity integral sub script X script K sub m sub k double prime squared psi sub eta, where the three terms on the right-hand side of two point thirty-three are uniformly bounded for absolute value eta is less than or equal to eta star by Assumptions two and three. This allows us to obtain the desired result.

Nonlinear response. Linear response is only valid up to certain values of eta, after which the nonlinear part of the response becomes too large. To study the crossover, one needs to consider higher order terms of the response. As for t h e invariant measure psi sub eta of the perturbed dynamics, the response can be expanded as a polynomial in eta in view of two point twenty-seven:

script E sub eta left parenthesis R right parenthesis equals integral sub script X R psi sub eta equals eta rho sub one plus eta squared rho sub two plus eta cubed rho sub three plus cdots. This allows us to define the kth-order response, denoted by rho sub k, characterized inductively for k greater than or equal to two as two point thirty-four rho sub k equals limit as eta approaches zero fraction numerator absolute value script E sub eta left parenthesis R right parenthesis minus left parenthesis eta rho sub one plus eta squared rho sub two plus cdots plus eta superscript k minus one rho sub k minus one right parenthesis absolute value over denominator eta superscript k end fraction equals integral sub script X R fraktur f sub k psi sub zero. The purpose and usefulness of writing higher order terms of the response will be made clear in Section three, when we attempt at reducing the contributions rho sub k for

Two point two point two. Numerical techniques to estimate transport coefficients. In this section, we discuss standard numerical techniques for computing transport coefficients. We first reformulate the linear response presented in Section two point two point one as an integrated correlation, through the celebrated Green-Kubo formula, and then outline the numerical difficulties associated with the estimation of transport coefficients, in particular the large statistical error of the associated estimators.

Reformulating the linear response as an integrated correlation. A useful corollary of two point twenty-six and two point twenty-four is that we can reformulate the definition of the linear response two point twenty as an integrated correlation function, called the Green-Kubo formula. To define it, we first consider the following operator identity two point thirty-five script L sub zero superscript negative one equals negative integral from zero to plus infinity e superscript t script L sub zero d t on the Hilbert space

L subscript zero superscript two left parenthesis psi subscript zero right parenthesis equals Pi subscript zero L squared left parenthesis psi subscript zero right parenthesis equals left brace varphi in L squared left parenthesis psi subscript zero right parenthesis such that the integral over mathcal X varphi psi subscript zero equals zero right brace. The identity, equation two point thirty-five, holds for underdamped and overdamped Langevin under certain conditions. In view of this identity, as well as equations two point twenty, two point twenty-six, and two point twenty-four, and the definition, equation two point ten, of the conjugated response S, we can write rho subscript one equals the limit as eta approaches zero the fraction mathbb E subscript eta of R, all over eta equals the integral over mathcal X R mathfrak f subscript one psi subscript zero equals negative the integral over mathcal X left parenthesis mathcal L subscript zero inverse R right parenthesis left parenthesis widetilde mathcal L subscript phys end subscript star one right parenthesis psi subscript zero equals the integral from zero to positive infinity mathbb E subscript zero of R left parenthesis X subscript t right parenthesis S left parenthesis X subscript zero right parenthesis, d t, equation two point thirty-six where the expectation mathbb E subscript zero is over all initial conditions X subscript zero distributed according to the invariant measure psi subscript zero, and over all realizations of the reference dynamics at hand. For Langevin dynamics, the conjugate response function reads equation two point thirty-seven

S left parenthesis q, p right parenthesis equals beta F left parenthesis q right parenthesis transposed M inverse p. Similarly, for overdamped Langevin dynamics, it reads

S left parenthesis q right parenthesis equals beta F left parenthesis q right parenthesis transposed nabla V left parenthesis q right parenthesis. In both cases, S is in L subscript zero squared left parenthesis psi subscript zero right parenthesis. We emphasize that, as already discussed in Section two point one, the expression for S comes from the generator widetilde mathcal L subscript phys of the perturbation, and not the observable

R. The Green-Kubo formula shows that a nonequilibrium property, the transport coefficient rho subscript one in this case, can be computed using simulations at equilibrium, that is for eta equals zero. Standard numerical techniques. Transport coefficients are often estimated in one of two ways:

One. Equilibrium techniques based on the Green-Kubo formula, equation two point thirty-six. To numerically estimate the quantity, equation two point thirty-six, one needs to discretize the continuous dynamics in time, using a fixed timestep Delta t greater than zero. This leads to the presence of some timestep bias of order O left parenthesis Delta t raised to the power theta right parenthesis, where theta depends on the numerical method at hand. Additionally, the time integral must be truncated


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

to some finite integration time T. This leads to some truncation bias, which is small due to the exponential convergence of etCo.

Last but not least, the expectation is computed using empirical averages over K realizations. This naturally suggests the following estimator for p-one:

PK,T equals the sum from k equals one to K of the integral of R of X k of X, d t, over K

Although there are clear advantages to using equilibrium techniques, for instance, correlation functions for different conjugate responses can be computed simultaneously, there is also one major challenge in using, equation two point thirty-six. The integral is a correlation term, which is a small quantity for large t, plagued by a large statistical error. The statistical error is therefore the main source of error, as the variance is expected to scale linearly with the integration time T. More precisely, it is shown that the statistical error of PK,T is of order T over K.

Overall, a tradeoff has to be considered for the choice of T as the bias is smaller for larger T while the variance increases with T.

Two. Nonequilibrium steady-state techniques. This method works by first approximating the limit in equation two point twenty by the finite difference En of R divided by n, with n sufficiently small to limit the bias, and next estimating the expectation with time averages as equation two point thirty-eight. the integral from zero to t of R of X, ds,

for response functions with average zero with respect to psi subscript zero. When computing such steady-state averages over long trajectories, the asymptotic variance of the trajectory average computed using the discretized dynamics coincides at dominant order in n with the asymptotic variance of the trajectory average computed using the corresponding continuous dynamics.

One source of error is the systematic error due to three different biases. As discussed in Proposition two point four, the finiteness of the integration time leads to some bias of order one over n t, which is typically smaller than the statistical error. Additionally, the fact that we consider n tends to zero leads to some bias of order n, as a consequence of Lemma two point two. Lastly, the time discretization of the continuous dynamics also leads to some time step bias.

As discussed in Proposition two point four below, the statistical error is dictated by a central limit theorem, so the variance of the estimator O n t scales as one over n squared t. The simulation time required to estimate P one with a sufficient statistical accuracy therefore scales as t proportional to n to the negative two, leading to very long integration times t. Such long simulation times are often prohibitive in practical cases of interest. These results, and the tradeoffs to be considered, are discussed in more detail in Section two point three.

Two point two point three. Application to mobility. The aim of this section is to illustrate the various previous results in the paradigmatic case of mobility. We consider the case where F belongs to real numbers to the power n is a constant force, and the state-space is X equals T to the d. We define the mobility for both overdamped Langevin and Langevin dynamics, and discuss how it is related to the self-diffusion by Einstein's relation.

From a physical point of view, it is expected that a nonzero constant force in some given direction induces a response from the system. At steady-state, this response is represented by some nonzero flux, due to the fact that the forcing F is not the gradient of a periodic function. This nonzero flux depends both on the perturbation and on the observable R in question.

For the Langevin dynamics two point eighteen, the perturbation nF is expected to induce a nonzero velocity in the direction F. The mobility is the proportionality constant between the externally applied force F and the observed average velocity in the direction F. Therefore, it is natural to consider the observable

R(p) equals F transpose M to the negative one p.

This gives us the following expression for the mobility, in view of two point twenty-six:

P one equals one over t integral d x R to the power n (F transpose M to the negative one p) f one forty.

It can be rewritten using the Green-Kubo formula two point thirty-six and the expression two point thirty-seven of the conjugate response as

P one equals B times the integral from zero to infinity of the expected value at zero of F transpose M to the negative one P t times F transpose M to the negative one p zero.

From this expression, it is easy to see that the mobility is related to the self-diffusion coefficient D F as

Two point thirty-nine P one equals B D F,

where

D F equals the limit of t tends to positive infinity expected value of F transpose times Q t minus Q zero squared all over two t,

with

Q t equals Q zero plus the integral from zero to t of M to the negative one p s ds the unperiodized displacement. The formula two point thirty-nine for D F is known as Einstein's relation.

For overdamped Langevin dynamics two point eleven, there is no notion of velocities. The system is however expected to drift in the direction F. This can be quantified by how much the gradient part of the force changes in the direction F. Thus, it is natural to consider the following observable

R(q) equals F transpose V V (q).

The mobility is then defined as the average projected force in the direction of the perturbation

P one equals the expected value of F transpose V f one forty.


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

For overdamped Langevin, the mobility is related to the self-diffusion D F through the following equality

B D F equals the absolute value of F squared minus P one equals the absolute value of F squared minus B times the integral from zero to B of the expected value of F transpose V of q t F transpose V of zero,

where the second expression involves the Green-Kubo formula for the linear response of F transpose V V.

Two point three. Numerical Analysis for N.E.M.D. In this section, we perform error analysis on the estimator two point thirty-eight. We obtain bounds on the variance, then on the finite-time integration bias. Without loss of generality, we consider response functions of the form R equals H O R, i.e. functions with zero average with respect to the invariant measure of the reference dynamics. The estimator O n t defined in two point thirty-eight converges almost surely, as t tends to infinity to

P n equals the integral of R y n equals P one plus O of n,

Two point forty where the last equality comes from Lemma two point two. However, O n t suffers both from a large asymptotic variance, of order o k o over n squared (with o k o the asymptotic variance for time averages of R computed with the reference dynamics), and a large finite-time sampling bias, of order one over n t. The aim of this section is to make precise the latter two statements.


## Bounds on the statistical error. The scaling of the statistical error is quantified in the following result.

PROPOSITION two point four. Suppose that Assumptions one through four hold true. Fix R E S zero and n E R. Assume that X zero is similar to H init for some initial probability measure H init (d x) such that M init (K n) is less than positive infinity for any n greater than one. Then the estimator Q n t converges almost surely to P one n as t tends to positive infinity, and the following central limit theorem holds:

V t times open parenthesis n t minus P one n close parenthesis as t tends to positive infinity in law converges to N (zero, zero K m).

Two point forty-one

Moreover, there exists O R zero such that for any n times x belongs to open parenthesis zero, positive infinity close parenthesis, there is C belongs to R plus (which depends on n times star and R) for which

V n less than n times star , the integral from zero to infinity of R times two n minus R two zero minus R two zero is less than or equal to C n squared.

Two point forty-two

This result shows that simulation times of order t proportional to n squared should be considered in order for the variance of the naive estimator two point thirty-eight to be of order one , and also for its bias to be of order n, i.e. of the same order of magnitude as the bias P one minus P one n arising from choosing n tends to zero. For completeness, the proof of two point forty-two is done at second-order, in order to determine the expression of the term o R zero characterizing the first-order variation of o R n with respect to n.

Proof. The central limit theorem two point forty-one holds by the results, since the Poisson equation minus L n R n equals H O R has a unique solution in H O B A n C L two of y for some integer n greater than or equal to one in view of two point five and two point six. Note that H O R n equals R n. To prove two point forty-two, we first write the asymptotic variance as

Two point forty-three O R n equals two times the integral of R H O n U n.

In view of Lemma two point five below, we introduce "widetilde R equals negative backslash mathcal L subscript zero to the power of negative one backslash Pi subscript zero widetilde backslash mathcal L subscript phys widehat R subscript zero in mathscr S ," so that

Two point forty-four

Integral over X of R Pi sub eta hat R sub eta psi sub eta equals integral over X of R Pi sub eta hat R sub zero psi sub eta plus eta integral over X of R Pi sub eta tilde R psi sub eta plus eta squared calligraphic R sub eta, with the remainder term

Calligraphic R sub eta equals integral over X of R fraction Pi sub eta left parenthesis hat R sub eta minus hat R sub zero minus eta tilde R right parenthesis over eta squared psi sub eta. By Lemma two point five and Assumption two, the remainder calligraphic R sub n bounded for eta in left bracket negative eta star, eta star right bracket. Note that, since Pi sub zero hat R sub zero equals hat R sub zero and Pi sub zero R equals R, we can write

Integral over X of R Pi sub eta hat R sub zero psi sub zero equals integral over X of R hat R sub zero psi sub zero minus left parenthesis integral over X of hat R sub zero psi sub eta right parenthesis left parenthesis integral over X of R psi sub zero right parenthesis equals integral over X of R Pi sub zero hat R sub zero psi sub zero. The same argument is valid for tilde R. We next use Lemma two point two to write the two integrals on the right hand side of two point forty-four as

Two point forty-five

Integral over X of R Pi sub eta hat R sub eta psi sub eta equals integral over X of R Pi sub zero hat R sub zero psi sub zero plus eta integral over X of R left parenthesis hat R sub zero fraktur f sub one plus Pi sub zero tilde R right parenthesis psi sub zero plus eta squared tilde calligraphic R sub eta, where

Tilde calligraphic R sub eta equals calligraphic R sub eta plus script R sub eta comma R hat R sub zero comma two plus eta script R sub eta comma R Pi sub zero tilde R comma one plus integral over X of R tilde R fraktur f sub one psi sub zero minus fraction one over eta squared left parenthesis integral over X of hat R sub zero psi sub eta right parenthesis left parenthesis integral over X of R psi sub eta right parenthesis minus fraction one over eta left parenthesis integral over X of tilde R psi sub eta right parenthesis left parenthesis integral over X of R psi sub eta right parenthesis. Two point forty-six

Equation two point forty-five leads to sigma sub R comma eta squared minus sigma sub R comma zero squared minus eta tilde sigma sub R comma zero squared equals eta squared tilde calligraphic R sub eta, with

Tilde sigma sub R comma zero squared equals two integral over X of R left parenthesis hat R sub zero fraktur f sub one plus Pi sub zero tilde R right parenthesis psi sub zero. In view of Lemma two point two and Assumption two, the remainder two point forty-six is uniformly bounded for eta in left bracket negative eta star, eta star right bracket. This proves that two point forty-two holds.

We conclude this section with a technical result used in the proof of Proposition two point four.

LEMMA two point five. Suppose that Assumptions one through four hold true. Fix eta star greater than zero and varphi in script S. Denote by m greater than or equal to one an integer such that varphi is in B sub m raised to infinity. Consider for any n in script R the unique solution phi sub eta in Pi sub eta B sub m raised to infinity of the Poisson equation negative script L sub eta phi sub eta equals Pi sub eta varphi, and define widetilde phi equals negative script L sub zero inverse Pi sub zero widetilde script L sub phys phi sub zero in script S. Then, there exists n greater than or equal to one and K in script R plus, such that for all eta less than or equal to eta star, the norm of Pi sub eta left parenthesis phi sub eta minus phi sub zero minus eta widetilde phi right parenthesis in B sub s raised to infinity is less than or equal to K eta squared. Proof. Since script L sub eta equals script L sub zero plus eta widetilde script L sub phys, a simple computation shows that


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

In view of Lemma two point two, and since fraktur f one has average zero with respect to

Psi zero, open parenthesis Pi sub eta minus Pi sub zero close parenthesis varphi equals negative eta integral over script X varphi fraktur f sub one psi zero minus eta squared script R sub eta, varphi, two equals negative eta integral over script X open parenthesis Pi sub zero varphi close parenthesis fraktur f sub one psi zero minus eta squared script R sub eta, varphi, two equals eta integral over script X widetilde script L sub phys script L sub zero to the negative one Pi sub zero varphi psi zero minus eta squared script R sub eta, varphi, two equals negative eta integral over script X open parenthesis widetilde script L sub phys phi zero close parenthesis psi zero minus eta squared script R sub eta, varphi, two equals negative eta open parenthesis one minus Pi sub zero close parenthesis widetilde script L sub phys phi zero minus eta squared script R sub eta, varphi, two. Therefore, negative script L sub eta open parenthesis phi sub eta minus phi zero minus eta widetilde phi close parenthesis equals eta squared widetilde script L sub phys widetilde phi minus eta squared script R sub eta, varphi, two equals eta squared Pi sub eta widetilde script L sub phys widetilde phi, because the right-hand side is eta squared widetilde script L sub phys widetilde phi up to a constant term, and has to be in the image of script L sub eta. It is clear that widetilde script L sub phys widetilde phi belongs to script S, as widetilde phi belongs to script S and widetilde script L sub phys stabilizes script S by Assumption four. Thus, there exists n greater than or equal to one such that widetilde script L sub phys widetilde phi belongs to B sub n to the infinity. Using the definition of the operator norm,

The norm of Pi sub eta open parenthesis phi sub eta minus phi zero minus eta widetilde phi close parenthesis sub B sub eta to the infinity equals eta squared the norm of script L sub eta to the negative one open parenthesis Pi sub eta widetilde script L sub phys widetilde phi close parenthesis sub B sub gamma to the infinity is less than or equal to eta squared the norm of script L sub eta to the negative one sub script B open parenthesis Pi sub eta B sub n to the infinity close parenthesis the norm of Pi sub eta open parenthesis widetilde script L sub phys widetilde phi close parenthesis sub B sub infinity to the infinity, where the norm of script L sub eta to the negative one sub script B open parenthesis Pi sub eta B sub eta to the infinity close parenthesis is uniformly bounded in view of equation two point six, as is the norm of Pi sub eta open parenthesis widetilde script L sub phys widetilde phi close parenthesis sub B sub n to the infinity by zero equation two point five. This gives the desired result.

Bounds on the finite-time bias. For completeness, we also state result on the finite-time bias of the estimator, which essentially says that this bias one over open parenthesis eta t close parenthesis. For technical reasons, this estimate however has to be formulated in a more cumbersome way. Nevertheless, bounds on the statistical error given in Proposition two point four are more important in practice, which is why we did not try to improve the bounds below.

LEMMA two point six. Consider the same setting as Proposition two point four, and assume that Sigma equals sigma sigma transposed belongs to script S. Then, for any k greater than or equal to one and any eta star greater than zero, there exist script C sub k and script M sub k which depend and left R right such that equation two point four seven

For all eta less than or equal to eta star, for all t greater than zero, the absolute value of the expected value of the estimated Phi sub eta comma t minus the estimated rho sub one comma eta is less than or equal to the fraction of C sub k over eta t plus M sub k eta raised to k. Proof. This result would be easy to prove if the estimated R sub eta belongs to script S, where the estimated R sub eta is the unique solution to the Poisson equation negative script L sub eta estimated R sub eta equals Pi sub eta R discussed in the proof of Proposition two point four. However, there is no result that ensures that this property holds, so we turn to an alternative proof where we approximate the estimated R sub eta with high precision by the estimated R sub eta comma k belongs to script S. More precisely, we introduce the estimated R sub eta comma k equals Q sub eta comma k plus one Pi sub eta R, where Q sub n comma k is the pseudo-inverse operator defined in two point twenty-nine, so that the estimated R sub eta comma k belongs to script S. Since the estimated R sub eta comma k belongs to C infinity left paren script X right paren, we use Itô's formula to write

Two point forty-eight

Differential of estimated R sub eta comma k left paren X sub t superscript eta right paren equals script L sub eta estimated R sub eta comma k left paren X sub t superscript eta right paren differential t plus gradient of estimated R sub eta comma k left paren X sub t superscript eta right paren transpose Sigma left paren X sub t superscript eta right paren differential W sub t. The martingale term in two point forty-eight is square integrable since, in view of two point seven and the fact that E, estimated R sub eta comma k belongs to script S so that the absolute value of Sigma gradient of estimated R sub eta comma k absolute value squared belongs to script S right paren, there exists ell in natural numbers such that is uniformly bounded for absolute value of eta less than or equal to eta star. Next, we write

Two point forty-nine with remainder term

In view of negative two point four eight, we write two point four nine as

Two point five zero

In view of negative two point seven and negative two point three two, the expected value of absolute value of is uniformly bounded for absolute value of eta less than or equal to eta star by belongs to. By taking expectations, two point five zero then leads to

Since there exists such that belongs to B n infinity. By Assumptions three and four, there exists n prime and K n prime, eta star prime depending on n, n prime, eta star, and k such that

Two point five one

In view of two point five one and negative two point seven,

The expected value of R hat sub eta comma k of X sub t superscript eta is less than or equal to the expected value of K sub n of X sub t superscript eta norm R hat sub eta comma k norm sub B sub n superscript infinity is less than or equal to K sub n prime comma eta star prime sup t in positive real numbers integral over X E to the power t L sub eta K sub n d mu sub init norm Pi sub eta R norm sub B sub n prime superscript infinity is less than or equal to K sub n prime comma eta star prime M sub n comma eta star norm Pi sub eta R norm sub B sub n prime superscript infinity integral over X K sub n mu sub init. This leads to two point forty-seven with

O

C sub k equals two K sub n prime comma eta star prime M sub n comma eta star integral over X K sub n mu sub init less than plus infinity, thus concluding the proof.

Three. Extending the range of linear response with synthetic forcings. We discuss in this section the notion of synthetic forcings, and how they can be used to extend the regime of linear response. We start by describing the notion of synthetic forcings in Section three point one, and give examples in Section three point two for both overdamped and underdamped Langevin dynamics. Then, we provide a methodology for choosing the magnitude of the forcings in Section three point three. Finally, we briefly discuss how to linearly combine multiple extra forcings in Section three point four.


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

Three point one. Notion of synthetic forcings. As discussed in Section two point one point one, a system with a nonequilibrium perturbation has a generator of the form

(Three point one) C sub n equals L sub zero plus n O,

where L is the generator of some perturbation to the reference dynamics with generator L sub zero. We considered in Section two only the case where L is Lphys - in other words, the perturbation corresponds to some physical perturbation on the system, which is the typical scenario in the context of statistical physics. We now consider, in addition to the physical perturbation, some possibly nonphysical extra perturbation, which we denote by Lextra, so that L in (three point one) is replaced by

L equals Lphys plus alpha Lextra,

for alpha in real numbers. We call the resulting perturbation a synthetic forcing.

The key requirement of synthetic forcings is that the addition of the extra forcing should preserve the invariant measure of the reference dynamics, thus preserving the linear response. In other words, the dynamics with generator

L sub n comma alpha equals L sub zero plus n times Lphys plus alpha Lextra has the same linear response as the dynamics associated with L sub n comma alpha equals L sub zero plus n Lphys when

Lextra integrated over X equals zero.

(Three point two)

We denote by U sub n comma alpha the invariant measure for the dynamics associated with the generator L sub n comma alpha, i.e. the solution to the stationary Fokker-Planck equation

(Three point three) L sub n comma alpha times U sub n comma alpha equals zero.

When there is no indication of the value of alpha, e.g. U sub n, it means that alpha equals zero.

From the definition (two point twenty-six) of the linear response O, it is indeed easy to see why the linear response is preserved with the addition of Lextra: the conjugate response S defined in (two point ten) is preserved, and so is f sub one in view of (two point twenty-four), which allows us to conclude by Lemma two point two. Let us emphasize that (three point two) is the key condition to be satisfied for extra forcings to be admissible. We provide various examples of admissible extra forcings in Section three point two. For technical reasons, the extra forcings we consider should satisfy the same conditions as Lphys in Assumption four.

One practical interest is to optimize the extra perturbation in order to increase the regime of linear response. As made precise in Proposition two point four, the variance of the estimator (two point thirty-eight) is of order O of n to the negative two. A larger linear regime therefore means that larger values of n can be considered without introducing too much bias on p sub one. This leads in turn to a smaller statistical error, and hence shorter simulation times to reach the same accuracy. One idea in particular is to look for Lextra which minimizes O sub two, the leading order n squared of the nonlinear response, as a proxy for minimizing the absolute value of E sub n of R minus p sub one, i.e. the nonlinear portion of the response. This is discussed in detail in Section three point three. This also naturally suggests that one could further combine k forcings in order to cancel the first k plus one orders of the response, as discussed in Section three point four.

Another approach to optimizing the perturbation is to increase the range of n for which the nonlinear response is within some desired distance from the linear regime, in relative error, also discussed Section three point three.

Three point two. Examples of synthetic forcings. To make synthetic forcings more concrete, we now go over some examples of extra forcings. We first outline in Section three point two point one the general classes of operators we consider. We then discuss more precisely examples for overdamped Langevin dynamics in Section three point two point two and for underdamped Langevin dynamics in Section three point two point three.

Three point two point one. General classes of extra forcings. When considering possible extra forcings, we restrict ourselves to differential operators of at most second order in order to realize them in Monte Carlo simulations. We consider the following classes of differential operators:

First-order differential operators Lextra equals GTVr, with G: X maps to R d such that div(Gyo) equals zero. The latter condition ensures that three point two is satisfied since Lextra equals negative GTV. r;

Second-order differential operators of the form Lextra equals negative delta star dz i or more generally negative delta Dijox i for some nonnegative function Dij: X maps to R positive. In the case Cextra equals negative delta x delta x;, the operator is self-adjoint, i.e. Cextra equals L'extra, so that three point two is easily seen to hold. For Lextra equals negative delta g Dijox i, it holds that Lextra equals negative delta g Dijox i, which also satisfies three point two.

Third. First-order differential operators with nontrivial zero order parts, such as Lextra equals zero star equals delta x U minus delta x i for yo of x equals e to the power of negative U of x. Through some abuse of notation, we use delta r U to denote the multiplication operator by the function delta z U. These operators satisfy Lextra equals zero x star, so that three point two holds.

The class of extra forcings outlined in items one and two can be easily implemented and realized in Monte-Carlo simulations. Implementing forcings of the form described in item three, however, requires some extra work to take care of the multiplication operator, as we now discuss.

We denote the class of extra forcings described in item three as Feynman-Kac forcings, as sampling the dynamics requires the use of the Feynman-Kac formula due to the nontrivial zero order term. Consider the general dynamics two point one with generator two point two, as presented in Section two point one point one. Suppose that the dynamics has a unique invariant probability measure with density yo of x equals e to the power of negative U of x. The perturbed dynamics with generator Ln, a equals Lo plus n times open bracket C phys plus a C extra close bracket, with C extra equals TV* for some vector in R d, can be sampled by evolving the SDE

dX t equals b of X t plus nF of X t minus na delta s times dt plus o of X t dW t,

and weighting trajectories with the Feynman-Kac weight

W t equals exp na integral over open bracket V U of X s close bracket ds.

In practice, this is done by evolving multiple replicas of the system with independent Brownian motions, and using resampling strategies to prevent the weights from degenerating.

From an analytical point of view, items one and two fit in the framework of Section two. Item three, however, does not directly fit in the framework of Section two. This is due to the fact that the steady-state measure of the dynamics with generator Ln, a equals Lo plus n times open bracket C phys plus Timex close bracket is not a probability measure in general. This is


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

the case only if the weights W t are renormalized. At the level of generators, this amounts to shifting the spectrum of Ln, a by An, a, where An, a is the nonzero real principal eigenvalue of the operator Ln, vector (see) references therein. The magnitude of An, vector can be made precise in terms of a and n for n small, and turns out to be of order O of n squared for n small, as formally derived in Appendix A.

Of course, by linearity, one can consider linear combinations of these extra forcings. In the next two sections, we give specific examples of each of the three classes of extra forcings discussed here for both overdamped and underdamped Langevin dynamics.

Three point two point two. Overdamped Langevin dynamics. We start by outlining some examples of synthetic forcings for the overdamped Langevin dynamics introduced in Section two point one point two. We consider successively the distinct classes of extra forcings following the general presentation of Section three point two point one.


## Example three point one (Divergence-free vector field). We consider a first-order differential operator

C extra equals GTV,

where G: X maps to R d is such that div open bracket G of q e to the power of negative V of q close bracket equals zero.

The resulting dynamics with the addition of C extra is d q t equals negative V V of q plus nF of q t plus anG of q t dt plus V two dW t.

β

Condition div open bracket G of q e to the power of negative V of q close bracket equals zero can be rewritten as div of G equals BGVV. This equality is satisfied when G is both divergence-free and orthogonal to VV, which is the situation considered. For instance, in any dimension d greater than two, with A an arbitrary anti-symmetric matrix, one possible choice for G is

G equals A VV.

As can be generalized to G equals some smooth, compactly supported function of V A V V. More generally, any divergence-free vector field in dimension d can be written as G equals VU one cross ... cross VU a minus one, where U i are scalar functions, a form which was used. Thus, more generally, G satisfies the divergence condition if and only if it is of the form

G equals VU one cross ... cross VU a minus one times e to the power of negative V.

For the one-dimensional dynamics, the only divergence-free vector field is G of q equals e to the power of negative V of q. Of course, drifts such as the previous may not be used as such in the dynamics when the position space is unbounded, as it is not clear whether the dynamics is well-posed because of the factor e and when it is, whether it admits a unique invariant probability measure. Moreover, Assumption four may not hold.

Example three point two (Modifying the fluctuation-dissipation relation). One possible choice for extra perturbations involving second-order derivatives is

C extra equals negative delta inverse V V T V q equals delta inverse four q minus V V T V q.

L n, a equals C o plus n open bracket C phys plus a C extra close bracket equals one plus a n C o plus n phys.

The dynamics associated with L n, Q reads d q t equals negative one plus a n V V of q t plus n F of q t dt plus one half times one plus a n dW t.

This amounts to increasing the magnitude of the terms involved in the fluctuation-dissipation as n increases when Q is greater than zero. Note that, in order for this perturbation to be admissible, we require that one plus a n is greater than zero.

More generally, one could consider extra forcings of the form negative V star D of q V for some D: X maps to R d cross d with values in the space of symmetric matrices, possibly with D constant.

Example three point three (Feynman-Kac forcing). This choice, although it showcases great promise and potential in extending the linear regime, as we will demonstrate in Sections four point two and four point three, is not practical to be simulated by a single long realization of the dynamics as the weights degenerate, rendering the simulation inefficient. Its general form is

C extra equals TV* equals the sum of delta g, from i equals one to d for some vector in R d. The generator Lo plus n times open bracket Lphys plus QLextra close bracket is the sum of first and second-order differential operators and a weight. Its stochastic representation corresponds to evolving the SDE

d q t equals negative V V of q t plus nF of q t minus a n times g dt plus one half β dW t,

and using the Feynman-Kac formula for the weight involving TVV.

Three point two point three. Langevin dynamics. We now outline some examples for Langevin dynamics, presented in Section two point one point three. Since this dynamics evolves two variables, namely positions q and momenta p, we can in theory use both differential operators Vq and Vp to construct our synthetic forcings. This leads to additional options for each class of extra forcings.

Example three point four (Divergence-free vector field). The extra perturbation can be chosen as a first-order differential operator of the form

Čextra equals GTV equals G{ V q plus G two Vp,

where G one, G two are such that divq(G one TV) plus divp(G two TV) equals zero.

A perturbation of similar form to Čextra has been used and studied. For instance, in any dimension d greater than two, a natural choice is G equals AVH, or more generally G equals &'(H)AVH, where A is an antisymmetric matrix. Typical choices include


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

the symplectic matrix negative I zero zero I,

or, more generally, linear combinations of matrices of the form

A equals negative BT zero B

zero or A one zero zero,

A two with A one, A two antisymmetric. In all these expressions, A one, A two and B can be functions of (q,p). The choice Čextra leads to the generator

(Čextra4) (q, p) equals G one(q,p)TVq plus G two(q,p)}Vp,


## and the dynamics

dqt equals M negative one pt dt plus an G one(qt, Pt) dt,

dpt equals negative VV(qt) dt plus n(F(qt) plus @ G two(qt, Pt)) dt negative YM negative one pt dt plus VB twenty-seven dWt.

When G equals JVH with J the symplectic matrix, the extra perturbation corresponds to rescaling the Hamiltonian part of the dynamics, which is equivalent, up to a time rescaling, to changing the strength of the fluctuation-dissipation.

Example three point five (Modified fluctuation-dissipation). We first consider an operator that is second-order in p. A simple choice for the extra forcing is Lextra equals negative B negative one.

Ln, a equals Cham plus (y plus an) CFD plus Cphys.

For this forcing to be admissible, we require that one plus on greater than zero. The dynamics associated with Ln, a reads dqt equals M negative one pt dt,

dpt equals negative VV(qt) dt plus nF(qt) dt negative (y plus an) M negative one pt dt plus two(y plus an) β dWt.

The effect of the extra forcing is to rescale the strength of the fluctuation-dissipation, either increasing it when an greater than zero, or reducing it when an less than zero. More generally, one can scale this forcing by a function of q, i.e. consider Lextra equals negative a(q) two with a(q): X -> R. One can also extend this form to matrix-valued diffusions of the form D(q,p) Vp.

We can similarly consider a second-order forcing in q. One possible choice for the generator is then Lextra equals negative B negative one Vq seven q. Here, we require that on greater than zero. The associated dynamics is dqt equals M negative one pt dt negative an VV (qt) dt plus one plus V two zero one B.

dpt equals (negative VV(qt) dt plus nF(qt)) dt negative YM negative one pt dt plus V twenty-seven dWt,

β

where Bt is a standard d-dimensional Brownian motion independent of Wt. One can also generalize this choice by scaling it by a function of p, leading to the more general choice negative b(p) VV q, or introduce a matrix-valued diffusion and consider VD(q, p) Vq.

Additionally, one could consider a mixed-term forcing, such as negative B negative one V q p or negative- Vg. However, since the diffusion matrix must be symmetric and positive- definite, this prevents us from considering these mixed forcings without adding also a contribution negative one Vq. Upon writing Ln,a as the sum of a first-order differential operator and Do: V two, we require that Da be symmetric positive, so that one can simulate the associated SDE upon taking the square root of Do, with

Da equals Do plus QD, Do equals Y zero Id zero zero,

where D denotes the diffusion associated with the extra forcings.

Example three point six (Feynman-Kac forcing). One possible form of the general forcing in item three of Section three point two point one is the following, for two functions § one : Rd -> R and § two : X -> R:

Čextra equals § one (p) TV* plus § two (q) TV.

The associated dynamics reads dqt equals M negative one pt dt negative an § one (pt) dt,

dpt equals negative VV (qt) dt plus n(F(qt) negative a § two (qt)) dt negative YM negative one pt dt plus V twenty-seven β dWt,

whose trajectories are reweighted using the Feynman-Kac weight involving § one (Ps) TVV (qs) plus § two (qs) TM negative one ps in the integral.

Three point three. Choosing the magnitude of the forcing. The synthetic forcing is comprised of a physical forcing and an extra one, which translates into a perturbation Lphys plus QLextra at the level of generators. We discuss here how to choose the magnitude o of the extra forcing in order to optimize it in terms of the linear response.

Recall from Section two point two point one that, for small values of n, we can think of the response as a polynomial in seven:

ra (n) equals En, (R) equals np one (a) plus n two p two (a) plus nn negative one pn negative one (a) plus O (n).

In practice, we want to choose a such that the contribution from nonlinear terms is minimized. There are two main approaches to choosing such an optimal a, by (i) canceling the second-order response, or (ii) bounding the relative error with respect to the linear regime. We next discuss both options.

Canceling the second-order response. A first approach to reduce the nonlinear response is to cancel the second-order term o two, as this is the dominant part of the nonlinear bias when n is small. The second-order response is characterized by f two in, which reads here f two (a) equals Lo one Č phys plus @ Č extra Lo one S equals f two , phys plus @ f two , extra,

where we decomposed the second-order perturbation of the invariant measure into its physical and synthetic parts. Since f two is linear in a, the value of a for which p two is


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

cancelled is easily obtained from the definition of the second-order response. Indeed,

rho sub two (alpha) equals the integral over X R mathfrak f sub two, phys psi sub zero plus alpha integral over X R mathfrak f sub two, extra psi sub zero equals rho sub two plus alpha rho sub two, extra. Therefore, rho sub two (alpha star) equals zero for alpha star equals negative the fraction of the integral over X R mathfrak f sub two, phys psi sub zero over the integral over X R mathfrak f sub two, extra psi sub zero, equation three point one three,

provided that the integral over X R mathfrak f sub two, extra psi sub zero is not equal to zero. The latter condition ensures that widetilde mathcal L extra has a nontrivial contribution to the second-order response, and can therefore be used to cancel the second-order response. An important remark is that although alpha star cancels rho sub two, it might significantly increase rho sub three and higher order terms.

Note that for Feynman-Kac forcings, the computation of alpha star must be reformulated. This is due to the fact that equation two point two five comes from the Fokker-Planck equation, which admits a nontrivial principle eigenvalue for Feynman-Kac forcings, as discussed in Section three point two point one and made precise in Appendix

A. In general, the optimal value alpha star cannot be determined a priori. It requires, in principle, two sets of simulations with alpha sub one not equal to alpha sub two, from which alpha star can be extrapolated due to the linearity of rho sub two (alpha) in alpha. We discuss in Section five how to implement this approach for actual systems of interest.

Remark three point seven. For certain situations, it is possible to determine the impact of the extra perturbations from the response curve for the physical forcing. Consider for instance the setting of Example three point two. We define mathbb E sub eta, alpha as the steady-state average for psi sub eta, alpha, the solution to the Fokker-Planck equation mathcal L sub eta, alpha dagger psi sub eta, alpha equals zero. Since mathcal L sub eta, alpha is proportional to mathcal L sub eta over one plus alpha eta, zero (recall that we require one plus alpha eta not equal to zero), a simple computation shows that psi sub eta, alpha equals psi sub eta over one plus alpha eta, zero, so forall eta in mathbb R, q u a d r sub alpha (eta) equals r sub zero (eta over one plus alpha eta). Then,

r sub alpha (eta) equals r sub zero prime (zero) eta over one plus alpha eta plus one half r sub zero double prime (zero) eta squared over (one plus alpha eta) squared plus O (eta cubed) equals r sub zero prime (zero) eta plus [ one half r sub zero double prime (zero) minus alpha r sub zero prime (zero) ] eta squared plus O (eta cubed). This allows us to find the optimal alpha which cancels rho sub two, given by alpha equals the fraction with numerator r sub zero double prime evaluated at zero and denominator two times r sub zero prime evaluated at zero equals the fraction with numerator rho sub two and denominator rho sub one. This result suggests that, for the example presented here, the magnitude of the extra forcing should be chosen so that rho sub two extra equals negative rho sub one. Bounding the relative error. From a practical viewpoint, and following the usual bias/variance tradeoff, it might be more advantageous to stay close enough to the linear response for larger eta, even if that means decreasing the true linear regime. In order to make these statements quantitative, we consider the relative error delta in the response relative to the linear response, that is delta sub alpha of eta equals the absolute value of the fraction with numerator r sub alpha of eta minus rho sub one eta and denominator rho sub one eta. For an extra perturbation widetilde mathcal L sub extra and alpha in the set of real numbers fixed, the response stays in the neighborhood of the linear response until a certain value of eta, at which point it deviates too far from the linear regime. Since delta sub alpha of zero equals zero, we look, for some small fixed value epsilon greater than zero, for the smallest value of the absolute value of eta such that delta sub alpha of eta equals epsilon, which we denote by eta sub alpha of epsilon. The question of optimizing alpha can be reformulated as finding alpha such that eta sub alpha of epsilon is maximized:

Three point fifteen alpha star of epsilon equals the argument max of alpha in the set of real numbers of eta sub alpha of epsilon, eta sub alpha of epsilon equals the argument min of eta in the set of real numbers such that the absolute value of eta satisfies delta sub alpha of eta is greater than or equal to epsilon. As we tighten the bound epsilon, the value of alpha star of epsilon gets closer to the value alpha star for which rho sub two of alpha star equals zero. This comes from the fact that eta sub alpha of epsilon is of order big O of epsilon for alpha not equal to alpha star, and of order big O of the square root of epsilon for alpha equals alpha star. Indeed, three point fourteen can be written as delta sub alpha of eta equals the absolute value of rho sub two extra times alpha minus alpha star eta plus order big O of eta squared.

Intuitively, canceling the leading order term, namely rho sub two in the small eta regime, is equivalent to minimizing the deviation from the linear regime, the latter being implied by the limit epsilon approaches zero. Figure two illustrates how alpha star and alpha star of epsilon can yield drastically different response curves. The functions r sub alpha of eta are fourth-order polynomials in eta whose coefficients have been hand-picked in order to demonstrate the possibly very different behaviors of r sub alpha star of eta and r sub alpha star of epsilon of eta. Figure two a shows the full response curves r sub alpha of eta, and Figure two b shows the corresponding relative error curves relative to the linear response three point fourteen. The curve obtained by choosing alpha star minimizes the deviation from the linear regime for small n as the second-order response rho sub two is canceled. On the other hand, the curve for alpha star of epsilon equals zero point zero five slightly departs from the linear regime earlier than the one associated with alpha star. It stays, however, in the vicinity of the linear response for much larger n. This behavior is more clearly observed in figure two b.


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

In most practical applications, using a plus epsilon is the choice of interest, as the points on the response curve are anyway computed with some numerical error, such as timestep discretization and statistical error. There is, however, a tradeoff to be considered. As one tightens the acceptable relative error by decreasing epsilon, the value of na epsilon is also decreased. In practice, values of epsilon in the range zero point zero one to zero point one are small enough to lead to a bias of a few percent in relative magnitude, but large enough so that the benefit of the increased magnitude of the forcing is significant. We further illustrate the tradeoff in Section four with numerical results for several observables for overdamped and underdamped Langevin dynamics.

As a final remark in this section, note that computing a plus epsilon requires computing the full response curve. Although this is not practical, the aim here is to provide a proof of principle demonstrating the potential computational gains obtained by making use of synthetic forcings and decide, between various strategies, the most promising one in order to adapt the approach to actual systems of interest.

Three point four. Linearly combining extra forcings. As discussed in Section three point three, with the addition of some extra forcing Lextra, it is possible to find a value of sigma which cancels the second-order response p two due to the linearity of f two in sigma, as shown in three point one two. We can extend this notion to linear combinations of extra forcings. In particular, one can combine k forcings in order to cancel the first k nonlinear orders of the response. That is, for alpha equals alpha one to alpha k, the synthetic perturbation Lphys plus alpha one Lextra one plus alpha k Lextra k can be used, with alpha chosen such that p two a to p k plus one a equals zero. This is a nonlinear equation in alpha, with k unknowns scalar values and k conditions to solve.

Four. Numerical results. The aim of the numerical illustrations presented in this section is to demonstrate the potential of the synthetic forcing approach, on the examples given in Section three point two. The numerical results are obtained by discretizing the partial differential equations determining the invariant probability measure of each system, namely the Fokker-Planck equation three point three and the Poisson equation two point two three. The use of this method, particularly in low-dimensional systems, allows us to extensively and thoroughly examine the quality of synthetic forcings, as we can easily compute full response curves and individual orders of the response, in contrast to Monte Carlo simulations, for which some statistical error and timestep discretization bias are present. This numerical method, however, cannot be used as such for higher dimensional systems, as solving the associated partial differential equations becomes too cumbersome a task. Thus, for higher dimensional systems, Monte Carlo simulations are usually preferred.

We first discuss in Section four point one the numerical methods used, then present the numerical results for the one and two-dimensional overdamped Langevin, and one-dimensional Langevin dynamics in Sections four point two, four point three and four point four, respectively. We finally discuss in Section four point five the impact of the synthetic forcings approach on variance reduction in the estimation of transport coefficients.

Four point one. Numerical method. The full response curve and the linear response are computed by solving the associated Fokker-Planck equation for each dynamics, and the Poisson equation two point two three, respectively. The main advantage of numerical methods based on solving partial differential equations is that the discretization error can be systematically reduced to a very small value by refining the mesh used to represent the functions at hand. There are two situations in which the solutions to partial differential equations are required to determine the response to external perturbations, which we outline below.

Approximation of the linear response rho one. The linear response is obtained by computing fraktur f one and approximating the integral on the right-hand side of two point two six. To approximate fraktur f one, we solve the Poisson equation two point two three, which we recall here for convenience:

Four point one

L zero star fraktur f one equals negative tilde L phys star one. For overdamped Langevin dynamics, we directly solve four point one as we consider a bounded position space, namely the torus T d. For Langevin dynamics, instead of solving for fraktur f one in the expansion two point two one, we solve for psi bar one in psi eta equals psi zero plus eta psi bar one plus eta squared psi bar two plus so on, i.e. psi bar one equals fraktur f one psi zero. This function satisfies the Poisson equation

Four point two

L zero dagger psi bar one equals negative tilde L phys dagger psi zero, which is equivalent to reformulating four point one in terms of the L two adjoint. Due to the unbounded momentum space for Langevin dynamics, solving four point two makes the problem easier to solve numerically than four point one. Indeed, the unbounded momentum space needs to be truncated. A natural choice when solving for psi bar one is to set Dirichlet boundary conditions at the boundaries of the domain in p, which is consistent with the fact that psi bar one q p is expected to vanish as the absolute value of p approaches positive infinity. In contrast, there is no natural boundary condition for fraktur f one in two point two six when the momentum space is truncated.

Once an approximation of fraktur f one or psi bar one is obtained, we perform a quadrature on one of the following integrals to directly find the linear response

Rho sub one equals the integral over x of r script f sub one psi sub zero equals the integral over x of r bar psi sub one. More generally, this procedure can be extended by using the recursive formula two point twenty-five, which allows for the computation of response terms of arbitrary orders; this is used in particular to compute rho sub two, phys and rho sub two, extra when computing the value of alpha star defined in three point thirteen.

Approximation of the full response r sub alpha of eta. In this work, we compute the full response in order to quantify how much, and how quickly the response deviates from the linear regime. In actual applications, one typically does not compute the full response curve, in particular when using Monte Carlo simulations. The quantity of interest, namely the transport coefficient, comes from the linear response, which can be obtained from computing a single point (or typically two to ensure linearity), so computing the full response curve is not of interest.

The full response curve can be computed by solving the Fokker-Planck equation three point three, which we recall for convenience

Four point three

Script L sub eta, alpha dagger psi sub eta, alpha equals zero, and then performing a quadrature on the integral r sub alpha of eta equals the integral over x of r psi sub eta, alpha. Solving the P D E. For the discretization of the P D Es four point one, four point two and four point three, we use a finite-difference scheme. Periodic boundary conditions are used in the spatial variable since we always consider q in T superscript d for both overdamped Langevin and Langevin dynamics, with d equals one or d equals two. For overdamped Langevin dynamics, we use a centered finite-difference scheme. For the one-dimensional Langevin dynamics, the momentum


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

variable is first truncated to negative Pmax, Pmax, then its domain is discretized with step size hp. Dirichlet boundary conditions are imposed at p equals plus or minus Pmax. We ensured that our truncated value of the momentum Pmax equals six is large enough so that it does not affect the numerical results. A centered scheme is also used for Langevin dynamics, except for the transport term minus p M inverse q in the Fokker-Planck equation two point seventeen, where an upwind scheme is used (refer to Appendix B for the precise expressions of the aforementioned numerical schemes). All computations were performed with the Julia language.

Four point two. Overdamped Langevin dynamics - one-dimensional case. We present in this section the numerical results for the one-dimensional overdamped Langevin dynamics two point thirteen on X equals T, with potential energy

Four point four V of q equals cosine two T q.

We consider the observable

Four point five R of q equals open parenthesis a cosine two T q plus b sine two T q close parenthesis e B V of q,

where a, b in R. We choose this observable for two reasons. First, by construction, it has average zero with respect to the Gibbs probability measure, with density proportional to e to the negative B V. Second, we can tune the coefficients a and b to control the magnitude of the individual orders of response. This allows us to choose a and b such that the first and second-order responses are normalized, i.e. P one equals P two equals one, which makes it easier to compare the quality of each synthetic forcing.

Due to the symmetries of the potential energy function four point four, we can directly compute the values of a and b such that p one equals P two equals one. More precisely, it can be shown that f one and f two are respectively odd and even on negative one-half, one-half so that b controls the magnitude of P one and a controls the magnitude of P two. The value of b such that p one equals one is easily computed using two point thirty-four to be minus sine two T q f one of q d q four point six b equals Z inverse f one d a, Z equals e to the negative V d q. Similarly, the value of a such that P two equals one is negative one

Four point seven a equals Z inverse cosine two T q f two d q

The spatial domain T equals zero, one is discretized into m equals two thousand points, with uniform step size h equals one over m. The simulations were performed with inverse temperature B equals one and mass M equals one, which is also the setting for the results in two dimensions obtained in Section four point three. Moreover, we consider the forcing F equals one, as this is the only nongradient forcing in dimension one on the torus.

We present the full response curves and the associated linear response for each of the three synthetic forcings discussed in Section three point two point two. Figures three a, three b and three c correspond to the Feynman-Kac forcing three point nine, modified fluctuation-dissipation three point eight and divergence-free vector field three point five, respectively. Note that in dimension one, three point five reduces to a single option, namely equals e v d. d a'

Four point eight which is the one used here. For each of the plots, we show the linear response, the full response curve r sub zero of eta for alpha equals zero, the response curve for r sub alpha star of eta for alpha star computed using three point thirteen, and response curves for some additional values of alpha in R for illustrative purposes. In some cases, in particular when the response curve associated with alpha star sees marginal improvement in extending the linear regime, we also compute the curve for alpha star of epsilon, where we choose epsilon equals zero point zero five. Lastly, Figure three d includes all synthetic forcings. Note that the maximal value of the forcing is much larger for Figure three d, where we compare the best choices for the magnitude of each synthetic forcing; this is also the setting for the illustrations presented in Sections four point three and four point four.

Alpha star equals negative zero point eight three five. (d) Comparing alpha star for all forcings.

The choice alpha star, namely the one that cancels the second order response rho two, performs quite well for the Feynman-Kac and divergence-free forcings, as seen in Figures three a and three c. It allows to extend the range of linearity for eta greater than one, an increase of over tenfold when compared to the original response curve for alpha equals zero. This allows for a variance reduction of a factor of order one thousand for the estimator (two point thirty-eight), as documented in Section four point five.

Figure three b illustrates the discussion of Section three point three about choosing the values of alpha allowing to stay longer in an approximate linear response. Although the value of the parameter alpha such that rho two of alpha equals zero is alpha star equals one point zero for the modified fluctuation-dissipation, we see that alpha star of zero point zero five equals zero point six three nine is a much more nicely behaved curve, staying within five percent


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

relative error for a large eta regime. This is a consequence of the fact that although alpha star cancels rho two, it might significantly increase rho three and higher order terms.

Four point three. Overdamped Langevin dynamics - two-dimensional case. We now present the numerical results for overdamped Langevin dynamics in dimension two, defined on script capital X equals mathbb T squared, with the following periodic potential energy:

V of q equals one half cosine of two pi q one plus cosine of two pi q two plus kappa cosine of two pi of q one minus q two, with kappa in mathbb R. The observable considered here is of the same form as (four point five), and reads

R of q equals a cosine of two pi q one plus b sine of two pi q one, times e to the power of beta V of q. For observables of this form, expressions (four point six) and (four point seven) can be generalized to higher dimensions to compute the normalization constants. As in Section four point two, this ensures that rho one equals rho two equals one when kappa equals zero. When kappa is nonzero but not too large, rho one and rho two are of order one, which is convenient to observe deviations from the linear regime.

For all numerical results presented here, we considered kappa equals zero point three and a constant nongradient forcing F equals one comma zero in mathbb R squared. The spatial domain mathbb T squared equals zero comma one squared was discretized using a regular product mesh of m q equals two hundred points per dimension.

presented in Figure four c.

the results are qualitatively similar to those from Section four point two, apart from two main differences. First, we present a divergence-free vector field of the form gradient V transpose A gradient, with A the symplectic matrix given by (three point eleven), which has an underwhelming impact on increasing the linear regime as seen in Figure four d, even for alpha star of zero point zero five equals two point zero. It seems therefore not to be a good option to consider. Second, Figure four e shows that the Feynman-Kac forcing performs better than the exponential divergence-free field. On the other hand, the modified fluctuation-dissipation (three point eight) is once again underwhelming, as seen in Figure four b, with response curve for alpha star of zero point zero five equals zero point five nine once again performing better than alpha star equals one point three zero one. Note that the value alpha star of epsilon was not computed for the Feynman-Kac and the exponential divergence-free forcings, as alpha star sufficiently extends the regime of linear response for those cases.

Four point four. Langevin dynamics - one-dimensional case. We present here the numerical results associated with the one-dimensional Langevin dynamics, where the potential energy function is the same as the one used for the one-dimensional overdamped Langevin dynamics case, namely, and the same observable as in Section Four point two. The normalization constants A and B for rho sub one and rho sub two are chosen to be with Z the same normalization constant as in Section Four point two. The spatial domain T equals zero to one was discretized using m q equals two hundred points, with uniform step size h q equals one divided by m q. The unbounded momentum space was truncated to negative P max, P max with P max equals

EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

Six point zero, with Dirichlet boundary conditions at P equals plus or minus p sub max, and then discretized into m sub p equals one thousand points with uniform step size h sub p equals two P max divided by m sub p minus one. The simulations were performed with Beta equals gamma equals M equals one. Note that when computing the response associated with the divergence-free vector field for large values of eta, as presented in Figure five e, the momentum space is truncated to

P sub max equals ten. The results presented in Figure five correspond to the response curves for each of the synthetic forcings discussed in Section three point two point three. Figures five a and five b correspond to the position and momentum components of the modified fluctuation-dissipation forcing presented in Example three point five, respectively, namely modified curly L sub extra equals negative partial sub q star partial sub q, comma modified curly L sub extra equals negative partial sub p star partial sub p. Figures five c and five d correspond to the position and momentum components of the Feynman-Kac forcing presented in Example three point six, respectively, namely modified curly L sub extra equals partial sub a star equals V prime minus partial sub q, comma modified curly L sub extra equals partial sub p star equals p minus partial sub p. Lastly, Figure five e corresponds to the divergence-free forcing.

For both modified fluctuation-dissipation forcings, Figures five a and five b, we see that alpha star does not preserve linearity for a large eta regime, suggesting instead that alpha sub star of epsilon is the better choice for practical applications; the same conclusion was drawn for the modified fluctuation-dissipation forcing for overdamped Langevin in Section four point two. Among the two forcings, it seems better to modify the fluctuation-dissipation in P as the response remains longer in the linear response regime for the optimal value alpha sub star of epsilon. Both Feynman-Kac forcings showcase great potential in extending the linear regime. Once again, Figures five d and five f suggest that opting for the extra forcing in the P variable is the superior choice.

Lastly, the divergence-free forcing greatly increases the linear regime, as seen in Figures five e and five f. This behavior, as well as the ease to implement it in Monte Carlo simulations, make it is the most appealing choice of forcing, allowing to substantially reduce the variance of the estimator, as discussed in Section four point five. Although the Feynman-Kac extra forcing also demonstrates great potential in extending the linear regime, the challenges associated with its implementation render it an impractical choice.

Four point five. Scaling of the variance. We discuss in this section the scaling of the variance sigma sub R comma eta squared divided by eta squared, with the addition of synthetic forces, and in particular numerically illustrate the potential of synthetic forcings as a tool for variance reduction. See Appendix B for details on the numerical computation of. We emphasize that the bias on the estimator, made precise, is negligible when compared to the variance, hence we concentrate on the variance. We anyway want to remain in the linear response regime so, by construction, the bias should be small.

Recall from Section two point three, and in particular in Proposition two point four, that the estimator P-hat sub eta comma t defined in two point three eight has asymptotic variance of order sigma sub R comma eta squared over eta squared. Indeed, two point four two suggests that this asymptotic variance is of the same order as the one associated with the equilibrium estimator, i.e. sigma sub R comma zero squared over eta squared, up to a small bias of order eta: four point nine.

This suggests that the asymptotic variance sigma sub R comma eta squared has sufficiently small variations in n, which validates increasing eta as a way to substantially reduce the variance.

For each synthetic forcing and a fixed value of alpha, we compute sigma sub R comma eta squared over eta squared with


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

na defined in three point one five, i.e. the first value of n at which the response curve departs and in relative error relative to the linear response. For the results here presented, we use epsilon equals zero point zero five. For each of the dynamics, the scaled asymptotic variance as a function of n is illustrated in Figure six, where the values of na epsilon are represented as dashed vertical lines to highlight the great reduction in variance potential. As expected, Figure six is consistent with four point nine, and it shows that increasing the regime of linear response has a dramatic effect on the variance.

In order to quantify the variance reduction, we define the gain as the ratio of the variance of the equilibrium system and its synthetic counterpart:

gain equals no epsilon squared O R, no epsilon squared.

na epsilon squared O R, na epsilon.

four point ten.

For each of the cases presented in Table one, namely the modified-fluctuation dissipation, Feynman-Kac forcing and divergence-free vector field, a is chosen to be a* or a+ epsilon, and the associated quantity na epsilon is computed, where no epsilon equals zero point zero five for all three dynamics. Note that for Langevin dynamics, the results here presented for the modified fluctuation-dissipation and the Feynman-Kac forcing both correspond to their p counterparts.

The results in Table one show that the variance can be dramatically reduced with the use of synthetic forcings. Although no choice of extra forcing is universally better, we can achieve reduce the variance by a factor of over one thousand in all cases.

Five. Extensions and perspectives. Let us conclude this work by discussing potential extensions of our approach and practical applications to real molecular dynamics systems. The notion of synthetic forcings, as here presented, can be applied to a number of actual systems to assist in the computation of transport coefficients, e.g. Lennard-Jones fluids for the computation of shear viscosity, or systems of atom chains for the computation of thermal transport.

The methodology here presented, however, must undergo some adaptation to be applied to actual systems. The numerical method we rely on, namely discretizing and solving the associated PDEs, does not scale well to higher dimensions and thus cannot be used as such. One typically relies on Monte Carlo simulations, which normally limits the number of values of n used due to the high computational cost. Additionally, the computation of the optimal values of o, presented in Section three point three, also cannot be done as such, as it relies on either the PDE approach, or the computation of full response curves.

One preliminary idea for the computation of o in real systems is the notion of prescreening. Transport coefficients are intensive quantities, i.e. they do not depend too drastically on the system size. This suggests, in practice, that one performs two simulations with small system sizes, with o one, from which the value of a* can be extrapolated, which can then be used in a large scale simulation. The results here presented suggest that such an adaptation, which is work in progress, is worth the effort.

Quantifying the magnitude of An,Q. For a general perturbed dynamics, we write the generator Ln,a as Ln,a equals Lo plus n times L sub phys plus alpha times L sub extra, with L sub extra equals L sub V star for


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

Feynman-Kac forcings. The associated Fokker-Planck equation is then

A point one.

left parenthesis script L sub zero plus eta tilde script L sub phys plus alpha eta tilde script L sub extra right parenthesis dagger psi sub eta comma alpha equals lambda sub eta comma alpha psi sub eta comma alpha. For a fixed value alpha, formally expanding psi sub eta comma alpha and lambda sub eta comma alpha in powers of eta yields

A point two.

psi sub eta equals psi sub zero plus eta bar psi sub one plus eta squared bar psi sub two comma alpha plus ellipsis , quad lambda sub eta comma alpha equals eta bar lambda sub one comma alpha plus eta squared bar lambda sub two comma alpha plus ellipsis. Note that bar psi sub one has no alpha dependency, since the addition of alpha tilde script L sub extra leaves script f sub one invariant due to three point two, as discussed in Section three point one.

We substitute the expansions A point two in the Fokker-Planck equation A point one. Identifying terms with the same orders

A point three.

I N led to O of eta: script capital L zero dagger bar psi one plus (tilde script capital L phys dagger plus alpha tilde script capital L extra dagger) psi zero minus bar lambda one comma alpha psi zero equals zero, O of eta squared: script capital L zero dagger bar psi two comma alpha plus (tilde script capital L phys dagger plus alpha tilde script capital L extra dagger) bar psi one minus bar lambda one comma alpha bar psi one minus bar lambda two comma alpha psi zero equals zero. From the O of eta expression, an integration leads to

A point four bar lambda one comma alpha integral over script capital X psi zero equals integral over script capital X script capital L zero dagger bar psi one plus integral over script capital X tilde script capital L phys dagger psi zero plus alpha integral over script capital X tilde script capital L extra dagger psi zero. From the definition of the L two-adjoint, it follows that the first two terms on the right-hand side of A point four are zero, since dot script capital L zero one equals tilde script capital L phys one equals zero. The remaining term can be written as integral over script capital X tilde script capital L extra dagger psi zero equals integral over script capital X (tilde script capital L extra one) psi zero equals integral over script capital X (xi superscript T nabla star one) psi zero equals integral over script capital X xi superscript T nabla one psi zero equals zero. Thus, we conclude that bar lambda one comma alpha equals zero. Similarly, integrating A point three on X led to A point five bar lambda two comma alpha equals alpha integral over script capital X tilde script capital L extra dagger bar psi one equals alpha integral over script capital X (tilde script capital L extra one) bar psi one, which is generally a nonzero quantity. This suggests that

Lambda sub eta comma alpha equals alpha eta squared integral over script X of the quantity tilde script L sub extra one end quantity bar psi sub one plus the quantity O of eta cubed end quantity. Reformulating the Poisson equation. Computing the optimal value alpha star defined in expression three point thirteen requires computing the second-order response, as discussed in Section three point three. In particular, this is done by using the recursive expression two point twenty-five, obtained from the Fokker-Planck equation via formal asymptotics. We reformulate expression two point twenty-five for Feynman-Kac systems to compute the second-order response, using that, in view of expression A point three,

Bar psi sub two comma alpha equals quantity negative script L sub zero inverse end quantity dagger of quantity tilde script L sub phys dagger plus alpha tilde script L sub extra dagger end quantity bar psi sub one minus bar lambda sub two comma alpha psi sub zero end quantity, where the value of bar lambda sub two comma alpha is determined by expression A point five. This procedure could be extended to arbitrary orders by identifying terms with the same orders in eta in expression A point one.

the density of the invariant probability measure for the systems at hand, namely over-damped Langevin dynamics in one and two dimensions, and Langevin dynamics in one dimension. This approach can be straightforwardly extended to solving Poisson equations with nontrivial right-hand sides such as expressions two point twenty-three or the integrand in the asymptotic variance two point forty-three. We start each section by first discussing the discretizations associated with the equilibrium dynamics, after which we mention the modification needed when adding perturbations.

For all systems, the spatial domain, namely the torus Td equals open bracket zero comma one close bracket d, is discretized into ma points with uniform step size hq equals one over mq in each direction. While Vn denotes the invariant measure at the continuous level, we use th to denote its discretized counterpart, namely the approximations of the values of Un at the grid points.

B point one. Overdamped Langevin dynamics. For a continuous function u: T maps to R, we denote by open bracket u close bracket i equals u of Qi, where Qi equals ihq are the mesh points. Similarly, for a continuous function u: T superscript two maps to R, we denote by open bracket u close bracket i comma j equals u of Qi comma j, where Qi comma j equals open bracket ihq comma jhq close bracket are the mesh points. The Fokker-Planck equation to discretize for the overdamped Langevin dynamics expression two point eleven reads

(B point one) open bracket percent equals div open bracket V over zero close bracket plus equals AV zero equals VTV one over zero plus AV forty zero plus negative A forty zero.

Using centered finite differences, the discretization of expression B point one in dimension one is given by prime open bracket b close bracket i plus one minus open bracket four close bracket i minus one over two hq plus open bracket V prime close bracket i open bracket To close bracket i plus open bracket b close bracket i plus one minus two open bracket b close bracket i plus open bracket b close bracket i minus one q equals zero.

(B point two)

Periodic boundary conditions are imposed, i.e. open bracket b close bracket zero equals open bracket forty close bracket ma. In two dimensions, applying centered finite differences to the Fokker-Planck B point one yields open bracket Og one V close bracket i comma j open bracket four close bracket i plus one close bracket minus open bracket V close bracket i minus one close bracket over two hg plus open bracket zero q two V close bracket i comma j open bracket V close bracket i comma j plus one minus open bracket V close bracket i comma j minus close bracket plus open bracket AV close bracket i comma j over two hg plus open bracket zero close bracket i plus one close bracket plus open bracket V close bracket i minus one comma five minus four open bracket close bracket comma plus open bracket one close bracket comma plus close bracket minus close bracket close bracket.

Periodic boundary conditions are imposed, i.e. open bracket V close bracket zero comma colon equals open bracket V close bracket mq semicolon and open bracket close bracket comma zero equals open bracket four close bracket comma mg.

Discretization of perturbations. We now consider several classes of perturbation operators. One typical form is L equals FTV, with F equals open bracket F one comma F two close bracket belongs to R superscript two for two-dimensional dynamics. Its L two-adjoint acts as

(B point three) Etyo equals negative div open bracket F close bracket vo minus FT Vyo.

Perturbations of this form include the physical perturbations Lphys considered throughout this work, divergence-free vector fields three point five, and the differential term in the Feynman-Kac forcing three point nine. In dimension one, the right-hand side of B point three is discretized with a centered finite difference as negative open bracket F close bracket open bracket V close bracket minus open bracket F close bracket open bracket b close bracket i plus one minus open bracket b close bracket i minus one over two hg.


## EXTENDING LINEAR RESPONSE WITH SYNTHETIC FORCINGS

In dimension two, perturbations of the form B point three are discretized with centered finite differences as zero open bracket four close bracket i comma j plus one minus open bracket V close bracket j minus one end parenthesis over two hg zero open bracket V close bracket i plus one comma one minus open bracket V close bracket i minus one close bracket plus open bracket two close bracket minus open bracket F close bracket i comma j two hq

Another example is the modified fluctuation-dissipation perturbation three point eight, preceded by a factor on as presented in this work. Since it corresponds to the generator two point twelve of the dynamics at hand, its discretization corresponds in any dimension to rescaling the discretized Fokker-Planck by open bracket one plus an close bracket.

We also consider zero-order operators, such as the source term for the Feynman-Kac forcing three point nine, namely TVV. As terms of this form include no differential operators acting on yo, their discretization is trivially done, in any dimension, by direct evaluation, e.g. open bracket V close bracket open bracket V close bracket in dimension one.

B point two. Langevin one D. For the one-dimensional Langevin dynamics, we discretize the unbounded momentum space as follows: we first truncate it to open bracket negative P max comma P max close bracket, then discretize it into mp interior points with uniform step size hp equals two P max over mp minus one. For a continuous function u: T cross R maps to R, we denote by open bracket u close bracket i comma j equals u of Qi comma Pj, where Qi equals ihq and Pj equals jhp are the mesh points.

The numerical scheme for the Fokker-Planck equation two point seventeen for Langevin dynamics is obtained with centered finite differences, except for the transport term pr M inverse Vqyo, where an upwind scheme is used. In dimension one, expression two point seventeen reads

(B point four) Lov equals negative Cham v plus Y M inverse plus M inverse pap four plus B inverse zero two four.


## The discretization of B point four then reads

P plus V plus P plus dVoli M

plus yPj bi,j plus one minus bi,j minus one V; Vi, j plus one minus V,j minus one two hp M minus two hp M equals zero, zero plus MẸ Y four, i plus one minus two four plus four, j minus h two plus where p plus equals max p, zero,

p equals min p, zero,

h zero bi,j minus bi minus one,j hq minus h a

Periodic boundary conditions are imposed on the positions, i.e. four equals Vmq; for any one less than or equal to j less than or equal to mp.

Discretization of perturbations. For Langevin dynamics, perturbations of the form B point three can correspond to differential operators acting on the positions or momenta, i.e. FTVq and FTVp. In dimension one, these options reduce to negative Fogo and negative FOpyo, both of which are trivially discretized with centered finite differences.

For the modified fluctuation-dissipation in p, its discretization corresponds to scaling the LFD term in two point sixteen by y plus an. For its position counterpart negative eight negative one q its discretization corresponds to adding B point two, scaled by on.

Upwind scheme for Langevin. We now motivate the upwinding used to discretize the transport term P T M negative one nabla q in the Fokker-Planck equation two point seventeen. In particular, the use of a centered finite difference with an even number of points m q in the spatial domain would lead to independent submeshes, and hence might give incorrect results, an issue known as odd-even decoupling. To overcome this, one resorts to decentered finite differences, in particular upwinding.

Recall that equation two point three can be seen as the stationary solution to the evolution PDE partial t psi equals L dagger psi. To implement the upwinding scheme, we write the transport term in the Fokker-Planck in the form of the advection equation, that is partial t psi plus P T M negative one nabla q psi equals zero. The scheme used to discretize the components of nabla q psi depends on the sign of the components of p. The partial derivative is discretized with a scheme decentered on the left when P is greater than or equal to zero, and decentered on the right when P is less than or equal to zero. The discretization of p partial q psi in dimension one at a mesh point Q i, P j is therefore done as follows:

p fraction numerator left bracket Psi zero h right bracket i plus one, j minus left bracket Psi zero h right bracket i, j over h q denominator, and p less than zero, p fraction numerator left bracket Psi zero h right bracket i, j minus left bracket Psi zero h right bracket i minus one, j over h a denominator, and p greater than zero. Acknowledgments. This project has received funding from the European Union's Horizon twenty twenty research and innovation program under the Marie Sklodowska- Curie grant agreement number nine four five three three two, and from the European Research Council under the European Union's Horizon twenty twenty research and innovation programme project EMC two, grant agreement number eight one zero three six seven. We also acknowledge funding from the Agence Nationale de la Recherche, under grants A.N.R. one nine C E four zero zero zero one zero zero one QuAMProcs and A.N.R. two one C E four zero zero zero zero six SINEQ.