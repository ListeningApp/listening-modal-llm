## Coarse-graining in time with the Functional Renormalisation Group: Relaxation in Brownian Motion

We apply the functional Renormalisation Group to study relaxation in a stochastic process governed by an overdamped Langevin equation with one degree of freedom, exploiting the connection with supersymmetric quantum mechanics in imaginary time. After reviewing the functional integral formulation of the system and its underlying symmetries, including the resulting Ward- Takahashi identities for arbitrary initial conditions, we compute the effective action I from the fRG, approximated in terms of the leading and subleading terms in the gradient expansion: the Local Potential Approximation and Wavefunction Renormalisation respectively. This is achieved by coarse-graining the thermal fluctuations in time resulting in e.g. an effective potential incorporating fluctuations at all timescales. We then use the resulting effective equations of motion to describe the decay of the covariance, and the relaxation of the average position and variance towards their equilibrium values at different temperatures. We use as examples a simple polynomial potential, an unequal Lennard-Jones type potential and a more complex potential with multiple trapping wells and barriers. We find that these are all handled well, with the accuracy of the approximations improving as the relaxation's spectral representation shifts to lower eigenvalues, in line with expectations about the validity of the gradient expansion. The spectral representation's range also correlates with temperature, leading to the conclusion that the gradient expansion works better for higher temperatures than lower ones. This work demonstrates the ability of the fRG to expedite the computation of statistical objects in otherwise long-timescale simulations, acting as a first step to more complicated systems.


## I. INTRODUCTION

Stochastic processes appear in all kinds of contexts in physics: from the Brownian motion of small particles in a thermal bath to exotic scalar fields experiencing quantum fluctuations in the early inflationary universe, many problems of interest can be described by the overdamped Langevin equation. In this work we employ an effective description of the stochastic dynamics that captures the aggregate effect of fluctuations embodied in an effective action I[x(t)], a functional of the average position x(t) = which can be thought of as an analogue to the statistical free energy and can be derived from the partition function or generating functional via a Legendre transform. Once obtained, the effective action can be used to compute n-point correlation functions of the particle's position, characterizing the system's statistical properties. To obtain this effective action we will be coarse-graining the system in time such that we obtain e.g. an effective potential that incorporates thermal fluctuations on all timescales. To achieve this we will use a technique known as the functional, or exact, or non-perturbative Renormalisation Group - see for a review and an entry point to the literature on the subject, for a comprehensive overview of applications as well as e.g. for more elementary introductions.

The renormalisation group was brought to full force through the work of K. Wilson who used it to understand phase transitions and since then the RG has become a widely used technique in modern physics with many applications in both particle physics and condensed matter physics. The RG is relevant whenever fluctuations significantly influence the state (static or dynamical) of a physical system. A recent popular incarnation of this programme is the functional RG formulation. Wetterich showed - see also - how one can define I' at some particular energy or momentum scale A in the UV (for us this will correspond to small timestep/high frequency) where the theory is known and then create an RG flow that interpolates through all energy (frequency/momentum) scales down to the IR (i.e. decreasing fluctuation frequency/increasing characteristic timestep of fluctuation here). This change of the effective theory at different scales, the fundamental idea behind the RG, can be formulated in an integro-differential equation known as the Wetterich equation:

One where Ik is the effective action at scale K, T R denotes a trace over spatio-temporal points (an integral over space-time) and a trace over all other relevant indices, Rk is an IR regulator that acts as a cut-off for fluctuations below (momentum/frequency) scale K, and I two is the second functional derivative of Ik. A simple zero-dimensional manifestation of this flow equation in the context of the Boltzmann equilibrium distribution is illuminating and is reviewed in Appendix A. At the end of the flow, as K goes to zero, all fluctuations are included and the full effective action T is obtained.

In this work we solve equation one in the context of the dynamics of particles under the influence of a deterministic force, stemming from an arbitrary potential, and thermal fluctuations. We will study a simple polynomial potential, a double Lennard-Jones potential, as well as one containing multiple barriers/trapping wells, serving as a toy model of an energy landscape on which particles can diffuse. To solve one we employ a widely used approximation scheme, the gradient expansion, to second order. We find good agreement with simulations (and the Fokker-Planck equation where it proved amenable to a numerical solution) at moderate to high temperatures and that this correlates with the spectral representation of the relaxation process, i.e. the overlap between the initial condition (a delta function initial probability distribution) and the spectrum of the Fokker Planck operator. In particular, the more the resulting spectrum is shifted towards lower-lying eigenvalues, the better the gradient expansion agrees with the exact evolution. This is in line with expectations about the validity of the gradient expansion, namely that it better captures slower evolution which should be associated with the lower eigenvalues. Furthermore, we expect that for a fixed initial condition lower temperatures correspond to a spectrum shifted towards higher eigenvalues and, correspondingly, worst performance of the gradient expansion.

We start in Section Two by reviewing the connection between Langevin dynamics and Supersymmetric Quantum Mechanics in imaginary time, first shown in - see e.g. for a review of this connection. The path integral formulation then allows us to apply the fRG program directly. We include a brief summary of how the Langevin equation can be reformulated in terms of a probability distribution function whose evolution is described by the Fokker-Planck equation and how the latter relates to a Euclidean Schrödinger equation. We close the section by discussing the symmetries of the resulting theory and their implications through Ward-Takahashi type relations, paying attention to the fact that the initial state may not be that of equilibrium.

In Section Three we present the flow equations for the effective action utilising a slight modification of the results of for supersymmetric RG flows. As we explain, the flow equation derived from the supersymmetric formulation ensures compatibility with the equilibrium Boltzmann distribution, a feature not directly obvious from the application of the renormalisation group to the

Onsager-Machlup form of the generating functional. To turn the functional integro-differential equation one into a mathematically more tractable form we employ two commonly used approximations for the effective action Tk: the Local Potential Approximation (LPA) as well as the LPA augmented by Wavefunction Renormalisation (WFR). In the LPA, the effect of fluctuations is progressively taken into account during the flow by the effective potential Vk (x) experienced by the particle, which is altered compared to the bare, fundamental potential V (x). Wavefunction Renormalisation (WFR) involves a second function Zk(x) which can be interpreted as a redefinition of position x to Z(x). These are also known as the first two (leading and subleading) orders in a gradient expansion of T.

In Section Four we derive the effective equations of motion (EEOM) through variational derivatives of the effective action T. We do this first for the one point function, or average position x, whose equation of motion simply reduces to an over-damped equation in an effective potential with no noise i.e. purely classical. We then obtain an equation for the evolution of the two point function; this Green's function equation allows us to solve for the Variance and Covariance of the stochastic process. Solutions to these deterministic equations with appropriate initial conditions can then approximate the relaxation towards equilibrium.

In Section Five we present numerical solutions to the flow equations for three types of potential: a simple polynomial one, an unequal LJ type potential and a "rugged" potential consisting of an underlying harmonic x squared potential with the addition of six Gaussian bumps and dips. We also consider different temperatures, effectively controlling the strength of thermal fluctuations compared to the classical force. Naturally, we find that the end results of the flow equations differ, with higher temperatures resulting in potentials that carry less memory of the bare potentials' morphology. In section Six the numerical solution of the LPA flow equation accurately reproduces static equilibrium quantities, as it should. We also examine the characteristic decay behaviour of the connected two-point function (x(0)x(t)) or covariance at equilibrium by utilizing both the effective potential Vk->0 and the WFR function Zk-10 and find good agreement with exact results down to relatively low temperatures when deviations start becoming pronounced.

In Section Seven we examine how well the LPA plus WFR approximation to the effective action can handle relaxation towards equilibrium in our potentials starting from a fixed initial condition (Pini (x) equals eight(x minus Xini)). Numerical solutions to the EEOM for the one- and two-point functions are compared to direct numerical simulation of equation four and/or numerical solutions to the Fokker Planck equation. We find that under the LPA plus WFR approximations, the fRG solutions give a good description of the relaxational evolution and are able to capture overshoots of the variance in the potentials we examine. Similarly to equilibrium, the approximations fare worse as the temperature is decreased and the classical force determined by the potential's slope becomes dominant. We suggest that this behaviour is correlated to the spectral decomposition of the relaxation in terms of eigenvalues of the relevant Fokker-Planck operator: the more the spectral decomposition of Langevin, Langevin x (t) equals, Langevin x (t sub ini) x (t) equals and Langevin x squared (t) equals is shifted towards lower eigenvalues, the better the LPA plus WFR approximation performs.

We conclude in Section Eight. Appendix A derives the zero-dimensional analogue of the Wetterich equation one for the effective potential corresponding to the equilibrium Boltzmann distribution while in Appendix B we include a derivation of the solution of one hundred thirteen that provides the two-point function. In Appendix C we explicitly show that the determinant appearing in the path integral directly follows from the boundary conditions imposed in two point A.


## Two. Brownian Motion as Supersymmetric Quantum Mechanics

This section reviews Brownian motion and its path integral formulation in terms of the action functional of Supersymmetric Quantum Mechanics. In the next section we will exploit this link to derive the RG flow equations.

Brownian motion for a single particle of mass M moving in a potential V bar (x), coupled to an external heat bath with temperature T can be described by the Langevin equation:

M d squared x plus gamma dot x equals negative m partial sub x V (x) plus f (t)

Langevin f (t) f (t prime) equals two D gamma squared delta (t minus t prime)

where gamma is a frictional coefficient, f (t) is a Gaussian "noise" term and V (x) is the potential in which the particle moves. D equals k sub b T divided by gamma is the diffusion constant, given so as to match the Boltzmann equilibrium distribution (should an equilibrium state exist). Hereafter, we will be concerned with the overdamped limit:

dot x equals negative epsilon partial sub x V (x) plus eta (t) Langevin eta (t) eta (t prime) equals two D delta (t minus t prime)

to which the system settles over a timescale epsilon equals m divided by gamma which we assume to be short. Note that the overdamped equations are a consistent approximation to the full dynamics as long as epsilon squared V double prime much less than one. We will be examining the impact of changing the temperature, and hence changing the strength of the fluctuating force n, on the coarse-grained effective theory. Let us therefore introduce a reference temperature T sub zero and a dimensionless parameter Upsilon which allows us to dial the temperature around T sub zero. Writing D equals D sub zero Upsilon we further define dimensionless variables

X equals square root of two D sub zero epsilon widehat X, quad T equals epsilon widehat T. Six.

V of X equals two D sub zero over epsilon widehat V of widehat X, quad eta of T equals square root of two D sub zero over epsilon widehat eta of widehat T. Seven.

in terms of which the dynamical equation becomes

D widehat X over D widehat T equals negative partial widehat V over partial widehat X plus widehat eta of widehat T. Eight.

Expected value of widehat eta of widehat T widehat eta of widehat T prime equals Upsilon delta of widehat T minus widehat T prime. Nine.

From here onwards we will be dropping the hats for simplicity of notation but generally refer to dimensionless quantities unless otherwise stated.


## A. The Brownian Motion Path Integral

In order to bring the tools of Quantum Field Theory to bear, we will need to reformulate the stochastic differential equation eight in terms of a path integral. In this subsection we will outline one known way to obtain this path integral, aiming to link this to Supersymmetric Quantum Mechanics. Our final expression, and the starting point of our subsequent analysis, is the Brownian Motion transition probability twenty-four, expressed in terms of an integral over possible histories weighted by the action twenty-five, to which the busy reader may progress if uninterested in the details of the derivation. We will be using a condensed functional notation of infinite dimensional functional integrals but all expressions can be considered as limits of finite, high dimensional ordinary integrals. This derivation is based on the path integral reformulation by De Dominicis, Peliti and Janssen of the well known Martin-Siggia-Rose approach for stochastic dynamics, first developed in. More details on these path integrals, including the corresponding finite discretisation of the stochastic process can be found in- see also for a pedagogical exposition.

The dynamics of the dimensionless Langevin equa- tion eight can be captured in terms of the Probability Distribution Function PDF script P of observing the particle X sub F T equals T sub F given that initially, at T equals T sub I, the particle was at X sub I. By definition this can be expressed as:

script P of X sub F given X sub I equals expected value of delta of X of T sub F minus X sub F. Ten.

where the expectation value is taken over all possible realisations of the noise eta of T and delta of X of T sub F minus X sub F is the Dirac delta function. Put another way, X of T sub F is the position at T sub F for a given noise history eta of T and the brackets indicate averaging over all possible noise histories, or stochastic paths, which start at X sub I and end up at X of T sub F equals X sub F at T sub F. To express this in a path integral form, we can rewrite the PDF using a Gaussian measure for the nois e five and express the average as script P of X sub F given X sub I equals integral script D eta of T delta of X of T sub F minus X sub F exp open bracket negative integral D T eta squared of T over two Upsilon close bracket. Eleven.

where each noise history is weighted by the exponential factor in the above expression. We now consider the identity

One equals the integral DX sub f the integral from x sub i to x sub f D x of t delta of x of t minus x sub eta of t equals the integral DX sub f the integral from x sub i to x sub f D x of t delta of x dot plus V sub x minus eta of t d e t M.

Equals the integral from x sub j D x of t delta of x dot plus V sub x minus eta of t det M.

where the matrix M of t, t prime is:

M is equivalent to the partial derivative of x dot plus V sub x minus eta of t with respect to x of t prime equals the partial derivative with respect to t plus V sub x x delta of t minus t prime. This identity expresses the obvious fact that, if the particle starts at some x sub i and follows a particular history x sub eta of t dictated by the Langevin equation without disappearing, it will end up somewhere after time t sub f. We have used the standard subscript notation to denote derivative with respect to that variable e.g. V sub x x equals the partial derivative of V with respect to x x. Note that the path integral in equation thirteen is over all paths starting at x sub i at t sub i and ending at y x at t sub f. Inserting this 'fat unity' factor equation thirteen into equation eleven and noting that the delta function there restricts x of t sub f to be x sub f we obtain:

P of x sub f given x sub i equals the integral from x of t sub i equals x sub i to x of t sub f equals x sub f D eta D x delta of x dot plus V sub x minus eta det M times the exponential of the negative integral d t of eta squared of t divided by two upsilon.

where the D x of t integral is taken over all paths beginning at x sub i and ending at x sub f. We can rewrite the delta function as a functional Fourier transform using a new variable x tilde which is usually called the response field:

Delta of x dot plus V sub x minus eta equals the integral D x tilde exponential of i the integral d t x tilde of x dot plus V sub x minus eta.

There are a couple of standard ways we can incorporate det M into an exponential. We can formally write

M equals the partial derivative with respect to t times one plus the inverse partial derivative with respect to t V sub x x is equivalent to the partial derivative with respect to t M tilde.

where

The inverse partial derivative with respect to t of t, t prime equals lambda theta of t minus t prime minus one minus lambda theta of t prime minus t.

Imposing retarded causal boundary conditions, which are appropriate for the problem at hand, requires that we set lambda equals one and we find

Det M equals det of the partial derivative with respect to t times det M tilde proportional to the exponential of Tr log of M tilde proportional to the exponential of one half the integral d t V sub x x.

where we used the Stratonovich prescription theta of zero equals one half. Alternatively, and to make the link with supersymmetry, we can use anticommuting Grassmann variables C and C bar such that:

The determinant of M equals the integral of script capital D C times script capital D bar C times the exponential of the integral of d t bar C left parenthesis partial t plus V comma x x right parenthesis C. (twenty)

The determination of the determinant of M then requires appropriate boundary conditions for bar C and C, which are

C left parenthesis t subscript in right parenthesis equals zero, comma bar C left parenthesis t subscript f right parenthesis equals zero. (twenty-one)

Other choices are possible but lead to determinant values that are different from, corresponding to non-causal boundary conditions for the stochastic problem. The boundary condition is implied by the discretised form of the path integral. Its appropriateness is verified by direct computation in Appendix C. The discretised path integral can also be consulted to infer that we must further impose tilde x left parenthesis t subscript f right parenthesis equals zero. (twenty-two)

Although introducing C and bar C is not strictly necessary, it pays to keep the determinant expressed in this form since, as we see below, it allows us to conveniently express hidden symmetries of the resulting action. Inserting equations sixteen and twenty into fifteen we obtain:

(twenty-three)

script capital P left parenthesis x subscript f vertical bar x subscript i right parenthesis equals the integral of script capital D eta script capital D x script capital D tilde x script capital D C script capital D bar C the exponential of the integral of d t left brace negative the fraction eta squared over two upsilon plus i tilde x left parenthesis dot x plus V comma x minus eta right parenthesis right brace right brace bar C left parenthesis partial t plus V comma x x right parenthesis C right brace. We can now trivially perform the gaussian integral over eta to obtain the path integral in terms of the Brownian Motion action script capital S subscript BM left parenthesis x, tilde x, bar C, C right parenthesis colon script capital P left parenthesis x subscript f vertical bar x subscript i right parenthesis equals the integral of script capital D x script capital D tilde x script capital D C script capital D bar C the exponential of negative script capital S subscript BM left parenthesis x, tilde x, bar C, C right parenthesis script capital S subscript BM left parenthesis x, tilde x, bar C, C right parenthesis equals the integral of d t left brace the fraction upsilon over two tilde x squared minus i tilde x left parenthesis dot x plus V, x right parenthesis right brace. (twenty-four)

left brace minus bar C left parenthesis partial t plus V, x x right parenthesis C right brace. (twenty-five)

Computing this path integral, which henceforth shall be called the Brownian Path Integral, without resorting to some approximation is in general impossible analytically. Instead, we will be using numerical solutions to the FRG flow equations to compute it in the L P A plus WFR approximations.


## Redefining our fields as:

x(t) equals Vr six(t) V(x) equals TW(y)

õ equals Vr one (phi-F) čc equals ipp

(twenty-six)

S subscript BM[y, F, p,p] equals left bracket W(Pf) minus W(Pi) right bracket plus S subscript susY (twenty-seven) where

S subscript susY [p, È, p, p] equals the integral of d t sixty-two plus F two plus iFW, left brace six (six) minus i p left parenthesis O t plus W, forty-four ( y) right parenthesis p. (twenty-eight)

Action twenty-eight describes the dynamics of Euclidean, or imaginary time, Supersymmetric Quantum Mechanics where p and p are the fermionic fields and y and F are the bosonic fields. The same action also describes Brownian motion and the BM action is equivalent to the SUSY QM one up to a factor depending on the initial and final positions xi and xf; these terms can be simply taken outside the path integral as an exponential prefactor.

Variation of S subscript susY with respect to F yields its "equation of motion" F equals negative iW, which when substituted back into S subscript susY yields the "on mass-shell" action

S O M (comma P, P) equals the integral of d t two sixty-two plus left brace W,. two minus i p left parenthesis O t plus W, p p right parenthesis p

(twenty-nine)

We will keep working with the auxiliary field F and twenty-eight as it allows for the symmetry transformations to take on a simpler form, linear in all fields.

It is illuminating to express the above action in terms of the original dimensional variables and perform the integration over p and p, leading to the alternative form of the term stemming from the determinant:

S O M [x] equals the integral of d t two D m small a squared plus two m V, two minus D m E V, E T L. (thirty)

Note that two D m has the dimensions of action and therefore plays in the thermal problem a role analogous to h in quantum mechanics - see also section II B in this respect. Unlike h of course, it can be varied by changing the temperature, therefore controlling the strength of fluctuations.


## B. The Fokker-Planck equation and the spectral expansion

Before moving on to the FRG we outline the more standard procedure as to how the on-mass shell action thirty can be obtained from the Fokker-Planck equation which resembles a Euclidean Schrödinger equation. We will see later - in section VIID - that the spectral expansion method outlined here confirms the validity of the FRG approach at moderate to high temperatures.

Instead of working with the Langevin equation directly once can deal with the probability distribution of position:

P(x,t) equals (eight(x-In)) (thirty-one)

where In is the solution to four for a given noise function n (i.e. a specific particle trajectory). It can be shown that this evolves according to the following P D E:

@P(x,t) O t equals O z left parenthesis P(x, t) d z V right parenthesis plus two Op x squared P(x,t)

(32) which is known as the Fokker-Planck (F-P) equation. It is usually more useful however to rescale the PDF like so: P(x,t) = e-V/IP(x,t) (33) This leads to the F-P equation taking the form:

partial differential of P(x,t) with respect to t equals big upsilon divided by two partial squared differential of P(x,t) with respect to x squared plus big upsilon P(x,t)

(thirty-five)

which resembles a Euclidean Schrödinger equation with big upsilon over two playing the role of h in controlling the fluctuation amplitude, as one might expect.

Equation (thirty-four) can be solved in terms of a spectral expansion. Writing

P(x,t) equals the sum from n equals zero to infinity of c sub n P sub n of x e to the power of negative E sub n t

(thirty-six)

we find that P sub n satisfy the corresponding, time independent Euclidean Schrödinger equation one half V comma z squared big upsilon V comma x x P sub n equals E sub n P sub n

(thirty-seven)

The lowest eigenfunction with E zero equals zero is P sub zero of x equals Ne to the power of negative V of x over T

(thirty-eight) corresponding to the equilibrium distribution P_eq(x) equals P sub zero of x squared. The P sub n of x eigenfunctions are complete and orthonormal integral [dx p sub n of x P sub m of x equals delta sub m n

(thirty-nine)

greater than P sub n of x P sub n of x sub zero equals delta of x minus x sub zero for n equals one to infinity

(forty)

The conditional probability, a quantity akin to the evolution operator or propagator in quantum mechanics, can be expressed in terms of the spectral expansion as

P tilde of x comma t given x sub zero at time zero equals the sum from n equals zero to infinity of P sub n of x P sub n of x sub zero e to the power of negative E sub n t. P of x comma t given x sub zero at time zero equals e to the power of negative V of x over big upsilon P tilde of x comma t given x sub zero at time zero e to the power of positive V of x sub zero over big upsilon

Any correlation function can then be expressed by using this equation. An economic notation can be achieved by using Dirac bra-ket notation in terms of which for example

P tilde of t zero equals the sum from n equals zero to infinity of ket n e to the power of negative E sub n t bra n

Correlation functions can then be expressed in the spectral expansion as:

bra f of x of t ket g of x of zero bra state zero of f state n e to the power of negative E sub n t n state g state i n ket where, explicitly bra zero of f state n equals the integral from negative infinity to infinity of dx P sub zero of x f of x P sub n of x. Bra n of g ket i n equals the integral from negative infinity to infinity of dx P sub n of x g of x P tilde of x zero

Note that the "out state" in the stochastic problem is always bra zero and the "in state" is defined in terms of

P tilde of x t equals zero. We can also write the conditional probability

P of x t given x sub zero at time zero equals bra x of e to the power of negative V of x over big upsilon P tilde of t zero e to the power of positive V of x sub zero over big upsilon ket x sub zero governed by the above Euclidean Schrödinger equation, as a path integral

P of x t given x sub zero at time zero equals script N exp of epsilon over two D times the quantity V of x minus V of x sub zero times the integral from x at zero equals x sub zero to x at t equals x script D x of tau exp of negative integral d tau over two D m quantity one half m times partial differential of tau x squared minus U bar of x where we have reinstated the dimensionful variables. We therefore recover the "on mass-shell" path integral obtained earlier. Note the importance of including the determinant in order to obtain the partial squared differential of x x V term in the Schrödinger potential

U bar. Before proceeding to the next sections we should add a comment regarding the above path integrals. Beyond being expressions that allow formal manipulations, they can also be understood as limits of large multivariate integrals arising from the discretization of time evolution into small discrete time intervals. In general, this discretization results in apparent ambiguities. In our case this can also be linked to the discretization of the Langevin equation the index i refers to the i-th time interval x sub i equals x sub i minus one plus V prime of x sub i star delta t plus integral from t sub i minus one to t sub i of ds xi of s where X sub I star equals alpha X sub I plus left parenthesis one minus alpha right parenthesis X sub I minus one. In the above discussions and manipulations we have tacitly assumed alpha equals one half (Stratonovich) which, in the continuous limit is equivalent to setting Theta left parenthesis zero right parenthesis equals one half. It is well known however that, as long as the noise amplitude does not depend on X (known as additive noise), the solution to the Langevin equation is unique, as is the corresponding Fokker-Planck equation. Our path integrals respect this and all results derived from them are independent of the choice of alpha. Calculations with the discrete version, show that contributions from terms involving alpha cancel. For example, one can start from the discretized path integral with an arbitrary choice of alpha and obtain a unique Fokker-Planck equation. In the continuum formulation, the supersymmetry discussed in subsection two capital D below imposes the cancellation of terms where the ambiguous quantity Theta left parenthesis T equals zero right parenthesis appears. This is also reflected in the path integral forty-eight through the special form of the potential U left parenthesis X right parenthesis in terms of the "superpotential" V left parenthesis X right parenthesis. Overall, this non-dependence on alpha ultimately stems from the inclusion of the determinant detM in thirteen. These considerations support the view that the formal path integrals considered here are well defined and free from any ambiguity.


## C. Correlation functions from the generating functional

One way to compute correlation functions is through the use of objects called generating functionals. In this subsection we will outline how these generating functionals yield correlators in practice. We will then outline in section three how the f R G can be used to compute these generating functionals in the first place and therefore how to obtain correlation functions in section four. The first generating functional we examine is the partition functional calligraphic Z left parenthesis J right parenthesis which depends on source terms J left parenthesis T right parenthesis (in analogy with a magnetic field source term M left parenthesis X right parenthesis in spin systems)

calligraphic Z left parenthesis J right parenthesis equals integral D capital phi exp left bracket negative calligraphic S sub capital B capital M left bracket capital phi right bracket plus integral D T J capital phi right bracket fifty which, under variation with respect to J will give any required correlator. In the above functional integral, capital phi stands collectively for left parenthesis phi left parenthesis T right parenthesis, F tilde left parenthesis T right parenthesis, rho left parenthesis T right parenthesis, rho bar left parenthesis T right parenthesis right parenthesis and J left parenthesis T right parenthesis for all the corresponding currents integral D T J capital phi equivalent integral D T left parenthesis J sub phi phi plus J sub F tilde F tilde plus rho bar zeta plus zeta bar rho right parenthesis fifty-one

The only constraint we will require of the currents is that they satisfy J left parenthesis T sub in right parenthesis equals J left parenthesis T sub F right parenthesis equals zero at the initial and final times T sub in and

T sub F. The averages of the fields are defined by average phi left parenthesis T right parenthesis end average equivalent integral D capital phi capital phi left parenthesis T right parenthesis exp left bracket negative calligraphic S sub capital B capital M left bracket capital phi right bracket right bracket fifty-two equals fraction with numerator delta calligraphic Z left bracket J right bracket over denominator delta J left parenthesis T right parenthesis evaluated at J equals zero, fifty-three the two point correlation function is:

average phi left parenthesis T sub one right parenthesis phi left parenthesis T sub two right parenthesis end average equivalent fraction with numerator integral D capital phi capital phi left parenthesis T sub one right parenthesis capital phi left parenthesis T sub two right parenthesis exp left bracket negative calligraphic S left bracket capital phi right bracket right bracket over denominator integral D capital phi exp left bracket negative calligraphic S left bracket capital phi right bracket right bracket, fifty-four

P equals the fraction of the partial derivative delta squared script Z of J with respect to delta J of t sub two and delta J of t sub one. Subscript J equals zero.

and similarly for higher correlation functions. Note that the usual normalization by a factor script Z of zero to the power of negative one that is included in general, is omitted here since for this theory, script Z of zero equals one by construction.

Defining script W of J is equivalent to the natural log of script Z of J.

allows us to compute connected correlation functions (or Ursell functions) as:

the expected value of Phi of t sub one through Phi of t sub n subscript C equals the fraction of the partial derivative delta to the power of n script W of J with respect to delta J of t sub one through delta J of t sub n. Subscript J equals zero.

For instance, the connected two-point function (more commonly known as covariance) G of t sub one, t sub two is:

G of t sub one, t sub two is equivalent to the expected value of Phi of t sub one Phi of t sub two subscript C equals the expected value of Phi of t sub one Phi of t sub two minus the expected value of Phi of t sub one times the expected value of Phi of t sub two. This equals the fraction of the partial derivative delta squared script W of J with respect to delta J of t sub one and delta J of t sub two. Subscript J equals zero.


## D. Symmetry transformations for script S sub BM and Ward-Takahashi identities

In this subsection, we recall the transformations that leave the action script S sub BM invariant, up to boundary terms. We comment on the implications of such symmetries, also paying attention to the boundary terms that are usually dropped under the assumption of equilibrium, or, equivalently, a corresponding infinite amount of elapsed time between initial and final states. For us to later use SUSY fRG flow equations in section three, it is crucial to verify the presence of this symmetry in an out-of-equilibrium context.

In general, invariances of the action imply relations between various correlation functions in field theory, generally known as Ward-Takahashi (W-T) identities. Their derivation can be summarized as follows: A general infinitesimal transformation of the fields Phi arrow Phi prime equals Phi plus delta Phi will generically change the action S arrow script S prime equals script S plus delta script S. Also, shifting J arrow J plus delta J leads to delta script Z equals the integral over t of the partial derivative delta script Z with respect to delta J of t times delta J of t equals the integral of script D Phi e to the power of negative script S of Phi plus the integral over t J Phi times negative delta S plus J delta Phi plus delta J Phi, where we used that a) Phi is simply an integration variable in fifty and script Z is not altered by a change in Phi but only D equals D prime. The transformation involves no non-trivial Jacobian determinant. Symmetries of the dynamical system comprise of transformations for which delta S is, at most, a total derivative (or a total divergence for higher dimensions): delta script S equals the integral over t of d over dt script A equals script A of t sub f minus script A of t sub i equals left bracket script A right bracket sub t sub i to t sub f. Further choosing delta J such that, for a given delta Phi, J delta Phi plus delta J Phi equals zero, the integral over t of the partial derivative delta script Z with respect to delta J of t times delta J of t equals the integral of script D Phi left bracket script A right bracket sub t sub i to t sub f e to the power of negative script S of Phi plus the integral over t J Phi.

Differentiating this master equation with respect to J and setting J equals zero, gives relations between correlations functions that are necessitated by the symmetry under

Phi arrow Phi plus delta Phi. For our case, given two independent, infinitesimal Grassmann variables epsilon and € the following transformations of the fields.

phi arrow phi plus i bar epsilon rho minus i bar rho epsilon

F tilde transforms to F tilde minus bar epsilon dot rho minus dot bar rho epsilon, rho transforms to rho plus dot varphi minus i F tilde epsilon, bar rho transforms to bar rho plus bar epsilon times dot varphi plus i F tilde (sixty-two) (sixty-three) (sixty-four)

leave S sub B M invariant up to a boundary term at the initial time t sub i r: S sub B M transforms to S sub B M plus bar rho sub i n times i dot varphi plus F tilde plus two i W sub varphi i n epsilon (sixty-five)

where a subscript 'in' denotes the initial time t sub i n. The boundary term at t sub f has been eliminated using the boundary condition (twenty-one). Note that the bar epsilon transformation leaves S sub B M invariant identically, irrespective of the boundary conditions.

Adding source currents J sub varphi, J sub F tilde, zeta, bar zeta to the action

S sub B M transforms to S sub B M minus the integral with respect to t of J sub varphi varphi plus J sub F tilde F tilde plus bar rho zeta plus bar zeta rho (sixty-six)

and requiring appropriate transformations of those currents,

J sub varphi transforms to J sub varphi plus dot bar zeta epsilon plus bar epsilon dot bar zeta (sixty-seven)

J sub F tilde transforms to J sub F tilde plus i bar zeta epsilon minus i bar epsilon zeta (sixty-eight)

zeta transforms to zeta plus epsilon times i J sub varphi minus dot J sub F tilde, bar zeta transforms to bar zeta minus bar epsilon times i J sub varphi plus dot J sub F tilde (sixty-nine) (seventy)

we have

J Phi transforms to J Phi minus bar epsilon d over d t of rho J sub F tilde minus varphi zeta minus d over d t of bar rho J sub F tilde minus varphi bar zeta epsilon (seventy-one)

We therefore see that the transformations result in

S sub B M minus J Phi transforms to S sub B M minus J Phi plus bar rho sub i n times i dot varphi plus F tilde plus two i W sub varphi i n epsilon (seventy-two)

and the exponent in the integrand of fifty only changes by a lower boundary term that is also independent of E.

The field transformation sixty-one to sixty-four are linear shifts that leave the integration the path integral invariant. Coupled with the shift in the currents we find, setting epsilon equals zero the integral with respect to t of delta Z over delta J sub varphi of t dot zeta minus i delta Z over delta J sub F tilde of t zeta minus delta Z over delta bar zeta of t times i J sub varphi plus dot J sub F tilde equals zero (seventy-three)

while for bar epsilon equals zero we obtain the integral of d t times the quantity delta Z over delta J sub phi of t multiplied by dot zeta tilde plus i times delta Z over delta J sub F tilde of t times bar zeta minus delta Z over delta zeta of t times the quantity i J sub phi minus dot J sub F tilde equals the integral of D Phi times the quantity negative bar rho sub in times the quantity i dot phi sub in plus F tilde sub in plus two i W sub in prime times e to the power of negative S sub BM plus the integral of d t J Phi of.

d over d tau times the expected value of phi of t prime phi of tau plus the expected value of phi of t prime W prime of phi of tau minus i times the expected value of rho of t prime bar rho of tau equals zero.

which, along with the original Langevin equation, allows us to infer that i times the expected value of rho of t prime bar rho of tau equals one over the square root of Upsilon times the expected value of phi of t eta of tau,

meaning that the expected value of rho of t prime bar rho of tau is proportional to the response of phi of t prime to noise eta of tau, clearly a retarded quantity proportional to Theta of t prime minus.

the square root of Upsilon times the expected value of x tilde of tau phi of t prime equals negative the expected value of bar rho of tau rho of t prime.

which confirms that the expected value of phi of t prime x tilde of tau is the retarded response function or propagator. Importantly, equation seventy-seven also establishes that in a diagrammatic expansion closed ghost loops act to cancel closed loops involving the retarded propagator. This ensures Z of J equals zero equals one, which simply reflects conservation of probability, and furthermore that correlators do not depend on the ill-defined quantity Theta of zero, reflecting the well-known fact that, for additive noise, the discretization of the stochastic differential equation (Ito, Stratonovic etc) does not matter.

Differentiating seventy-four with respect to J sub phi of t prime, bar zeta of tau and setting J equals zero gives, with the use of seventy-seven and recalling that integration over F tilde gives

F tilde goes to negative i W with respect to phi, two times d over d tau expected value of phi of t prime phi of tau minus i square root of Upsilon expected value of x tilde of tau phi of t prime plus i square root of Upsilon expected value of x tilde of t prime phi of tau equals negative i Upsilon expected value of x tilde sub in phi of tau expected value of x tilde sub in phi of t prime.

This is a modified Fluctuation-Dissipation relation with the term on the right-hand side accounting for the initial condition. Sending T sub I N to negative infinity makes the right-hand side vanish and we recover the Fluctuation-Dissipation relation at equilibrium:

D by D tau of the average of phi of T prime phi of tau equals I times the square root of Upsilon over two times the average of X tilde of tau phi of T prime minus the average of X tilde of T prime phi of tau equation seventy-nine


## Three. Applying the Functional Renormalisation Group

The functional renormalisation group has already been applied to study nonequilibrium physics. Recently, the functional renormalisation group has further been used for averaging fluctuations in the temporal domain of Langevin dynamics, but without direct use of the supersymmetry. As discussed, the physically inspired conditions the authors require of their flow equations are straightforwardly imposed by the Supersymmetric flow. The Supersymmetric flow equation itself was first derived, but without making any connection to stochastic dynamics. This connection was made independently, which however considered a field theory in extended spatial dimensions and smoothing the corresponding spatial fluctuations, not temporal fluctuations as we do here. In fact, the authors obtain a slightly different flow equation when wavefunction renormalisation is included since they do not connect the action functional they study to Brownian motion and the corresponding equilibrium Boltzmann distribution. This Supersymmetric functional renormalisation group flow has only been very recently utilized in the context of stochastic dynamics in early universe inflation.

The formulation of the functional renormalisation group involves the Wetterich equation which is a functional infinite dimensional integro-differential equation describing the flow of the effective action between the microscopic and macroscopic scale. This flow is controlled by a parameter K that ranges from the ultraviolet cutoff Lambda down to the infrared regime as K approaches zero. In our Brownian motion scenario, microscopic regime refers to a small timestep to a long timestep. The definition Lambda is proportional to one over delta T. The Condensed Matter interpretation of the cutoff being inversely proportional to the lattice size, the only difference here being that the Condensed Matter lattice is in space and ours is in time. We will use the functional renormalisation group ultimately to calculate correlation functions of the particle position. As this derivation uses known techniques and results we refer the busy reader to our basic equations and main results of this section: equation eighty-eight for the Local Potential Approximation to the RG flow and when we also include Wavefunction Renormalisation they are ninety-five and ninety-six.

The functional renormalisation group formulation adds a regulating term to the action in our definition of the generating functional:

Z sub K of J equals the integral of D Phi exp of negative S of Phi minus delta S sub K of Phi plus the integral of T J Phi equation eighty where the regulating term delta S sub K of Phi is quadratic in

Phi: delta S sub K of Phi equals one-half times the integral of T and T prime Phi of T R sub K of T and T prime Phi of T prime equation eighty-one

Crucially R sub K is an infrared regulator that depends on a Renormalisation scale K and the modes. The precise form of begin array text momentum frequency P of K R sub K text is not crucially important and it is chosen in order to optimize calculations but it should suppress infrared modes and vanish as K approaches zero, limit as K approaches zero of R sub K equals zero, ensuring that the full effective action is recovered in this limit. By defining the mean field as X of T is equivalent to average of Phi of T we can construct the Regulated Effective Action:

Gamma sub K of X equals the integral of T J X minus W sub K of J minus delta S sub K of X equation eighty-two where W sub K of J equals the natural log of Z sub K and X refers to all the relevant mean fields.

From the Regulated Effective Action one can obtain the Wetterich equation

Partial K Gamma sub K of X equals one-half S T R of the integral of T and T prime partial K R sub K of T and T prime times R sub K plus Gamma sub K superscript two inverse equation eighty-three which is a functional equation determining how Gamma sub K changes as K approaches zero. Gamma superscript left two right is the second functional derivative with respect to the relevant fields and STr refers to the supertrace - see for details. The equation evolves Gamma sub K from the microscopic scale left K equals Lambda right, where Gamma sub Lambda equals Script S, down to the IR regime left K equals zero right where the full effective action Gamma left chi right equals Gamma sub K equals zero left chi right, encoding the effect of all fluctuations, is obtained. A simplified derivation for one degree of freedom at equilibrium, which however captures all the relevant manipulations, can be found in Appendix

A. As demonstrated in the previous section, our Brownian motion problem is actually SUSY Q M. We can therefore apply the f R G technology and incorporate the effect of thermal fluctuations by following the flow of the effective action Gamma sub K via the Wetterich equation. Synatschke et. al have analysed a system with action Script S sub S U S Y in light of its underlying symmetries - see also. We adopt their results here. They find that from a supersymmetric perspective, the appropriate regulating term takes the form

Delta Script S sub K equals integral sub tau tau superscript prime R sub two left K, Delta tau right left negative dot phi left tau right dot phi left tau prime right plus F left tau right F left tau prime right minus I bar psi left tau right dot psi left tau prime right right plus two I R sub one left K, Delta tau right left ceiling phi left tau right F left tau prime right minus bar psi left tau right psi left tau prime right right ceiling (eighty-four)

where Delta tau is equivalent to tau minus tau prime. Such a form was also suggested, however we will see that compatibility with the Boltzmann distribution suggests setting R sub two to approach zero. The flow equations are discussed below.


## A. Local Potential Approximation

In practice, calculating Gamma sub K exactly is usually impossible and we must consider a truncation to make the functional equation tractable. The most common approximation is the so-called derivative expansion. The Local Potential Approximation, the leading order in the derivative expansion, is the assumption that the only part of the effective action that depends on our momentum scale K is the superpotential W. The effective action then takes the form:

Gamma sub K left phi, F, bar psi, psi right equals integral D tau left one half dot phi squared plus one half F squared plus I F W sub K comma phi left phi right right minus I bar psi left partial sub T plus W sub K comma phi phi right psi right (eighty-five)

such that Gamma sub K equals Lambda equal Script S sub S U S Y under the condition W sub K equals Lambda left phi right equals W left phi right with

(eighty-six)

phi is equivalent to left angle varphi right angle, F is equivalent to left angle tilde F right angle, psi is equivalent to left angle rho right angle, bar psi is equivalent to left angle bar rho right angle are the mean fields, and we also denote chi is equivalent to left angle X right angle equals square root Upsilon phi. In this approximation the only thing changing with K directly, progressively incorporating the effect of fluctuations on different timescales, is W sub K. This means we only have one flow equation to solve which turns out to be.

Partial derivative with respect to k of W sub k of phi equals the integral from negative infinity to infinity of dp over four pi times the quantity of one plus r sub two times partial derivative with respect to k of r sub one minus partial derivative with respect to k of r sub two times the quantity of r sub one plus partial derivative with respect to phi squared of W sub k of phi, all over p squared plus the quantity of r sub one plus partial derivative with respect to phi squared of W sub k of phi squared. We notice that if we set r sub two equals zero and choose a local-in-time r sub one of k sub negative tau minus tau prime equals k delta of tau minus tau prime, the so-called Callan-Symanzik regulator then this choice effectively adds a quadratic term to the potential W goes to W plus k phi squared and leads to a relatively simple flow equation:

Partial sub k W sub k left parenthesis phi right parenthesis equals one fourth dot one divided by k plus partial sub phi squared W sub k left parenthesis phi right parenthesis.

In terms of the physical variables we have

Partial sub k V sub k left parenthesis chi right parenthesis equals UPSILON over four dot one divided by k plus partial sub chi squared V sub k left parenthesis chi right parenthesis.

which shows explicitly the effect of dialing the temperature T: the higher the temperature the faster the flow as a result of stronger thermal fluctuations. Equation eighty-eight can be discretized in the chi direction and become a set of coupled ODEs that can be solved in the k direction in order to obtain a numerical solution.

It is important to note that equation eighty-eight is identical to the flow of the effective potential that corresponds to the equilibrium Boltzmann distribution, see and A P pendix C with R to k k. We therefore see that the form of mathcal S sub S U S Y and deriving flow equations that respect its symmetries establishes automatic consistency with the equilibrium Boltzmann distribution. If one started directly from the Onsager-Machlup functional thirty and naively treated it as an N equals one Euclidean scalar theory in one- dimension with the combination U equals one-half left parenthesis V sub comma x right parenthesis squared minus UPSILON over two V sub comma x x as the scalar potential to be evolved along the RG stackrel negative f l o w o n d would have obtained a different flow equation

On partial sub k U sub k left parenthesis phi right parenthesis equals one-half integral from negative infinity to infinity d p over two pi partial sub k R sub k divided by p squared plus R sub k plus partial sub phi squared U sub k left parenthesis phi right parenthesis.

The corresponding Callan-Symanzik regulator would be R sub k equals k squared, giving

Partial sub k U sub k left parenthesis phi right parenthesis equals one-half k over square root of k squared plus partial sub phi squared U sub k left parenthesis phi right parenthesis.

It is unclear how or if the end-of-the-flow potential U sub k equals zero from this equation would relate to the physical potential

V sub k equals zero. B. Wave Function Renormalisation

In the previous subsection we assumed that the effective action Gamma sub k only depends on the renormalisation scale through the form of the potential. We now allow for the field varphi itself to be renormalised which results in a scaling. The new effective action in the SUSY formalism is:

Gamma sub k left parenthesis phi, bar psi, psi right parenthesis equals integral d t one-half Z sub comma phi squared dot phi squared plus one-half left parenthesis W sub comma phi over Z sub comma phi right parenthesis squared minus i bar psi left parenthesis Z sub comma phi squared partial sub t plus Z sub comma phi Z sub comma phi phi dot phi minus Z sub comma phi phi W sub comma phi over Z sub comma phi plus W sub comma phi phi right parenthesis psi.

where we have suppressed the explicit dependence on k of W and Z to avoid overly cluttered notation. From now on we will in general drop this explicit dependence on k for W, V, Z and zeta, defined below, only restoring it when we are directly comparing it to the original cutoff value. We introduce another identification in addition to twenty-six:

zeta left parenthesis x right parenthesis equals square root of UPSILON Z left parenthesis phi right parenthesis Right arrow zeta sub comma x equals Z sub comma phi.

bar c c equals negative i zeta sub comma x bar psi psi.

such that the on-shell effective action for Brownian motion is now written as:

Gamma sub k left parenthesis chi, bar c, c right parenthesis equals integral d t one over two UPSILON zeta sub comma chi squared dot chi squared plus one over two UPSILON left parenthesis V sub comma chi over zeta sub comma chi right parenthesis squared minus bar c left parenthesis zeta sub comma chi squared partial sub t plus zeta sub comma chi zeta sub comma chi chi dot chi minus zeta sub comma chi chi V sub comma chi over zeta sub comma chi plus dot V sub comma chi chi right parenthesis c.

The regulator term becomes more complicated for this action and we do not reproduce it here, see for details of this. Following their approach one arrives at the LPA plus wave function renormalization flow equations:

Partial derivative with respect to K of V subscript K of chi equals Upsilon divided by four times one over K plus second partial derivative with respect to chi of V subscript K of chi equation ninety-five.

Partial derivative with respect to K of zeta subscript comma chi equals Upsilon divided by four times P divided by zeta subscript comma chi times D squared equation ninety-six.

D is equivalent to V subscript comma chi chi plus K zeta subscript comma chi squared. P is equivalent to four zeta subscript comma chi chi V subscript comma chi chi chi divided by D minus zeta subscript comma chi chi zeta subscript chi subscript comma chi minus three zeta subscript comma chi squared V subscript comma chi chi chi squared divided by four D squared equation ninety-seven equation ninety-eight.

which now consist of the previous LPA equation for the effective potential eighty-eight as expected, augmented by one more flow equation for the wavefunction renormalisation zeta subscript comma chi. As before we will integrate the LPA equation eighty-eight by discretising along the chi direction and solving the resulting set of coupled ODEs in K. Once the effective potential V subscript K of chi has been obtained the second PDE can be solved zeta subscript comma chi in a similar way. It is worth pointing out here approach differs slightly from in that the effective potential obeys the same equation as in the LPA approximation even with the inclusion of wave function renormalization. This is because the equilibrium state is described exactly by the LPA equation as we mentioned above and explicitly recall in Appendix A. The LPA flow equation was first solved in, while more recently wave function renormalization was included for a double well potential in.


## Four. The Effective Equations of Motion.

A standard formulation of classical mechanics involves the principle of least action. If one considers the classical action

Script S: Script S equals the integral dt L of x, dot x, minus jx equation ninety-nine.

where L of x, dot x is the Lagrangian and a source term has been added, one can obtain the equations of motion by requiring the variational derivative of Script S to be zero:

the fraction delta Script S over delta x equals j equation one hundred.

The Effective Action EA Gamma is so named because its definition makes it look like a classical action but includes the effect of fluctuations that have been integrated out. Defining e to the power of Script W of J equals the integral D Phi e to the power of negative Script S of Phi plus the integral dt J Phi equation one hundred one.

the effective action Gamma of X is then defined as

Gamma of X equals the integral t J X minus Script W of J equation one hundred two.

where

X equals the expected value of Phi. equation one hundred three.

We then have the fraction delta Gamma over delta X equals J equation one hundred four.

Therefore Gamma, the central object of the functional renormalization group, leads to effective equations of motion that incorporate the aggregate effects of the thermal fluctuations.


## A. The Effective Equation of Motion for the one point function.

In a similar way to how the classical action Script S of x can yield the classical equations of motion through variational derivatives, so too does Gamma of chi yield the effective equation of motion for the one point function (or average position)

chi: the fraction delta Gamma over delta chi of t equals zero equation one hundred five.

Here we have assumed there are no external sources (J equals zero). Under the I P A equation one hundred five is:

the fraction delta Gamma subscript K equals zero over delta chi of t equals second partial derivative of chi minus partial derivative with respect to chi of V subscript K equals zero of chi partial derivative with respect to chi squared of V subscript K equals zero of chi equals zero equation one hundred six.

where the final equality comes by assuming that source terms have been set to zero (i.e J of t equals zero). The wave function renormalization version of one hundred five reads:

zeta sub comma chi dot chi times negative partial sub chi V sub k equals zero divided by zeta sub comma chi squared partial sub chi chi squared V sub k equals zero minus zeta comma chi chi divided by zeta sub comma chi partial sub chi V sub k equals zero equals zero.

where partial sub x zeta and partial sub chi squared zeta are also evaluated at k equals zero. Both of these second order differential equations can actually be reduced to a first order differential equation like so:

dot chi equals negative V sub comma chi of chi.

where we have introduced the effective dynamical potential V tilde defined by

V tilde sub comma chi of chi equivalent to a piecewise function: V sub comma chi of k equals zero, chi for L P A or V sub comma chi of k equals zero, chi divided by zeta sub comma chi squared of k equals zero, chi for W F R.

Here we can clearly see that for L P A the effective and effective dynamical potentials are equivalent whereas W F R provides an additional factor for the latter.

Equation one hundred eight tells us that the equation of motion for the average position chi is an extremely simple first order differential equation that appears like a Langevin equation with no noise. This means that once you have obtained the effective dynamical potential you can compute the evolution of the average position chi trivially from any starting position.

At equilibrium the average position of the particle should not change, this means that dot chi equals zero. It naturally follows from this condition and the E E O M for x one zero eight that equilibrium is defined for both L P A and W F R by the condition partial sub chi V sub k equals zero of chi sub e q equals zero.

As the potential V sub k equals zero of chi should be convex by definition equation one twenty-seven tells us that chi sub e q corresponds to the minimum of V sub k equals zero of chi. Or more concretely:

limit as t approaches infinity of the expectation of x of t equals x that minimizes V sub k equals zero of x.

The equilibrium position is obviously the same for both L P A and W F R as they both lead to the same effective potential. As the equilibrium position is straightforwardly computed from the Boltzmann distribution verifying that the minimum of the effective potential matches the predicted equilibrium position is a good first test for the numerical solution of V sub k equals zero of x, at least close to its minimum.


## B. The E E O M for the two point function

Two-point function G of t comma t prime equals

The connected equals the expectation of x of t, x of t prime sub C equals delta squared calligraphic W divided by delta J of t delta J of t prime and the second functional derivative of the effective action Gamma sub k equals zero are inverse to each other integral d tau delta squared Gamma sub k equals zero divided by delta chi of t delta chi of tau delta squared calligraphic W sub k equals zero divided by delta J of tau delta J of t prime equals delta of t minus t prime.

Concretely, this means that the connected two-point function G of t comma t prime satisfies the following equation:

the second derivative with respect to t squared minus calligraphic U of chi of t G of t comma t prime equals negative two Delta delta of t minus t prime.

where calligraphic U of chi is:

\mathcal{U} left \chi \right equals left bracket V _ { , \chi \chi } squared plus V _ { , \chi } V _ { , \chi \chi \chi } , and text for LPA V _ { , \chi } squared plus fraction V _ { , \chi } V _ { , \chi \chi \chi } by \zeta _ { , \chi } fourth power minus fraction V _ { , \chi } squared \zeta _ { , \chi \chi \chi } by \zeta _ { , \chi } fourth power right parenthesis one one four minus fraction five V _ { , \chi } V _ { , \chi \chi } \zeta _ { , \chi \chi } by \zeta _ { , \chi } fifth power plus fraction five V _ { , \chi } squared \zeta _ { \chi \chi } by \zeta _ { , \chi } sixth power , text for WFR end bracket.

The derivation of the full solution to one hundred thirteen can be found in Appendix B but here we just highlight the two main results:


## The EEOM for the Variance

and the EEOM for the where \widetilde { Y } _ { i } left t \right equals Y _ { i } left t \right by Y _ { i } left zero \right are the normalised solutions to the homogeneous equation B two which can be obtained numerically. P left t \right equals one or \zeta _ { \chi } left parenthesis \chi left parenthesis t \right right parenthesis for LPA and WFR respectively and \lambda is defined below by one hundred nineteen. G _ { zero zero } equals G left parenthesis zero , zero right parenthesis is the initial variance at t equals zero If we take the equilibrium limit \chi right arrow \chi _ { e q } of the full EEOM for the two-point function one hundred thirteen we find that it simplifies to:

where and \bigtriangleup is defined as in one hundred fifteen. The notation vertical line means we have evaluated the function at k equals zero and at equilibrium

\chi equals \chi _ { e q } . The appropriate solution to one hundred eighteen providing the connected correlation function at equilibrium is

G _ { e q } left parenthesis t _ { one } , t _ { two } right parenthesis equals \mathrm { C o v } _ { e q } left parenthesis x left parenthesis t _ { one } \right parenthesis x left parenthesis t _ { two } right parenthesis right parenthesis equals fraction \Upsilon by two V _ { , \chi \chi } absolute value e superscript negative \lambda absolute value t _ { one } minus t _ { two } absolute value.

\Delta equivalence left bracket fraction \Upsilon by two , text for LPA fraction \Upsilon by two \zeta _ { \chi } squared , text for WFR end bracket one hundred fifteen.

t prime right arrow t : \mathrm { V a r } left parenthesis x \right parenthesis equivalence G left parenthesis t , t \right equals fraction \Upsilon by two \lambda P left parenthesis t \right \widetilde { Y } _ { one } left parenthesis t \right \widetilde { Y } _ { two } left parenthesis t \right plus fraction P left parenthesis zero \right by P left parenthesis t \right left bracket G _ { zero zero } minus fraction \Upsilon by two \lambda P left parenthesis zero \right right bracket \widetilde { Y } _ { two } squared left parenthesis t \right one hundred sixteen.

t prime right arrow zero , t greater than zero : \mathrm { C o v } left parenthesis x left parenthesis zero right parenthesis x left parenthesis t \right parenthesis equivalence G left parenthesis t , zero right parenthesis equals G _ { zero zero } \widetilde { Y } _ { two } left parenthesis t \right one hundred seventeen.

left parenthesis fraction d squared by d t squared minus \lambda squared right parenthesis G _ { e q } left parenthesis t _ { one } , t _ { two } right parenthesis equals negative two \Delta vertical line \delta left parenthesis t _ { two } minus t _ { one } right parenthesis one hundred eighteen.

\lambda squared equivalence left bracket V _ { , \chi \chi } squared vertical line , text for LPA and fraction V _ { , \chi \chi } squared by \zeta _ { , \chi } fourth power , text for WFR end bracket one hundred nineteen.

right arrow G _ { e q } left parenthesis t , t \right equivalence \mathrm { V a r } _ { e q } left parenthesis x \right parenthesis equals fraction \Upsilon by two V _ { , \chi \chi } vertical line one hundred twenty-one.

As the equilibrium variance is also easily computed from the Boltzmann distribution, equation one hundred twenty-one gives us a second test to verify that the effective potential has been computed correctly, at least around the minimum.

In the LPA approximation the variance and the decay rate of the autocorrelation function are both directly given by the curvature of the effective potential at its minimum. The inclusion of WFR however alters the decay rate without changing the equilibrium variance. This is as it should be since the latter is fixed by the equilibrium Boltzmann distribution. As we will see, WFR improves the decay rate which is indeed not exactly determined by the effective potential's curvature alone.


## V. SOLUTIONS TO THE FLOW EQUATIONS

In this section we obtain the resulting effective potential and wave function renormalisation for three types of potential. The first we consider is a simple polynomial in line with:

V of x equals one plus x plus x squared over two plus two x cubed over three plus x to the power of four over four

We will also consider a double-well made by two L J potentials back to back:

V of x equals four epsilon sub one times sigma to the power of twelve over x plus three to the power of twelve minus sigma to the power of six over x plus three to the power of six plus four epsilon sub two times sigma to the power of twelve over x minus three to the power of twelve minus sigma to the power of six over x minus three to the power of six where sigma will be taken to be one from here on in and epsilon sub one and epsilon sub two represent the depth of each well. We will choose epsilon sub one equals one, epsilon sub two equals ten meaning the left well is one unit deep and the right units deep (in two D sub zero over varepsilon units) and the potential is asymmetric. Clearly here the domain of interest is x in negative three to three as the potential diverges at x equals plus or minus three. Finally we also consider a "bumpy" bare potential consisting of a simple x squared underlying potential with additional gaussian bumps (or dips):

V of x equals x squared plus the sum from i equals one to n alpha sub i times the exponential of negative quantity x minus beta sub i squared over mu where there are n bumps or dips with the prefactor alpha sub i being positive or negative respectively. We will focus on an x squared plus three bumps and three dips in an asymmetrical setup. This potential could represent a rudimentary toy model for motion over a "potential energy landscape" with a series of local energy minima. This serves to clearly demonstrate the effect of local extrema on the final shape of the effective potential since the underlying x squared potential does not alter its shape under the RG flow. We chose the parameters to be for x squared plus six bumps/dips:

alpha sub one equals alpha sub four equals alpha sub five equals negative one point five, alpha sub two equals alpha sub three equals alpha sub six equals one point five, mu equals zero point zero six, beta sub one equals negative beta sub two equals zero point seven, beta sub three equals negative beta sub four equals one point four, beta sub five equals negative beta sub six equals two point one chi FIG. one: The flow of the polynomial Langevin potential V in the LPA for (a) Upsilon equals ten (High temperature/strong fluctuations) and (b) Upsilon equals one (Low temperature/Weak fluctuations). The dotted blue curve indicates the bare potential which is progressively changed, through dot-dashed green and dashed yellow, into the solid red, effective potential, as fluctuations are integrated out.

expressed in dimensionless units (we have set wide-hat x to x to avoid notational clutter).

We solve the LPA flow equation eighty-eight on a grid in the chi direction and using an adaptive step size Runge-Kutta ODE solver to evolve in the k direction. A similar approach was used for including ninety-six. The numerical derivatives in the chi direction were based on a finite difference scheme using the Fornberg method with a stencil size of five for the potentials under study. While increasing the grid size improves the accuracy of the numerical derivative it also increases the number of coupled ODEs to be solved, making the integration much more computationally expensive. A balance must be drawn depending on the potential in question. For our cases we considered thousand-one points and x in negative three to three for the unequal L-J potential and x in negative five to five for the other two. Figs. one, two, four, three and five, display the results.

Figs. one and two show the flow from the bare to the effective potential for a high, Upsilon equals ten, and a low, Upsilon equals one, temperature for the polynomial and unequal L-J potentials respectively. As K approaches zero is approached, a distinct single minimum develops, indicating the average position of the particle. As expected, the lower the temperature, the closest the effective minimum is to the bare potential's global minimum, reflecting the relative weakness of fluctuations to force the particle to spend time away from it. As one might expect, it takes 'longer' in K evolution for local features - e.g. barriers - to disappear in the Upsilon equals one case as fluctuations at each K scale have less energy than their equivalent for the Upsilon equals ten and the particle's stochastic motion between barriers is less frequent. Physically this means that the fluctuations we have integrated out up to scale K do not contribute significantly to the particle moving between minima.

We see a similar phenomenon in Fig. three for the flow from the bare to the effective potential for Upsilon equals three, and Upsilon equals one for an X squared potential with six gaussian bumps or dips. Here the original Langevin potential is much more complicated than in the previous two cases but the fRG is still able to smoothen out these features in a non-trivial way. This example further demonstrates how the flow of the effective potential is driven by the local curvature, the gaussian features imposed here, since for an X squared potential the fRG flow equation eighty-eight yields no change beyond an unphysical shift by an overall additive constant.

It is clear in all three figures that at the high temperature there is not much change in the shape of the potential when K has reached the value given by the green, dot-dashed line. Physically this means that the fluctuations integrated out in this range do not contribute significantly to the particle evolution and transition between minima. However, by the time K has been lowered to the value of the yellow, dashed line we have started to integrate over fluctuations over timescales relevant for inter-minima transitions. Naturally, when K equals zero is reached the potential is fully convex (as it must be by definition of T) with no local features to overcome. Similar behaviour is obtained where again we consider the corresponding

Upsilon equals three lower temperature. As one might expect it takes 'longer' in K evolution for the barrier to disappear as fluctuations at each K scale have less energy than their equivalent for the high temperature case. Of note is that not only is the evolution different but the final shape of V sub K equals zero left parenthesis X right parenthesis is different for the two different temperature regimes. Both the position and gradient near the global minimum are changed. This is suggestive of longer time scales required at lower temperatures to reach equilibrium. It also indicates longer times for the equilibrium covariance to decay, as we discuss below.

Regarding WFR, the full numerical solutions to (ninety-six) for the unequal L-J potential at Upsilon equals ten, two and for an X squared potential with six gaussian bumps or dips at Upsilon equals three, are shown in Figs. four and five respectively. We see that from the initial condition, Zeta sub X equals one everywhere, features appear as K approaches zero in direct contrast with the evolution of the effective higher temperatures it is clear that at K equals zero a local minima appears at the same place as the global minimum for the effective potential where the height of the local minima is linked to the equilibrium covariance - see equation one hundred nineteen. Looking at Fig. four (b) however we can see that this is no longer the case and the features generated by the fRG flow are much greater than in the high temperature case. We will see later that the neighbouring features in Zeta sub X will help to better describe dynamical evolution than the bare potential alone.


## VI. EQUILIBRIUM

As mentioned above and recalled in Appendix A, the LPA flow equation eighty-eight exactly corresponds to the effective potential of the equilibrium Boltzmann distribution

P of x equals N exp of negative two V of x over Upsilon. One hundred twenty-six.

We have verified that both the equilibrium position, given by the minimum of the effective potential,

partial with respect to chi V sub k equals zero of chi sub eq equals zero. One hundred twenty-seven.

and the equilibrium variance, defined from the effective potential's curvature through

Var sub eq of x equals Upsilon over two V sub comma chi chi. One hundred twenty-eight.

are reproduced to sub-percent accuracy, indicating the accuracy of the numerical solution to the LPA flow equation, at least around the minimum of the effective potential.

In addition to the static variance at equilibrium, the curvature of the effective potential around the minimum also determines the time dependence of correlations in equilibrium, quantified by the time dependent covariance or connected two-point function

Cov sub eq of x of t sub one x of t sub two equals Upsilon over two V sub comma v chi e to the power of negative lambda absolute value t sub one minus t sub two. One hundred twenty-nine.

Here, lambda corresponds to V sub comma chi chi within the IPA but the solution to the WFR flow equation ninety-six for zeta sub comma chi also contributes, providing a correction to lambda according to one hundred nineteen.

In Table. I we collect the values of lambda obtained using the fRG under LPA and WFR for different Upsilon values, and compare this directly to high accuracy numerical simulations of the Langevin equation four. We can clearly see from Table. I that the LPA can have good agreement with the simulation value for simple potentials at high temperature but can deviate drastically as temperature is lowered. Inclusion of the WFR factor zeta sub x reduces the deviation error from the value obtained in the simulations substantially to approximately one for the simplest cases and order of magnitude agreement for the most complicated, low temperature systems.

The decay of the equilibrium covariance is shown in Figs. six and seven for the polynomial and x squared plus six bumps/dips We can see - for the polynomial begin array potentials respectively. potential - in Fig. six left parenthesis a right parenthesis, Upsilon equals ten, that the LPA and WFR are both in good agreement with simulations and in Fig. six b, Upsilon equals eleven, that the WFR offers better agreement than the LPA. In Fig. seven a we can see that for Upsilon equals three the WFR prediction closely matches the simulations offering significant improvement over the LPA which closely matches the bare x squared potential. This indicates that even for highly non-trivial systems - where the computation of eigenvalues for these potentials is a non-trivial exercise - that the simulated decay is vastly different from the bare x squared potential - see Table. I and compare to the x squared prediction for square root two which is one - the fRG can appropriately capture these effects.

It is also worth pointing out that the simulated decay rate does not follow a pure exponential at all times in all cases. This can be best seen in the top plot of Fig. six b where the decay is initially close to the LPA, then the WFR decay before moving towards the eigen decay rate at late times. This sort of behaviour has been identified in similar systems in the early universe where it was noticed that the smallest non-zero eigenvalue's spectral coefficient was sufficiently small that higher order eigen- values would dominate the decay at earlier times. As LPA matches the decay rate predicted by the Boltzmann distribution and WFR is closer to the decay predicted by E one. We discuss this further below.


## VII. RELAXATION TOWARDS EQUILIBRIUM

In order to solve the equations of motion for the one point function x of t and two point function G of t,t' we must first solve the PDEs for the LPA and WFR to obtain the dynamical effective potential V and the function U. We will use the solutions obtained in Section V in order to compute these parameters and then solve the appropriate Effective Equation of Motion.


## A. The dynamical effective potentials

In section IV we introduced the notion of the dynam- ical effective potential V given by equation one hundred nine which together with one hundred eight describes the evolution of the average position, x. As the fRG guarantees that the fully effective potential V will be convex this implies that the dynamical effective potential V will also be either fully or extremely close to fully convex for LPA and WFR respectively thus greatly simplifying dynamical calculations. In the previous section we emphasised how the fRG LPA effective potential gives us the Boltzmann equilibrium quantities such as equilibrium position and variance. What we would like to emphasise now however is that away from the minimum of the effective potential the fRG gives us information that the near equilibrium Boltzmann assumption does not. To be concrete, an approximate Gaussian Boltzmann distribution would assume that the potential is of the form:

V Boltz of x equals four dot Var eq Upsilon of x minus X eq squared. One hundred thirty.

where X eq and Var eq are the equilibrium position and variance respectively. We show in Fig. eight how this approximation can break down dramatically as one moves away from the equilibrium position suggesting that the fRG captures the far away from equilibrium dynamics well. In principle one could attempt to include higher order cumulants of the Boltzmann distribution such as skewness and kurtosis into an approximate effective potential, however the relationship between these cumulants and higher derivatives of the effective potential is non- trivial and cumbersome to include. In any case it is not expected including these corrections would lead to significant improvement away from equilibrium.


## B. Accelerated trajectories

Having solved the appropriate flow equations to obtain the dynamical effective potentials we can now solve one hundred eight. Given the dynamical effective potential V it only takes a couple of seconds to obtain the full trajectory of x from some initial position Ci equals Xi to the equilibrium position. For the polynomial potential we initialised the particle far away from the equilibrium position at x equals four. In Fig. nine we show how the average position of the particle changes with time using direct simulation of the Langevin equation four over fifty thousand runs, by numerically solving the

F-P equation thirty-four and as calculated by the evolution in the dynamical effective potentials V given using the LPA and WFR methods at Y equals ten. All four trajectories agree to a very high precision.

In Fig. ten we plot the evolution of x of t for the unequal LJ potential where the particle begins in the smaller well at x equals negative one point eight seven eight and moves towards its equilibrium position. We see as before that the WFR trajectory closely matches the simulated trajectory offering significant improvement over the LPA computation. Note that for this system it was impossible to get convergent numerics for the evolution of the F-P equation thirty-four. This ability of the fRG to capture the non-trivial evolution of average position is also shown in Fig. eleven for the x squared potential plus six bumps slash dips which is a much more complex potential landscape at three different temperatures. Here the LPA trajectory offers improvement over the x squared prediction by converging to the correct equilibrium position and including WFR more closely matches the true simulated trajectory. Lowering the temperature generically decreases the accuracy of the fRG results. It is noteworthy that the fRG is able to reasonably capture these difficult dynamics well in systems where the F-P solution is difficult to obtain.

It is important to note the time advantage offered by the fRG. Solving the fRG flow equations is comparable in computation time to direct simulation while solving the F-P equation thirty-four takes longer than both. However the latter two methods obtain solutions that are only valid for a single initial condition. A huge advantage of the fRG is that once the dynamical effective potential V is obtained it is trivial to solve the EEOM one hundred eight in a couple of seconds for any initial position whereas for both direct numerical simulation of four and solving the F-P equation thirty-four one has to start again from scratch.


## C. Evolution of variance of x

For our accelerated trajectories we initialised the particles at the exact same point every time. This means that at t equals zero the probability distribution of the particles had zero variance Var of x equals zero. Using this as our initial condition we solved numerically the EEOM for the variance one hundred sixteen, derived in appendix B. In Fig. twelve we show how the variance evolves with time for the polynomial potential for Y equals ten. We can see that the LPA closely matches the numerical and F- P evolution until t equals zero point five before departing slightly although it still tends towards the correct equilibrium distribution.

In Fig. thirteen we show how the variance evolves with time for an unequal LJ. As with the one-point function the F-P was unable to give sensible statistics however the LPA is able to very well match the early simulated trajectory even capturing the overshooting of the variance. The WFR on the other hand is better at capturing the late-time decay to equilibrium.

Finally in Fig. fourteen we show how the variance evolves for the x squared plus six gaussian bumps slash dips potential at three different temperatures. As before, lowering the temperature decreases accuracy. In Fig. fourteen C the fRG once again clearly captures the overshooting which is a feature of the gaussian bumps' existence; the bare x squared evolution does not capture this behaviour and overall describes the evolution poorly, converging to the wrong equilibrium variance. Again as before the LPA much better describes the early evolution while WFR more accurately describes late time evolution.


## D. Comparison with the spectral expansion

The above results for the change in the relative performance of LPA plus WFR as temperature is lowered can be interpreted by resorting to the spectral expansion. In section II B we recalled how all observables can be computed in a standard way from the Schrödinger-like, Fokker-Planck equation thirty-four using an expansion in eigenfunctions and eigenenergies. It is straightforward to show that - given our initial conditions considered above - the average position and the two-point function can be expressed as:

P of t equals Chi subscript e q plus the sum from n equals one to infinity of left bracket e to the negative E subscript n t e to the V of x subscript zero divided by Upsilon p subscript n of x subscript zero right bracket times the integral from negative infinity to positive infinity d x x e to the negative V of x divided by Upsilon p subscript n of x left bracket one hundred thirty-one.

and

P equals x squared t equals P x squared sub E_q plus the sum from n equals one to infinity of open bracket e to the power of negative E sub n t e to the power of V of x sub zero over Upsilon p sub n of x sub zero close bracket times the integral from negative infinity to infinity d x x squared e to the power of negative V of x over Upsilon p sub n of x close bracket (one three two)

where the subscript E_q indicates the equilibrium value, and E sub n and p sub n of x are respectively the eigenvalues and normalized eigenfunctions of the corresponding Schrödinger-like problem. Obtaining the spectrum E sub n and p sub n of x may be complicated by the fact that the actual Schrödinger potential U bar (thirty-five) can develop temperature-dependent features as the temperature is decreased - see Fig. fifteen. Even for the simple polynomial potential in the Langevin equation it is clear that at low temperatures it becomes non-trivial, developing highly asymmetrical trapping wells. The increasing energy gap between the two minima indicates that, for a fixed initial condition, higher-order terms in the spectral expansion can become important as the temperature is lowered.

To illustrate the importance of these higher-order terms for the two-point function evolution in the polynomial potential we examine the accuracy of a finite truncation of the spectral expansion at two temperatures, Upsilon equals ten and Upsilon equals twenty-two, for the evolution of P equals x squared t, initializing trajectories at x equals one: P of x, t equals zero equals delta of x minus one. In

Fig. sixteen we plot the error associated with a finite truncation of the spectral expansion, keeping only the first two (dashed line) or fifty (solid line) terms, at two different temperatures Upsilon equals twenty-two (green, top curve) or Upsilon equals ten (blue, bottom curve). This error is computed by comparing the truncated expansion to the numerical solution of the Fokker-Planck equation. At early times, the error associated with keeping only two terms is larger than when fifty terms are kept, as one would expect, the discrepancy being more pronounced at lower temperatures. As the system relaxes, the contribution from the higher order terms decreases and the errors of the two truncations converge, until they are essentially indistinguishable at later times, as expected. This decay of the contribution from the higher eigenvalues occurs faster for the higher temperature, making the two-term truncation more accurate earlier. This observation reinforces our inference from the previous paragraph that as temperature is lowered, higher-order terms in the spectral expansion become more important for accurately describing the evolution, at least for a fixed initial condition. Crucially, this offers an explanation for why the LPA plus WFR offers poorer agreement as temperature is lowered since it would be expected to most accurately describe circumstances where the lowest order terms in a spectral expansion dominate.

The relation between the spectral expansion and the range of validity of the effective action's derivative expansion is not entirely straightforward however, as it would also depend on the initial condition. The quantification of this relation would be an interesting undertaking which we leave for future work.


## Eight. Summary

Collecting results scattered in the existing literature, we have recalled how Brownian motion can be formally described by a path integral involving a Euclidean Supersymmetric action and how an effective average action functional Gamma of chi, incorporating the effects of the fluctuating force and encoding all statistical properties of the process, can be calculated using functional Renormalisation Group methods. We emphasized the importance of utilizing the underlying symmetries of the problem, paying attention to the boundary terms which are often dropped, and showed how these can correctly incorporate any initial condition and, correspondingly, non-equilibrium evolution. The fRG flow equations were written down for the first two orders of the widely used derivative expansion of the effective action, referred to as the Local Potential Approximation (LPA) and Wavefunction Renormalisation (WFR). We used a particular type of regulator, the frequency independent Callan-Symanzik regulator, for which the flow equations take on a relatively simple form, and further recalled that obtaining flow equations within the supersymmetric framework is convenient for ensuring compatibility with the Boltzmann equilibrium distribution, something that is not a priori obvious or guaranteed if one starts with the Onsager-Machlup form of the action (thirty) and considers it a Euclidean N equals one scalar theory in one dimension with the Schrödinger potential U bar equals Upsilon over four V double prime, minus one over four open bracket V prime close bracket squared. We also reviewed how Brownian motion can be solved using a spectral expansion method of the Fokker-Planck (F-P) equation in a standard way.

The Effective Action I allows one to derive effective equations of motion for the average position, chi of t is equivalent to the average of x of t, and variance, the average of x squared of t, in an analogous manner to the classical equations of motion, by taking variational derivatives. We used the LPA and WFR to compute the elements entering the effective equation of motion, for instance the dynamical effective potential. We verified the accuracy of the equilibrium limit to these equations, further emphasizing the physical significance of certain aspects of the effective potential V sub k equals zero: namely how the minimum of V sub k equals zero corresponds to the equilibrium position and its second derivative evaluated at this point to the variance through equation one hundred twenty-eight. We noted here that while the LPA reproduces these equilibrium quantities, the accuracy of covariance's temporal evolution diminished as temperature was lowered.

Going beyond equilibrium, we examined how LPA plus WFR handle relaxation towards it for the average position X of t in potentials such as a polynomial, a doublewell comprised of two Lennard-Jones type interactions, or a bare x squared plus gaussian bumps. The latter potential clearly demonstrates that the FRG is capable of capturing the effect of the non-trivial local features of this potential. In fact, the FRG could still offer reasonable approximations even in those cases where the Fokker-Planck numerics failed to converge. We have also shown how the FRG can closely match the relaxation of the variance x squared of t to its equilibrium value: for both the unequal Lennard-Jones type potential and the x squared plus gaussian bumps, the LPA variance has reasonable accuracy and still captures highly non-trivial behavior such as the variance overshooting its equilibrium value before settling to it. This is in a system where numerically solving the Fokker-Planck equation failed to provide good results, at least using standard methods. Again, we find that accuracy decreases with decreasing temperature.

A clear conclusion that can be drawn from the above investigations is that decreasing the temperature negatively impacts the accuracy of using the LPA plus WFR derivative expansion for the FRG to describe Brownian motion in the potentials we examined. This appears to correlate with the increasing importance at lower temperatures of higher order terms in the spectral expansion; indeed, it is expected that the lowest order terms in the derivative expansion, LPA plus WFR, are best placed to describe evolution dominated by the lowest non-zero eigenvalues of the Fokker-Planck spectral expansion. It would seem that the derivative expansion of the FRG for studying thermal fluctuations has utility in the range from moderate temperatures, roughly when the classical force is comparable to the noise, up to the very high temperature regime where the small local features of the potential become less relevant.

Although our conclusions on the temperature dependent relation between the spectral expansion and the derivative expansion of the FRG are suggestive and reasonable given the premise of the latter, a more precise quantitative comparison would be called for and should be addressed in future work. The insights gained from a more detailed, quantitative understanding of the FRG's range of validity when applied to the dynamical studies of thermally driven systems may lead to interesting and important applications. There are also issues relevant to the technicalities of applying the FRG programme and which may lead to better convergence properties. For example, the recent findings suggest that an appropriately optimized regulator, which also excludes the regime w greater than k from contributing to the flow, can ensure good convergence properties and a sizeable radius of convergence. Comparisons are non-trivial because the supersymmetry of the Brownian motion problem makes the structure of the flow equations different to that of a simple scalar theory. This is an important question to be resolved however and we hope to return to it in future work.

Future work could also examine if higher order approximations beyond the WFR offer any advantage, as these might better capture higher order terms in a spectral expansion. One could further investigate an ensemble of initial conditions and try to quantify better the computational time gain the FRG offers. It is worthwhile trying to see if there is a more concrete way to determine a priori which systems will be well described by the FRG before having to compare to numerical simulations or doing a spectral expansion analysis. An interesting application that we did not touch upon here might be thermal barrier escape, which in this formulation seems to be more akin to tunneling in the corresponding euclidean quantum mechanics; it would indeed be interesting to flesh out any analogies, if they exist. Most importantly, further understanding the application of FRG techniques to stochastically driven systems may allow extension to systems with more degrees of freedom, such as field theories and or systems with a large number of particles. Advances in the above directions may lead to progress in theoretically tackling a broad range of physical phenomena with large separation between fundamental timescales of thermal fluctuations and long emergent timescales of macroscopic change, addressing what is now a major barrier for predictive simulations across scientific and engineering disciplines including materials science, drug design, protein folding, and cosmology.


## Appendix A: The equilibrium flow equation

In equilibrium, all equal-time expectation values can be obtained from the generating function

Z of J equals integral over d x e to the power of negative two V of x divided by r plus J x.

in a manner directly analogous to that described in the text but with functional derivatives replaced by ordinary derivatives with respect to J. In a spirit identical to the renormalisation group but in the much simpler setting of one just degree of freedom, we can define a modified generating functional.

Z sub k of J equals integral dx e to the power of negative two V of x over Upsilon minus one-half R of k x squared plus Jx with an additional quadratic term controlled by an arbitrary function R of k of a parameter k, satisfying limit as k approaches zero R of k equals zero, giving back the original Z of J. Correlation functions are generated by W sub k of J equals ln Z sub k of J via chi sub k equivalent to the expectation value of x sub k equals the partial derivative of W sub k of J with respect to J, the expectation value of x squared sub k minus chi sub k squared equals the partial derivative squared of W sub k of J with respect to J squared et cetera. In the limit k equals zero and after setting J equals zero the usual predictions of the equilibrium Boltzmann distribution are recovered.

The source J has been considered as an external, inde- pendent variable controlling expectation values such as chi and higher correlators. One could also consider chi as the independent variable, solving chi equals the partial derivative of W with respect to J for J of chi and defining the effective potential U of chi via a Legendre transform

Gamma sub k of chi plus W sub k of J equals J chi minus one-half R of k chi squared

Gamma of chi equivalent to two U of chi over Upsilon

The partial derivative of Gamma sub k with respect to chi equals J sub k minus R of k chi implying that the minimum of the effective potential de- fines the equilibrium expectation value of x (at J equals zero and k equals limit d k equals zero). Generating function W sub k of J on k can be easily obtained as

The partial derivative sub k W sub k of J equals negative one-half partial derivative sub k R times the quantity partial derivative squared W sub k of J with respect to J squared plus the quantity partial derivative W sub k of J with respect to J squared which is an "RG equation" for W sub k of J. We can also obtain an equation determining how Gamma sub k of chi runs with k. Recip- rocally, taking chi independent variable, J becomes the derivative function of chi and k. Taking a k derivative of (A6) at fixed chi we obtain

The partial derivative sub k Gamma sub k of chi equals one-half partial derivative sub k R times the partial derivative squared W sub k with respect to J squared

To express the right-hand side in terms of Gamma sub k of chi, consider the first relation of (A3). Taking a chi derivative we find

The quantity partial derivative squared Gamma sub k with respect to chi squared plus R times partial derivative squared W sub k with respect to J squared equals one

Hence, the "RG flow" of Gamma is determined by

The partial derivative sub k Gamma sub k of chi equals one-half partial derivative sub k R times the quantity partial derivative squared Gamma with respect to chi squared plus R to the negative one

Note also that, at k approaches zero the expectation value of x squared minus chi squared equals Upsilon over two partial derivatives with respect to chi squared U of chi sub eq and hence the variance at equilibrium is determined by the curvature of the effective potential around its minimum.

All the above manipulations can be generalized to many or even infinite degrees of freedom and continuum actions, leading to the Wetterich equation which is directly equivalent to equation A ten, and the relations of section four A. For this work it is important to note that the equilibrium effective potential U of chi discussed here obeys the LPA flow equation exactly if we choose

R of k equals k. Appendix B: Derivation of the two point function


## We start from equation one hundred thirteen repeated here for clarity:

the second derivative with respect to t minus Q of t times G of t, t prime equals negative Upsilon divided by P of t times delta of t minus t prime (B one)

Where Q of t equals the script U of chi of t is given by equation one hundred fourteen and P of t equals one or zeta sub chi squared of chi of t for LPA and WFR respectively. If we now consider the homogeneous version of equation B one:

the second derivative of f of t minus Q of t times f of t equals zero (B two)

script W of t is defined as Y one of t times the first derivative of Y two of t minus the first derivative of Y one of t times Y two of t equals constant (B three)

We take Y one of t to be the growing solution and Y two of t to be the decaying solution. Substituting the ansatz G of t, t prime equals Y one of t times F of t, t prime where F is some function to be determined into equation B one we obtain: the first derivative of F of t, t prime equals one divided by Y one squared of t times the negative Upsilon times Y one of t prime divided by P of t prime times theta of t minus t prime plus C one of t prime (B four)

where theta of t minus t prime is the Heaviside step function and C one of t prime is a 'constant-of-integration' function of t prime to be determined. If we now integrate equation B four we obtain the following expression for

G of t, t prime: G of t, t prime equals negative Upsilon times Y one of t divided by P of t prime times the quantity theta of t minus t prime times the integral from t prime to t of Y one of t prime divided by Y one squared of u d u plus C two of t prime plus C one of t prime times Y one of t times the integral from t to u of d u divided by Y one squared of u (B five)

where C sub two left parenthesis t prime right parenthesis is another 'constant-of-integration' function of t prime to be determined. To compute the integrals in B five we note that by the definition of the Wronskian:

Y sub one left parenthesis t right parenthesis integral from nothing to t left parenthesis vertical bar W left parenthesis u right parenthesis divided by Y sub one squared left parenthesis u right parenthesis vertical bar right parenthesis d u equals mu Y sub one left parenthesis t right parenthesis plus Y sub two left parenthesis t right parenthesis B six where mu is simply a constant of integration. As the Wronskian is constant here we can simply write:

Y sub one left parenthesis t right parenthesis integral from nothing to t left parenthesis d u divided by Y sub one squared left parenthesis u right parenthesis vertical bar right parenthesis equals one divided by W left parenthesis mu Y sub one left parenthesis t right parenthesis plus Y sub two left parenthesis t right parenthesis right parenthesis B seven such that B five becomes:

G left parenthesis t comma t prime right parenthesis equals Upsilon divided by W P left parenthesis t prime right parenthesis left parenthesis bar C sub one left parenthesis t prime right parenthesis Y sub two left parenthesis t right parenthesis plus bar C sub two left parenthesis t prime right parenthesis Y sub one left parenthesis t right parenthesis right parenthesis left parenthesis plus theta left parenthesis t minus t prime right parenthesis left parenthesis Y sub one left parenthesis t right parenthesis Y sub two left parenthesis t prime right parenthesis minus Y sub one left parenthesis t prime right parenthesis Y sub two left parenthesis t right parenthesis right parenthesis right parenthesis B eight where C sub one and C sub two have been rescaled to bar C sub one and bar C sub two in order to absorb some irrelevant constant factors. We note that the functions bar C sub i can only be linear combinations of Y sub one and

Y sub two colon bar C sub one left parenthesis t prime right parenthesis equals alpha Y sub one left parenthesis t prime right parenthesis plus beta Y sub two left parenthesis t prime right parenthesis bar C sub two left parenthesis t prime right parenthesis equals gamma Y sub one left parenthesis t prime right parenthesis plus delta Y sub two left parenthesis t prime right parenthesis B nine B ten where the constants alpha comma beta comma gamma and delta will be determined later. Combining all this together we obtain the most general solution:

G left parenthesis t comma t prime right parenthesis equals Upsilon divided by W P left parenthesis t prime right parenthesis left parenthesis left bracket alpha minus theta left parenthesis t minus t prime right parenthesis right bracket Y sub one left parenthesis t prime right parenthesis Y sub two left parenthesis t right parenthesis plus beta Y sub two left parenthesis t prime right parenthesis Y sub two left parenthesis t right parenthesis plus gamma Y sub one left parenthesis t prime right parenthesis Y sub one left parenthesis t right parenthesis left parenthesis plus left bracket delta plus theta left parenthesis t minus t prime right parenthesis right bracket Y sub two left parenthesis t prime right parenthesis Y sub one left parenthesis t right parenthesis right parenthesis B eleven

To obtain the values of the constants we must now impose physical conditions:

One. G left parenthesis t comma t right parenthesis should remain finite as t approaches infinity i.e. an equilibrium distribution exists at late times implies gamma equals zero. Two. Covariance G left parenthesis t comma zero right parenthesis should remain finite as t approaches infinity implies delta equals negative one. Three. The equilibrium form of G left parenthesis t comma t prime right parenthesis should be symmetric under t reversible arrow t prime implies alpha equals zero. Four. Setting the initial condition to be G left parenthesis zero comma zero right parenthesis equals G sub zero zero implies

These give us the two point function:

G of T, T prime equals upsilon over two lambda P of T prime times open bracket theta of T minus T prime close bracket Y tilde sub one of T prime Y tilde sub two of T plus theta of T prime minus T Y tilde sub two of T prime Y tilde sub one of T close bracket plus P of zero over P of T prime times open bracket G sub zero zero minus upsilon over two lambda P of zero close bracket Y tilde sub two of T prime Y tilde sub two of T (B twelve)

where Y tilde sub I of T is defined as Y sub I of T over Y sub I of zero and we have normalized the Wronskian as script W equals negative two lambda Y sub one of zero Y sub two of zero (B thirteen)

which is the value at equilibrium when

Q of T approaches lambda squared, Equation (B twelve) has two important limits: The Variance

T prime approaches T: Var of X is defined as G of T, T equals upsilon over two lambda P of T Y tilde sub one of T Y tilde sub two of T plus P of zero over P of T open bracket G sub zero zero minus upsilon over two lambda P of zero close bracket Y tilde sub two squared of T (B fourteen)

and the Covariance T prime approaches zero, T greater than zero:

Cov of X of zero X of T is defined as G of T, zero equals G sub zero zero Y tilde sub two of T (B fifteen)

Equations (B fourteen) and (B fifteen) are the main results of this appendix.


## Appendix C: Explicit computation of the determinant

In this appendix we recall the computations explicitly showing that

M equals integral script D c script D bar c exp open bracket integral D T bar c of partial T plus V comma X X c close bracket proportional to exp open bracket one half integral D T V comma X X close bracket det

(C one)

when the boundary conditions c of T sub in equals zero, quad bar c of T sub f equals zero (C two)

are chosen. We first work with the more general condition c of T sub in equals e to the power of negative i nu c of T sub f, quad e to the power of negative i nu bar c of T sub in equals bar c of T sub f (C three)

From here onwards we will be working in the time interval T in open bracket zero, T close bracket to simplify notation. Note that such a boundary condition ensures that integral from zero to T D T d by d T of open bracket bar c c close bracket equals zero (C four)

allowing us to write det M equals integral script D c script D bar c exp open bracket one half integral from zero to T D T open bracket c, bar c close bracket of zero over F minus F dagger over zero open bracket c, bar c close bracket close bracket (C five)

where

F equals Ot plus V,XX, F equals negative Ot plus V,XX

(C six)

Therefore the operator in the exponent of (C five) is self-adjoint and the path integral is properly defined. The eigenfunctions and eigenvalues of F and F dagger

Fun equals anUn, Flvn equals anUn

(C seven)

zero one T

one an equals i open bracket two pi eta plus one close bracket T plus T

(C eight)

n equals zero, plus minus one, plus minus two, ... and

Un of T equals V T one exp

(C nine)

zero D T open bracket an minus V comma z close bracket T

Un of T is equal to V T one exp

(C ten)

They form an orthonormal and complete set zero T D T um of T Un of T equals zero mn

Un of t times Un of t prime equals delta of t minus t prime

Expanding c in Un and c in Un with Grassmann coefficients bn and bn respectively, we can represent the determinant as

Using (C eight) we have n equals negative eight Pi an times which gives zero D T V one equals T

one two