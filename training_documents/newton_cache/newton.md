## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Abstract

We consider solving large scale nonconvex optimisation problems with nonnegativity constraints. Such problems arise frequently in machine learning, such as nonnegative least-squares, nonnegative matrix factorisation, as well as problems with sparsity-inducing regularisation. In such settings, first-order methods, despite their simplicity, can be prohibitively slow on ill-conditioned problems or become trapped near saddle regions, while most second-order alternatives involve nontrivially challenging subproblems. The two-metric projection framework, initially proposed by Bertsekas, alleviates these issues and achieves the best of both worlds by combining projected gradient steps at the boundary of the feasible region with Newton steps in the interior in such a way that feasibility can be maintained by simple projection onto the nonnegative orthant. We develop extensions of the two-metric projection framework, which by inexactly solving the subproblems as well as employing non-positive curvature directions, are suitable for large scale and nonconvex settings. We obtain state-of-the-art convergence rates for various classes of nonconvex problems and demonstrate competitive practical performance on a variety of problems.


## One. Introduction

We consider high-dimensional problems of the form x in R d min f of x, subject to x greater than or equal to zero,

where d is much greater than one and f from R d to R is twice continuously differentiable and possibly nonconvex function. Despite the simplicity of its formulation, such problems arise in many applications in science, engineering, and machine learning. Typical examples in machine learning include nonnegative formulations of least-squares and matrix factorisation. Additionally, problems involving sparsity inducing regularisation such as l one norm, which are typically non-smooth, can be reformulated into a differentiable objective with nonnegativity constraints.

Many methods have been developed to solve x in R d min f of x, subject to x greater than or equal to zero. First-order methods, such as projected gradient descent, can be very simple to implement and as such are popular in machine learning. However, they come with well-known deficiencies, including relatively-slow convergence on ill-conditioned problems, sensitivity to hyper-parameter settings such as learning rate, and difficulty in escaping flat regions and saddle points. On the other hand, general purpose second-order algorithms, for example, projected Newton method and interior point methods, alleviate some of these issues such as susceptibility to ill-conditioning and or stagnation near flat regions. However, due to not leveraging the simplicity of the constraint, these advantages come at the cost of introducing highly non-trivial and challenging subproblems.

By exploiting the structure of the constraint in x in R d min f of x, subject to x greater than or equal to zero, Bertsekas proposed the two-metric projection framework as a natural and simple adaptation of the classical Newton's method for unconstrained problems. By judicious modification of the Hessian matrix, this framework can be effectively seen as projecting Newton's step onto the nonnegative orthant. This allows for the best of both worlds, blending the efficiency of classical Newton's method with the simplicity of projected gradient descent. Indeed, similar to the classical Newton's method, the subproblem amounts to solving a linear system, while like projected gradient-descent, the projection step is straightforward.

Contribution. In this paper, we design, theoretically analyse, and empirically evaluate novel two-metric projection type algorithms with desirable complexity guarantees for solving large scale and nonconvex optimisation problems with nonnegativity constraints. Both Algorithms One and Two are Hessian-free in that the subproblems are solved inexactly using the minimum residual method and only require Hessian-vector product evaluations. To achieve approximate first-order optimality, we leverage the theoretical properties of minimum residual, as recently established, for example, nonnegative curvature detection and monotonicity properties, and we show the following:

quire Hessian-vector product evaluations. To achieve ap- proximate first-order optimality (see Definition 2.1), we leverage the theoretical properties of MINRES, as recently established in (Liu & Roosta, 2022a), e.g., nonnegative cur- vature detection and monotonicity properties, and we show the following:

One. Under minimal assumptions, Algorithm One achieves global iteration complexity that matches those of first-order alternatives.

Two. Under stronger assumptions, Algorithm Two enjoys a global iteration complexity guarantee with an improved rate that matches the state of the art for second-order methods.

Three. Both variants obtain competitive oracle complexities, that is, the total number of gradient and Hessian-vector product evaluations.

Four. Our approach enjoys fast local convergence guarantees.

Five. Our approach exhibit highly competitive empirical performance on several machine learning problems.

To our knowledge, the complexity guarantees outlined in this paper are the first to be established for two-metric projection type algorithms in nonconvex settings.

Notation. Vectors and matrices are denoted, respectively, by bold lowercase and uppercase letters. Denote the non-negative orthant by R sub plus super d. The open ball of radius R around X is denoted by B left parenthesis x comma R right parenthesis triangleq left brace z in R super d such that double vert z minus x double vert less than R right brace. The inequalities, greater than or equal to and less than or equal to, are often applied element-wise. Big-O complexity is denoted by script O with hidden log- arithmic factors indicated by tilde script C. Denote components of vectors by superscript and iteration counters as subscripts, e.g., x sub k super i is i super th component of the k super th iterate of x. As a natural extension, a set of indices in the superscript de- notes the subvector corresponding to those components, e.g., letting left bracket d right bracket equals left brace one comma ellipsis comma d right brace, if script I is subseteq left bracket d right bracket and v in R super d then v super script I equals left parenthesis v super i mid i in script I right parenthesis in R super absolute value script I absolute value. Let g left parenthesis x right parenthesis equals nabla f left parenthesis x right parenthesis and H left parenthesis x right parenthesis equals nabla super two f left parenthesis x right parenthesis denote the gradient and Hessian of f, respectively. Denote the dk-active and &k-inactive sets, respectively, by script A left parenthesis x sub k comma delta sub k right parenthesis equals left brace i in left bracket d right bracket such that zero less than or equal to x sub k super i less than or equal to delta sub k right brace, (two a)

script I left parenthesis x sub k comma delta sub k right parenthesis equals left brace i in left bracket d right bracket mid x sub k super i greater than delta sub k right brace. (two b)

When the context is clear, we suppress the dependence on X sub k and delta sub k, e.g., g sub k and H sub k for g left parenthesis x sub k right parenthesis and H left parenthesis x sub k right parenthesis and x sub k super script I or x sub k super script I sub k instead of x sub k super script I left parenthesis x sub k comma delta sub k right parenthesis. We also denote

H sub k super script I equals left brace left parenthesis H sub k right parenthesis sub i j mid i comma j in right. left. script I left parenthesis x sub k comma delta sub k right parenthesis right brace. Two. Background and Related Work


## We now briefly review related works for solving one and some essential background necessary for our presentation.

First-order Methods. The projected gradient method is among the simplest techniques for solving optimisation problems involving convex constraints. Indeed, the projected gradient iteration for minimisation over a convex set Omega is simply given by x sub k plus one equals script P sub Omega left parenthesis x sub k minus alpha sub k g sub k right parenthesis where script P sub Omega colon R super d right arrow R super d is the orthogonal projection onto Omega defined by script P sub Omega left parenthesis x right parenthesis equals arg min sub z in Omega double vert z minus x double vert. When alpha sub k is chosen appropriately, e.g., via line search, the projected gradient method is known to converge under essentially the same conditions and at the same rate as the unconstrained variant. Many variations of this method have also been considered, e.g., spectral projected gradient, proximal gradient, and accelerated proximal gradient with its extensions to non-convex settings.

Of course, the effectiveness of the projected gradient method relies heavily on the computational cost associated with computing P subscript upper Omega left parenthesis x right parenthesis. While this can be challenging for general convex sets, in the case of upper Omega equals upper Real positive to the power of d, it is simply given by left bracket upper P left parenthesis x right parenthesis right bracket ^ { i } equals x ^ { i }, if x ^ { i } greater than zero, and left bracket upper P left parenthesis x right parenthesis right bracket ^ { i } equals zero, otherwise. Note that, for notational simplicity, we omit the dependence of upper P on upper Omega in our context. Nonetheless, while the projected gradient method is a simple choice for solving (one), it shares the common drawbacks of first-order methods alluded to earlier, such as susceptibility to ill-conditioning.

Second-order Methods. By incorporating Hessian information, second-order methods hold the promise to alleviate many of the well-known deficiencies of first-order alternatives, e.g., they are typically better suited to ill-conditioned problems. For constrained problems, generic projected (quasi) Newton methods involve iterations of the form X sub k plus one equals X sub k plus alpha sub k P sub k where

P sub k equals the argument minimize over X in Omega the inner product of g sub k and P plus the inner product of P and B sub k P over two,

where alpha sub k is an appropriately chosen step-size, e.g., backtracking line search, and B sub k captures some curvature information of f at X sub k (and also potentially the step-length as in the proximal arc search). For B sub k equals I we recover a projected gradient variant, whereas for B sub k equals H sub k, or some approximation, we obtain projected (or more generally proximal) Newton-type methods. The main drawback of this framework is that the subproblem may no longer be a simple projection even when Omega is a simple, and one has to resort to an optimisation subroutine to (approximately) solve.

An alternative is the interior point framework, where the constraints are directly integrated into the objective as "barrier" functions. While the subproblems in this framework amount to solving linear systems, to produce accurate solutions the barrier function must ap-


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

proach the constraint, which can lead to highly ill conditioned subproblems. Some recent works consider interior point methods for one. In particular, in capped Newton-CG with a preconditioned Hessian is used to optimise a log barrier augmented objective. Due to issues arising from increasingly ill-conditioned subproblems, the practical efficacy of this method seems to be inferior when compared to projection-based methods, including those of first-order.

The issue with the general purpose second-order methods discussed so far is that, unlike projected gradient, they do not leverage the simplicity of the nonnegativity constraints and the corresponding projection. In this light, a naïve adaptation of the projected gradient would imply directly projecting the Newton step on the constraints, e.g., X sub k plus one equals the projection over Omega of X sub k minus alpha sub k H sub k inverse g sub k. Unfortunately, such a direct adaptation may lead to ascent directions for the objective function at the boundary. To that end, the two-metric projection (TMP) framework offers an ingenious solution. Specifically, at each iteration, the component indices, ceiling D, are divided into the approximately bound, J sub k plus, and free sets, J sub k minus, given by

J sub k plus equals the set of i in D such that X sub k i is less than or equal to delta, g sub k i is greater than zero, J sub k minus equals D excluding J sub k plus where delta is greater than zero. A matrix, D sub k, is then chosen to be "diagonal" with respect to set J sub k plus, that is,

D sub k i j equals zero, i in J sub k plus, j in D excluding i, and the update is simply given by

X sub k plus one equals the projection of X sub k minus alpha sub k D sub k g sub k.

It has been shown that TMP is asymptotically convergent under certain conditions and reasonable choices of D sub k. For example, for strongly convex problems, the non-diagonal portion of D sub k can consist of the inverse of the Hessian sub-matrix corresponding to the indices in J sub k minus. In this case, the update reduces to a scaled gradient in J sub k plus and a Newton step in J sub k minus. Bertsekas also shows that, under certain conditions, TMP can preserve fast "Newton like" local convergence. Practically, TMP type algorithms have been successfully applied to a range of problems. In large scale and nonconvex settings, employing the Newton step as part of the update may be infeasible or even undesirable. Indeed, not only can Hessian storage and inversion costs be prohibitive, the existence of negative curvature can lead to ascent directions.

With a view to eliminate the necessity of forming and inverting the Hessian, Kim et al. extend TMP to utilize a quasi-Newton update with asymptotic convergence guarantees in the convex setting. Also in this vein, Xie and Wright considered "projected Newton-CG", which entails a combination of the projected gradient and the inexact Newton steps that preserve the simplicity of projection onto R plus to the power of D. In particular, Newton-CG steps are based on the capped CG procedure of Royer et al.. Unfortunately, the gradient and Newton-CG steps are not taken simultaneously. Instead, the algorithm employs projected gradient steps across all components until optimality is attained in the approximately active set. Only at that point is the Newton-CG step applied in the approximately inactive set. This implies that the algorithm may take projected gradient steps at most iterations, potentially impeding its practical performance.

Hessian-free Inexact Methods. In high-dimensional settings, storing the Hessian matrix may be impractical. Moreover, an approximate direction can often be computed at a fraction of the cost of a full Newton step. In this context, Hessian-free inexact Newton-type algorithms leverage Krylov subspace methods, which are particularly well-suited for these scenarios. Krylov subspace solvers can recover a reasonable approximate direction in just a few iterations and only require access to the Hessian-vector product mapping, V maps to H of X V. The computational cost of a Hessian-vector product is comparable to that of a gradient evaluation and does not require the explicit formation of H. Indeed, H of X V can be computed by obtaining the gradient of the map X maps to the inner product of G of X and V using automatic differentiation, leading to one additional back propagation compared to computing

G of X. Complexity in Optimisation. Recently, there has been a growing interest in obtaining global worst case iteration complexity guarantees for optimisation methods, namely a bound on the number of iterates required for the algorithm to compute an approximate solution. For instance, in unconstrained and nonconvex settings, gradient descent produces an approximate first-order optimal point satisfying the norm of G of X is less than or equal to Epsilon G in at most big O of Epsilon G to the power of negative two iterations for objectives with Lipschitz continuous gradients. This rate has been shown to be tight. Without additional assumptions, similar rates have also been shown for second-order methods. However, for objectives with both Lipschitz continuous gradient and Hessian, this rate can be improved to big O of Epsilon G to the power of negative three halves, which is also shown to be tight over a wide class of second-order algorithms. Second-order methods which achieve this rate include cubic regularised Newton's method and its adaptive variants, modified trust region based methods and line search methods including Newton-CG and Newton-MR as well as their inexact variants. Many of the above works also provide explicit bounds on the operational complexity, that is, a bound on the number


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

of fundamental computational units (e.g. gradient evaluations, Hessian vector products) to obtain an approximate solution.

In the constrained setting, direct comparison between bounds is difficult due to differences in approximate optimality conditions; see discussion in Xie and Wright for the bound constraint case. However, the algorithms in Cartis et al.; Birgin and Martínez achieve big O of Epsilon G to the power of three halves for a first-order optimal point with certain types of constraints, which is shown to be tight in Cartis et al.. More specific to the bound constraint case, the Newton-CG log barrier method of O'Neill and Wright achieves a complexity of big O of Deg to the power of I minus one half two plus Epsilon G to the power of three halves, while the projected Newton-CG algorithm of Xie and Wright obtains a rate of big O of Epsilon G under a set of approximate optimality conditions similar to this work.


## Optimality Conditions. Recall that X satisfies the first-order necessary conditions for one if

X is greater than or equal to zero, and the partial derivative of F of X with respect to I is zero, if X sub I is greater than zero, F of X is greater than zero, if X four is equal to zero.

Six.

We seek a point which satisfies these conditions to some E tolerance. There are a number of ways to adapt six into an approximate condition. In this work we adopt Xie and Wright, Definition one.


## Definition two point one. Epsilon-Optimal Point. A point, X, is called Epsilon-approximate first-order optimal, Epsilon-FO, if

G sub I is greater than or equal to negative V Epsilon, for all I in A of X, V Epsilon. Seven A

Norm of the diagonal of X A G four is less than or equal to Epsilon, Seven B

Norm of G I is less than or equal to Epsilon, Seven C

We take Seven A and Seven B to be trivially satisfied if A of X, V Epsilon is empty and similar for Seven C if I of X, V Epsilon is empty.

This definition has been shown to be asymptotically exact. Lemma two point two. Suppose that E sub K converges to zero and we have a sequence such that X sub K satisfies the corresponding E sub X-FO optimality condition. If X sub K converges to X star then X star satisfies Six.


## Three. Newton-MR Two-Metric Projection

We now propose and theoretically study our extensions of the TMP framework, which involves simultaneously employing gradient and inexact Newton steps, which are, respectively, restricted to the active and inactive sets.


## Three point one. MINRES and Its Properties

The inexact Newton step is based on the recently proposed Newton-MR framework.

2022), where instead of CG, subproblems are approximately solved using the minimum residual (MINRES) method (Paige & Saunders, 1975). Recall that the tth iteration of MINRES is formulated as s of t equals arg min absolute value of H s plus G squared. S in K t of H, g equation eight where K t of H, g equals Span of g, H g, and so on to H t minus one g, is the Krylov subspace of degree t generated from H and g. On each iteration M I N R E S minimizes the squared norm of the residual of the Newton system over the corresponding Krylov subspace. Note that, from an optimization perspective, the residual itself can be viewed as the gradient of the second-order Taylor approximation typically considered by second-order methods, that is, r approximately equals negative H s minus g equals negative gradient of s in g, s plus s, H s. This highlights an advantage of M I N R E S over C G. Indeed, unlike C G, which aims to minimize the second-order Taylor approximation, minimization of the residual norm remains well defined even if H is indefinite. For more theoretical and empirical comparisons between C G and M I N R E S, see Lim et al. twenty twenty-four.

Recently, Liu and Roosta established several properties of M I N R E S that make it particularly well-suited for nonconvex settings. For example, to assess the availability of a non-positive curvature direction in M I N R E S, one merely needs to monitor the condition r of t minus one, H r of t minus one is less than or equal to zero, equation nine

This condition is shown to be both necessary and sufficient for the existence of non-positive curvature directions in K t of H, g. In addition, M I N R E S enjoys a natural termination condition in non-convex settings. More specifically, for any user specified tolerance n greater than zero, the termination condition

H r of t minus one is less than absolute value H s of t minus one, equation ten is satisfied at some iteration. Note that the left hand side, H r of t minus one, is simply the residual of the normal equation H two s equals negative H g. Condition ten is particularly appealing in non-convex settings where we might have g not in the range of H and therefore r is not zero for all s in R d. In this case, a more typical termination condition r of t minus one is less than n may never be satisfied for a given n greater than zero. By contrast, condition ten is applicable in all situations since H r of t minus one is guaranteed to monotonically decrease to zero, while absolute value H s of t minus one is monotonically increasing. Remarkably, both conditions nine and ten can be computed with a scalar update directly from the M I N R E S iterates without any additional Hessian-vector products; see Lemma A point one.

A Newton-M R step is computed by running M I N R E S until condition nine is detected, in which case r of t minus one is returned. Since r of t minus one is a non-positive curvature direction, we label this


## Inexact Newton-type Methods for Optimization with Non-negativity Constraints

case as a "non-positive curvature" step. Otherwise, when the termination condition ten is satisfied, S of t minus one is returned. This step serves as an approximate solution to equation eight and so we label this case as a "solution" step. Let p denote the direction returned by negative curvature detecting M I N R E S. Liu and Roosta shows that p serves as a direction of first and second-order descent for the function f, namely p, g is less than zero and p, g plus p, H p divided by two is less than zero, as well as a direction of non-ascent for the norm of its gradient, that is, p, H g is less than zero for a solution step and p, H g equals zero for a non-positive curvature step.

We include the full M I N R E S algorithm as well as some additional properties in Appendix A.


## Three point two. Global Convergence: Minimal Assumptions

We first present a variant that is globally convergent under minimal assumptions. Algorithm one is our simplest variant of the Newton-MR two-metric projection method. Recalling the definition of the x-active and &k-inactive sets as in left two to the power of one, Algorithm one combines an active set gradient step i.e., left. P subscript k superscript script A equals negative G subscript k superscript script A right equals with an inactive set Newton-MR step i.e., P subscript k superscript script I equals S subscript k superscript script I, if D subscript type equals S O L, and P subscript k superscript script I equals R subscript k superscript script I, if left. D subscript T V E equals N P C right. In Algorithm one, the curvature condition nine is considered with a positive tolerance, bar varsigma equals left D plus one right varsigma greater than zero, i.e., left angle R superscript left T negative one right, H R superscript left T negative one right right angle is less than or equal to bar varsigma norm R superscript left T negative one right norm squared. Lemma B. one demonstrates that left angle R superscript left I right, H R superscript left I right right angle is greater than bar varsigma norm R superscript left I right norm squared for all zero less than T minus one is a certificate that H is s-strongly positive definite over script K subscript T left H, G right. Once the step direction is computed, the step size is selected with a line search criteria similar to that of Bertsekas. Specifically, letting x subscript k left alpha right equals script P left x subscript k plus alpha P subscript k right, we find alpha that, for some rho element of left zero, one over two, right, satisfies f left x subscript k left alpha right right minus f left x subscript k right is less than or equal to rho left angle G subscript k superscript script A comma script P left x subscript k superscript script A plus alpha P subscript k superscript script A right minus x subscript k superscript script A right angle plus alpha rho left angle G subscript k superscript script I, P subscript k superscript script I right angle. eleven,

Note that the term corresponding to the inexact set in eleven is negative due to the descent properties of P subscript k superscript script I discussed earlier. On the other hand, the active set term in eleven is negative due to the descent properties of the gradient mapping. This is crucial for our analysis as it allows us to consider the decrease in the inactive and active sets independently of each other. The two terms are unified since left angle G subscript k, script P left x subscript k plus alpha P subscript k right minus x subscript k right angle equals left angle G subscript k superscript script A, script P left x subscript k superscript script A plus alpha P subscript k superscript script A right minus x subscript k superscript script A right angle, plus alpha left angle G subscript k superscript script I, P subscript k superscript script I right angle, so long as alpha is chosen small enough. This is a direct consequence of script I left x subscript k, delta subscript k right containing only strictly feasible indices.


## Algorithm one Newton-MR TMP (Minimal Assumptions)

one: Input Initial point x subscript zero is greater than or equal to zero, active set tol left brace delta subscript k right brace, optimal- ity tol left brace epsilon subscript k right brace, MINRES inexactness tol eta greater than zero, NPC tol bar varsigma equals left D plus one right varsigma varsigma greater than zero, Line search parameter rho less than one over two. two: for

<LATEX>\mathcal{A} \left( x _ { k } , \delta _ { k } \right) \text { and } \mathcal{I} \left( x _ { k } , \delta _ { k } \right) \text { as in } \left( 2 \right) .</LATEX> Four: if (seven) is satisfied then

Five: Terminate.

<LATEX>\mathrm { p } _ { k } : \left\{ \begin{array}{} \mathrm { p } _ { k } ^ { \mathcal{A} } \leftarrow - \mathrm { g } _ { k } ^ { \mathcal{M} } , \\ \\ \left( \mathrm { p } _ { k } ^ { \mathcal{I} } , \mathrm { D } _ { \mathrm { t y p e } } \right) \leftarrow \mathrm { M I N R E S } \left( \mathrm { H } _ { k } ^ { \mathcal{I} } , \mathrm { g } _ { k } ^ { \mathcal{I} } , \eta , \bar { \varsigma } \right) \end{array} \right.</LATEX> Eight: if <LATEX>\mathrm { D } _ { \mathrm { t y p e } } = \mathrm { S O I }</LATEX> then

<LATEX>\alpha _ { k } \leftarrow \text { Algorithm } Five \text { with } \alpha _ { 0 } = One \text { and } \left( 1 1 \right) .</LATEX> Ten: else if <LATEX>\mathrm { D } _ { \mathrm { t y p e } } = \mathrm { N P C }</LATEX> then

<LATEX>\alpha _ { k } \leftarrow \mathrm { A l g o r i t h m } Six \mathrm { w i t h } \alpha _ { 0 } = One \mathrm { a n d } \left( 1 1 \right) .</LATEX> Twelve: end if

Thirteen:

<LATEX>\mathrm { x } _ { k + One } = \mathcal{P} \left( \mathrm { x } _ { k } + \alpha _ { k } \mathrm { p } _ { k } \right)</LATEX> Fourteen: end for

In Liu & Roosta, it was shown that when MINRES algorithm the returns an NPC step, the line search for <LATEX>\alpha</LATEX> could run in a forward tracking mode (cf. Algorithm Six). In numerical experiments, it was demonstrated that the forward tracking line search was beneficial because it allowed for very large steps to be taken, particularly in flat regions where progress would otherwise be slow. Our theoretical analysis in Appendix B demonstrates that a forward tracking line search can also be used in Algorithm One for NPC type steps.

To analyse the global complexity of Algorithm One, we only require typical assumptions on Lipschitz continuity of the gradient and lower-boundedness of the objective.

Assumption Three point One. There exists <LATEX>Zero \leq L _ { g } < \infty</LATEX> such that for all <LATEX>x ,</LATEX> <LATEX>\mathrm { y } \in \mathbb{R} _ { + } ^ { d } ,</LATEX> <LATEX>\| \mathrm { g } \left( \mathrm { x } \right) - \mathrm { g } \left( \mathrm { y } \right) \| \leq L _ { g } \| \mathrm { x } - \mathrm { y } \| .</LATEX> Assumption Three point Two. We have

<LATEX>- \infty < f _ { * } \leq f \left( \mathrm { x } \right) ,</LATEX> <LATEX>\forall \mathrm { x } \in \mathbb{R} _ { + } ^ { d } .</LATEX> With these minimal assumptions we can provide a guarantee of convergence of Algorithm One in Theorem Three point Three, the proof of which we deferred to Appendix B.

Theorem Three point Three (Global Complexity of Algorithm One). Let <LATEX>\epsilon _ { g } \in \left( Zero , One \right)</LATEX> and <LATEX>\varsigma > Zero .</LATEX> Under Assumptions Three point One and Three point Two, if we choose <LATEX>\delta _ { k } = \epsilon _ { k } = \epsilon _ { g } ^ { One half }</LATEX> and <LATEX>\bar { \varsigma } = \left( d + One \right) \varsigma ,</LATEX> Algorithm One produces an <LATEX>\epsilon _ { g } - F O</LATEX> point in at most <LATEX>\mathcal{O} \left( \epsilon _ { g } ^ { - Two } \right)</LATEX> iterations.

Remark Three point Four. The "big-O" rate obtained in Theorem Three point Three hides a dependence on the problem constants and algorithm parameters <LATEX>\rho ,</LATEX> <LATEX>\varsigma</LATEX> s, <LATEX>L _ { g } ,</LATEX> <LATEX>\eta ,</LATEX> which are, in particular, independent of d. However, the proof of Theorem Three point Three (and, indeed, Theorem Three point Eight) implies that the worst case constant hidden by the


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

big-O notation could have an unfortunate dependence on the problem constants (e.g., <LATEX>L _ { g } ^ { Three } .</LATEX> This could suggest poor practical performance despite the desirable dependence on <LATEX>\epsilon _ { g } .</LATEX> However, as we show numerically in Section Four, such worst case analyses are rarely indicative of typical performance in practice.


## Three point Three. Global Convergence: Improved Rate

It is possible to modify Algorithm one to improve upon the convergence rate of Theorem three point three, albeit under stronger assumptions. This is done in Algorithm two where, by appropriate use of curvature information, we can obtain an improved complexity rate. Algorithm two shares the same inactive/active sets, line search strategies, and projection based feasibility with Algorithm one. There are, however, some main differences. A key distinction lies in the certification of strictly positive curvature nine rather than strongly positive curvature, i.e., unlike Algorithm one where we set bar varsigma greater than zero, in Algorithm two we set the NPC tolerance to bar varsigma equals zero. Another notable difference is the introduction of Type two steps. Type two steps set the active portion of the step to zero and occur when the active set optimality conditions seven a and seven b are satisfied otherwise Type one steps, i.e., steps similar to Algorithm one, are used but the inactive set tolerance seven c is unsatisfied. Because the active set termination conditions are satisfied, removing the active portion of the step is not expected to significantly impede the algorithm's progress. By the same token, we can analyse Type two steps using second-order curvature information, similar to the unconstrained Newton-MR algorithm, without having to account for the curvature related to the projected gradient portion of the step. Additionally, to achieve an improved rate over Algorithm one, MINRES inexactness tolerance must scale with epsilon sub k in Algorithm two.

For our analysis, we need additional assumptions including the Lipschitz continuity of the Hessian.

Assumption three point five. There exists zero less than or equal to L sub H less than infinity that for all X,

Y belonging to the set of positive real numbers to the power of D, norm of H of X minus H of Y is less than or equal to L sub H norm of X minus Y. Additionally, we make some regularity assumptions on the output of the MINRES iterations.

Assumption three point six. There exists a constant omega greater than zero, independent of X, such that the NPC direction from MINRES, P equals r to the power of T minus one, satisfies

Norm of r to the power of T minus one is greater than or equal to omega norm of G. We note that a lower bound for the relative residual is available directly prior to termination. In fact, recall that if an NPC direction is returned, the termination condition ten must not yet be satisfied. In this case, Assumption three point one and Lemma A. one together imply that norm of r to the power of T minus one is greater than or equal to eta norm of G divided by the square root of eta squared plus L sub G squared. For Algorithm one, this lower bound is directly utilised to establish convergence with no requirement for Assumption three point six. However, for Algorithm two, N depends on epsilon sub K, which could lead us to believe that the lower bound


## Algorithm two Newton-MR TMP (Improved Rate)

One: Input Initial point X sub zero greater than or equal to zero, active set tolerance delta sub K, optimality epsilon sub K epsilon sub K, MINRES inexactness tolerance eta equals epsilon sub K theta and theta greater than zero, search parameter rho less than one half, NPC tolerance

Bar varsigma equals zero. Two: for

K equals zero, one, through D zero three: Update sets A of X sub K, delta sub K and I of X sub K, delta sub K as in two.

Four: if A of X sub K, delta sub K not equal to the empty set and not seven a or not seven b then

Flag equals Type one. Five:

Six: else if I of X sub K, delta sub K not equal to the empty set and not seven c then

Flag equals Type two. Eight: else

P sub k colon left curly brace begin array P sub k superscript calligraphic A left arrow left curly brace begin array negative G sub k superscript calligraphic A comma I f Flag equals Type one comma and zero comma I f Flag equals Type one comma and zero I f Flag equals Type two comma and left parenthesis P sub k superscript calligraphic I comma D sub type right parenthesis left arrow M I N R E S left parenthesis H sub k superscript calligraphic I comma G sub k superscript calligraphic I comma eta comma bar varsi right parenthesis and end array right curly brace end array right curly brace twelve colon if D sub type equals S O L then

Thirteen: Ok Algorithm five with

Alpha zero equals one and one one. Fourteen: else if D type equals NPC then

Fifteen:

Alpha k with Algorithm six with alpha zero equals one and one one. Sixteen: end if

Seventeen:

X k plus one equals P x k plus alpha k p k. Eighteen: end for on the relative residual prior to termination does too. In particular, at first glance, this might suggest that the smaller the inexactness tolerance eta, the more iterations MINRES is expected to perform before NPC detection. We argue that this is not the case. Firstly, an upper bound on the number of MINRES iterations until a NPC direction is encountered is independent of the termination criteria eta. In fact, by construction, the MINRES iterates are independent of the termination tolerance eta and the magnitude of norm g norm see discussion and numerical examples around (Assumption four). Additionally, in the case where g is not in the range of H, we always have norm r (t - one) norm is greater than or equal to norm (I - H H dagger) g norm, which is clearly independent of eta. Together, these lines of argumentation constitute our justification for Assumption three point six.

Recall that Algorithm one includes a manual verification of user specified strongly positive curvature over K t H, g in D type equals SOI case, while Algorithm two only certifies strict positive curvature through the NPC condition nine. Liu and Roosta demonstrated that as long as the NPC condition nine has not been detected, we have T t is positive where T t in the real numbers t by t is the symmetric tridiagonal matrix obtained in the tth iteration of MINRES (see Appendix A for more


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

details). Our next assumption strengthens this notion.

Assumption three point seven. There exists sigma is greater than zero such that for any x k in the sequence of SOL type iterates returned by Algorithm two, we have

T t is positive sigma I. Assumption three point seven implies that, as long as the NPC condition nine has not been detected, for any v in K t H, g we have〈v, Hv〉is greater than or equal to sigma norm v norm squared. Assumption three point seven is satisfied by an objective function whose Hessian contains positive g-relevant eigenvalues (eigenspaces not orthogonal to the gradient) uniformly separated from zero. A simple example is an under-determined least-squares problem.

Together, Assumptions three point six and three point seven allow us to control the curvature of our step, which is necessary to obtain an improved rate over Algorithm one using a Lipschitz Hessian upper bound. We now present the convergence result for Algorithm two. We defer the proof to Appendix C.

Theorem three point eight (Global Complexity of Algorithm two). Let epsilon g in (zero, one). Under Assumptions three point one, three point two and three point five to three point seven, if we choose delta k equals epsilon k equals epsilon g to the power of one half, Algorithm two produces an Eg-FO point in at most big O epsilon g to the power of negative three halves iterations.

Remark three point nine. A direct corollary to Theorems three point three and three point eight, under some mild additional assumptions, is a bound on the operational complexity in terms of gradient and Hessian-vector product evaluations. In particular, to produce an epsilon g minus FO point, the operation complexity for Algorithms one and two is, respectively, big O epsilon g to the power of negative two and big O tilde epsilon g to the power of negative three halves see Appendix D.

Remark three point ten. In all our algorithms, each step includes the Newton-MR component. The integration of the gradient and Newton-MR step is feasible in our algorithm due to the properties of the MINRES iterates (Lemmas A point two and A point three), allowing for a more flexible analysis with only first-order information. In contrast, it appears that second-order information is crucial for achieving descent with the capped-CG procedure, a central aspect of Xie and Wright. This constraint prevents the algorithm from taking a step simultaneously comprised of gradient and Newton-CG components.


## Three point four. Local Convergence

An advantage of the original TMP method of Bertsekas is that we get fast local convergence, a property that is shared by many Newton-type methods. We now show that our algorithm, in a slightly modified form, also exhibits this property. The basis for the local convergence is the fact that, under certain conditions, projected gradient algorithms are capable of identifying the true set of active constraints in a finite number of iterations. This result was first established for projected gradient with bound constraints in Bertsekas but has been extended to a variety of constraints. In the case of two-metric projection, once the active set is identified, the combined step reduces to an unconstrained Newton step in the inactive set.

For the analysis, we consider a "local phase" variant of Algorithm one. Specifically, we maintain flexibility in defining the outer and inner termination conditions and tolerances, eliminate the strongly positive curvature validation, and only perform backtracking line search from alpha sub zero equals one to ensure the step length remains bounded. The pseudo-code for this local phase version is given in Algorithm four for completeness. To show that the active set is identified in a finite number of iterations, we need non-degeneracy and second-order sufficiency assumptions, which are standard in this context.

Assumption three point eleven. A local minima, X sub star, is non-degenerate if left bracket g of X sub star right bracket super i is greater than zero, for all i in script A of X sub star comma zero. Assumption three point twelve. A local minima, X sub star, satisfies the second-order sufficiency condition if zero is less than inner product of Z and H of X sub star and Z for all Z not equal to zero such that Z super i equals zero if i in script A of X sub star comma zero. Theorem three point thirteen (Active Set Identification). Let f satisfy Assumption three point one and x plus be a local minima satisfying Assumptions three point eleven and three point twelve. Let the sequence of iterates generated by Algorithm four with delta chosen according to equation forty-four. There exists delta sub acrv greater than zero such that if X sub bar k in B of X sub star comma delta sub acrv, then script A of X sub k comma delta equals script A of X sub k comma zero equals script A of X sub star comma zero all k is greater than or equal to bar k plus one. We defer the proof to Appendix E. Once the active set is identified, our method reduces to unconstrained Newton-MR on the inactive set. Local convergence is therefore a simple corollary of Theorem three point thirteen.

Corollary three point fourteen (Local Convergence). For k is greater than or equal to bar k plus one (cf. Theorem three point thirteen), the convergence of Algorithm four is driven by the local properties of the Newton-MR portion of the step.

Remark three point fifteen. The local convergence of Newton-MR is similar to that of other inexact Newton methods. Suppose that we use a relative residual tolerance, norm r super script I norm less than or equal to eta norm g super script I norm, as the criteria for the MINRES termination. Under Assumption three point twelve, we know that H of X sub star is positive definite on the inactive indices. Therefore, by applying Nocedal and Wright, we obtain a superlinear convergence if we choose eta equals script O of one and let X sub k be close enough to X sub star. If we choose eta equals script O of norm g sub k norm and the Hessian is Lipschitz then we can improve the rate to quadratic.

Remark three point sixteen. A central ingredient in the projected Newton-CG of Xie and Wright is the damping of the Hessian in the form of diagonal perturbation (i.e., H plus epsilon I for all Newton-CG steps in the inactive set. While this facilitates an optimal global complexity, an unfortunate consequence, at least in theory, is that the algorithm no longer enjoys a guaranteed fast Newton-type local convergence rate. In other words, one can at best show linear rates in local regimes.


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

Four. Numerical Experiments

We now compare the performance of our method for solving one with several alternatives using various convex and non-convex examples. Specifically, we consider Algorithm two (denoted by MR), projected Newton-CG (denoted by CG) as in Xie and Wright, and projected gradient with line search (denoted by PG). For convex problems, we also include FISTA with line search, while for non-convex settings, we compare against the proximal gradient with momentum and fine-tuned constant step size (denoted by PGM) from Lin et al. We exclude proximal Newton methods due to the difficulty of solving its subproblems at each iteration. We also do not consider the Newton-CG log barrier method due to poor practical performance observed in Xie and Wright.

For all applicable methods we terminate according to seven with epsilon underscore g equals ten to the power of negative eight. Instead of the highly implementation dependent "wall-clock" time, here we plot the objective value against the number of oracle calls, i.e., the number of equivalent function evaluations. For completeness, however, we also include plots of objective value against wall-clock time in Appendix F point Five. The PyTorch implementation for our experiments is available here. All experiments were performed on a GPU cluster. See Appendix F point Three for further experimental details.


## Four point one. Sparse Regularisation With L one Norm

We first consider sparse regression using one-regularisation

Minimise over x in R d f of x plus lambda times L one norm of x, twelve where f is a smooth function. Although the objective function in twelve is nonsmooth, it can be reformulated into a smooth optimisation problem with nonnegativity constraints; see Appendix F point Two for details. We consider two examples in this context.

Multinomial Regression. In Figures one and two, we consider convex multinomial regression with C classes where f is given by sixty-two. The FISTA method is applied directly to twelve. While FISTA clearly outperforms the others, our method is competitive. Further simulations showing fast local convergence of our method on these examples are given in Appendix F point Four.

Neural Network. Figure three shows the results using a two layer neural network where f is non-convex and defined by sixty-three. Again, PGM is applied directly to twelve and its step size is fine-tuned for best performance. We once again observe superior performance of our method compared with the alternatives.

d equals twenty-seven thousand six hundred fifty-seven with lambda equals ten to the power of negative. Four point two. Nonnegative Matrix Factorisation

Given a nonnegative data matrix Y in R plus n by m nonnegative matrix factorisation aims to produce two low rank, say r, nonnegative matrices W in R plus n by eta and H in R plus r by m such that Y approximately equals WH. This can be formulated as

Minimise over W greater than or equal to zero and H greater than or equal to zero D of Y, WH plus R lambda of W, H, thirteen where D of blank, blank is a 'distance' and R lambda of blank, blank is a regularisation term. In Figure four, we consider a text dataset and cosine similarity based distance function, while in Figure five, we use an image dataset and a Euclidean distance function with a nonconvex regulariser; see Appendix F point Three for details. Clearly, our method outperforms all others across both problems.


## Five. Conclusions and Future Directions

We developed Newton-MR variants of the two-metric projection framework. By inexactly solving the subproblems using MINRES as well as employing non-positive curvature directions, our proposed variants are suitable for large scale and nonconvex settings. We demonstrated that, under


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

certain assumptions, the convergence rates of our methods match the state-of-the-art and showcased competitive practical performance across a variety of problems.

Possible avenues for future research include extensions to box constraints, variants with second-order complexity guarantees, and the development of stochastic algorithms.


## Impact Statement

This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

A. MINRES and Newton-MR

In this section, for completeness, we discuss MINRES and provide some of its fundamental properties. We note that our presentation is essentially that of Liu and Roosta, Appendix A as the notation and implementation is well adapted to our setting. Recall that MINRES combines the Lanczos process, a QR decomposition, and an updating formula to iteratively solve a symmetric linear least-squares problem of the form minimize |Hs plus g|| squared two.

We now discuss each of these aspects in detail.

Lanczos Process. Recall that, starting from v one equals g over ||g||, after t iterations of the Lanczos process, the Lanczos vectors {V one, V two, ..., V plus one}, form a basis for the Krylov subspace K plus one H, g. Collecting these vectors into an orthogonal matrix

V of t plus one equals [V one, ... V of t plus one] in R d x (t plus one)

we can write

H V of t equals V of t plus one times T t, where T t in R (t plus one), t is an upper Hessenberg matrix of the form

T t equals ã one B two

B two ã two

, T, A B plus one e capital T.

T t

B three ten to the power of eighteen ten

This relation yields the underlying update process of the MINRES iterations for t greater than or equal to two as,

Hvt equals BtVt minus one plus sum V plus plus B plus one V plus one.

The Lanczos process terminates when beta t plus one equals zero. We remark that computing an expansion of the basis requires a single Hessian-vector product, H Vt. The basis for the Krylov subspace allows us to significantly simplify eight. Indeed, let St be a solution to eight at iteration t. By St in Kt(H, g), we have st equals Vt yt for some yt in Rt. Hence, the residual can be written as rt equals negative g minus Hst equals negative g minus HVtyt equals negative g minus Vt plus one Ttyt equals negative Vt plus one open absolute value g close absolute value e one plus Ttyt.

In the final equality, we applied the orthogonality of the basis vectors and v one equals g over the norm of g. Applying this expression to equation eight and using the orthogonality of Vt plus one, we obtain the reduced tridiagonal least-squares problem absolute value of g e one plus Tt yt norm zero one.

min open fourteen close where thirty-one equals the norm of g.

QR Factorisation. The next step in the MINRES procedure is to solve equation fourteen by computing the full QR factorisation QtTt equals Rt where Qt belongs to the real numbers raised to the power of t plus one by t plus one and Rt belongs to the real numbers raised to the power of t plus one by t. Because It is already close to being upper triangular, we form the QR factorisation using a series of Householder reflections to annihilate the sub-diagonal elements. Each Householder reflection affects only two rows of Tt. We can summarise the effect of two successive Householder reflections fourteen


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

for three less than i less than t quad minus quad one as open left parenthesis one, one, one, one right parenthesis open left parenthesis ci minus one, si minus one, zero, ci minus one, si minus one right parenthesis open left parenthesis gamma i minus two, delta i minus one, zero, zero right parenthesis open left parenthesis beta i minus one, alpha i minus one, beta i, zero, zero, beta i, alpha i, beta i plus one right parenthesis equals open left parenthesis one, zero, zero right parenthesis open left parenthesis ci minus one, si minus one, zero, si minus one, ci minus one right parenthesis open left parenthesis gamma i minus two to the power of two, delta i minus one to the power of two, epsilon i, zero, zero, gamma i minus one, delta i, zero, beta i, alpha i, beta i plus one right parenthesis equals open left parenthesis gamma i minus two to the power of two, delta i minus one to the power of two, epsilon i, zero, zero, gamma i minus one to the power of two, delta i to the power of two, epsilon i plus one, zero, zero, gamma i, delta i plus one right parenthesis comma ci equals the fraction of gamma i over gamma i to the power of two comma si equals the fraction of beta i plus one over gamma i to the power of two comma gamma i to the power of two equals square root open left parenthesis gamma i close parenthesis to the power of two plus beta i plus one to the power of two equals ci gamma i plus si beta i plus one period We therefore form Q sub t as a product of the Householder reflection matrices

Q sub t equals product from i equals one to t Q sub i, i plus one, Q sub i, i plus one, is similar to open left parenthesis I sub i minus one, si sub t, si sub t, si sub t, ci sub t, I sub t minus i right parenthesis period It is also clear that R sub t is given by

R sub t equals the left parenthesis of gamma sub one to the power of left bracket two right bracket comma delta sub two to the power of left bracket two right bracket comma epsilon sub three and so on. Comma comma comma end. Blank gamma sub t minus one to the power of left bracket two right bracket comma delta sub t to the power of left bracket two right bracket blank gamma sub t to the power of left bracket two right bracket blank gamma sub t to the power of left bracket two right bracket right parenthesis. Comma quad widetilde of R sub t equals the left parenthesis of R sub t comma zero to the power of intercal equals right parenthesis. Applying Q sub t to widetilde of beta sub one e sub one, we obtain

Q sub t widetilde of beta sub one e sub one equals widetilde of beta sub one left parenthesis of c sub one comma s sub one c sub two comma v dots comma s sub one s sub two cdots s sub t minus one c sub t c sub t right parenthesis equals left parenthesis of tau sub one comma tau sub two comma ellipsis tau sub t comma phi sub t right parenthesis equals left parenthesis of t sub t comma phi sub t right parenthesis. Applying the Q R factorisation to solve fourteen gives

Min sub y sub t norm widetilde of beta sub one e sub one plus widetilde of T sub t y sub t norm equals min sub y sub t norm Q sub t to the power T left parenthesis widetilde of beta sub one Q sub t e sub one plus Q sub t widetilde of T sub t y sub t right parenthesis norm equals min sub y sub t norm left parenthesis of t sub t comma phi sub t right parenthesis plus left parenthesis of R sub t comma zero to the power T right parenthesis y sub t norm. An immediate implication of this result is

Phi sub t equals norm r sub t norm fifteen


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Update. The key to the computational efficiency of MINRES is the existence of vector update formula, which eliminates the requirement to form or store the matrices involved in the Lanczos and QR factorisation processes, i.e., V sub t comma Q sub t comma widetilde of R sub t comma and check of T sub t. Define W sub t from the upper triangular system W sub t R sub t equals V sub t as

Left parenthesis of gamma sub one to the power of left bracket two right bracket comma delta sub two to the power of left bracket two right bracket comma epsilon sub three left parenthesis v sub one right parenthesis comma v sub two comma cdots left parenthesis v sub t right parenthesis equals left parenthesis w sub one right parenthesis ellipsis gamma sub two to the power of left bracket two right bracket comma delta sub three to the power of left bracket two right bracket comma ddots ddots ddots and ddots and ddots end f sub t minus one to the power of left bracket two right bracket left end fifteen

By reading off fifteen, we see that

V sub t equals epsilon sub t w sub t minus two plus delta sub t to the power of left bracket two right bracket w sub t minus one plus gamma sub t to the power of left bracket two right bracket w sub t. The computation for the MINRES iterate can now be written as

S sub t equals V sub t Y sub t equals W sub t R sub t Y sub t equals W sub t T sub t equals left parenthesis W sub t minus one quad W sub t right parenthesis left parenthesis begin array T sub t minus one backslash tau sub t end array right parenthesis equals S sub t minus one plus tau sub t W sub t, where we set S sub zero equals zero. With this result in mind, we give the full MINRES method in Algorithm Three. We remark that, in Algorithm Three, we have also included steps for verifying the inexactness condition ten (Algorithm Three-Line ten) as well as certifying left angle bracket R sub t, H R sub t right angle bracket is greater than or equal to theta norm R sub t norm squared for some user specified theta is greater than or equal to zero (Algorithm Three-Line seven).


## Algorithm three MINRES(H, g, n, two)

One: Input Hessian H, gradient g, inexactness tolerance eta greater than zero, and NPC tolerance vartheta greater than or equal to zero. Two:

phi sub zero equals widetilde beta sub zero equals norm of g, r sub zero equals negative g, v sub one equals r sub zero divided by phi sub zero, v sub zero equals s sub zero equals w sub zero equals w sub negative one equals zero. Three: s sub zero equals zero, c sub zero equals negative one, delta sub one equals tau sub zero equals zero, t equals one.

Four: while True do q sub t equals H v sub t, widetilde alpha sub t equals inner product of v sub t and q sub t, q sub t equals q sub t minus widetilde beta sub t v sub t minus one, q sub t equals q sub t minus widetilde alpha sub t v sub t. widetilde beta sub t plus one equals norm of q sub t. Six: delta t left parenthesis begin array delta sub t super left square bracket two right square bracket and epsilon sub t plus one; gamma sub t and delta sub t plus one end array equals left parenthesis begin array c sub t minus one and s sub t minus one; s sub t minus one and negative c sub t minus one end array left parenthesis begin array delta sub t and zero; widetilde alpha sub t and widetilde beta sub t plus one end array. Zero if negative c sub t minus one gamma sub t is less than or equal to vartheta then

Eight: return left parenthesis r sub t minus one, D sub type equals NPC. Nine: end if

Ten: if phi sub t minus one square root of gamma sub t squared plus delta sub t plus one squared is less than or equal to eta square root of phi sub zero squared minus phi sub t minus one squared then left parenthesis s sub t minus one, D sub type equals SOL. Twelve: end if delta sub t super left square bracket two right square bracket equals square root of gamma sub t squared plus widetilde beta sub t plus one squared. Fourteen: if delta sub t super left square bracket two right square bracket is not equal to zero then

Fifteen: c sub t equals gamma sub t divided by gamma sub t super left square bracket two right square bracket, s sub t equals widetilde beta sub t plus one divided by gamma sub t super left square bracket two right square bracket, tau sub t equals c sub t phi sub t minus one,

phi sub t equals s sub t phi sub t minus one. Sixteen: w sub t sub sim equals left parenthesis v sub t minus gamma sub t super left square bracket two right square bracket w sub t minus one minus epsilon sub t w sub t minus two right parenthesis divided by gamma sub t super left square bracket two right square bracket,

s sub t equals s sub t minus one plus tau sub t w sub t. Seventeen: if widetilde beta sub t plus one is not equal to zero then v sub t plus one equals q sub t divided by widetilde beta sub t plus one, r sub t equals s sub t squared r sub t minus one minus phi sub t c sub t v sub t plus one. Nineteen: end if c sub t equals zero, s sub t equals one. c sub t equals zero, s sub t equals one, tau sub t equals zero, phi sub t equals phi sub t minus one, r sub t equals r sub t minus one, s sub t equals s sub t minus one. Twenty-two: end if

T becomes T plus one. Twenty-four: end while

We now collect several properties of the MINRES for reference; see Liu and Roosta for more details and properties. Firstly, we give some scalar expressions for the quantities of interest in nine and ten in the MINRES algorithm


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Lemma A point one MINRES scalar updates. We have the following

Proof. Sixteen a follows from the construction of the MINRES algorithm. The proof of sixteen d, sixteen c, and sixteen b is given in Liu and Roosta.

Next we give some helpful properties of the SOL and NPC steps.

Lemma A point two D Sub type equals SOL. Any iterate of MINRES, s super t, satisfies and

Suppose that negative curvature has not been detected up to iteration T. Then,

Further, consider Assumption three point one and suppose there exists some rho greater than zero such that for any v in K sub t of H, g, we have <v, H v> is greater than or equal to rho ||v|| squared. Then,

where

C sub rho, L sub g is defined as rho over L sub g squared. Proof. The relation seventeen follows from Liu and Roosta, while eighteen follows from the fact that zero is in K sub t of H, g and s super t minimizes eight. Also, nineteen follows from Liu and Roosta. For the right-hand-side of twenty, we use seventeen and the fact that s super t is in K sub t of H, g to get rho ||s super t|| squared is less than or equal to <s super t, H s super t> is less than or equal to ||s super t|| ||H s super t|| is less than or equal to ||s super t|| ||g|| implies ||s super t|| is less than or equal to ||g|| over rho. We show the left-hand-side of twenty using a monotonicity argument. In particular, consider the first iterate s super one. It is easy to see that the solution to eight over the Krylov subspace K sub one of H, g is Span{g} is given by the minimum of s in K sub one of H, g ||H s + g|| squared equals the minimum of beta in real numbers ||beta H g + g|| squared implies beta equals negative <g, H g> over ||H g|| squared. The step is therefore given by s super one equals negative <g, H g> over ||H g|| squared g. We can apply <g, H g> is greater than or equal to rho ||g|| squared and ||H g|| is less than or equal to L sub g ||g|| to obtain

||r super t|| equals phi sub t. Sixteen a

<r super t minus one, H r super t minus one> equals negative c sub t minus one gamma sub t ||r super t minus one|| squared, ||H s super t minus one|| equals the square root of phi sub zero squared minus phi sub t minus one squared, ||H r super t minus one|| equals phi sub t minus one square root of gamma sub t squared plus delta sub t plus one squared. Sixteen b, Sixteen c, Sixteen d norm of H s raised to the t is less than or equal to norm of g,

inner product of s raised to the t and H g is less than or equal to zero.

inner product of s raised to the t and g is less than or equal to negative inner product of s raised to the t and H s raised to the t.

C sub varrho comma L sub g norm of g is less than or equal to norm of s raised to the t is less than or equal to norm of g over varrho,

norm of s raised to the one is equal to inner product of g and H g over norm of H g squared norm of g greater than or equal to varrho over L sub g squared norm of g.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

The full results follows from the monotonicity of the MINRES iterates, that is, as long as negative curvature remains undetected up to iteration t greater than or equal to one we have norm of s raised to the t is greater than or equal to norm of s raised to the one is greater than or equal to varrho over L sub g squared norm of g. Lemma A point three D type equals NPC. Suppose that the MINRES algorithm returns D type equals NPC so that our step is r raised to the t minus one. Then,

inner product of r raised to the t minus one and g equals negative norm of r raised to the t minus one squared.

Additionally, the residual norm is upper bounded by the gradient.

norm of r raised to the t minus one is less than or equal to norm of g.

Proof. The relation twenty-one follows from the MINRES properties directly. We get twenty-two by noting that norm of H s raised to the t minus one squared equals norm of r raised to the t minus one plus g squared equals norm of r raised to the t minus one squared plus two inner product of r raised to the t minus one and g plus norm of g squared equals norm of r raised to the t minus one squared minus two norm of r raised to the t minus one squared plus norm of g squared equals norm of g squared minus norm of r raised to the t minus one squared. For the third line, we applied twenty-one. The final equality and the nonnegativity of the norm implies the result.


## B. Global Convergence - Minimal Assumptions

In this section, we detail the proof of the global convergence of Algorithm one, that is, Theorem three point three. We first demonstrate that the uniform positive curvature certification of the residuals, r raised to the i, provides a bound on the curvature of the Hessian over the corresponding Krylov subspace.

Lemma B point one Strong Positive Curvature Certification. By verifying inner product of r raised to the t minus one and H r raised to the i is greater than varrho norm of r raised to the i squared, for i equals zero to t minus one, we obtain inner product of v and H v is greater than or equal to varrho over t plus one norm of v squared,

for any v in K sub t left parenthesis H comma g right parenthesis. Proof. Let v in K sub t left parenthesis H comma g right parenthesis. We can write

K sub t left parenthesis H comma g right parenthesis equals span left brace r raised to the zero, r raised to the one, to r raised to the t minus one right brace, and therefore there exists a set of scalars, left brace beta sub i right brace sub i equals zero to t minus one, such that

V equals sum from I equals zero to T minus one beta sub I R to the power of left parenthesis I right parenthesis. Using this fact and the certificates left angle bracket R to the power of left parenthesis I right parenthesis comma H R to the power of left parenthesis I right parenthesis right angle bracket is greater than or equal to bar Varsigma norm R to the power of left parenthesis I right parenthesis norm squared gathered for I equals zero comma ellipsis comma T minus one, we obtain

Left angle bracket V comma H V right angle bracket equals left angle bracket sum from I equals zero to T minus one beta sub I R to the power of left parenthesis I right parenthesis comma sum from I equals zero to T minus one beta sub I H R to the power of left parenthesis I right parenthesis right angle bracket equals sum from I equals zero to T minus one sum from J equals zero to T minus one beta sub I beta sub J left angle bracket R to the power of left parenthesis I right parenthesis comma H R to the power of left parenthesis J right parenthesis right angle bracket equals sum from I equals zero to T minus one beta sub I squared left angle bracket R to the power of left parenthesis I right parenthesis comma H R to the power of left parenthesis I right parenthesis right angle bracket is greater than or equal to sum from I equals zero to T minus one beta sub I squared bar Varsigma norm R to the power of left parenthesis I right parenthesis norm squared, twenty-four


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

where the second to last equality follows from the H-conjugacy of the residuals. Using Bernstein, we get

One divided by T plus one norm sum from I equals zero to T minus one beta sub I R to the power of left parenthesis I right parenthesis norm squared is less than or equal to sum from I equals zero to T minus one beta sub I squared norm R to the power of left parenthesis I right parenthesis norm squared, which gives the desired result.

Note that since T appears in the lower bound twenty-three, there is a dependence on the number of MINRES iterations undertaken and hence X. However, T is bounded above by D. For this reason, in the sequel, bar Varsigma equals left parenthesis D plus one right parenthesis Varsigma for some Varsigma is greater than zero. Indeed, this choice implies that, under the conditions of Lemma B point one, for any

V in calligraphic K sub T left parenthesis H comma G right parenthesis we have left angle bracket V comma H V right angle bracket is greater than or equal to Varsigma norm V norm squared, twenty-five

We now demonstrate that the line search procedure eleven terminates for a small enough step size.

Lemma B point two Step-size Lower Bound. Suppose F satisfies Assumption three point one. If at iteration K of Algorithm one, we have calligraphic I left parenthesis X sub K comma delta sub K right parenthesis is not equal to empty set, then the largest step size, alpha sub K, that satisfies the line search criteria eleven, also satisfies the following lower bound alpha sub K is greater than or equal to minimum left parenthesis two left parenthesis one minus rho right parenthesis divided by L sub G minimum left parenthesis one comma Varsigma right parenthesis comma delta sub K divided by norm P sub K to the power of calligraphic I norm right parenthesis, twenty-six

On the other hand, if calligraphic I left parenthesis X sub K comma delta sub K right parenthesis equals empty set, the bound is given by alpha sub K is greater than or equal to two left parenthesis one minus rho right parenthesis divided by L sub G, twenty-seven

Proof. We note that the proof of Lemma C point one utilizes no curvature properties of the residual. With this fact in mind, the proof is entirely the same as Lemma C point one in Appendix C with Varsigma taking the place of O.

The following lemma gives the amount of decrease obtained from the inactive set step whenever the inactive set is nonempty and the inactive set termination condition is not satisfied.

Lemma B point three (Sufficient Decrease: Inactive Set Case). Suppose F satisfies Assumption three point one. Let X subscript K plus one equals the projection of X subscript K plus alpha subscript K P subscript K be the update computed at iteration K of Algorithm one, where alpha subscript K satisfies the line search criterion. Suppose the inactive set of X subscript K comma delta subscript K is not equal to the empty set and the termination condition is not satisfied. If the residual type equals the solution, then

F of X subscript K plus one minus F of X subscript K is less than negative rho Varsigma minimum of the quantity two times one minus rho times the minimum of the quantities one and Varsigma times the product of the constants divided by the gradient constant times the square of epsilon subscript K, comma the product of the constants and delta subscript K times the square of epsilon subscript K. where the constant is as defined in equation twenty. Otherwise,

With the residual type equals NPC, F of X subscript K plus one minus F of X subscript K is less than negative rho minimum of the quantity two times one minus rho times the square of eta divided by the product of the gradient constant and the sum of the squares of eta and the gradient constant times the square of epsilon subscript K comma the product of eta and delta subscript K divided by the square root of the sum of the squares of eta and the gradient constant times the square of epsilon subscript K. Proof. Since alpha subscript K satisfies the line search condition, we have

F of X subscript K plus one minus F of X subscript K is less than or equal to rho times the inner product of the gradient of K projection of X subscript K plus alpha P subscript K minus X subscript K plus alpha rho times the inner product of the gradient of K P subscript K is less than or equal to alpha rho times the inner product of the gradient of K P subscript K, where we use the fact that the inner product of the gradient of K projection of X subscript K plus alpha P subscript K minus X subscript K is less than or equal to zero. We now consider the residual type equals the solution and the residual type equals NPC cases.


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

When the residual type equals the solution, we have P subscript R equals S subscript K. Using the line search condition comma the left-hand side inequality in equation twenty with Varsigma equals eta, we have

F of X subscript K plus one minus F of X subscript K is less than or equal to P A K times the inner product of the gradient of K comma S subscript K all squared is less than or equal to negative P A K of the inner product of S subscript K and the projection is less than negative P S A K times the absolute value is less than negative P S minimum of two times one minus P

gradient minimum of one comma Varsigma absolute value is less than negative P S minimum of two times one minus P L G minimum of one comma Varsigma all squared is less than negative P S minimum of two times one minus P minimum of one comma Varsigma squared is less than negative P S minimum of two times one minus P minimum of one comma Varsigma constant gradient epsilon subscript K Varsigma gradient where we applied the norm of gradient greater than Varsigma on the final line.

When the residual type equals NPC, we have, P equals the residual factor. We first note that, since the inexactness condition has not been met, by applying Assumption three point one and using the fact that the norm of the Hessian is squared equals the norm of the gradient squared minus the norm of the residual squared,

we get the norm of the residual is greater than or equal to the square root of eta squared plus the gradient squared gradient norm minus

Let W equal eta divided by the square root of eta squared plus the gradient squared. Proceeding similarly to the solution case but using equation twenty-one, we have

F of X subscript K plus one minus F of X subscript K is less than or equal to P A K times the inner product of the gradient of K comma the absolute value of I

is less than or equal to negative P A K times the absolute value of the residual is less than negative P minimum two times one minus P gradient squared is less than negative P minimum two times one minus P W squared gradient is less than negative P minimum two times one minus P W squared gradient epsilon again, making use of the norm of the gradient greater than six percent in the final line.

The following lemma covers the case when the inactive set termination condition is satisfied, that is, I(Xk, zero k) equals empty set or (seven c) holds. In this case, we expect the inactive set step to be small and so we analyse the decrease due to the active set portion of the step, using the fact that at least one of the active set termination conditions (seven a) or (seven b) must be unsatisfied. Lemma B. four (Sufficient Decrease: Active Set Case). Suppose that f satisfies Assumption three point one. Let X k plus one equals P (X k plus O k Pk) be the update computed at iteration k of Algorithm one, where a k satisfies the line search criterion (eleven). Suppose that at least one of the active set termination conditions, (seven a) or (seven b), is not satisfied. If I(X k, zero k) equals empty set, then f (X k plus one) minus f (X k) is less than negative p min section one half (one minus p)

, twenty-one minus L g min one, two eighty-two

However, if I(X k, zero k) does not equal empty set and (seven c) is satisfied, we have f (X k plus one) minus f (X k) is less than negative p min a. min twenty-one minus zero zero min min one, five min one, five percent two eighty-two one half twenty


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Proof. Since alpha k satisfies the line search criterion we have f (x k plus one) minus f (x k) is less than or equal to rho g k upper A, P left (x k upper A plus alpha k p k upper A) minus x k upper A plus alpha k rho g k upper I, p k upper I is less than or equal to rho g k upper A, P left (x k upper A plus alpha k p k upper A) minus x k upper A, where we apply g k upper I, p k upper I is less than or equal to zero. From here the proof proceeds similarly to Lemma C. three. Indeed, if (seven a) or (seven b) are unsatisfied, (thirty-six) gives f (x k plus one) minus f (x k) is less than negative rho min left {one half, alpha k min left one, epsilon k squared divided by two delta k squared right} right} epsilon k squared,

and it only remains to apply a bound on alpha k. If I left (x k, delta k right) equals empty set, we use (twenty-seven) to obtain f (x k plus one) minus f (x k) is less than negative rho min left {one half, two (one minus rho) divided by L g} min left one, epsilon k squared divided by two delta k squared right} right} epsilon k squared. Otherwise, we have I left (x k, delta k right) does not equal empty set. In this case, we must lower bound delta k divided by norm p k upper I in (twenty-six). We therefore use (twenty) with varrho equals varsigma, section (twenty-two), as well as the fact that (seven c) is unsatisfied to obtain min left varrho , one right norm p k upper I is less than or equal to norm g k is less than or equal to epsilon k squared implies delta k min left one, varrho right over epsilon k squared is less than or equal to delta k divided by norm p k upper I. We now apply this bound to (twenty-six) and combine with (twenty-eight) to get f (x k plus one) minus f (x k) is less than negative rho min left one half, min left {two (one minus rho) divided by L g , delta k over epsilon k squared right} min left one, varrho right min left one, epsilon k squared divided by two delta k squared right} right} epsilon k squared. Proof of Theorem three point three. We posit that the algorithm must terminate in at most

K equals ceiling of F subscript zero minus F subscript asterisk times epsilon subscript g to the power of negative two over minimum of c subscript one, c subscript two iterations, where c subscript one equals rho minimum of two varsigma times one minus rho minimum of one, varsigma C subscript varsigma, L subscript g squared over L subscript g, varsigma C subscript varsigma, L subscript g, two times one minus rho omega squared over L subscript g, omega, with omega equals eta over square root of eta squared plus L subscript g squared, c subscript two equals rho minimum of one half, one half minimum of two times one minus rho over L subscript g, one, minimum of one, varsigma, and C subscript varsigma, L subscript varrho is as in equation twenty. Suppose otherwise, that is, the algorithm fails to terminate until at least iteration K plus one. For iterations k equals one, to K, the termination conditions must be unsatisfied. We divide the iterates up in the following manner

K subscript one equals k in the range K such that I of X subscript k, epsilon subscript g to the power of one half is not empty, norm of g subscript k by I is greater than or equal to epsilon subscript g, and

K subscript two equals k in the range K not in K subscript one such that A of X subscript k, epsilon subscript g to the power of one half is not empty, there exists I in A of X subscript k, epsilon subscript g to the power of one half, g subscript k by I less than negative square root of epsilon subscript g or norm of diag of X subscript k by A, g subscript k by A is greater than or equal to epsilon subscript g. Since the algorithm has not terminated, ceiling of K equals K subscript one union K subscript two. If k in K subscript one we apply Lemma B point three and combine the SOL and NPC

cases with epsilon subscript q less than one to obtain F of X subscript k plus one minus F of X subscript k is less than negative rho minimum of two varsigma times one minus rho minimum of one, varsigma C subscript varsigma, L subscript g squared over L subscript g, varsigma C subscript varsigma, L subscript g, two times one minus rho omega squared over L subscript g, omega epsilon subscript g squared equals negative c subscript one epsilon subscript g squared.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

If k in K subscript two, we instead combine the results of Lemma B point four to obtain

F of X subscript k plus one minus F of X subscript k is less than negative rho minimum of two minimum one minus L subscript g.

two times one minus P point one minimum of one, five, greater than epsilon subscript g less than or equal to negative C subscript two six epsilon subscript g.

Finally, we obtain

F subscript zero minus F subscript X is greater than or equal to F subscript zero minus F of X greater than or equal to F of X minus F of X subscript k plus one greater than or equal to absolute value of curly brackets C subscript one plus absolute value of K subscript two squared subscript k equals zero to K minus one greater than or equal to absolute value of K plus absolute value of K subscript two minimum of c subscript one, c subscript two equals K minimum of c subscript one, c subscript two,

which contradicts the definition of K.


## C. Global Convergence - Improved Rate

In this section, we provide the proof of Theorem three point eight. Recall that we denote the update to X subscript k for some step size, a, by X subscript k of a equals P of X subscript k plus at P subscript k.

Recall that Algorithm two involves two types of steps: Type one and Type two. We summarise the step types, the optimality conditions, as well as the corresponding lemmas in Table one.

Our first three lemmas, Lemmas C point one to C point three, will demonstrate that Type I steps produce sufficient decrease in the function value. The analysis of Type I steps builds off of Xie and Wright twenty twenty-three which demonstrated that projected gradient can achieve good progress, in terms of guaranteed decrease, when the active termination conditions seven a and seven b are unsatisfied. However, unlike Xie and Wright twenty twenty-three, which only uses a first-order step, we also incorporate second-order update in the form of Newton-MR step in the inactive set of indices.

As shown in Lemma C point one, combining the steps in this manner suggests that the lower bound on the step size may depend inversely on the length of the Newton-MR step. This, in turn, could lead to small step sizes if the Newton-MR step is large. We deal with this issue by splitting our analysis into two cases. The first case, Lemma C point two, deals with large gradients on the inactive set where we expect good progress due to the corresponding large Newton-MR step on the inactive set. By contrast, the second case, Lemma C point three, deals with small gradients on the inactive set where we can expect to see small inactive set steps and therefore lower bounded step sizes. In this way, we trade off the convergence due to the inactive and active sets to always ensure sufficient decrease at the required rate.

Recall that Assumption three point one implies that, for any y, x in the set of real numbers four, we have f of y is less than or equal to f of x plus the inner product of the gradient of f of x and y minus x plus plus nine times the norm of x minus y squared.

Twenty-nine


## We now give the proof of Lemmas C point one to C point three.

Lemma C point one, Type I Step: Step-size Lower Bound. Assume that f satisfies Assumptions three point one and three point seven. Suppose a Type I step is taken at iteration k of Algorithm two. If I of Xk and the expected value of k is not empty, then the largest step size which satisfies the line search criteria eleven, expected value of k, satisfies the following lower bound

The expected value of k is greater than or equal to the minimum negative bracket, two times one minus p, Lg, the minimum of one, zero,

Thirty

However, if I of Xk and zero k is empty, then

The expected value of k is two times one minus p, Lg

Thirty-one


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Proof. If the mathematical set I of x subscript k and the expected value of k is not empty, suppose alpha is less than or equal to the fraction of the expected value of k over the norm of p subscript k to the set I, which is less than or equal to the fraction of the expected value of k over the infinity norm of p subscript k to the set I, so that for each i in the set I of x subscript k and the expected value of k, we have the projection of x subscript k to i plus alpha p subscript k to i equals x subscript k to i plus alpha p subscript k to i. The Lipschitz gradient upper bound twenty-nine yields f of x subscript k of alpha is less than or equal to f of x subscript k plus the inner product of g subscript k and P of x subscript k plus alpha p subscript k minus x subscript k plus the fraction of L subscript g over two times the norm of P of x subscript k plus alpha p subscript k minus x subscript k squared equals f of x subscript k plus the inner product of g subscript k to the set A, P of x subscript k to the set A minus alpha g subscript k to the set A minus x subscript k to the set A plus alpha the inner product of g subscript k to the set I and p subscript k to the set I plus the fraction of L subscript g alpha squared over two times the norm of p subscript k to the set I squared. It is clear from this bound that the line search will terminate for any alpha such that langle g sub k sup script A, P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A rangle plus alpha langle g sub k sup script I, p sub k sup script I rangle plus fraction L sub g over two norm P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A norm squared plus fraction L sub g alpha squared over two norm p sub k sup script I norm squared minus rho left parenthesis langle g sub k sup script A, P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A rangle plus alpha langle g sub k sup script I, p sub k sup script I rangle right parenthesis,

is nonpositive. Starting with the active set terms of thirty-two. We use the projection inequality norm P left parenthesis x right parenthesis minus P left parenthesis y right parenthesis norm squared less than or equal to langle x minus y, P left parenthesis x right parenthesis minus P left parenthesis y right parenthesis rangle combined with the feasibility of x sub k sup script A (which implies P left parenthesis x sub k sup script A right parenthesis equals x sub k sup script A) to obtain left parenthesis one minus rho right parenthesis langle g sub k sup script A, P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A rangle plus fraction L sub g over two norm P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A norm squared less than or equal to left parenthesis one minus rho right parenthesis langle g sub k sup script A, P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A rangle minus fraction alpha L sub g over two langle g sub k sup script A, P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A rangle less than or equal to left parenthesis left parenthesis one minus rho right parenthesis minus fraction alpha L sub g over two right parenthesis langle g sub k sup script A, P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A rangle. By langle g sub k sup script A, P left parenthesis x sub k sup script A minus alpha g sub k sup script A right parenthesis minus x sub k sup script A rangle less than or equal to zero, the active terms of thirty-two are nonpositive if left parenthesis one minus rho right parenthesis minus fraction alpha L sub g over two greater than or equal to zero implies alpha less than or equal to fraction two left parenthesis one minus rho right parenthesis over L sub q. If script I left parenthesis x sub k, delta sub k right parenthesis equals empty set, then thirty-one follows directly from this bound.

alpha left one minus rho right langle g sub k sup mathcal cap I comma s sub k sup mathcal cap I rangle plus fraction L sub g alpha squared over two norm s sub k sup mathcal cap I norm squared leq alpha left negative left one minus rho right langle s sub k sup mathcal cap I comma H sub k s sub k sup mathcal cap I rangle plus fraction alpha L sub g over two norm s sub k sup mathcal cap I norm squared right leq alpha left negative left one minus rho right sigma norm s sub k sup mathcal cap I norm squared plus fraction alpha L sub g over two norm s sub k sup mathcal cap I norm squared right equals alpha left negative left one minus rho right sigma plus fraction alpha L sub g over two right norm s sub k sup mathcal cap I norm squared period alpha leq fraction two sigma left one minus rho right over L sub g period If D sub type equals N P C comma that is comma p sub k sup mathcal cap I equals r sub k sup mathcal cap I comma we apply left two one right to space o b t a i n alpha left one minus rho right langle g sub k sup mathcal cap I comma r sub k sup mathcal cap I rangle plus fraction L sub g alpha squared over two norm r sub k sup mathcal cap I norm squared leq negative alpha left one minus rho right norm r sub k sup mathcal cap I norm squared plus fraction L sub g alpha over two norm r sub k sup mathcal cap I norm squared equals alpha left negative left one minus rho right plus fraction L sub g alpha over two right norm r sub k sup mathcal cap I norm squared comma


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

which is negative when two left one minus P right

L sub g

If both the inactive and active terms of left thirty-two right are nonpositive then the line search will certainly terminate. Collecting the bounds on the step size, we can see that the largest O k which satisfies the line search criteria also satisfies the following lower bound

Q k is greater than or equal to min left two left one minus P right over L sub g min left one comma o right comma I P T I eight k

Lemma C point two Type I Step: Inactive Set Decrease. Assume that f satisfies Assumptions three point one, three point six and three point seven. Suppose that a Type I step is taken at iteration k of Algorithm two but both I of X k comma O k slash empty set and norm g k norm is greater than percent . Let a k be the largest step size satisfying the line search condition eleven so that X k plus one equals P of X k plus O k P k . If D type equals S O L then f of X k plus one minus f of X k less than negative Po min two left one minus P right min one comma zero C two L sub g Ex comma Co comma L sub g O k E k to the power of three halfs .

Otherwise, if D type equals N P C ,

f of X k plus one minus f of X k less than negative P min left two left one minus P right W squared L sub g minus epsilon cubed k omega delta kappa epsilon k

Proof. Line search criterion and the negativity of left g k comma P of X A minus O k S A minus X A implies left thirty-three right f of X k plus one minus f of X k less than or equal to P g k comma P of X k minus Q k g k minus X k plus a k P g k comma P R less than or equal to P a k S k comma P k

We now divide into two cases, depending on the step type selected by M I N R E S period

If D type equals S O L comma then P x equals s k period Using the line search condition left thirty-three right comma left nineteen right comma Assumption three point seven, the lower bound on O k from Lemma C point one comma and the left-hand-side inequality of left twenty right with at equals o comma we have f of Xk plus one minus f of Xk is less than or equal to pak of gk, sk is less than or equal to negative pok of Sk, HESK

summation minus rho sigma alpha k is less than or equal to negative po minimum of two times one minus p times Lg minimum of one, zero, eight k I k norm I norm squared is less than or equal to negative po minimum of two times one minus p times Lg minimum of one, zero, norm Sk one squared point eight k norm SEII

is less than or equal to negative po minimum two times one minus p minimum of one, zero, Co, Lg Lg less than negative po minimum two times one minus p minimum of one, zero, Co, Lg Lg where for the last inequality, we used the fact that I k three-half k


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

If D of typc equals NPC, then p of k to the power of I equals r of k to the power of I. We use, but apply and Assumption three point six to get f of x of k plus one minus f of x of k is less than or equal to rho alpha of k inner product g of k to the power of I, r of k to the power of I is less than or equal to negative rho alpha of k norm r of k to the power of I norm squared is less than or equal to negative rho minimum of two times one minus rho divided by L of g norm r of k to the power of I norm squared, delta of k norm r of k to the power of I norm is less than or equal to negative rho minimum of two times one minus rho omega squared divided by L of g norm g of k to the power of I norm squared, delta of k omega norm g of k to the power of I norm less than negative rho minimum of two times one minus rho omega squared divided by L of g epsilon of k cubed, delta of k omega epsilon of k to the power of three-halves, again, making use of norm g of k to the power of I norm greater than epsilon of k to the power of three-halves in the final line.

Lemma C. three Type I Step: Sufficient Reduction. Assume that f satisfies Assumptions three point one and three point seven. Suppose that a Type I step is taken on iteration k of Algorithm Two so that A of x of k, delta of k is not empty and either seven a or seven b is unsatisfied. Let alpha of k be the largest step size satisfying the line search condition eleven so that x of k plus one equals P of x of k plus alpha of k p of k. If A of x of k, delta of k is not empty and norm g of k to the power of I norm is less than or equal to epsilon of k to the power of three-halves, then k,

f of x of k plus one minus f of x of k less than negative rho minimum of one-half, minimum of one, sigma minimum of two times one minus rho divided by L of g, delta of k divided by epsilon of k to the power of three-halves minimum of one, epsilon of k squared divided by two delta of k squared epsilon of k squared. Otherwise, if

A of x of k, delta of k is empty, f of x of k plus one minus f of x of k is less than negative rho minimum of one-half, two times one minus rho divided by L of g minimum of one, epsilon of k squared divided by two delta of k squared epsilon of k squared. Proof. Since alpha of k satisfies the line search sufficient decrease condition, the negativity of inner product g of k to the power of I, p of k to the power of I, implied by nineteen and twenty-one, gives

The analysis proceeds depending on which optimality condition is unsatisfied.

Case one seven a: G sub k superscript i less than negative epsilon sub k for some i in script A of x sub k comma delta sub k. In this case we can see that

G sub k superscript i of script P of x sub k superscript i minus alpha sub k G sub k superscript i minus x sub k superscript i equals negative alpha sub k of G sub k superscript i squared less than negative alpha sub k epsilon sub k squared. We immediately see from the term wise nonpositivity of thirty-four that

F of x sub k plus one minus F of x sub k is less than negative rho alpha sub k epsilon sub k squared. Case two seven b: Continuing from thirty-four we obtain

F of x sub k plus one minus F of x sub k is less than or equal to rho of left angle G sub k superscript script A comma script P of x sub k superscript script A minus alpha sub k G sub k superscript script A right angle plus alpha sub k left angle G sub k superscript script I comma p sub k superscript script I right angle less than or equal to rho left angle G sub k superscript script A comma script P of x sub k superscript script A minus alpha G sub k superscript script A minus x sub k superscript script A right angle equals rho sum over i in script A of x sub k comma delta sub k G sub k superscript i of script P of x sub k superscript i minus alpha G sub k superscript i minus x sub k superscript i. Thirty-four

F of x sub k plus one minus F of x sub k is less than or equal to rho sum over i in script A of x sub k comma delta sub k G sub k superscript i of script P of x sub k superscript i minus alpha G sub k superscript i minus x sub k superscript i equals rho of the sum over i in script A of x sub k comma delta sub k where alpha sub k G sub k superscript i is greater than or equal to x sub k superscript i minus G sub k superscript i x sub k superscript i plus the sum over i in script A of x sub k comma delta sub k where alpha sub k G sub k superscript i is less than x sub k superscript i minus alpha sub k of G sub k superscript i squared. Thirty-five


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Note each sum in thirty-five is term-wise negative. Since diagonal x A G A is greater than six percent, we have

E sub k colon diagonal x g squared equals E dot A of X sub k comma delta sub k i i

This implies two possible cases: either v i left angle g squared i in A of X sub k comma delta sub k i eight k g a squared equals two eighty-two point four g i squared.

In either case, the negativity of each term of thirty-five implies f of X sub k plus one minus f of x sub k is less than negative P min

Combining with Case one gives f of X sub k plus one minus f of x sub k is less than negative P min, and zero percent equals negative P min two, U k, one twenty-eight percent squared, epsilon squared k

Thirty-six

If I of X sub k comma delta sub k equals empty set, we apply thirty-one to obtain f of X sub k plus one minus f of X sub k is less than negative P min one two of one minus P squared L g min of one comma two,

On the other hand, if I of X sub k comma zero k not equal to empty set, the lower bound for ok in thirty depends inversely on the inactive portion of the step double vertical bars P E double vertical bars. The step size can therefore become small if double vertical bars P g double vertical bars is too large. To avoid this, we will make use of the fact that the gradient is bounded. In particular, by combining the right inequality of twenty and twenty-two, we obtain min of one comma zero vertical bar P F I vertical bar less than or equal to G k I less than or equal to E x squared,

which implies epsilon ok min of one comma zero raised to the power of three over two k two of one minus P L g

Imposing this on the step size lower bound thirty gives

Q k greater than or equal to min of one comma zero min

The decrease is therefore given by f of X sub k plus one minus f of X sub k is less than negative P min two one, alpha k min one, two eighty-two epsilon less than or equal to negative P min less than or equal to negative P min, min of one comma zero min two of one minus P L g one raised to the power of three over two Q k k min. Twenty percent


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

The next three lemmas (Lemmas C point four to C point six) demonstrate the sufficient decrease of Type two steps. Recall that a Type two steps occurs once active set optimality is reached. Type two steps are taken until the inactive set optimality seven C is satisfied termination or a new index falls into the active set and disrupts active set optimality, in which case we resume Type one steps. The Type two step consists of only a Newton-MR step in the inactive indices no step is taken in the active indices. Indeed, a Type two direction can be written with possible reordering of indices as x sub k left paren alpha right paren minus x sub k equals left paren zero semicolon script P left paren x sub k superscript script I plus alpha p sub k superscript script I right paren minus x sub k superscript script I right paren. Eliminating the active portion of the step allows us to leverage a second-order analysis of the inactive indices without having to account for the curvature of the projected gradient portion of the step. Indeed, the analysis of the algorithm reverts to essentially that of unconstrained Newton-MR, with some minor modifications to account for the projection. Specifically, with possible reordering of the indices, we partition the Hessian into four blocks as

H sub k equals left paren H sub k superscript script A semicolon H sub k superscript O semicolon H sub k superscript O semicolon H sub k superscript script I right paren, where H sub k superscript script A and H sub k superscript script I are the submatrices corresponding to the active and inactive indices respectively and H sub k superscript O is the remaining off-diagonal blocks of the Hessian. Under the Lipschitz Hessian condition Assumption three point five and using alpha less than or equal to delta sub k over norm p sub k superscript script I norm so that script P left paren x sub k superscript script I plus alpha p sub k superscript script I right paren equals x sub k superscript script I plus alpha p sub k superscript script I, we can write f left paren x sub k left paren alpha right paren right paren less than or equal to f left paren x sub k right paren plus inner product of left paren g sub k superscript script A semicolon g sub k superscript script I right paren, left paren zero semicolon alpha p sub k superscript script I right paren plus one half inner product of left paren zero semicolon c semicolon H sub k superscript script I right paren, left paren H sub k superscript script A semicolon H sub k superscript O semicolon H sub k superscript script I semicolon H sub k superscript script I right paren left paren zero semicolon alpha p sub k superscript script I right paren plus alpha cubed L sub H over six norm left paren zero semicolon p sub k superscript script I right paren norm cubed equals f left paren x sub k right paren plus alpha inner product of g sub k superscript script I, p sub k superscript script I plus alpha squared over two inner product of p sub k superscript script I, H sub k superscript script I p sub k superscript script I plus alpha cubed L sub H over six norm p sub k superscript script I norm cubed. thirty-seven

Our first lemma uses the expansion in thirty-seven to show that the largest step size satisfying the line search criterion is lower bounded.

Lemma C point four. Type Two Step: Step-size Lower Bound. Assume that F satisfies Assumption three point five. If Algorithm two selects a Type Two step at iteration K and MINRES returns D sub R Y E equals N P C, then for the largest step size, alpha sub K, satisfying the line search criterion eleven, we must have alpha sub K is greater than or equal to min of the square root of six times one minus rho over L sub H norm r sub K to the power of I, and delta sub K over norm r sub K to the power of I. Equation thirty-eight.

Otherwise, if D sub T Y P E equals S O L and Assumption three point seven holds, then alpha sub K is greater than or equal to min of one, the square root of three sigma times one minus two rho over L sub H norm s sub K to the power of I, and delta sub K over norm s sub K to the power of I. Equation thirty-nine.

Proof. We have already seen that, if alpha is less than or equal to delta sub K over norm p sub K to the power of I, equation thirty-seven holds. From eleven, the line search is satisfied for any o such that f of x sub K alpha minus f of x sub K minus rho alpha inner product g sub K to the power of I, p sub K to the power of I is less than or equal to zero. We now consider D sub T Y P E equals S O I and D sub T Y P E equals N P C cases. Let D sub T Y P E equals S O I so that p sub K to the power of I equals s sub K to the power of I. Applying thirty-seven, alpha is less than one, the


## Inexact Newton-type Methods for Optimization with Non-negativity Constraints

MINRES curvature condition nineteen and Assumption three point seven we have

F of x sub k of alpha minus F of x sub k minus rho alpha angle G sub k, S sub k sup I angle is less than or equal to alpha angle G sub k sup I, S sub k sup I angle plus alpha squared over two angle S sub k sup I, H sub k sup I S sub k sup I angle plus alpha cubed L sub H over six norm S sub k sup I cubed minus rho alpha angle G sub k, S sub k sup I angle is less than or equal to alpha times one minus rho angle G sub k sup I, S sub k sup I angle plus alpha over two angle S sub k sup I, H sub k sup I S sub k sup I angle plus alpha cubed L sub H over six norm S sub k sup I cubed equals alpha times one half minus rho angle G sub k sup I, S sub k sup I angle plus alpha over two times angle G sub k sup I, S sub k sup I angle plus angle S sub k sup I, H sub k sup I S sub k sup I angle plus alpha cubed L sub H over six norm S sub k sup I cubed is less than or equal to alpha times one half minus rho angle G sub k sup I, S sub k sup I angle plus alpha cubed L sub H over six norm S sub k sup I cubed is less than or equal to negative alpha times one half minus rho angle S sub k sup I, H sub k sup I S sub k sup I angle plus alpha cubed L sub H over six norm S sub k sup I cubed is less than or equal to negative alpha times one half minus rho sigma norm S sub k sup I squared plus alpha cubed L sub H over six norm S sub k sup I cubed equals alpha times negative quantity one half minus rho sigma plus alpha squared L sub H over six norm S sub k sup I norm squared. It can be seen that this upper bound is nonpositive if negative \left( \frac { one } { two } minus \rho \right) \sigma plus \frac { \alpha squared L subscript { H } } { six } \| \mathrm { s } subscript { k } superset { \mathcal{I} } \| \leq zero \Longrightarrow \alpha \leq \sqrt { \frac { three \sigma \left( one minus two \rho \right) } { L subscript { H } \| \mathrm { s } subscript { k } superset { \mathcal{I} } \| } } . Collecting the bounds on \alpha , the largest step size that satisfies the line search condition can be lower bounded as

\alpha subscript { k } \geq \min \left\{ one , \sqrt { \frac { three \sigma \left( one minus two \rho \right) } { L subscript { H } \| \mathrm { s } subscript { k } superset { \mathcal{I} } \| } } , \frac { \delta subscript { k } } { \| \mathrm { s } subscript { k } superset { \mathcal{I} } \| } \right\} . Now let \mathrm { D } subscript { \mathrm { t y p e } } equals \mathrm { N P C } so that \mathrm { p } subscript { k } superset { \mathcal{I} } equals \mathrm { r } subscript { k } superset { \mathcal{I} } . Applying the negative curvature of \mathrm { r } subscript { k } superset { \mathcal{I} } , (twenty-one) and (thirty-seven)

f \left( \mathrm { x } subscript { k } \left( \alpha \right) \right) minus f \left( \mathrm { x } subscript { k } \right) minus \rho \alpha \langle \mathrm { g } subscript { k } , \mathrm { r } subscript { k } superset { \mathcal{I} } \rangle \leq \alpha \langle \mathrm { g } subscript { k } superset { \mathcal{I} } , \mathrm { r } subscript { k } superset { \mathcal{I} } \rangle plus \frac { \alpha squared } { two } \langle \mathrm { r } subscript { k } superset { \mathcal{I} } , \mathrm { H } subscript { k } superset { \mathcal{I} } \mathrm { r } subscript { k } superset { \mathcal{I} } \rangle plus \frac { \alpha cubed L subscript { H } } { six } \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| cubed minus \rho \alpha \langle \mathrm { g } subscript { k } , \mathrm { r } subscript { k } superset { \mathcal{I} } \rangle \leq \alpha \left( one minus \rho \right) \langle \mathrm { g } subscript { k } superset { \mathcal{I} } , \mathrm { r } subscript { k } superset { \mathcal{I} } \rangle plus \frac { \alpha cubed L subscript { H } } { six } \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| cubed \leq negative \alpha \left( one minus \rho \right) \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| squared plus \frac { \alpha cubed L subscript { H } } { six } \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| cubed equals \alpha \left( negative \left( one minus \rho \right) plus \frac { \alpha squared L subscript { H } } { six } \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| \right) \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| squared . This upper bound is nonpositive if negative \left( one minus \rho \right) plus \frac { \alpha squared L subscript { H } } { six } \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| \leq zero \Longrightarrow \alpha \leq \sqrt { \frac { six \left( one minus \rho \right) } { L subscript { H } \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| } } . Therefore the largest step size that satisfies the line search condition, in the NPC case, is lower bounded as

\alpha subscript { k } \geq \min \left\{ \sqrt { \frac { six \left( one minus \rho \right) } { L subscript { H } \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| } } , \frac { \delta subscript { k } } { \| \mathrm { r } subscript { k } superset { \mathcal{I} } \| } \right\} . From Lemma C.4 we can see that, for a judicious choice of \delta subscript { k } , the step size is inversely scaling with the step length, except for the \alpha subscript { k } equals one in \mathrm { D } subscript { \mathrm { t y p e } } equals \mathrm { S O I } case. This inverse scaling is key to obtaining an improved rate. We therefore deal with the \alpha subscript { k } equals one case separately. Indeed, in Lemma C.5 we show that if \alpha subscript { k } equals one with \mathrm { D } subscript { \mathrm { t y p e } } equals \mathrm { S O L } the step length must be lower bounded by norm of the gradient of the next iterate (over the same inactive set). This lemma is similar to the result in Liu and Roosta, we include it for completeness.


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

Lemma C.5. Suppose Algorithm two selects a Type two step at iteration k with Dtype equals S O L and @k equals one, that is, an update of the form with possible reordering. Under Assumptions three point one, three point five and three point seven, we have negative eight k plus one I k divided by E k; E k equals,

T I S K greater than or equal to co min S I k,

where zero L g plus zero two one two plus two L H O two two zero

Proof. Since r T t minus one equals negative H T s T Sk t minus one minus gk

T E K H L, g and N P C has not been detected, Assumption Three point Seven implies

∥

forty

V I

For clarity, in the sequel we make the dependence of inactive set on the iteration explicit. Consider

Sk plus One that is, the indices of the gradient evaluated at Xk plus One corresponding to the inactive set at Xk. This portion of the next gradient "lives" in the same subset of the indices as gfk. The mean value theorem therefore implies that Ik

Ik minus H Tk Sk Ik dt.

Assumption Three point Five implies

Ik k minus H Ik STK one.

Using this bound, ten, and forty, we obtain

∥s ∥s less than or equal to L H two ∥s Ik two plus

∥

plus O E K L g Sk

∥

where the second to last line follows from the MINRES termination condition in Algorithm Two and the last line follows from Assumption Three point One. Rearranging this expression, we obtain a quadratic inequality in sk as zero less than or equal to L H O S T K two plus twenty k L g one minus twenty


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

We can bound <LATEX>\| \mathrm { s } _ { k } ^ { \mathcal{I} _ { k } } |</LATEX> by the positive root of this quadratic as

<LATEX>\| \mathrm { s } _ { k } ^ { \mathcal{I} _ { k } } \| \geq \frac { minus two \theta \epsilon _ { k } L _ { g } + \sqrt { four \theta ^ { two } \epsilon _ { k } ^ { two } L _ { g } ^ { two } + eight L _ { H } \sigma ^ { two } \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| } } { two L _ { H } \sigma }</LATEX> <LATEX>= \left( \frac { \left. minus \theta L _ { g } + \sqrt { \theta ^ { two } L _ { g } ^ { two } plus two L _ { H } \sigma ^ { two } \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| / \epsilon _ { k } ^ { two } } { } \right) } { L _ { H } \sigma } \right.</LATEX> <LATEX>= \left( \frac { \theta ^ { two } L _ { g } ^ { two } minus \left( \theta ^ { two } L _ { g } ^ { two } plus two L _ { H } \sigma ^ { two } \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| / \epsilon _ { k } ^ { two } \right) } { L _ { H } \sigma \left( minus \eta L _ { g } minus \sqrt { \theta ^ { two } L _ { g } ^ { two } plus two L _ { H } \sigma ^ { two } } \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| / \epsilon _ { k } ^ { two } \right) } \right) \epsilon _ { k }</LATEX> <LATEX>= \left( \frac { two \sigma \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| / \epsilon _ { k } ^ { two } } { L _ { g } \theta plus \sqrt { \theta ^ { two } L _ { g } ^ { two } plus two L _ { H } \sigma ^ { two } \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| / \epsilon _ { k } ^ { two } } } \right) \epsilon _ { k }.</LATEX> We now consider two cases. If

<LATEX>\| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| / \epsilon _ { k } ^ { two } greater than one</LATEX> <LATEX>\frac { two \sigma \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| / \epsilon _ { k } ^ { two } } { \theta L _ { g } plus \sqrt { \theta ^ { two } L _ { g } ^ { two } plus two L _ { H } \sigma ^ { two } \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| / \epsilon _ { k } ^ { two } } } equals \frac { two \sigma } { \theta L _ { g } \epsilon _ { k } ^ { two } / \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| plus \sqrt { \theta ^ { two } L _ { g } ^ { two } \epsilon _ { k } ^ { four } / \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| ^ { two } plus two L _ { H } \sigma ^ { two } \epsilon _ { k } ^ { two } / \| \mathrm { g } _ { k plus one } ^ { \mathcal{I} _ { k } } \| }</LATEX> <LATEX>greater than or equal to \frac { two \sigma } { \theta L _ { g } plus \sqrt { \theta ^ { two } L _ { g } ^ { two } plus two L _ { H } \sigma ^ { two } } }.</LATEX> On the other hand, if

Norm of G sub K plus one superscript I sub K divided by epsilon sub K squared is less than or equal to one. L sub G theta plus the square root of theta squared L sub G squared plus two L sub H sigma squared norm of G sub K plus one superscript I sub K divided by epsilon sub K squared is less than or equal to L sub G theta plus the square root of theta squared L sub G squared plus two L sub H sigma squared. Together, these cases imply that

Norm of S sub K superscript I sub K equals left parenthesis two sigma norm of G sub K plus one superscript I sub K divided by epsilon sub K squared divided by L sub G theta plus the square root of theta squared L sub G squared plus two L sub H sigma squared norm of G sub K plus one superscript I sub K divided by epsilon sub K squared right parenthesis epsilon sub K. Greater than or equal to two sigma divided by L sub G theta plus the square root of theta squared L sub G squared plus two L sub H sigma squared minimum of norm of G sub K plus one superscript I sub K divided by epsilon sub K squared and one epsilon sub K. We now demonstrate the sufficient decrease of the Type Two step.

Lemma C point six Type Two Step: Sufficient Decrease. Assume that F satisfies Assumptions three point one and three point five. Suppose that a Type Two step is taken on iteration K of Algorithm two, that is, I left parenthesis X sub K comma delta sub K right parenthesis is not equal to empty set and norm of G sub K superscript I is greater than epsilon sub K squared. Let X sub K plus one equal to P left parenthesis X sub K plus alpha sub K P sub K right parenthesis where alpha sub K is the largest step size satisfying the termination condition eleven, see Lemma C point four. Suppose that MINRES returns D sub NPE equals SOL and Assumption three point seven is satisfied. Then, if norm of G sub K plus one superscript I is greater than zero we have

F left parenthesis X sub K plus one right parenthesis minus F left parenthesis X sub K right parenthesis is less than negative rho sigma minimum of the square root of three sigma left parenthesis one minus two rho right parenthesis divided by L sub H C sub sigma comma L sub G to the power of three halves, epsilon sub K cubed, C sub sigma comma L sub G cubed delta sub K epsilon sub K squared, C sub zero squared norm of G sub K plus one superscript I squared divided by two epsilon sub K squared, C sub zero squared epsilon sub K squared divided by two. Where C sub zero is defined in Lemma C point five. Note that if norm of G sub K plus one superscript I equals zero strict inequality must be replaced with superscript mathfrak C sub zeta stackrel less than or equal to superscript mathcal W. On the other hand, if D sub RPPE equals NPC and Assumption three point six is satisfied, then

F left parenthesis X sub K plus one right parenthesis minus F left parenthesis X sub K right parenthesis is less than negative rho minimum of the square root of six left parenthesis one minus rho right parenthesis divided by L sub H omega to the power of three halves epsilon sub K cubed, omega delta sub K epsilon sub K squared.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints.

Proof. If D type equals SOL, PR equals SZ. Combining the line search sufficient decrease eleven, the descent condition for the SOL step nineteen and Assumption three point seven, we obtain

F of X sub K plus one minus F of X sub K is less than or equal to AKP of SK, GK

is less than or equal to negative OKP of SK, HESK

is less than or equal to negative OKP norm of SK squared.

Since QK is less than or equal to one, if the step size returned by the line search satisfies OK is less than one, then we must have norm of delta K is less than AK;

K delta K minus IST. norm squared

K thirty left parenthesis one minus two P right parenthesis as otherwise thirty-nine would imply K is greater than or equal to one. Therefore, by applying twenty with at equal to O, we obtain

F of X sub K plus one minus F of X sub K is less than or equal to negative PO minimum

LA SEIl norm of SK

is less than or equal to negative PO minimum three sigma left parenthesis one minus two P right parenthesis LH

is less than or equal to negative PO minimum thirty left parenthesis one minus two P right parenthesis LH

H.

is less than negative PO minimum thirty left parenthesis one minus two P right parenthesis LH C to the power of three halves zero comma La EK, Co, Lg OK, EK.

on the last line we use the fact that by assumption, norm norm greater than six percent. If the step size ok equals one is selected by the line search, we can use Lemma C point five to obtain

|sk | ≥ co minimum { |8k plus one norm / Ek, Ek } ,

which implies f(Xk plus one) minus f(xk) ≤ negative po |sk| squared less than POCO minimum { eighteen squared plus twelve over two,E .}

If |g| equals zero, the strict inequality must be replaced with "less than". Combining the bounds we obtain the result.

If Dtype equals NPC, PR equals rx. The line search condition (eleven), the step size lower bound (thirty-eight), (twenty-one) and Assumption three point six imply f(Xk plus one) minus f(Xk) ≤ akp(rk, Sk) .I .T)

less than akp |[[twelve six(one minus p) I k norm

≤ negative p minimum

≤ negative p minimum six(one minus p) LH norm r rk norm I cubed three halves, eight percent | k|

≤ negative p minimum six(one minus p) LH cubed three halves | T | cubed three halves less than p minimum six(one minus P) W cubed three halves ER, WOKETE LH

where the final inequality follows from the non-termination condition.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

We are finally ready to prove Theorem three point eight.

Proof of Theorem three point eight. Let f of zero equals f left parenthesis x sub zero right parenthesis. We posit that the algorithm terminates in

K equals left ceiling fraction two left parenthesis f of zero minus f star right parenthesis ε sub g cubed halves over minimum left brace c sub left parenthesis one, one right parenthesis, c sub left parenthesis one, two, right parenthesis, c sub left parenthesis two, two right parenthesis right brace plus one right ceiling, iterations where c sub left parenthesis one, one right parenthesis, c sub left parenthesis one, two, right parenthesis and c sub left parenthesis two, two right parenthesis are constants that will be defined later. Suppose, to the contrary, that the termination conditions is unsatisfied until at least iteration K plus one. Then for iterations k equals zero, dots, K at least one of the termination (seven a) to (seven c) conditions must be unsatisfied. We divide the Type I iterations brace one equals left brace k in left bracket K right bracket mid mathcal{A} left parenthesis x sub k, ε sub g squared halves right parenthesis does not equal empty, quad a n d quad left parenthesis exists i in mathcal{A} left parenthesis x sub k, ε sub g squared halves right parenthesis, quad g sub k superscript i less than square root ε sub g, quad o r quad norm diag left parenthesis x sub k superscript mathcal{A} right parenthesis g sub k superscript mathcal{A} norm ≥ ε sub g right parenthesis right brace, K one mathcal{K} sub one, one equals mathcal{K} sub one cap left brace k in left bracket K right bracket mid norm g sub k superscript mathcal{I} norm greater than ε sub g cubed quarters, quad a n d quad mathcal{I} left parenthesis x sub k, ε sub g squared halves right parenthesis does not equal empty right brace, mathcal{K} sub one, two equals mathcal{K} sub one cap left brace k in left bracket K right bracket mid norm g sub k superscript mathcal{I} norm ≤ ε sub q cubed quarters, quad o r quad mathcal{I} left parenthesis x sub k, ε sub q squared halves right parenthesis equals empty right brace. mathcal{K} sub two equals left bracket K right bracket setminus mathcal{K} sub one w e h a v e mathcal{I} left parenthesis x sub k, ε sub g squared halves right parenthesis does not equal empty a n d norm g sub k superscript mathcal{I} sub k norm greater than ε sub g. We divid For the Type II iterations them as follows mathcal K subscript two comma one equals mathcal K subscript two cap left brace k in left bracket K right bracket mid mathcal I left parenthesis bold x subscript k plus one comma epsilon subscript g superscript one half right parenthesis not equal to empty set comma quad bold a n d quad double vertical bar bold g subscript k plus one superscript mathcal I subscript k plus one double vertical bar greater than epsilon subscript g right brace comma mathcal K subscript two comma two equals mathcal K subscript two cap left brace k in left bracket K right bracket mid mathcal I left parenthesis bold x subscript k plus one comma epsilon subscript g superscript one half right parenthesis equals empty set comma quad bold o r quad double vertical bar bold g subscript k plus one superscript mathcal I subscript k plus one double vertical bar less than or equal to epsilon subscript g right brace period We now restate the results obtained for per-iteration decrease.

Type one step. For k in mathcal K subscript one comma one comma Lemma C point two applies and by combining the NPC and SOL cases and using epsilon subscript g less than one we obtain comma f left parenthesis bold x subscript k plus one right parenthesis minus f left parenthesis bold x subscript k right parenthesis less than negative min left brace c subscript left parenthesis one comma one right parenthesis superscript a epsilon subscript g superscript three halves comma c subscript left parenthesis one comma one right parenthesis superscript b epsilon subscript g superscript five fourths right brace less than or equal to negative min left brace c subscript left parenthesis one comma one right parenthesis superscript a comma c subscript left parenthesis one comma one right parenthesis superscript b right brace epsilon subscript g superscript three halves equals negative c subscript left parenthesis one comma one right parenthesis epsilon subscript g superscript three halves comma c subscript left parenthesis one comma one right parenthesis superscript a triangleq rho min left brace fraction two left parenthesis one minus rho right parenthesis omega squared over L subscript g comma fraction two left parenthesis one minus rho right parenthesis min left brace one comma sigma right brace sigma C subscript sigma comma L subscript g superscript two over L subscript g right brace comma c subscript left parenthesis one comma one right parenthesis superscript b triangleq rho min left brace omega comma sigma C subscript sigma comma L subscript g right brace comma quad bold a n d quad c subscript left parenthesis one comma one right parenthesis triangleq min left brace c subscript left parenthesis one comma one right parenthesis superscript a comma c subscript left parenthesis one comma one right parenthesis superscript b right brace period For k in mathcal K subscript one comma two comma Lemma C point three applies. Indeed comma for mathcal I left parenthesis bold x subscript k comma epsilon subscript g superscript one half right parenthesis not equal to empty set we obtain a decrease f left parenthesis bold x subscript k plus one right parenthesis minus f left parenthesis bold x subscript k right parenthesis less than negative fraction rho over two min left brace one comma min left brace one comma sigma right brace min left brace fraction two left parenthesis one minus rho right parenthesis over L subscript g comma fraction one over epsilon subscript g superscript one fourth right brace right brace epsilon subscript g less than or equal to negative fraction rho over two min left brace one comma min left brace one comma sigma right brace min left brace fraction two left parenthesis one minus rho right parenthesis over L subscript g comma one right brace right brace epsilon subscript g superscript three halves comma where on the second line we used epsilon subscript q less than one. The decrease in the case where mathcal I left parenthesis bold x subscript k comma epsilon subscript g superscript one half right parenthesis equals empty set is given by f left parenthesis bold x subscript k plus one right parenthesis minus f left parenthesis bold x subscript k right parenthesis less than negative fraction rho over two min left brace one comma fraction two left parenthesis one minus rho right parenthesis over L subscript q right brace epsilon subscript g superscript three halves. Combining these results we obtain forty-two f left parenthesis bold x subscript k plus one right parenthesis minus f left parenthesis bold x subscript k right parenthesis less than negative c subscript left parenthesis one comma two right parenthesis epsilon subscript g superscript three halves comma where c subscript left parenthesis one comma two right parenthesis triangleq fraction rho over two min left brace one comma min left brace one comma sigma right brace min left brace fraction two left parenthesis one minus rho right parenthesis over L subscript g comma one right brace right brace period


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

Type Two Step: For K in script K sub two one, we can apply the norm of G sub K plus one superscript script I sub K plus one is greater than epsilon sub G to further refine the bound for the SOL case. Note that because delta sub K equals delta sub K plus one equals epsilon sub G to the one half, and a Type Two step is taken, script N script I of x sub K plus one, epsilon sub G to the one half is a subset of script I of x sub K, epsilon sub G to the one half. Indeed, if

I is in script A of x sub K, epsilon sub G to the one half, we have P sub K superscript I equals zero and hence x sub K plus one superscript I equals x sub K superscript I is less than or equal to epsilon sub G to the one half, and script A of x sub K, epsilon sub G to the one half is a subset of script A of x sub K plus one, epsilon sub G to the one half. Together these results imply that

Epsilon sub G is less than the norm of G sub K plus one superscript script I sub K plus one is less than or equal to the norm of G sub K plus one superscript script I sub K. With D sub type equals S O I and using epsilon sub Q is less than one, Lemma C point six implies

F of x sub K plus one minus F of x sub K is less than negative rho sigma times the minimum of the square root of three sigma times one minus two rho times C sub sigma L sub G cubed over L sub H times epsilon sub G to the three halves, C sub sigma L sub G times epsilon sub G to the three halves, C sub zero squared over two, C sub zero squared times epsilon sub G over two, is less than or equal to negative rho sigma times the minimum of the square root of three sigma times one minus two rho times C sub sigma L sub G cubed over L sub H, C sub sigma L sub G, C sub zero squared over two times epsilon sub G to the three halves. With D sub type equals N P C, this becomes

F of x sub K plus one minus F of x sub K is less than negative rho times the minimum of the square root of six times one minus rho over L sub H times omega to the three halves, omega times epsilon sub G to the three halves, and so by combining the D sub type equals N P C and D sub type equals S O I cases, we have where

C subscript left parenthesis two, two right parenthesis defined as rho minimum of the set square root of the fraction three sigma cubed times one minus two rho times C subscript sigma comma L subscript G cubed over L subscript H, sigma C subscript sigma comma L subscript G, the fraction sigma c naught squared over two, square root of the fraction six times one minus rho times omega cubed over L subscript H, omega. For K in script K subscript two, two, the lower bound for the next gradient norm is no longer available. However, due to Lemma C.1, we have at least could be the iteration the algorithm terminates. We can therefore write

Absolute value script K subscript left parenthesis two, one right parenthesis less than or equal to absolute value script K subscript one plus one. We now bound the total decrease in terms of the number of iterations that must have occurred using inequalities forty-one to forty-three

F of x subscript k plus one minus F of x subscript k is less than negative c subscript left parenthesis two, two right parenthesis epsilon subscript g to the power of three halves, inequality forty-three

F of x subscript k plus one minus F of x subscript k is less than or equal to zero. Text of the algorithm, K in script K subscript two, two implies K plus one in script K subscript one unless K equals K final, in which case K plus one. Additionally, due to the non-termination

F to the power zero minus F star is greater than or equal to F to the power zero minus F of x subscript K plus one equals the sum from k equals zero to K of F of x subscript k minus F of x subscript k plus one equals the sum from k in script K subscript left parenthesis one, one right parenthesis of F of x subscript k minus F of x subscript k plus one plus the sum from k in script K subscript left parenthesis one, two right parenthesis of F of x subscript k minus F of x subscript k plus one plus the sum from k in script K subscript left parenthesis two, one right parenthesis of F of x subscript k minus F of x subscript k plus one plus the sum from k in script K subscript left parenthesis two, two right parenthesis of F of x subscript k minus F of x subscript k plus one is greater than the sum from k in script K subscript left parenthesis one, one right parenthesis of c subscript left parenthesis one, one right parenthesis epsilon subscript g to the power of three halves plus the sum from k in script K subscript left parenthesis one, two right parenthesis c subscript left parenthesis one, two right parenthesis epsilon subscript g to the power of three halves plus the sum from k in script K subscript left parenthesis two, two right parenthesis c subscript left parenthesis two, two right parenthesis epsilon subscript g to the power of three halves equals absolute value script K subscript left parenthesis one, one right parenthesis c subscript left parenthesis one, one right parenthesis epsilon subscript g to the power of three halves plus absolute value script K subscript left parenthesis one, two right parenthesis c subscript left parenthesis one, two right parenthesis epsilon subscript g to the power of three halves plus absolute value script K subscript left parenthesis two, two right parenthesis c subscript left parenthesis two, two right parenthesis epsilon subscript g to the power of three halves.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Since each term is positive, we get the absolute value of script cap K sub left parenthesis one comma one right parenthesis is less than the fraction f naught minus f star epsilon sub g to the negative three halves over c sub left parenthesis one comma one right parenthesis, the absolute value of script cap K sub left parenthesis one comma two right parenthesis is less than the fraction f naught minus f star epsilon sub g to the negative three halves over c sub left parenthesis one comma two right parenthesis, the absolute value of script cap K sub left parenthesis two comma two right parenthesis is less than the fraction f naught minus f star epsilon sub g to the negative three halves over c sub left parenthesis two comma two right parenthesis. Hence, if we add up the total number of iterations that must have been taken

K equals the absolute value of script cap K sub left parenthesis one comma one right parenthesis plus the absolute value of script cap K sub left parenthesis one comma two right parenthesis plus the absolute value of script cap K sub left parenthesis two comma one right parenthesis plus the absolute value of script cap K sub left parenthesis two comma two right parenthesis less than or equal to two times the absolute value of script cap K sub left parenthesis one comma one right parenthesis plus the absolute value of script cap K sub left parenthesis one comma two right parenthesis plus the absolute value of script cap K sub left parenthesis two comma two right parenthesis plus one less than the fraction two times f naught minus f star epsilon sub g to the three halves over c sub left parenthesis one comma one right parenthesis plus the fraction two times f naught minus f star epsilon sub g to the three halves over c sub left parenthesis one comma two right parenthesis plus the fraction f naught minus f star epsilon sub g to the three halves over c sub left parenthesis two comma two right parenthesis plus one less than or equal to the ceiling of the fraction two times f naught minus f star epsilon sub g to the three halves over the minimum of c sub left parenthesis one comma one right parenthesis comma c sub left parenthesis one comma two comma right parenthesis comma c sub left parenthesis two comma two right parenthesis plus one equals K, we arrive at a contradiction.


## D. Operational Complexity

The results in this section are corollaries of Theorem three point three and Theorem three point eight and the MINRES iteration bounds in Liu and Roosta. The following definitions are included from Liu and Roosta for completeness.

Let psi left parenthesis cap H comma g right parenthesis denote the set of g-relevant eigenvalues, that is, the eigenvalues whose eigenspace is not orthogonal to g. Denote psi equals the absolute value of psi left parenthesis cap H comma g right parenthesis and let psi sub negative, psi sub zero and psi sub positive be the number of negative, zero and positive g-relevant eigenvalues so that psi equals psi sub negative plus psi sub zero plus psi sub positive. We impose the following order on the eigenvalues lambda sub one greater than lambda sub two greater than ellipsis greater than lambda sub psi sub positive greater than zero greater than lambda sub psi sub positive plus psi sub zero plus one greater than ellipsis greater than lambda sub psi. Denote by cap U the matrix with columns which form an orthonormal basis of the i-th eigenspace with the convention that the leading column is the only column onto which the gradient has nonzero projection. For one less than or equal to i less than or equal to psi sub positive and psi sub positive plus psi sub zero plus one less than or equal to j less than or equal to psi, define the following matrices cap U sub i positive equals left bracket cap U sub one ellipsis cap U sub i right bracket comma cap U sub j negative equals left bracket cap U sub j comma ellipsis comma cap U sub psi right bracket. The columns of cap U sub i positive represent the eigenspaces of the i most positive g-relevant eigenvalues, while cap U sub j negative represents the eigenspaces corresponding to the j most negative g-relevant eigenvalues. As a special case, let cap U sub positive equals cap U sub psi positive and cap U sub negative equals cap U sub left parenthesis psi sub positive plus psi sub zero plus one right parenthesis negative. Finally, let cap U equals left bracket cap U sub positive comma cap U sub negative right bracket. We now state a key assumption for the result.

Assumption D point one. There exists tau greater than zero and L sub g squared divided by (L sub g squared plus eta squared) less than nu less than or equal to one such that for any x in the nonnegative real numbers to the d with g not in Null H at least one of the following statements (i)-(iii) must hold.

(i) If psi sub plus is greater than or equal to one and psi sub i is greater than or equal to one then there exists one less than or equal to i less than or equal to psi sub plus and psi sub plus plus psi sub zero plus one less than or equal to j less than or equal to psi such that min {lambda sub i, negative lambda sub j} greater than or equal to tau, norm (U sub i plus U sub j plus transpose + U sub j minus U sub j minus transpose) g norm squared greater than or equal to nu norm U U transpose g norm squared.

(ii) If psi sub plus is greater than or equal to one then there exists one less than or equal to i less than or equal to psi sub plus such that lambda sub i greater than tau, norm U sub i plus U sub i plus intercal g norm squared greater than or equal to nu norm U U intercal g norm squared. Eigenvalues outside of Psi H, g are essentially "invisible" to the Krylov subspace built out of products of H and


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

(iii) If psi sub minus is greater than or equal to one then there exists some psi sub plus plus psi sub zero plus one less than or equal to j less than or equal to psi such that negative lambda sub j greater than or equal to tau, norm U sub j minus U sub j minus intercal g norm squared greater than or equal to nu norm U U intercal g norm squared. Recall that UUT, U sub j minus U sub j minus intercal and U sub i plus U sub i plus intercal represent a projection onto corresponding eigenspaces. Each part of Assumption D point one has a natural interpretation as a requirement that there is at least one large enough magnitude g-relevant eigenvalue for which the projection of the gradient onto the corresponding eigenspaces is not too small. This is a significant relaxation of a more conventional uniform bound on the magnitude of the eigenvalues. For example, a uniform bound on the smallest magnitude eigenvalues min {lambda sub psi sub plus, negative lambda sub psi sub plus plus psi sub zero plus one} greater than or equal to tau, immediately implies Assumption D point one-(i) with i = psi sub plus, j = psi sub plus plus psi sub zero plus one and nu = one. See Liu and Roosta for further discussion of this assumption.

Assumption D point one allows us to bound the number of Hessian vector products that are required for MINRES to satisfy ten. Indeed, assuming g not in Null H, we appeal to Liu and Roosta to bound the number of iterations until the MINRES termination tolerance ten is satisfied as

T sub S O L equals the minimum of the ceiling of the fraction of the square root of L sub g over mu divided by four times the logarithm of the fraction of four over the fraction of eta squared over L sub g squared plus eta squared minus one minus nu plus one and g, where g denotes the grade of g with respect to H of L i u R. We note that T sub S O I has a logarithmic dependence on the inexactness tolerance,

eta. On the other hand if psi sub negative is greater than or equal to one and Assumption D point one dash three holds, we appeal to Liu and Roosta to bound the iterations required to obtain a NPC direction as

T sub N P C equals the minimum of the maximum of the ceiling of the fraction of the square root of two times the sum of L sub g and mu over mu divided by four times the logarithm of the fraction of two times the sum of L sub g and mu times one minus nu over mu nu plus one and one and g. When nu equals one, it is clear from the statement of Assumption D point one dash three that all g-relevant eigenvalues are negative, which implies that negative curvature is detected at the very first iteration, i.e., T sub N P C equals one. If we adopt the convention that T sub N P C equals infinity when psi sub negative equals zero or Assumption D point one dash three is unsatisfied we bound the number of MINRES iterations as T equals the minimum of T sub N P C and T sub S O L. If g belongs to N u l l of H then g is declared a zero curvature direction at the very first iteration. We now prove the operational complexity results.

Corollary D point two (First Order Operational Complexity Algorithm one). Under the conditions of Theorem 3 point three and Assumption D point one, the total number of gradient evaluations and Hessian vector products in Algorithm one to obtain an epsilon sub g dash F O point is big O of epsilon sub g to the negative two, for d sufficiently large.

Proof. Due to Theorem 3 point three, the total number of outer iterations is big O of epsilon sub g to the negative two. To obtain the operational result we simply need to count the total number of gradient evaluations and Hessian vector products per iteration. The work required for each step of Algorithm one is equivalent to the number of MINRES iterations (i.e. Hessian vector product) plus a single gradient evaluation. In the case of Algorithm one the termination tolerance eta has no dependence on epsilon sub g. Considering the discussion above, for sufficiently large d, we bound the number of Hessian vector products as big O of one. The conclusion follows from the fact that big O of epsilon sub g to the negative two times one plus big O of one belongs to big O of epsilon sub g to the negative two. Corollary D point three (First Order Operational Complexity Algorithm two). Under the conditions of Theorem 3 point eight and Assumption D point one, the total number of gradient evaluations and Hessian vector products in Algorithm two to obtain an epsilon sub g dash F O point is log O of epsilon sub g to the negative three halves, for d sufficiently large.

Proof. The result is similar to Corollary D point two. We utilise Theorem 3 point eight to bound the total number of outer iterations as big O of epsilon sub g to the negative three halves. For Algorithm two, the MINRES termination tolerance is eta equals theta square root of epsilon sub g, so we bound the total number of Hessian vector products as log O of one for d large. The conclusion follows.


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

E. Local Convergence

In this section we provide the detailed proof for Theorem 3 point thirteen. Our proof follows a similar line of reasoning as that in Bertsekas but with several modifications and alterations specific to our setting and methodology. We assume in this section that I of x sub star comma zero does not equal the empty set as otherwise the analysis boils down to convergence of projected gradient to a trivial solution x sub star equals zero. Our main aim is to show that after a finite number of iterations, the iterates eventually end up in the following subspace

X sub star equals the set of x in R to the d such that x to the i equals zero, i in A of x sub star comma zero. We start with a lemma to show that, by choosing our inexactness tolerance delta sub k equals delta, with

Zero is less than delta is less than one divided by two minimum of i in script I of X star zero X star to the i,

where X star is some local minima, we can properly "separate" the true active and inactive set if X k is close enough to X star. That is, we apply the correct update to the true active and inactive indices.

Lemma E point one. Let X be a local minima of one and X k be an iterate of Algorithm four with delta chosen according to forty-four. There exists Delta sep such that if X k in B of X star, Delta sep, then script A of X k, delta equals script A of X star, zero. Proof. Define

Delta sep triangleq minimum of one divided by two minimum of i in script I of X star, zero, X star to the i minus delta, delta greater than zero. We first we prove script I of X k, delta k superset script I of X star, zero. For any i in script I of X star, zero and X k in B of X star, Delta sep we have

X star to the i minus X k to the i less than Delta sep is less than or equal to X star to the i minus delta divided by two implies X star to the i divided by two minus X k to the i is less than or equal to negative delta divided by two implies X star to the i divided by two plus delta divided by two is less than or equal to X k to the i implies three delta divided by two is less than or equal to X k to the i implies delta is less than X k to the i,

where the second to last line follows from forty-four.

Next we show that script I of X k, delta subset script I of X star, zero. In particular, we prove the contrapositive i in script A of X star, zero implies i in script A of X k, delta. For i in script A of X star, zero we know that X star to the i equals zero and so for X k in B of X star, Delta sep we have


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

That is,

I in script A left parenthesis x subscript k comma delta right parenthesis. With this result in hand, we know that we apply the "correct" update to x subscript k. That is, true active indices receive a projected gradient update, while indices in the true inactive set receive a Newton-type step.

Recall the the second-order sufficient condition in Assumption three point twelve. This condition is equivalent to angle brackets z comma nabla squared f left parenthesis x subscript star right parenthesis z angle brackets greater than zero, z in X subscript star. By the continuity of the Hessian, we are free to choose Delta subscript cvx greater than zero such that for any x in B left parenthesis x subscript star comma Delta subscript cvx right parenthesis the Hessian remains strongly positive definite on the subspace X. In other words, the constant, mu, satisfying mu triangleq minimum subscript z in X subscript star, x in B left parenthesis x subscript star comma Delta subscript cvx right parenthesis angle brackets z comma, nabla squared f left parenthesis x right parenthesis z angle brackets over norm z norm squared greater than zero, (forty-five)

is well defined. In the current notation, even if script I left parenthesis x subscript k comma delta right parenthesis equals script I left parenthesis x subscript star comma zero right parenthesis we have p subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis not in X subscript star as p subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis in double struck R superscript vertical bar script I left parenthesis x subscript k comma delta right parenthesis vertical bar is a subvector. Therefore, as a notational convenience, in this section we take subvectors and submatrices corresponding to a certain subset of indices, e.g., p subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis to be padded with zeros in the removed indices. Note that this implies that p subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis, p subscript k superscript script A left parenthesis x subscript k comma delta right parenthesis in double struck R superscript d k k and p subscript k equals p subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis plus p subscript k superscript modified script A left parenthesis x subscript k comma delta right parenthesis k but leaves the mechanics of Algorithm four unchanged. Now if script I left parenthesis x subscript k comma delta right parenthesis equals script I left parenthesis x subscript star comma zero right parenthesis we have p subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis equals p subscript k superscript script I left parenthesis x subscript star comma zero right parenthesis in X subscript star. Indeed, it is easy to see that for any t equals zero comma ellipsis comma g. script K subscript t left parenthesis H subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis, g subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis right parenthesis subseteq X subscript star. In addition, if x subscript k in B left parenthesis x subscript star comma Delta subscript cvx right parenthesis then, by H subscript k superscript script I left parenthesis x subscript k comma delta right parenthesis equals H subscript k superscript script I left parenthesis x subscript star comma zero right parenthesis equals

H k, mu plays the role of Krylov subspace regularity constant, o, (cf. Assumption three point seven) on script K subscript t left parenthesis H subscript k superscript script I left parenthesis x subscript star comma zero right parenthesis, g subscript k superscript script I left parenthesis x subscript star comma zero right parenthesis right parenthesis k. Indeed, together, these results imply that, for any t equals zero comma ellipsis comma g, we have

S is an element of curly K sub T left parenthesis H sub K superscript curly I left parenthesis x sub K comma delta right parenthesis, g sub K superscript curly I left parenthesis x sub K comma delta right parenthesis right parenthesis then angle bracket s comma H sub K superscript curly I left parenthesis x sub K comma delta right parenthesis s angle bracket is greater than or equal to mu times norm s squared.

From it is clear that we can do away with the D sub type equals N P C case and Assumption three point seven. With this in mind, we now demonstrate that the step size produced by the line search in Algorithm four is bounded.

Lemma E.2. Assume that f satisfies Assumption three point one and x is a local minima of one satisfying Assumption three point twelve. Then if x sub K is an element of B left parenthesis x sub star comma minimum left brace Delta sub c w comma Delta sub s e p right brace right parenthesis the step size produced by the line search in Algorithm four satisfies alpha sub K element of left bracket bar alpha comma one right bracket where

Bar alpha triangleq minimum left brace one comma fraction two left parenthesis one minus rho right parenthesis mu over L sub g comma fraction delta over norm p sub K superscript curly I norm right brace period.

Proof. x sub K element of B left parenthesis x sub star comma minimum left brace Delta sub c v x comma Delta sub s e p right brace right parenthesis implies that curly I left parenthesis x sub K comma delta right parenthesis equals curly I left parenthesis x sub star comma zero right parenthesis is not equal to the empty set and it holds. It follows that MINRES always selects D sub type equals S O L step.

The result follows from the step size selection procedure in Algorithm four and the analysis in the S O L case of Lemma C.1.

Building on Lemma E.1, our next result, Lemma E.3, will show that, close enough to X sub star, the active set update will be large enough and the inactive set update small enough that the zero bound constraints at x sub K plus one coincide with the zero bound constraints at X star, i.e., curly A left parenthesis x sub K plus one comma zero right parenthesis equals curly A left parenthesis x superscript star comma zero right parenthesis. The intuition for this result is that the gradient and hence the step in the inactive indices should be going to zero as x sub K approaches X sub star. By contrast, in the active set, a non-degeneracy condition (Assumption three point eleven) ensures there is positive gradient in the active indices arbitrarily close to the boundary. When curly A left parenthesis x sub K plus one comma zero right parenthesis equals curly A left parenthesis x superscript star comma zero right parenthesis, the fixed active set and small inactive step can also be used to ensure that our iterates do not drift too far from the starting point. This is the second part of Lemma E.3.


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

Lemma E.3. Suppose that f satisfies Assumption three point one. Let X sub two be a local minima satisfying Assumptions three point eleven and three point twelve. If delta is chosen according to, then the following two results hold:

One. There exists Delta sub b m d greater than zero such that x sub K element of B left parenthesis x sub star comma Delta sub b n d right parenthesis implies curly A left parenthesis x sub K comma delta right parenthesis equals curly A left parenthesis x sub K plus one comma zero right parenthesis equals curly A left parenthesis x sub star comma zero right parenthesis. Two. Given a Delta greater than zero, we can choose Delta sub c l s element of left parenthesis zero comma Delta sub b n d right parenthesis such that norm x sub K minus x sub star norm less than Delta sub c l s implies that norm x sub K plus one minus x sub star norm less than Delta. Proof. We stipulate that Delta sub b n d is less than or equal to minimum left brace Delta sub s e p comma Delta sub e v x right brace. Note that, in this case, curly A left parenthesis x sub K comma delta right parenthesis equals curly A left parenthesis x sub star comma zero right parenthesis by Lemma E.1 and alpha sub K element of left bracket bar alpha comma one right bracket where bar alpha defined as min of one, two times one minus rho times mu over L sub g, delta over norm p sub k superscript I. Equation forty-eight by Lemma E point two. It is also clear that MINRES selects D sub t w e equals SOL. We first show that the step size, alpha sub k, can be uniformly lower bounded for x sub k close enough to X star. We do this by showing that the step norm p sub k superscript I can be upper bounded. Specifically, due to forty-six, the step, p sub k superscript I, is upper bounded by the gradient magnitude (compare with rho equals mu) norm p sub k superscript I is less than or equal to norm g sub k superscript I over mu. Equation forty-nine

Next we use the continuity of nabla f of x and the fact that g star superscript I of x star, zero equals zero to choose Delta sub zero less than or equal to min of Delta sub s e p, Delta sub c v x such that x sub k in B of x star, Delta sub zero implies norm g sub k superscript I of x sub k, delta equals norm g sub k superscript I of x star, zero less than or equal to mu delta over two, where in the first equality we used Lemma E point one. This implies norm p sub k superscript I less than or equal to delta over two. Equation fifty and hence by forty-eight bar alpha defined as min of one, two times one minus rho times mu over L sub q. We now show that A of x star, zero is a subset of A of x sub k plus one, zero. Let i in A of x star, zero. Define e sub k as x sub k minus x star. By Assumption three point eleven and the continuity of nabla f of x, there exists Delta sub one such that, for norm e sub k less than or equal to Delta sub one, g of x sub k raised to the power j equals g of x star plus e sub k raised to the power j greater than gamma over two, for all j in A of x star, zero. Consider Delta sub two equals min of Delta sub zero, Delta sub one, bar alpha gamma over two. If x sub k in B of x star, Delta sub two, we have x sub k raised to the power i equals x sub k raised to the power i minus x star raised to the power i less than Delta sub two less than or equal to bar alpha gamma over two. Using this bound and the lower bound for the gradient and step size we compute the update as

X sub K sup I minus alpha sub K G sub K sup I is less than or equal to X sub K sup I minus the quantity bar alpha gamma divided by two is less than or equal to zero implies X sub K plus one sup I equals P of the quantity X sub K sup I plus alpha sub K P sub K sup I equals zero , which implies

I in script A of the quantity X sub K plus one , zero . Next, we show script A of the quantity X sup star , zero contains script A of the quantity X sub K plus one , zero . In particular, we prove the contrapositive statement I in script I of the quantity X star , zero implies I in script I of the quantity X sub K plus one , zero . Suppose I in script I of the quantity X star , zero the result will follow by showing that the X sub K plus one remains bounded away from zero. Let Delta sub b n d equals the minimum of the set Delta sub zero , Delta sub one , Delta sub two , Delta sub sep , Delta sub e v x . Having X sub K in B of the quantity X star , Delta sub b n d implies script I of the quantity X star , zero equals script I of the quantity X sub K , delta . Additionally, the bound applies and so alpha in the interval bar alpha , one implies

Alpha absolute value P sub K sup I absolute value is less than or equal to the norm of P sub K sup script I of the quantity X sub K , delta is less than or equal to delta divided by two ,


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

which yields

X sub K sup I plus alpha P sub K sup I is greater than or equal to X sub K sup I minus alpha absolute value P sub K sup I absolute value is greater than or equal to X sub K sup I minus the quantity delta divided by two is greater than the quantity delta divided by two ,

where the final inequality follows from I in script I of the quantity X star , zero equals script I of the quantity X sub K , delta implies X sub K sup I is greater than delta . Finally we compute the step as

X sub K plus one equals P of the quantity X sub K sup I plus alpha P sub K sup I equals X sub K sup I plus alpha P sub K sup I is greater than zero , which is the result.

Now for the second part of the result. Fix Delta greater than zero . From the first part of the result we know that for X sub K in B of the quantity X star , Delta sub b n d we have script A of the quantity X sub K , delta equals script A of the quantity X sub K plus one , zero equals script A of the quantity X star , zero , which implies X sub K plus one sup script A of the quantity X sub K , delta equals X sub K plus one sup script A of the quantity X sub K plus one , zero equals zero and X star sup script A of the quantity X sub K , delta equals X star sup script A of the quantity X star , zero equals zero . Applying these equalities we obtain

Norm of x sub k plus one minus x star equals norm of x sub k plus one superscript I of left parenthesis x sub k comma delta right parenthesis minus x star superscript I of left parenthesis x sub k comma delta right parenthesis equals norm of left bracket P of left parenthesis x sub k plus alpha sub k p sub k right parenthesis right bracket superscript I of left parenthesis x sub k comma delta right parenthesis minus x star superscript I of left parenthesis x sub k comma delta right parenthesis equals norm of left parenthesis x sub k plus alpha sub k p sub k right parenthesis superscript I of left parenthesis x sub k comma delta right parenthesis minus x star superscript I of left parenthesis x sub k comma delta right parenthesis less than or equal to norm of x sub k superscript I of left parenthesis x sub k comma delta right parenthesis minus x star superscript I of left parenthesis x sub k comma delta right parenthesis plus alpha sub k norm of p sub k superscript I of left parenthesis x sub k comma delta right parenthesis less than or equal to norm of x sub k minus x star plus norm of g sub k superscript I of left parenthesis x sub k comma delta right parenthesis divided by mu, where we drop the projection on line three due to left parenthesis x sub k plus alpha sub k p sub k right parenthesis superscript I of left parenthesis x sub k comma delta right parenthesis greater than delta divided by two when x sub k belongs to B left parenthesis x star comma Delta sub b n d right parenthesis. Again,

Equals g sub k superscript I of left parenthesis x sub k comma delta right parenthesis equals g sub k superscript I of left parenthesis x star comma zero right parenthesis k so, by the continuity of nabla f left parenthesis x right parenthesis, we are free to choose Delta sub three so that x sub k belongs to B left parenthesis x star comma Delta sub three right parenthesis implies g k

Norm of g sub k superscript I of left parenthesis x sub k comma delta right parenthesis equals norm of g sub k superscript I of left parenthesis x star comma zero right parenthesis less than mu Delta divided by two. Finally, we can choose Delta sub c l s equals minimum left brace Delta sub b n d comma Delta sub three comma Delta divided by two right brace so that, if x sub k belongs to B left parenthesis x star comma Delta sub c l s right parenthesis, we have

Norm of x sub k plus one minus x star less than or equal to norm of x sub k minus x star plus norm of g sub k superscript I of left parenthesis x sub k comma delta right parenthesis divided by mu less than Delta divided by two plus Delta divided by two equals Delta. The second part of Lemma E point three can be used with the choice Delta equals Delta sub b n d to obtain

Norm of x sub k minus x star less than Delta sub c l s implies norm of x sub k plus one minus x star less than Delta sub b n d. In this case, we can guarantee, due to Delta sub c l s less than Delta sub b n d and the first part of Lemma E point three applied to x sub k, that

A of left parenthesis x sub k comma delta right parenthesis equals A of left parenthesis x sub k plus one comma zero right parenthesis equals A of left parenthesis x star comma zero right parenthesis. And from x sub k plus one belongs to B left parenthesis x star comma Delta sub b n d right parenthesis and the first part of Lemma E point three again

Script A of X subscript k plus one comma delta equals Script A of X subscript k plus two comma zero equals Script A of X subscript star comma zero. Together, these results show that X subscript k in B of X subscript star comma Delta subscript c L S implies X subscript k plus one comma X subscript k plus two in X subscript star. This means that the iterates of our algorithm essentially "look" like unconstrained minimization in this subspace. Unfortunately, with the results we have so far, we cannot guarantee that the iterates continue to stay close enough to the minima beyond iteration k plus two. Lemma E point four will overcome this problem by using the second-order sufficient condition and adapting an unconstrained optimization result. The main idea is that the "strict convexity" on X subscript star induced by Assumption three point twelve implies that there exists a small "basin" restricted to X subscript star that the iterates will not leave once they enter. We can then use Lemma E point three to show that our iterates eventually enter X, and the corresponding basin.


## Inexact Newton-type Methods for Optimization with Nonnegativity Constraints

Lemma E point four. Let f satisfy Assumption three point one and X subscript star be a local minima satisfying Assumptions three point eleven and three point twelve. Let delta be chosen according to forty-four. If there is an iterate, X subscript k, of Algorithm four such that Script A of X subscript k comma delta equals Script A of X subscript k comma zero equals Script A of X subscript star comma zero and Script A of X subscript k plus one comma zero equals Script A of X subscript star comma zero i.e. X subscript k, X subscript k plus one in X subscript star then there exists a neighborhood restricted to X x of X subscript star comma Script N of X subscript star comma, such that if Xk in Script N of X subscript star and then X subscript k plus one in Script N of X subscript star. Additionally, Script N of X subscript star is independent of the iterates and can be chosen arbitrarily small, i.e., for any Delta greater than zero we have

Script N of X subscript star is a subset of B of X subscript star comma Delta. Proof. We fix Delta less than or equal to Delta subscript c v x and define

Script N of X subscript star equals the set of X in B of X subscript star comma Delta intersect X subscript star such that f of X is less than or equal to f of X subscript star plus the fraction mu over two times the fraction Delta over one plus L subscript g over mu squared. We will show that this set is the desired neighborhood on X subscript star in the sense there exists an open ball in the relative interior of X subscript star. The mean value theorem implies that there is a constant t in the interval zero comma one such that for any

X, Y in Script R to the power of d, f of Y equals f of X plus the inner product of nabla f of X comma Y minus X plus one-half inner product of Y minus X comma nabla squared f of X plus t times Y minus X times Y minus X. Fifty-two

We obtain, by Assumption three point one,

F of y is less than or equal to F of x plus the inner product of the gradient of F at x and the difference between y and x plus the quantity L sub g divided by two times the norm of the difference between y and x squared. Let x equal X and y belong to the intersection of B at x star, Delta, and X star. The fact that y and X star only have nonzero components in the set I of x star, zero, while the optimality condition seven c implies the gradient of F at x star only has zero components in the set I of x star, zero, allows us to write

F of y is less than or equal to F of x star plus the quantity L sub g divided by two times the norm of the difference between y and x star squared, so by choosing y close enough to X star, we have y belongs to the set N of x star. This implies that the set N of x star is a neighborhood of X star, in

X star. Let x equal X and y equal x sub k for x sub k belong to the intersection of B at x star, Delta, and X star. Then, x star plus t times the difference between x sub k and x star belongs to the intersection of B at x star, Delta, and X, for any t in the interval from zero to one. Hence,

Forty-five applied to fifty-two yields the quantity mu divided by two times the norm of the difference between x sub k and x star squared is less than or equal to F of x sub k minus F of x star. Fifty-three

Next, we seek to bound the distance between subsequent errors. Since the set A of x sub k, Delta equals the set A of x sub k plus one, zero, equals the set A of x star, zero, we have x sub k plus one to the power of the set A of x sub k, Delta equals x sub k plus one to the power of the set A of x sub k plus one, zero, equals zero, and x star to the power of the set A of x sub k, Delta, equals x star to the power of the set A of x star, zero, equals zero. We compute

The norm of x sub k plus one minus x star equals the norm of x sub k plus one raised to the script I of x sub k plus one comma zero minus x star raised to the script I of x star comma zero equals the norm of x sub k plus one raised to the script I of x sub k comma delta minus x star raised to the script I of x sub k comma delta equals the norm of the projection of x sub k plus alpha sub k p sub k raised to the script I of x sub k comma delta minus x star raised to the script I of x sub k comma delta equals the norm of x sub k raised to the script I of x sub k comma delta minus x star raised to the script I of x sub k comma delta plus alpha sub k p sub k raised to the script I of x sub k comma delta is less than or equal to the norm of x sub k raised to the script I of x sub k comma delta minus x star raised to the script I of x sub k comma delta plus alpha sub k times the norm of p sub k raised to the script I of x sub k comma delta comma.

where the fourth line follows from script I of x sub k comma delta equals script I of x sub k plus one comma zero and i in script I of x sub k plus one comma zero implying that zero is less than x sub k plus one raised to the power of i equals the projection of x sub k raised to the power of i plus alpha sub k p sub k raised to the power of i implies the projection of x sub k raised to the power of i plus alpha sub k p sub k raised to the power of i equals x sub k raised to the power of i plus alpha sub k p sub k raised to the power of i. Since script I of x sub k comma delta equals script I of x star comma zero and x sub k in the ball of x star comma delta sub cvx comma, we know equation forty-nine holds. We can refine equation forty-nine by combining Assumption three point one, script I of x sub k comma delta equals script I of x sub k comma zero equals script I of x star comma zero and equation seven c to obtain the norm of g sub k raised to the script I of x sub k comma delta equals the norm of g sub k raised to the script I of x sub k comma zero minus g star raised to the script I of x star comma zero is less than or equal to the norm of g sub k minus g star is less than or equal to L sub g times the norm of x sub k minus x star equals L sub g times the norm of x sub k raised to the script I of x sub k comma delta minus x star raised to the script I of x sub k comma delta.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Combining this bound,

alpha sub k is less than or equal to one, left parenthesis forty-nine right parenthesis text and left parenthesis fifty-four right parenthesis norm x sub k plus one minus x sub star norm is less than or equal to norm x sub k superscript script I left parenthesis x sub k comma delta right parenthesis minus x sub star superscript script I left parenthesis x sub k comma delta right parenthesis norm plus L sub g over mu norm x sub k superscript script I left parenthesis x sub k comma delta right parenthesis minus x sub star superscript script I left parenthesis x sub k comma delta right parenthesis norm equals left parenthesis one plus L sub g over mu right parenthesis norm x sub k superscript script I left parenthesis x sub k comma delta right parenthesis minus x sub star superscript script I left parenthesis x sub k comma delta right parenthesis norm equals left parenthesis one plus L sub g over mu right parenthesis norm x sub k minus x sub star norm. Fifty-five

We now show that this is enough to guarantee that x sub k plus one is in script N left parenthesis x sub star right parenthesis. In particular, if x sub k is in script N left parenthesis x sub star right parenthesis then Xk is in B left parenthesis x sub star comma Delta sub cvx right parenthesis, so by combining the definition of script N left parenthesis x sub star right parenthesis and fifty-three we have mu over two norm x sub k minus x sub star norm squared is less than or equal to f left parenthesis x sub k right parenthesis minus f left parenthesis x sub star right parenthesis is less than or equal to mu over two left parenthesis Delta over one plus L sub g over mu right parenthesis squared implies norm x sub k minus x sub star norm is less than Delta over one plus L sub g over mu. Applying fifty-five we have

The norm of X sub K plus one minus X sub star is less than Delta, which implies that X sub K plus one is in B of X sub star, Delta cap X sub star. In addition, Alpha sub K satisfies the line search criterion, which guarantees that f of X sub K plus one is less than or equal to f of X sub K and so f of X sub K plus one minus f of X sub star is less than or equal to f of X sub K minus f of X sub star is less than or equal to Mu over two times the quantity Delta over one plus L sub G over Mu squared, which implies X sub K plus one is in Script N of X sub star, as needed. In the above argument we are free to replace Delta with any Delta prime in zero to Delta which implies that we can always choose Script N of X sub star sufficiently small.

We our now ready to prove Theorem three point thirteen.

Proof of Theorem three point thirteen. Note that we are free to choose the neighbourhood Script N of X sub star of X sub two on X sub star from Lemma E point four small. We therefore select Delta sub zero less than Delta sub C V X and Script N of X sub star to satisfy the following inclusions

B of X sub star, Delta sub zero cap X sub star is subset or equal to Script N of X sub star is subset or equal to B of X sub star Delta sub B N D cap X sub star. Fifty-six.

By the second part of Lemma E point three, there exists Delta sub C L S less than or equal to Delta sub B N D such that the following inclusions hold

X sub K in B of X sub star, Delta sub C L S Longrightarrow X sub K plus one in B of X sub star, Delta sub zero. Fifty-seven.

Choose Delta sub a c t v equals Delta sub c l, and suppose that x sub bar k is in B left( x sub star, Delta sub a c t v right). The first inclusion of fifty-seven, implies script A left( x sub bar k, delta right) equals script A left( x sub bar k plus one, zero right) equals script A left( x sub star, zero right), i.e. x sub bar k plus one is in X sub star, by Delta sub c l s is less than or equal to Delta sub b n d and the first part of Lemma E point three. This fact and the second inclusion of fifty-seven, implies x sub bar k plus one is in script N left( x sub star right) and therefore, by the second inclusion of fifty-six, script A left( x sub bar k plus one, delta right) equals script A left( x sub bar k plus two, zero right) equals script A left( x sub star, zero right), Again by the first part of Lemma E point three. Combining what we have so far, we obtain script A left( x sub bar k plus one, delta right) equals script A left( x sub bar k plus one, zero right) equals script A left( x sub star, zero right), which is the result for bar k plus one. Additionally, however, we can apply Lemma E point four applied to the iterate k plus one to obtain x sub bar k plus two is in script N left( x sub star right). The argument for bar k plus one may now be repeated for k is greater than bar k plus two. For instance, fifty-six and x sub bar k plus two is in script N left( x sub star right) implies x sub bar k plus two is in B left( x sub star, Delta sub b n d right) and so script A left( x sub bar k plus two, delta right) equals script A left( x sub bar k plus three, zero right) equals script A left( x sub star, zero right) by Lemma E point three and x sub bar k plus three is in script N left( x sub star right) by Lemma E point four, which yields the result for bar k plus two and sets up the argument for x sub bar k plus three. Continuing in this fashion yields the result for the given

Delta sub a c t v. F. Further Details and Extended Numerical Results

In this section we provide some additional elements of our proposed methods, further details on our experimental setup, and also give a more complete description of various problems we consider for our numerical simulations.


## F point one. Line Search Algorithms

Here, we gather the line search algorithms used for the theoretical analysis as well as the empirical evaluations of our methods.


## F point two. Smooth Reformulation of Nonsmooth L one Regression

Consider L one regularization of a smooth function, f, as given in twelve. Unfortunately, even when f is smooth, the objective twelve is non-differentiable when x superscript i equals zero for some i equals one, through d. However, it was shown in Schmidt et al. two thousand seven that one can reformulate twelve into a smooth problem by splitting x into positive and negative parts, i.e., x sub plus equals max left( zero, x right) and x sub minus equals negative min left( zero, x right), where "max" and "min" are taken elementwise. Indeed, we have the identities and x superscript i equals x sub plus superscript i minus x sub minus superscript i, absolute value of x superscript i equals x sub plus superscript i plus x sub minus superscript i, which we can use to reformulate fifty-eight as a constrained problem on script R superscript two d. In particular, the following auxiliary function is equivalent to the objective of twelve

F of x plus and x minus equals f of x plus minus x minus plus lambda sum from i equals one to d of x plus to the power of i plus x minus to the power of i. If we make the identification z equals x plus, x minus belongs to real numbers to the power of two d, we obtain the auxiliary minimisation problem defined by min over z belongs to real numbers to the power of two d F of z subject to z greater than or equal to zero.

The nonpositivity condition in fifty-eight ensures that z can be interpreted as the positive and negative part of the underlying variable, x. The gradient and Hessian of the auxiliary function, F, are given by gradient of F of x plus, x minus equals, open parenthesis, gradient of f of x plus minus x minus plus lambda one sub d by one, negative gradient of f of x plus minus x minus plus lambda one sub d by one, close parenthesis, comma, Hessian of F of x plus, x minus equals, open parenthesis, Hessian of f of x plus minus x minus, negative Hessian of f of x plus minus x minus, negative Hessian of f of x plus minus x minus, Hessian of f of x plus minus x minus, close parenthesis. Remark F point one (Evaluating the gradients and Hessian-vector products). Clearly, evaluating the gradient of F requires only a single evaluation of the original gradient, gradient of f. On the other hand, for computing a Hessian-vector product of F with a


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

vector V equals left-parenthesis V sub one transposed, V sub two transposed right-parenthesis transposed element of double-struck cap R superscript two D, we have nabla superscript two F left-parenthesis X sub plus, X sub minus right-parenthesis V equals left-parenthesis begin array nabla superscript two F left-parenthesis X sub plus minus X sub minus right-parenthesis V sub one minus nabla superscript two F left-parenthesis X sub plus minus X sub minus right-parenthesis V sub two end array right-parenthesis, which requires two Hessian-vector products of the original function F in the form nabla superscript two F left-parenthesis X right-parenthesis W where

W element of double-struck cap R superscript D. As a sanity check, we show that the first order stationary points of equation fifty-eight and equation twelve coincide. The first order necessary conditions for equation fifty-eight imply that for J equals one, dots, D and

I equals J, X sub plus superscript star element of I greater than or equal to zero, and left brace begin array left bracket nabla F left-parenthesis X sub plus superscript star minus X sub minus superscript star right-parenthesis right bracket superscript I plus lambda equals zero, iff X sub plus superscript star element of I greater than zero, left bracket nabla F left-parenthesis X sub plus superscript star minus X sub minus superscript star right-parenthesis right bracket superscript I plus lambda greater than or equal to zero, iff X sub plus superscript star element of I equals zero, end array right brace, equation fifty-nine and for J equals D plus one, dots, two D and

I equals J minus D, X sub minus superscript star element of I greater than or equal to zero, and left brace begin array negative left bracket nabla F left-parenthesis X sub plus superscript star minus X sub minus superscript star right-parenthesis right bracket superscript I plus lambda equals zero, iff X sub minus superscript star element of I greater than zero, negative left bracket nabla F left-parenthesis X sub plus superscript star minus X sub minus superscript star right-parenthesis right bracket superscript I plus lambda greater than or equal to zero, iff X sub minus superscript star element of I equals zero, end array right brace. equation sixty

On the other hand, the first order stationary points of the problem equation twelve can be expressed in terms of the Clarke subdifferential as those points X superscript star for which zero element of nabla F left-parenthesis X superscript star right-parenthesis plus partial mod X superscript star mod sub one. That is, for I equals one, dots, D, we have left brace begin array left bracket nabla F left-parenthesis X superscript star right-parenthesis right bracket superscript I plus lambda equals zero if X superscript star element of I greater than zero, left bracket nabla F left-parenthesis X superscript star right-parenthesis right bracket superscript I minus lambda equals zero if X superscript star element of I less than zero, mod left bracket nabla F left-parenthesis X superscript star right-parenthesis right bracket superscript I mod less than or equal to lambda if X superscript star element of I equals zero. end array right brace, equation sixty-one

We first show that if Z star equals left bracket X plus star, X minus star right bracket satisfies fifty-nine and sixty then X star equals X plus star minus X minus star satisfies sixty-one. First, suppose left bracket X star right bracket to the I is greater than zero. In this case, we must have left bracket X star right bracket to the I equals left bracket X plus star right bracket to the I is greater than zero equals left bracket X minus star right bracket to the I, which from the first case of fifty-nine implies the first case of sixty-one. When left bracket X star right bracket to the I is less than zero, since left bracket X star right bracket to the I equals left bracket X minus star right bracket to the I is greater than zero equals left bracket X plus star right bracket to the I, the first case of sixty implies the first case of sixty-one. Finally, when left bracket X star right bracket to the I equals zero, we have left bracket X plus star right bracket to the I equals left bracket X minus star right bracket to the I equals zero, and we appeal to the second case of both fifty-nine and sixty to obtain left bracket nabla F left parenthesis X star right parenthesis right bracket to the I is greater than or equal to negative lambda, and left bracket nabla F left parenthesis X star right parenthesis right bracket to the I is less than or equal to lambda, which implies the absolute value of left bracket nabla F left parenthesis X star right parenthesis right bracket to the I absolute value is less than or equal to lambda, i.e., the third case of sixty-one.

We now show that if X star equals X plus star minus X minus star satisfies sixty-one, then if Z star equals left bracket X plus star, X minus star right bracket satisfies fifty-nine and sixty. Consider the first case of sixty-one. Noting again that left bracket X star right bracket to the I equals left bracket X plus star right bracket to the I is greater than zero equals left bracket X minus star right bracket to the I, it clearly implies the first and the second cases of fifty-nine and sixty, respectively (recall lambda is greater than zero). Similarly, the second case of sixty-one implies the second and the first cases of fifty-nine and sixty, respectively. Finally, it is clear that the third case of sixty-one implies the second case for both fifty-nine and sixty.


## F point three. Additional Experimental Details

Oracle Calls as Complexity Measure Following the typical convection in the optimisation literature, in all our experiments, we plot the objective value against the total number of oracle calls for function, gradient, and Hessian-vector product evaluations. We adopt this approach because the measurement of "wall-clock" time can be heavily dependent on specific implementation details and computational platform. In contrast, counting the number of equivalent function evaluations, as an implementation and system independent unit of complexity is more appropriate and fair. More specifically, upon evaluating the function, computing its gradient is equivalent to one additional function evaluation, and computing a Hessian-vector product requires two additional function evaluations compared to a gradient evaluation. For example, in neural networks, for a given data at the input layer, evaluation of network's output, i.e., function evaluation, involves one forward propagation. The corresponding gradient is computed by performing one additional backward propagation. After computing the gradient, an additional forward followed by a backward propagation give the corresponding Hessian-vector product.

Parameter Settings In all experiments we set epsilon subscript k equals delta subscript k equals square root of epsilon subscript g as per Theorem three point eight. For the Newton-MR TMP we set the inexactness condition for MINRES, i.e., ten, to eta equals ten to the minus two for convex problems and eta equals one for nonconvex problems. We apply a less stringent tolerance in the nonconvex case to maximise the chances of terminating early with a "good enough"


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

SOL type solution. Indeed, running the solver too long increases the odds that spurious negative curvature direction will arise as part of iterations. Since such directions never occur in convex settings, one can afford to solve the subproblems more accurately.

For projected Newton-CG, we use the parameter settings from the experiments in Xie and Wright. Specifically, in the notation of Xie and Wright, we set the accuracy parameter and backtracking parameter to zeta equals theta equals zero point five and the step acceptance parameter to eta equals zero point two. Furthermore, following the algorithmic to have equivalent termination conditions, we modify the gradient negativity check description of Xie and Wright, and from g sub L superscript i is less than negative epsilon sub L to the three halves to g sub k superscript i is less than negative epsilon sub k for this method.

For projected gradient and Newton-MR TMP, we set the scaling parameter in Algorithms five and six to zeta equals zero point five and the sufficient decrease parameter to rho equals ten to the negative four. All line searches are initialised from alpha sub zero equals one. We note that, for both FISTA and PGM, we terminate the iterations when absolute value of left parenthesis f left parenthesis x sub k right parenthesis plus lambda norm x sub k norm sub one minus left parenthesis f left parenthesis x sub k minus one right parenthesis plus lambda norm x sub k minus one norm sub one right parenthesis is less than ten to the negative eight on the L one problem and absolute value of f left parenthesis x sub k right parenthesis minus f left parenthesis x sub k minus one right parenthesis is less than ten to the negative eight otherwise. We set the momentum term in PGM to beta equals zero point nine and select the fixed step size by starting from alpha equals one and successively shrinking the step size by a factor of ten until the iterates are stable for the duration of the experiment, i.e., no divergence or large scale oscillations. This procedure resulted in a step size of alpha equals ten to the negative three for the L one MLP (Figure three) and alpha equals one for the NNMF problems (Figures four and five).

We now give a more complete description of each of the objective functions.

Multinomial Regression We first consider is the problems of multinomial regression on C classes. Specifically, consider a set of data items left brace a sub i, b sub i right brace sub i equals one to n subset of real numbers to the d times left brace one, up to C right brace. Denote the weights of each class as x sub one, up to, x sub C and define x equals left bracket x sub one, up to, x sub C minus one right bracket. We are free to take x sub C equals zero as class C is identifiable from the weights of the other classes. The objective, f, is given by f left parenthesis x right parenthesis equals one over n summation from i equals one to n summation from c equals one to C minus one negative one left parenthesis b sub i equals c right parenthesis log left parenthesis softmax left parenthesis x sub c, a sub i right parenthesis right parenthesis,

where one left parenthesis dot right parenthesis is the indicator function and softmax left parenthesis x sub c, a sub i right parenthesis equals the fraction of exp left parenthesis inner product of x sub c, a sub i right parenthesis over summation from c equals one to C exp left parenthesis inner product of x sub c, a sub i right parenthesis. In this case, the objective is convex. We allow for a constant term in each set of weights, x sub c, which we do not apply the L one penalisation to.

All methods for this example are initialised from x sub zero equals zero. Neural Network Again, suppose we have a set of data items left brace a sub i, b sub i right brace sub i equals one to n subset of real numbers to the d times left brace one, up to C right brace. We consider a small two layer network with a smooth activation function. Specifically, we consider the sigmoid weighted linear unit (SiLU) activation defined by sigma left parenthesis x right parenthesis equals the fraction of x over one plus e to the negative x. We note that the SiLU activation is similar to ReLU and is the product of a linear activation with a standard sigmoid activation. We define a network, h left parenthesis dot semicolon x right parenthesis parameterised by the weights, x, with the following architecture

Input D goes to Linear one hundred goes to Si LU goes to Linear one hundred goes to Si LU goes to Linear ten, where the number in brackets denotes the size of the output from the layer. Note that we allow for a bias term in each linear layer which we do not apply the L one penalty to. The objective function, F, is given by cross entropy loss incurred by the network over the entire dataset

F of X equals negative one divided by N sum from I equals one to N log of exp of H of A sub I semicolon X to the power B sub I divided by sum from C equals one to C exp of H of A sub I semicolon X to the power C.

The weights for layer I, denoted X, are initialised with the default PyTorch initialisation, that is, via independent uniform draw

X sub I is distributed according to U from negative square root of K to square root of K, where K equals one divided by number of Inputs with number of Inputs the number of input features into the layer.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

NNMF Problem A common choice for is a standard Euclidean distance function

WH) equals one minus norm squared F,

where norm squared F is the Frobenius matrix norm. In this case, is nonconvex in both W and H, when considered simultaneously, but convex so long as one of the variables is held fixed. This motivates the standard approach to solving based on alternating updates to W and H where one variable is fixed while optimising over the other.

By contrast, to test our algorithm, we specifically consider solving as a nonconvex problem in W and H simultaneously. For our first experiment, we consider a text data application. When comparing text documents, we aim to have a similarity measure that is independent of document length. Indeed, we consider documents similar if they have similar word frequency ratios. This notion of similarity is naturally captured by measuring alignment between vectors, which motivates the use of a loss function based on cosine similarity as

D of Y,WH equals one minus cosine theta of Y sub I, WH sub I.

where theta of Y sub I, WH sub I is the angle between the ith predicted and true document. This loss function only considers the alignment between documents. Indeed, we can write cosine theta of Y sub I, WH sub I equals Y sub I, WH sub I.

However, using this representation it is clear that, due to the nonnegativity of Y and WH, ranges between zero and one. It is also clear that is equivalent to a Euclidean distance with normalisation norm squared of WH sub I.

equals Y sub I.

In our second example, we consider with a standard Euclidean distance function and a nonconvex regularisation term R one. Specifically, we consider a version of the smooth clipped absolute deviation regularisation first proposed in Fan and Li. SCAD uses a quadratic function to smoothly interpolate between a regular one penalty and a constant penalty norm X is less than one,

SCAD A comma A of X equals

A minus one, norm X is less than A, norm X is greater than A.

The SCAD penalty reduces the downward bias on large parameters typical of the one penalty while still allowing for sparsification of small parameters. We consider a twice smooth clipped absolute deviation, which we call TSCAD. TSCAD replaces the quadratic interpolant with a quartic, Q X comma A of X, which allows for a twice continuously differentiable penalty norm X is less than A, A minus one.

TSCAD A comma A of X equals Q X comma A of X.

norm X is greater than A.

The regularisation term is simply given by

R X of W, H equals sum over I and J of TSCAD A comma A of W sub I J plus sum over I and J of TSCAD A comma A of H sub I J.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Due to the inherent nonconvexity of the NNMF problem, initialisation is key to obtaining good results. We utilised a simple half normal initialisation. Indeed, because the data matrix for each NNMF example satisfies zero is less than or equal to Y is less than or equal to one, we produced the initialisation by drawing W sub zero prime sub I J is distributed according to N of zero comma one and H sub zero prime sub I J is distributed according to N of zero comma one and normalising in the following manner

W sub zero maps to W sub zero prime elementwise absolute value divided by square root of max of elementwise absolute value of W sub zero prime H sub zero prime, H sub zero maps to H sub zero prime elementwise absolute value divided by square root of max of elementwise absolute value of W sub zero prime H sub zero prime, where elementwise absolute value of dot is taken elementwise. This initialisation was found to result in nontrivial solutions to


## F point four. Simulations For Fast Local Convergence

In Figures six and seven, we consider an extended version of the results in Figures one and two, respectively. Specifically, we plot the progress in each of the termination conditions seven. Part a of all figures depict the gradient norm on the inactive set. For Newton-MR TMP, this is the termination condition associated with the Newton-MR portion of the step. We see in both Figures six and seven that, for our method, the inactive set termination condition is steadily reduced until a point is reached where the convergence becomes extremely rapid. This is consistent with the theoretical predictions in Theorem three point one three and Corollary three point one four. We note that projected Newton-CG exhibits similar behaviour once it reaches Newton-CG step phase but to a lesser extent.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

F point five. Timing Results

For completeness, in the following section we give results presented in Section four in terms of "wall-clock" time. As noted earlier, wall-clock timing results are implementation and platform dependent. In particular, results are unreliable for small time scales. However, we note that, over larger time scales, the wall-clock time results generally conform with the corresponding oracle call results.


## Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

Five times ten to the power of negative one, ten to the power of negative five, ten to the power of negative three, ten to the power of negative one, ten to the power of one, ten to the power of three, ten to the power of negative one Time in seconds. Figure eleven. Wall-clock timing results for NNMF with cosine distance on top one thousand TF-IDF features of the twenty Newsgroup dataset