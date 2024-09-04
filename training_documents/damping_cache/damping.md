## Research Article On a Nonlocal Damping Model in Ferromagnetism

We consider a mathematical model describing nonlocal damping in magnetization dynamics. The model consists of a modified form of the Landau-Lifshitz-Gilbert equation for the evolution of the magnetization vector in a rigid ferromagnet. We give a global existence result and characterize the long time behaviour of the obtained solutions. The sensitivity of the model with respect to large and small nonlocal damping parameters is also discussed.


## One. Introduction and Preliminary Results

In this work, we are dealing with a mathematical model arising in the theory of magnetization dynamics with nonlocal damping. We will consider the model proposed by Nembach et al. It is given by a modified Landau-Lifshitz-Gilbert equation. The modification lies in the presence of a second-order space derivative of magnetization in the effective field. To describe the model equations, we consider section two of R cubed a bounded and regular open set of R cubed. The generic point of R cubed is denoted by x. We assume that a ferromagnetic material occupies the domain two.

In what follows, S two represents the unit sphere of R cubed. The magnetization field of the ferromagnetic material which belongs to S two almost everywhere is denoted by M of t and x. Its evolution is governed by the following modified Landau-Lifshitz-Gilbert equation.

One plus alpha squared times the partial derivative of M with respect to t minus alpha times the cross product of M and the effective field equals negative M cross the effective field.

The first equation in the set of t between zero and T times Q.

Subject to initial conditions

M of zero and x equals M naught of x in Q.

and boundary conditions

Cross product of M and the normal derivative of the effective field at the boundary plus alpha times partial M with respect to t equals zero on the boundary of Q.

where the symbol x denotes the vector cross product in R cubed. The positive constant alpha represents the damping parameter. The effective magnetic field H depends on M and is given by

H of M equals D times Laplacian of M plus the Gilbert term times the cross product of M and M plus Lee term of M plus the demagnetizing field.

The first term on the right-hand side of the fourth equation is called the exchange magnetic field, where the positive constant D is the exchange coefficient and the term parameterized by the positive constant describes nonlocal damping in ferromagnets. The term was introduced in past studies. The third term is the bulk anisotropy field, which generally is taken as linear with respect to M, and the demagnetizing field satisfies in the set of t between zero and T times R cubed the stray field equation divergence of demagnetizing field plus M equals zero, curl of demagnetizing field equals zero.

The fifth equation where M is the extension by zero of M outside the magnetic domain Q.

Notice that, for the sake of simplicity, the bulk uniaxial anisotropy field, generally taken as linear in M, and the magnetostatic field which satisfy the stray field equation are not considered since they only induce more computations and have no mathematical influence on the results we obtain.

We define the energy

The energy C of t equals D times the integral over the set of the magnitude of the gradient of M squared with respect to x.

The following energy estimate holds.

Lemma One. If M is a solution of problem one, then it satisfies, at least formally, the energy estimate

The time derivative of energy of t plus two times zeta times the integral over the set of the magnitude of the partial time derivative of M squared with respect to x plus two alpha over one plus alpha squared times the integral over the set of the magnitude of the partial time derivative of M squared with respect to x equals zero.

Proof. The techniques to obtain the seventh equation are analogous to those used, for example, in past studies. We rewrite Landau-Lifshitz-Gilbert equation one in the following form:

The term alpha times the partial time derivative of M minus the term one plus alpha squared times H equals alpha times M cross the term alpha times the partial time derivative of M minus the term one plus alpha squared times H minus the term one plus alpha squared times H.

Multiplying the eighth equation by the term alpha times the partial time derivative of M minus the term one plus alpha squared times H and using the saturation constraint magnitude of M squared equals one almost everywhere yields to alpha over one plus alpha squared times the magnitude of the partial time derivative of M squared equals H dot product with the partial time derivative of M.

Integrating the ninth equation on the set, the right-hand side of the ninth equation becomes

The tenth equation

The integral over the set of H dot product with the partial time derivative of M with respect to x equals negative D times the integral over the set of the partial time derivative of M times the second partial time derivative of M with respect to x minus zeta times the integral over the set of the partial spatial derivative of the partial time derivative of M squared with respect to x plus the integral over the boundary of the set of D times the partial normal derivative of M plus zeta times the partial normal derivative of the partial time derivative of M times the partial time derivative of M with respect to the boundary, where we have used the summation convention that repeated indices are summed over and partial sub i denotes the derivative with respect to space variable x. Converting the two last terms of the right-hand side of the tenth equation allows us to get

Seven. Before dealing with problem one, let us first review some previous results. We limit ourselves to mentioning a handful of references concerning existence and we refer to the survey for a more detailed bibliographical account. The general framework although without nonlocal damping, that is, the case zeta equals zero has been established in earlier papers using Faedo-Galerkin/Penalization method. This method gives an approximated sequence of solutions converging to a global solution of the problem. Next results concern systems with further dissipation terms. For example, the modification considered consists in adding to the standard dissipation term in the LLG equation another higher-order term of the type Delta squared M. The Faedo-Galerkin method is also used to solve the problem. In a model with dry-friction dissipation, which is accounted by adding a dry-friction-like term to the standard Gilbert damping,


## Journal of Applied Mathematics

is studied. Let us mention that a model of ferromagnetic material with hysteresis effects is studied. In this model, the magnetic moment behavior is described by the nonlinear Landau-Lifshitz equation with an additional term modeling the hysteresis. This term takes the form of a maximal monotone operator acting on the time derivative of the magnetic moment. For this relaxed model, local existence of regular solutions is proved. Note that in the framework of current-induced magnetization dynamics, the work addresses global existence of weak solutions to a LLG equation where a transport term is added to effective field taking into account the effect of the injected current. A model of magnetization switching with inertial effects modeled by means of a second-order time derivative term in the effective field is considered where existence of weak solutions and their long time behavior was established. All these proofs are based on some penalization and using various kinds of regularizations.

To state the existence result, we start with the definition of weak solutions to problem one.

Definition two. Given that M sub zero belongs to the space H one of Omega such that absolute value M sub zero equals one almost everywhere over Omega, we call M of t, x a weak solution to LLG equation one for all T greater than zero, M belongs to the space L infinity over the interval zero to T in H one of Omega, partial t M belongs to L two over the interval zero to T in L two of Omega intersecting L infinity over the interval zero to T in L two of Omega, and M satisfies the saturation constraint absolute value M of t, x equals one for almost everywhere in

R plus cross Omega two M of zero equals M sub zero in the trace sense;

three for all G in the space H one of Q intersecting C zero of Q, there holds one over one plus alpha squared integral over Q of the quantity partial t M minus alpha M cross partial t M dotted with G dx dt equals D integral over Q of M cross partial i M dotted with partial i G dx dt plus zeta integral over O of M cross partial i partial t M dotted with partial i G dx dt four for all t greater than or equal to zero we have eight of t plus two zeta integral from zero to t integral over Omega of the absolute value of gradient partial t M squared dx plus two alpha over one plus alpha squared integral from zero to t integral over Omega of the absolute value of partial t M squared dx dt is less than or equal to eight of zero,

where ampersand of t is given by six. We have the following global existence result.

Theorem three. Let M sub zero belong to the space H one of Omega be such that absolute value M sub zero of x squared equals one almost everywhere. Then there exists a global weak solution M of problem one in the sense of Definition two.

Proof. The proof follows a standard scheme Faedo-Galerkin method with a penalization of the saturation constraint as usual in general Landau-Lifshitz-Gilbert equation.


## Journal of Applied Mathematics

The rest of the paper is divided as follows. In the next section we investigate the long time behavior of the solutions. Section Three discusses the sensitivity of the obtained solutions with respect to nonlocal damping factor zeta. More precisely we characterize the limit problem for both high and small zeta. We conclude the paper in Section Four by giving some comments.


## Two. The Limit as t Goes to Plus Infinity

We investigate the long time behavior of the solutions. More precisely, we study the w-limit set of the trajectories and characterize the at-limit points as solutions of a suitable stationary problem. We proceed as in Carbou-Fabrie.

Let M be a weak solution of one. We call w-limit set of the trajectory M the following set:

omega left parenthesis M right parenthesis equals left brace m in double-struck H superscript one left parenthesis Omega right parenthesis comma exists t subscript n comma limit subscript n rightwards arrow plus infinity t subscript n equals plus infinity comma M left parenthesis t subscript n comma dot right parenthesis right brace.

- m in double-struck H superscript one left parenthesis Omega right parenthesis weakly.

Consider a weak solution M of one. From the energy estimate twelve, the at-limit set omega left parenthesis M right parenthesis is nonempty. We denote by fraktur m a point of this set. There exists a nondecreasing sequence left parenthesis t subscript n right parenthesis subscript n comma such that t subscript n rightwards arrow plus infinity and M left parenthesis t subscript n comma dot right parenthesis right harpoon above m in widetilde Vdash l superscript one left parenthesis Omega right parenthesis weakly. Since Omega is a smooth bounded domain, then M left parenthesis t subscript n comma dot right parenthesis tends to m in double-struck L superscript p left parenthesis Omega right parenthesis strongly for p in left bracket one comma six left bracket comma text and right period right. extracting a subsequence, we assume that M left parenthesis t subscript n comma dot right parenthesis tends to fraktur m almost everywhere, so that the saturation constraint absolute value m equals one is satisfied almost everywhere. In addition, we remark that, for all n comma absolute value M left parenthesis t subscript n comma dot right parenthesis equals one almost everywhere, so that double-vertical-bar M left parenthesis t subscript n comma dot right parenthesis double-vertical-bar subscript L superscript infinity left parenthesis Omega right parenthesis equals one. By interpolation inequalities in double-struck L superscript p spaces, we obtain that, for all p less than plus infinity comma M left parenthesis t subscript n comma dot right parenthesis tends to m in double-struck L superscript P left parenthesis Omega right parenthesis strongly.

For s in left parenthesis negative one comma one right parenthesis and x in Omega we define for n large enough m subscript n left parenthesis s comma x right parenthesis equals M left parenthesis t subscript n plus s comma x right parenthesis period.

We have the following convergence result.

Lemma four. The sequence left parenthesis m subscript n right parenthesis subscript n greater than or equal to one satisfies the following convergences:

m subscript n long rightwards arrow m quad in L squared left parenthesis left parenthesis negative one comma one right parenthesis times Omega right parenthesis strongly comma m subscript n right harpoon above m quad in L squared left parenthesis left parenthesis negative one comma one right parenthesis semicolon double-struck H superscript one left parenthesis Omega right parenthesis right parenthesis weakly.

Proof. Following fourteen, we have the estimate one half Integral from negative one to one Integral from Omega absolute value m subscript n left parenthesis s comma x right parenthesis minus M left parenthesis t subscript n comma x right parenthesis absolute value squared d x d s less than or equal to Integral from t subscript n minus one to plus infinity Integral from Omega absolute value partial-differential subscript t M left parenthesis tau comma x right parenthesis absolute value squared d x d tau. partial-differential subscript t M lies in L squared left parenthesis R plus times Omega right parenthesis comma one gets limit subscript n rightwards arrow plus infinity one half Integral from negative one to one Integral from Omega absolute value m subscript n left parenthesis s comma x right parenthesis minus M left parenthesis t subscript n comma s right parenthesis absolute value squared d x d s equals zero.

Since M left parenthesis t subscript n comma dot right parenthesis tends to m in L squared left parenthesis Omega right parenthesis strongly, m subscript n tend to m in double-struck L squared left parenthesis left parenthesis negative one comma one right parenthesis semicolon double-struck L squared left parenthesis Omega right parenthesis right parenthesis strongly. Moreover, we have obviously seen that the gradient of m sub n for n greater than or equal to one is bounded in L two of negative one to one times Omega so there exists a subsequence still denoted by m sub n for n greater than or equal to one such that m sub r tends to m in L two of negative one to one in one of Omega weakly and in the double-struck L two of negative one to one in double-struck L two of Omega strongly almost everywhere in negative one to one times Omega. This ends the proof of the lemma.

Now, we consider a function rho in script C sub zero infinity of negative one to one such that zero is less than or equal to rho of tau is less than or equal to one, the absolute value of rho prime of tau is less than or equal to two. In the weak formulation eleven we take as test function G of t, x equals rho of t minus t sub n Psi of x, where Psi is a function lying in script D of closure of Omega and n fixed. We obtain after the change of variables s equals t minus t sub n one over one plus alpha squared times the integral from negative one to one the integral over Omega of partial t m sub n of s, x minus alpha m sub n of s, x times partial t m sub n of s, x. Multiplying by Psi of x rho of s d x d s minus D integral from negative one to one the integral over Omega m sub n of s, x times partial t m sub n of s, x multiplied by partial t Psi of x rho of s d x d s minus zeta integral from negative one to one the integral over Omega m sub n of s, x times partial i of partial t m sub n of s, x multiplied by partial i Psi of x rho of s d x d s equation eighteen

We take the limit of the previous equation when N tends to positive infinity. In order to pass to the limit, we bound each term of the above formulation. For example, for the last term we have absolute value of the integral from negative one to one of the integral over omega of M sub N of S comma X times partial sub I partial sub T M sub N of S comma X dot partial sub I Psi of X rho of S D X D S is less than or equal to the integral from negative one to one of the integral over omega of the absolute value of M sub N of S comma X times partial sub I partial sub T M sub N of S comma X absolute value of partial sub I Psi of X times absolute value of rho of S D X D S less than or equal to the integral from negative one to one of the integral over omega of the absolute value of M sub N of S comma X times partial sub I partial sub T M sub N of S comma X absolute value of partial sub I Psi of X D X D S less than or equal to the square root of the integral from negative one to one of the integral over omega of the absolute value of M sub N of S comma X times partial sub I partial sub T M sub N of S comma X squared D X D S raised to the power of one half times the integral from negative one to one of the integral over omega of the absolute value of partial sub I Psi of X squared D X D S raised to the power of one half less than or equal to the square root of the integral from negative one to one of the integral over omega of the absolute value of partial sub I partial sub T M sub N of S comma X squared D X D S raised to the power of one half times the integral from negative one to one of the integral over omega of the absolute value of partial sub I Psi of X squared D X D S raised to the power of one half less than or equal to the square root of two times the integral from T sub N minus one to T sub N plus one of the integral over omega of the absolute value of partial sub I partial sub T M of S comma X squared D X D S raised to the power of one half times the integral over omega of the absolute value of partial sub I Psi of X squared D X raised to the power of one half. (nineteen)

Since V partial sub T M belongs to L squared left parenthesis R plus times omega right parenthesis, this last term tends to zero as N goes to positive infinity. In the same way we pass to the limit in the other terms to obtain the integral from negative one to one of rho of S D S the integral over omega of M of X times partial sub I M of X dot partial sub I Psi of X D X equals zero, (twenty)

which implies the integral over omega of M of X times partial sub I M of X dot partial sub I Psi of X D X equals zero, (twenty-one)

for all

Psi element of script D left parenthesis bar omega right parenthesis. We proved the following.

Theorem five. If M is a weak solution of open parenthesis one close parenthesis, then each point M in omega left parenthesis M right parenthesis is a weak solution of the steady state system

M element of left bracket K right bracket to the power of one left parenthesis omega right parenthesis semicolon absolute value of M equals one, almost everywhere M times delta M equals zero in omega (twenty-two)

which should be understood in the weak sense (twenty-one).

Remark six. The solutions of (twenty-two) are known as harmonic maps to the unit sphere, which turn up in several equations in physics, such as Ginzburg-Landau equation, and were extensively investigated mathematically in the past decades due to their importance both in mathematics and in many applied fields; see, for example, Some results on the dynamic version of (twenty-two) can be found.


## Three. Limiting Process for High and Small Nonlocal Damping

We first analyze the limiting process when zeta goes to positive infinity. We denote by M to the power of zeta a global weak solution of LLG equation (one) associated with zeta and the initial data M sub zero and satisfying the energy inequality (seven). We have the estimates.

Lemma seven. There exists C greater than zero independent of zeta such that the sequence M to the power of zeta satisfies the estimates

Modulus of M superscript zeta as a function of t and x squared equals one almost everywhere, Norm of gradient M superscript zeta subscript L superscript infinity of the positive real numbers to L superscript two of Omega is less than or equal to constant, Norm of gradient partial t M superscript zeta in L squared of the positive real numbers to L squared of Omega is less than or equal to C zeta superscript negative one, Norm of partial t M superscript zeta in L squared of the positive real numbers to L squared of Omega is less than or equal to constant.

We also have the following.


## Lemma eight. The sequence M superscript zeta is compact in

L subscript loc superscript two of the positive real numbers to L squared of Omega. Lemmas seven and eight imply the following convergence results.

Lemma nine. There exists a subsequence still denoted by m superscript zeta such that

Twenty-four

M superscript zeta weakly star converges to M in L superscript infinity of the positive real numbers to H superscript one of Omega, Partial t M superscript zeta weakly converges to partial t M in L squared of the positive real numbers to H superscript negative one of Omega, Gradient M superscript zeta weakly converges to gradient M in L squared of the positive real numbers to L squared of Omega, Gradient partial t M superscript zeta strongly converges to zero in L subscript loc superscript squared of the positive real numbers to L squared of Omega, Partial t M superscript zeta strongly converges to zero in L subscript loc superscript squared of the positive real numbers to L squared of Omega, M superscript zeta strongly converges to M in L subscript loc superscript squared of the positive real numbers to lowercase l squared of Omega. Moreover, M satisfies the saturation condition modulus of M equals one.

The above convergences allow one to conclude.

Theorem ten. Let M be the limit of a subsequence of M superscript zeta as zeta goes to positive infinity. Then, the domain Omega is uniformly magnetized.

Remark eleven. The result of Theorem ten is of interest. In fact, the added term in the effective field can act as a control for magnetization switching.

Our aim now is to pass to the limit as zeta goes to zero in one. We denote by M superscript zeta a global weak solution of LLG equation one associated with zeta and the initial data M subscript zero and satisfying the energy inequality seven. The bound on square root of zeta times gradient partial t M superscript zeta in L squared of zero to tilde T semicolon L squared of Omega allows one to get the following.

Theorem twelve. Let M be the limit of a subsequence of M superscript zeta. Then, M satisfies

Partial t M minus alpha M times partial t M equals negative one plus alpha squared M times D Laplace M in positive real numbers times Omega, M of zero equals M subscript zero in Omega, M times D partial n M equals zero on the boundary of Omega.

Twenty-five

Moreover, M satisfies the saturation condition modulus of M of t and x equals one almost everywhere.

Remark thirteen. From twenty-five, we can say that, for lower values of zeta, the magnetic nonlocal damping vanishes and the classical switching continues forever. In other words, the magnetization precesses several times around the effective field direction before it reaches equilibrium.


## Four. Concluding Remarks

In this paper, we have considered nonlocal damping in magnetization dynamics. The model consists of a generalized LLG equation that contains a term characterizing nonlocal damping expressed in terms of Laplace partial t M in the effective field. The long time behaviour of the solutions is characterized and the sensitivity of the model to nonlocal damping parameter is discussed. The results obtained can be applied without difficulty to the case of effective field with anisotropy and demagnetizing fields. Note that the model considered in this paper neglects the additional damping due to transversal spin currents whose form is M cross O comma M. In this case the LLG equation takes the following form.

M minus M cross M equals negative one plus X squared M

times the amplitude of A M plus delta O comma M plus zeta M cross O comma M.

Interestingly, the additional damping cannot be written in terms of the free energy, and therefore it cannot be derived from the functional derivative of the free energy with respect to the local magnetization. This new term can significantly change the domain-wall structure in ferromagnetic materials. It would be interesting to consider this problem from both the theoretical and the numerical points of view. In particular, global existence of weak solutions will require more detailed studies.

We finally mention that an important progress was done to design schemes constructing the weak solutions to the general LLG equation. Several schemes were proposed and their convergence to weak solutions was proved. A significant step forward in the convergence theory of numerical schemes has been done recently. This will be helpful to give a strategy for efficient computer implementation which may reflect the true nature of the augmentation of the LLG model considered in this paper.


## Conflict of Interests

The authors declare that there is no conflict of interests regarding the publication of this paper.