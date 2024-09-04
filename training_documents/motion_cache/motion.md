## Relative Motion Dynamics in the Restricted Three-Body Problem

This paper discusses the derivation and simplification of equation sets for the relative motion dynamics characterization in the restricted three-body problem. As opposed to previous models proposed in the literature, the relative motion is studied in a frame local to the target spacecraft, the local-vertical local-horizon frame, and spacecraft state is expressed with respect to the primary about which they are orbiting. The exact description of the relative dynamics is derived, as well as simplified equation sets based on both the elliptic and the circular restricted three-body problems. The accuracy of the simplified sets is analyzed by means of extensive numerical simulations on a realistic rendezvous scenario with a target on lunar orbit.

One. Introduction

The study of the spacecraft relative dynamics is one of the most trending topics in the space research field. As a matter of fact, the characterization of the relative motion is a critical step in the design and the analysis of all the space missions requiring the coordination of two or more spacecraft. Notable examples are rendezvous and docking missions and formation flying, which have drawn the interest of the space community for decades. Worth of mention are also future missions such as in-orbit servicing, debris mitigation, and assembly of large orbital structures, which are increasing the interest in the subject.

Relative motion in the two-body problem and, in particular, in near-Earth orbits has been studied extensively. The first and most remarkable models were proposed during the nineteen sixties: the Clohessy-Wiltshire equations and the Tschauner-Hempel equations. For years, these sets of equations have been the model of reference for the analysis and the design of relative guidance, navigation, and control systems, because they provide linear models for the study of relative motion in circular and elliptic orbits. However, the two sets are based on the following main assumptions: the spacecraft relative separation is significantly small compared with the distance from the primary body center of mass, and no orbital perturbations act on them. These assumptions limit the use of the two equation sets in applications such as formation flying, which generally requires to maintain formations over long mission times, while satisfying high-accuracy requirements in order to meet the mission objectives. In such cases orbital perturbation must be taken into account in order to predict the long-term motion, and the linearization error may be non-negligible if long baselines are considered. Therefore, a wide variety of models have been proposed in the literature to overcome these limitations.

The attention received by the study of relative motion in three-body scenarios is not comparable to the two-body case. Depending on the three-body system considered, when the spacecraft fly near the biggest primary, the influence of the second primary is generally modeled as an orbital perturbation (third-body perturbation). However, several missions under study are targeting celestial bodies where the third-body influence must be explicitly taken into account in the relative dynamics. Two examples are Phobos Sample Return mission and the Human Lunar Exploration Precursor Program. With reference to the former, the orbital dynamics around Phobos is particularly complex, because the small mass-ratio and length-scale of the Mars-Phobos system result in a sphere of influence of the Martian moon, which is very close to its surface. Hence, the two-body problem is an inaccurate approximation of the spacecraft's dynamics in the vicinity of Phobos. In the Human Lunar Exploration Precursor Program an habitable station, the Deep Space Gateway, will fly a near-rectilinear halo orbit. Again, two-body-based equation sets cannot be used in this context, because non-Keplerian orbits typical of three-body systems are considered, and models based on the two-body problem generally exploit the characteristic of the Keplerian orbits. Therefore, ad hoc models for relative motion description in the three-body problem must be identified.

The approach generally adopted in the literature is based on the numerical computation of the difference between the equations that regulate the motion of the two spacecraft. More specifically, the circular restricted three-body problem is used to model the single spacecraft dynamics, and then the difference is used to numerically describe the relative motion. Examples of this kind of approach applied to formation-flying and rendezvous missions can be found. This type of description has two main limitations. First the use of circular restricted three-body problem equations is inaccurate for some three-body systems, as, for instance, in the Earth-Moon and in the Mars-Phobos cases, where the system eccentricity has a non-negligible influence. Hence, the elliptic restricted three-body problem must be considered. Second, these sets are developed in a frame rotating with the primaries, generally referred to as the synodic or pulsating reference frame, and centered on one of them, or on their common center of mass, or even in a libration point. Historically, relative motion, especially in rendezvous missions, is studied in a frame local to the target or leader spacecraft, such as the local-vertical local-horizon frame. This choice eases the integration of measurements acquired by spacecraft relative positioning sensors. In addition, the use of a local frame allows to better understand and to characterize the chaser or follower dynamics as seen from the target or leader. This is particularly important in rendezvous and docking missions, in order to analyze and to assess the safety of the maneuvers performed by an incoming chaser spacecraft. Some studies try to solve these limitations. For instance, local frames are considered but only for the analysis and the visualization of the results, not for derivation of the equations of relative motion. The general restricted three-body problem setup is considered, but spacecraft position and velocity is considered with respect to the Sun-Earth L Two libration point, and the relative motion is expressed in the synodic frame.

In this paper we propose a characterization of the relative dynamics in a restricted three-body context as seen in a frame local to a target. In particular, we consider a pair of spacecraft, in the following referred to as chaser and target, flying in the vicinity of the smallest primary, in a region where the third-body effect must be explicitly considered into the relative dynamics. Spacecraft position and velocity vectors are expressed with respect to the smallest primary center of mass. Considering, for instance, the Earth-Moon system, this feature is particularly useful in the case one of the spacecraft loses the line of sight with the ground stations on Earth, because measurements are taken with respect to the Moon. In addition, target orbits in restricted three-body scenarios are generally expressed with respect to the smallest primary. The LVLH frame centered on the target is used as a local frame. As opposed to the cited references, the LVLH frame is defined with reference to the smallest primary, in analogy with the frame definition used for rendezvous in Earth orbits, because vehicles incoming from its surface are expected to approach the target. A general set of equations of relative motion in the restricted three-body problem is derived. Conversely to the aforementioned references, the derivation is performed directly in the LVLH frame, making the resulting equation set particularly appealing for rendezvous and docking operations. The only assumption made is the spacecraft having negligible masses with respect to the primaries. Thus, the equations have general validity, and are not restricted to the elliptic or circular three-body problem. Then, the ER3BP and the CR3BP are considered, in order to derive simplified equation sets. A linearization of the sets is also performed in order to provide linear models useful for preliminary relative guidance, navigation, and control system design. The accuracy of the equation sets is analyzed by means of extensive Monte Carlo simulations. The HLEPP is used as a reference mission scenario, and an Earth-Moon NRHO is considered for the target. Linear two-body-based equation sets were also considered in the analysis, and their accuracy compared against the three-body based sets. Given the chosen reference mission, and in order to ease the general readability, in the paper we will refer to the Earth-Moon system. Nevertheless, application of the proposed equation to other three-body systems is straightforward, because the simplifications considered in the paper are not based on any peculiar characteristic of the lunar orbit or of the Earth-Moon system.

The paper is organized as follows. In Section two a brief review of the ER3BP and of the CR3BP is provided, and the spacecraft equations of motion with respect to the Moon are derived. Section three discusses the derivation of equations of relative motion for the exact description of the relative dynamics of a chaser spacecraft with respect to a target in the restricted three-body problem context. Possible simplifications of the relative dynamics are discussed in Section four, where four equation sets are derived. The accuracy of the sets is analyzed in Section five. Conclusions are drawn in Section six.


## Two. Restricted Three-Body Dynamics

Consider the three-body system composed by the Earth and the Moon primary bodies and a spacecraft i, with masses M sub E, M sub M, and m sub i, respectively. Their positions with respect to an inertial frame I is denoted with R sub E, R sub M, and R sub i, respectively.

One thousand three hundred twenty-three m sub i

M sub E R sub E equals G M sub M M sub E R sub EM plus G m sub i M sub E R sub EI R sub EM R sub EI

M sub M R sub MLz equals G P m entity two plus G m sub i M sub M

where r sub E I equals R sub i minus R sub E and r sub M I equals R sub i minus R sub M denote the position of the spacecraft i with respect to the Earth and to the Moon, r sub EM equals R sub M minus R sub E is the position of the Moon with respect to the Earth, and G is the universal gravitational constant. Relative positions norms are indicated with r sub E I, m sub I, and r sub EM. The notation R sub z denotes the acceleration of the body as seen from the inertial frame.

Equations of motion of spacecraft i with respect to the Earth and to the Moon are then given by:

R sub E ILz equals R sub i minus R sub ELz equals G M sub E plus m sub i r sub e minus r sub E I minus G M sub M seven point three I m sub I plus

(one)

r sub EM

(two)

We now assume that the mass of the spacecraft i is negligible with respect to the primaries masses (i.e., m sub i is less than M sub E and m sub i is less than M sub M); that is, we consider the restricted three-body problem. Under this assumption the orbital motion of the two primaries is not affected by the spacecraft, and Equations (one) and (two) simplify to:

(three)

where H sub E equals G M sub E and U sub M equals G M sub M are the primaries' gravitational parameters.

Assume now that the primaries revolve around their common barycenter in elliptic orbits (elliptic restricted three-body problem). The motion of the two primaries can then be obtained from the solution of the classical two-body problem.

The equations of motion for the spacecraft i are generally written in a frame that rotates with the primaries. A Moon or synodic reference frame M: R sub M; I sub M, J sub M, K sub M is introduced, with origin in the Moon center of mass, and unit vectors defined as follows:

I sub M equals T sub EM, I sub M equals K sub M cross I sub M, K sub M equals A sub M L E , H sub M L E

where H sub M L E equals r sub EM cross R sub EM Lz is the specific angular momentum of the Moon with respect to the Earth, and H sub M slash E equals absolute value H sub M slash E absolute value; see Figure one. The Earth-Moon system, and consequently the frame M, rotates with respect to the inertial frame I with angular velocity omega M slash I equals omega M slash I K sub M.

The acceleration of the spacecraft i in the frame M is given by:

R sub M ILz equals R sub M I M plus two omega M slash I cross I sub M I M plus omega M slash I cross I sub M plus omega M slash I

cross omega M slash I cross I sub M

(four)

where two omega M slash I cross R sub M I M is the Coriolis acceleration and omega M slash I cross omega M slash I cross I sub M is the centripetal acceleration term.

In the Moon frame we have that r sub EM equals negative r sub EM I sub M, and the spacecraft position vectors with respect to the Moon and to the Earth are defined as follows:

I sub M I equals x M plus V I sub M plus two K sub M, r sub EI equals x sub I minus T sub EM I sub M plus V I sub M plus z sub I K sub M

Introducing Equation (three) in Equation (four), we obtain the equations of motion for the spacecraft I in the Moon reference frame:

left bracket double dot r sub m i right bracket sub script cap M equals negative two a sub m divided by i times left bracket dot r sub m i right bracket sub script cap M minus left bracket dot o sub m divided by i right bracket sub script cap M times r sub m i minus o sub m divided by i times left parenthesis o sub m divided by i times r sub m i right parenthesis minus mu sub m fraction r sub m i divided by r sub m i to the power of three minus mu sub e left parenthesis fraction r sub e i divided by r sub e i to the power of three minus fraction r sub e m divided by r sub e m to the power of three right parenthesis equation five or in terms of components in the frame cap M colon left parenthesis double dot x sub i equals two o sub m divided by i dot y sub i plus dot o sub m divided by i y sub i plus o sub m divided by i to the power of two x sub i minus mu sub m fraction x sub i divided by r sub m i to the power of three minus mu sub e left parenthesis fraction x sub i minus r sub e m divided by r sub e i to the power of three plus fraction one divided by r sub e m squared right parenthesis right parenthesis double dot y sub i equals negative two o sub m divided by i dot x sub i minus dot o sub m divided by i x sub i plus o sub m divided by i to the power of two y sub i minus mu sub m fraction y sub i divided by r sub m i to the power of three minus mu sub e fraction y sub i divided by r sub e i to the power of three equation six double dot z sub i equals negative mu sub m fraction z sub i divided by r sub m i to the power of three minus mu sub e fraction z sub i divided by r sub e i to the power of three where the distances of the spacecraft from the Moon and the Earth are given by:

r sub e i equals square root left parenthesis x sub i minus r sub e m right parenthesis squared plus y sub i squared plus z sub i squared comma r sub m i equals square root x sub i squared plus y sub i squared plus z sub i squared comma Equation six can be normalized expressing the distances in units of the Moon orbit semi-major axis c comma time in units of the inverse of the Earth-Moon mean angular motion n left parenthesis i.e comma introducing the new time variable tau equals n t comma and the masses such that M sub e plus M sub m equals one period The generic distance x and the associated derivatives are related to the nondimensional variables tilde chi as follows:

x equals a tilde x comma dot x equals a fraction d tilde x divided by d t equals a fraction d tilde x divided by d tau fraction d tau divided by d t equals a n tilde x prime comma double dot x equals a n fraction d tilde x prime divided by d t equals a n squared tilde x prime prime comma where the prime denotes derivation with respect to the normalized time variable z period Note that the angular velocity is now expressed in units of n semicolon thus:

o equals n tilde o comma dot o equals fraction d a divided by d t equals fraction d a divided by d tau fraction d x divided by d t equals n squared fraction d tilde o divided by d tau equals n squared tilde o prime The mass ratio parameter mu is defined as:

mu equals fraction mu sub m divided by mu sub e plus mu sub m equals left parenthesis one plus fraction M sub e divided by M sub m right parenthesis to the power of negative one Since M sub e plus M sub m equals one comma Moon and Earth gravitational parameters are then mu sub m equals mu and mu sub e equals one minus mu comma respectively.

Equation six can now be written in nondimensional form as follows:

seven nonsequiter nonsequiter nonsequiter and the normalized distances of the spacecraft from the Earth and the Moon are given by

R underscore E I tilde equals the square root of open parenthesis X underscore I tilde minus R underscore EM tilde close parenthesis squared plus Y underscore I tilde squared plus Z underscore I tilde squared, comma space R underscore MI tilde equals the square root of X underscore I tilde squared plus Y underscore I tilde squared plus Z underscore I tilde squared. Equation seven further simplifies if we assume the Moon and the Earth rotating around the Earth-Moon barycenter in circular orbits; that is, we consider the CR three BP. In this case R underscore EM tilde equals one, A underscore MI tilde equals one, and A underscore MI tilde prime equals zero, and equations seven simplify as follows:

Open parenthesis X underscore I tilde double prime equals two Y underscore I tilde prime minus X underscore I tilde minus mu fraction X underscore I tilde over R underscore MI tilde cubed minus open parenthesis one minus mu close parenthesis open parenthesis fraction X underscore I tilde minus one over R underscore EI tilde cubed plus one close parenthesis close parenthesis.

Z underscore I tilde double prime equals negative mu fraction Z underscore I tilde over R underscore MI tilde cubed minus open parenthesis one minus mu close parenthesis fraction Z underscore I tilde over R underscore EI tilde cubed.

R underscore EI tilde equals the square root of open parenthesis X underscore I tilde minus one close parenthesis squared plus Y underscore I tilde squared plus Z underscore I tilde squared, comma space R underscore MI tilde equals the square root of X underscore I tilde squared plus Y underscore I tilde squared plus Z underscore I tilde squared. For the sake of simplicity, in the following sections the overlying tilde will be dropped, and derivation with respect to the normalized time will be denoted with the Newton notation. Thus, all variables and parameters must be considered normalized.


## Three. Relative Motion Equations in the Restricted Three-Body Problem

A. Exact Relative Dynamics

Consider a target and a chaser spacecraft orbiting around the Moon and subject to both Earth and Moon gravitational influences. Their equations of motions with respect to the Moon are given by Eq. three:

Open bracket double dot R close bracket underscore I equals negative mu fraction R over R cubed minus open parenthesis one minus mu close parenthesis open parenthesis fraction R plus R underscore EM over norm R plus R underscore EM cubed minus fraction R underscore EM over R underscore EM cubed close parenthesis close parenthesis.

Open bracket double dot R underscore C close bracket underscore I equals negative mu fraction R underscore C over R underscore C cubed minus open parenthesis one minus mu close parenthesis open parenthesis fraction R underscore C plus R underscore EM over norm R underscore C plus R underscore EM cubed minus fraction R underscore EM over R underscore EM cubed close parenthesis close parenthesis.

where R and R underscore C denote target and chaser position with respect to the Moon.

The aim of this section is to describe the motion of the chaser relative to the target in the LVLH frame L colon open brace R semicolon T hat, J hat, K hat close brace centered on the target center of mass. The unit vectors of L are defined as follows:

where H equals RX i M is the target-specific angular momentum with respect to the Moon, and H equals H. The unit vectors î, j, and k in the rendezvous literature are generally referred to as V-bar, H-bar, and R-bar, respectively. Note that the LVLH frame is defined with respect to the Moon, because the target is supposed to fly on lunar orbits, and vehicles incoming from the Moon surface or lower and higher orbits are expected to approach the target (as, for instance, is envisaged in the HLEPP).

With reference to Figure two, the chaser position with respect to the Moon is given by:

Eleven re equals r plus p where p is the relative position of the chaser with respect to the target. The time derivative of Equation eleven in the inertial frame is:

Twelve where wi is the angular velocity of L (i.e., of the target) with respect to I. Further derivation of Equation twelve in I yields:

Thirteen

Noting that wiL equals wiL, and introducing Equations nine and ten in Equation thirteen, we obtain the nonlinear equations of relative motion in the LVLH frame:

negative plus one minus mu norm r plus re m r plus re m three norm r plus p plus re m r plus p plus re m mu norm r plus p eleven three r plus p r

Fourteen

The angular velocity of the LVLH frame with respect to the inertial frame can be computed by composition of angular velocity vectors:

Fifteen wi equals wl m plus wm i where wi m and wm i are the angular velocities of L with respect to M, and of M with respect to I, respectively.

The LVLH angular acceleration with respect to I is given by: wilL equals wimL plus wm iL equals wi m plus wm iM minus wl m cross wm i

Sixteen

Equation fourteen, along with Equations fifteen and sixteen, composes a set of nonlinear equations with time-varying parameters:

One r, wl m, and wl m which depend on the target motion around the Moon

Two re m, wm i, and w m i, characteristics of the Earth-Moon system orbital motion

Equation fourteen exactly describes the relative motion in the LVLH frame in the restricted three-body problem, providing that no orbital perturbations act on the spacecraft (e.g., solar radiation pressure). The consideration of the restricted three-body problem provides the option to model the primary bodies in either an elliptic or circular orbit around each other, depending on the three-body system considered.

In the following, the expressions of wl m and wl m are derived, in order to complete the nonlinear description of the relative dynamics in the LVLH frame.


## B. LVLH Angular Velocity and Acceleration

We now look for an analytical expression of the LVLH frame angular velocity and acceleration vectors with respect to the Moon frame, which exploits only kinematics relationships. To this end, the same considerations adopted in are here used to find an expression for wi m. The angular acceleration wi m is then obtained by differentiation.

Consider the time derivatives of the LVLH frame unit vectors as seen in M:

M ; LAM equals wl m cross one, kM equals wi m cross E

Left vector multiplication of the previous expressions by the relative unit vector gives:

IM equals x wl m cross equals wl m minus wl m which can be summed up obtaining:

Seventeen

The time derivative of the unit vector k is:

Eighteen

Noting that r equals negative rk and e equals negative rk, we can write:

r equals negative r dot k equals negative r dot k plus wl m cross r dot k equals negative r dot plus wl m dot r cross equals negative r M dot k Nineteen

Substitution of Equation nineteen into Equation eighteen gives:

AM equals negative M plus two M equals negative M D

Twenty

Note that eM dot j equals zero since the target velocity as seen in M is perpendicular to H, by definition of the specific angular momentum. For the unit vector j we have the following time derivative:

LIM equals negative L H M minus H H

Twenty-one

According to the definition of j, we have that H equals negative H j. Hence, Equation twenty-one simplifies as follows:

Twenty-two

<LATEX>a _ { l / i } = o _ { l / m } + \widehat { k } _ { m } , \quad \left[ \dot { a } _ { l / i } \right] _ { \mathcal{L} } = \left[ \dot { o } _ { l / m } \right] _ { \mathcal{L} } - o _ { l / m } \times \widehat { k } _ { m }</LATEX> Downloaded by UNIVERSITY OF TOKYO Hongo on September 5, 2023 | http://arc.aiaa.org | DOI: 10.2514/1.A34390

Noting that <LATEX>\left[ \dot { h } \right] _ { \mathcal{L} } = - \dot { h } \widehat { J } ,</LATEX> we can write <LATEX>\dot { h }</LATEX> as:

<LATEX>\dot { r } = \frac { 1 } { r } r \cdot \left[ \ddot { r } \right] _ { \mathcal{M} }</LATEX> <LATEX>T h e \quad a n g u l a r \quad a c c e l e r a t i o n \quad a l o n g \quad k \quad i s :</LATEX> <LATEX>\dot { o } _ { l / m } ^ { z } = - \left( \frac { \dot { r } } { h ^ { 2 } } - 2 \frac { r \dot { h } } { h ^ { 3 } } \right) h \cdot \left[ \ddot { r } \right] _ { \mathcal{M} } - \frac { r } { h ^ { 2 } } \left( \left[ \dot { h } \right] _ { \mathcal{M} } \cdot \left[ \ddot { r } \right] _ { \mathcal{M} } + h \cdot \left[ \ddot { r } \right] _ { \mathcal{M} } \right)</LATEX> <LATEX>= \left( \frac { \dot { r } } { r } - 2 \frac { \dot { h } } { h } \right) o _ { l / m } ^ { z } - \frac { r } { h ^ { 2 } } h \cdot \left[ \ddot { r } \right] _ { \mathcal{M} }</LATEX> where

H dot equals negative the left H dot right sub script M dot J hat equals negative the left H dot right sub script M dot J hat plus O sub L over M times H right dot J hat equals negative the left H dot right sub script M dot J hat.

since W sub L over M times H is perpendicular to H and, consequently, to J hat. Substitution of equation twenty-three into equation twenty-two yields the time derivative of J:

The left H dot right sub script M dot double R equals R times double R right sub script M dot double R equals zero. Given the target acceleration, equation twenty-nine, the jerk double R right sub script M can be computed by direct derivation:

Double R right sub script M equals negative two A sub M over I times double R right sub script M minus three A dot sub M over I right sub script M times double R right sub script M minus O double dot sub M over I right sub script M times R minus O dot sub M over I right sub script M times O sub M over I times R minus W sub M over I times O dot sub M over I right sub script M times R minus O sub M over I times W sub M over I times R dot right sub script M minus Mu partial over partial R left R over R cubed right R dot right sub script M minus one minus Mu times partial over partial R left R plus R sub E M over norm R plus R sub E M cubed right R dot right sub script M plus R dot sub E M right sub script M minus partial over partial R sub E M left R sub E M over R sub E M cubed right R dot sub E M right sub script M.

Double J hat right sub script M equals negative one over H left H dot right sub script M dot I hat times I hat plus left H dot right sub script M dot K hat times K hat equals negative one over H left R times double R right sub script M dot I hat times I hat equals negative one over H left double R right sub script M times I hat times R right dot I hat equals negative R over H left double R right sub script M dot J hat times I hat.

In the previous derivation, the following result was used:

where

Left H dot right sub script M dot K hat equals R times double R right sub script M dot K hat equals zero justified by the fact that R times double R right sub script M is perpendicular to R, that is, to K hat. The time derivative of I hat is given by:

\left[ \dot \{ r \} \_ \{ e m \} \right] \_ \{ \mathcal \{M\} \} equals \left[ \dot \{ r \} \_ \{ e m \} \right] \_ \{ L \} minus o \_ \{ m slash i \} times r \_ \{ e m \} and

\frac \{ \partial \} \{ \partial q \} \left[ \frac \{ q \} \{ q superscript three \} \right] equals \frac \{ one \} \{ q superscript three \} \left( I minus three \frac \{ q q superscript T \} \{ q squared \} \right) with I denoting the identity matrix.

Concluding, the LVLH angular velocity with respect to the Moon is given by:

\left[ \dot \{ \left[ \right. \} \right] \_ \{ \mathcal \{M\} \} equals \left[ \widehat \{ j \} \right] \_ \{ \mathcal \{M\} \} times \widehat \{ k \} plus \widehat \{ j \} times \left[ \widehat \{ k \} \right] \_ \{ \mathcal \{M\} \} equals \frac \{ r \} \{ h \} \left( \left[ \widehat \{ r \} \right] \_ \{ \mathcal \{M\} \} cdot \widehat \{ j \} \right) \widehat \{ j \} plus \frac \{ one \} \{ r \} \left( \left[ \widehat \{ r \} \right] \_ \{ \mathcal \{M\} \} cdot \widehat \{ \imath \} \right) \widehat \{ k \} Substitution \quad of \quad Equations \left( twenty \right) , \left( twenty four \right) , and \left( twenty five \right) into \quad Equation. \left( seventeen \right) yields: a \_ \{ l / m \} equals o \_ \{ l / m \} superscript y \widehat \{ j \} plus o \_ \{ l / m \} superscript z \widehat \{ k \} equals \left( minus \frac \{ one \} \{ r \} \left[ \dot \{ r \} \right] \_ \{ \mathcal \{M\} \} cdot \widehat \{ l \} \right) \widehat \{ j \} plus \left( \frac \{ r \} \{ h \} \left[ \ddot \{ r \} \right] \_ \{ \mathcal \{M\} \} cdot \widehat \{ j \} \right) \widehat \{ k \} Note that in Equation. (twenty-six) the component of the angular velocity along the V-bar direction is zero due to the definition of the LVLH frame.

Solution of the dot products in Equation. (twenty-six) leads to simplified expressions for o \_ \{ l / m \} superscript \{ \mathcal \{Y\} \} and w \_ \{ l / m \} superscript z. For the H-bar component we have:

a \_ \{ l / m \} superscript y equals minus \frac \{ one \} \{ r \} \left[ \dot \{ r \} \right] \_ \{ \mathcal \{M\} \} cdot \widehat \{ r \} equals minus \frac \{ one \} \{ h r squared \} \left[ \dot \{ r \} \right] \_ \{ \mathcal \{M\} \} cdot \left( h times r \right) equals minus \frac \{ one \} \{ h r squared \} h cdot \left( r times \left[ \dot \{ r \} \right] \_ \{ \mathcal \{M\} \} \right) equals minus \frac \{ h \} \{ r squared \} twenty-seven and its angular acceleration is:

The R-bar component of w \_ \{ l / m \} simplifies as follows:

w \_ \{ l / m \} superscript z equals \frac \{ r \} \{ h \} \left[ \ddot \{ r \} \right] \_ \{ \mathcal \{M\} \} cdot \widehat \{ j \} equals minus \frac \{ r \} \{ h squared \} h cdot \left[ \ddot \{ r \} \right] \_ \{ \mathcal \{M\} \} twenty-eight where the target acceleration is given by Equation. (five):

\left{ \ddot \{ \mathrm \{ Mer \} \} \left( \ddot \{ \left[ r \right] \} \_ \{ \mathcal \{M\} \} text { is given by Equation } . \left( twenty nine \right) , \mathrm \{ and \} \left[ \ddot \{ r \} \right] \_ \{ \mathcal \{M\} \} text { by Equation } . \left( thirty \right) \right. \right. IV. Simplification of the Equations of Relative Motion

Because of the nonlinearity of the gravitational acceleration and the presence of several time-varying parameters, the equations of relative motions derived in Section. III, namely, Equation. fourteen, along with angular velocity and acceleration vectors given by Equations. thirty-one and thirty-two, may be difficult to use for the development of guidance and navi- gation systems. Two possible simplifications are here discussed, aimed at linearizing the equation set and at reducing the number of time-varying parameters.

\left[ \ddot \{ r \} \right] \_ \{ \mathcal \{M\} \} equals minus two o \_ \{ m slash i \} times \left[ \dot \{ r \} \right] \_ \{ \mathcal \{M\} \} minus \left[ \dot \{ o \} \_ \{ m slash i \} \right] \_ \{ \mathcal \{M\} \} times r minus o \_ \{ m slash i \} times \left( o \_ \{ m slash i \} times r \right) minus mu \frac \{ r \} \{ r cubed \} minus \left( one minus mu \right) \left( \frac \{ r plus r \_ \{ e m \} \} \{ \| r plus r \_ \{ e m \} \| cubed \} minus \frac \{ r \_ \{ e m \} \} \{ r \_ \{ e m \} cubed \} \right) twenty-nine frame are obtained \quad by \quad direct \quad derivation \quad of \quad Equations. \left( twenty seven \right) and \left( twenty eight \right) . The angular acceleration along the H-bar is given by:


## A. CR three B P Assumption

Under the assumption of primaries revolving in circular orbits, the number of time-varying parameters in Equation. fourteen reduces. As a matter of fact, in the CR three B P setup we have the following simplifications:

A dot sub l slash m superscript y equals negative the derivative of H over R squared plus two times the derivative of R H over R cubed equals negative one over R times the derivative of H over R plus two times the derivative of R O sub l slash m superscript y, where the derivative of the norm of R is computed as follows:

R sub EM equals negative Iota hat sub M, the derivative of R sub EM equals zero, A sub M slash I equals K hat sub M, the derivative of O sub M slash I equals zero, the second derivative of O sub M slash I equals zero. The angular velocity and acceleration of the LVLH frame with respect to the inertial frame simplify as follows:

Open curly brace, A sub L slash M superscript Y equals negative H over R squared, A sub L slash M superscript Z equals negative R over H squared times H dot R, close curly brace.

Integral of W dot sub L slash M superscript Y equals negative one over R times the derivative of H over R plus two times the derivative of R W sub L slash M superscript Y. Open curly brace, O R L sub L slash M equals negative negative over R times R over R plus two R O L sub L slash M prime, the derivative of O sub L slash M superscript Z equals the derivative of R over R minus two times the derivative of H over H O sub L slash M superscript Z minus R over H squared times H dot the second derivative of R.

In addition, the computation of the target acceleration and jerk in equations thirty-one B and thirty-two B becomes:

R sub mathcal M equals negative two times A sub M slash I cross R sub mathcal M minus A sub M slash I cross A sub M slash I cross R minus Mu times R over R cubed minus one minus Mu times R plus R sub EM over the norm of R plus R sub EM cubed minus R sub EM. The second derivative of R sub mathcal M equals negative two O sub M slash I cross the second derivative of R sub mathcal M minus O sub M slash I cross O sub M slash I cross the derivative of R sub mathcal M minus Mu times the partial derivative with respect to R times the derivative of R over R cubed minus one minus Mu times the partial derivative with respect to R times R plus R sub EM over the norm of R plus R sub EM cubed times R sub mathcal M.


## B. Linearization of the Gravitational Acceleration

Consider the gravitational acceleration on the chaser, due to the two primaries:

G sub M of R sub C equals negative Mu R sub C over R sub C cubed, G sub E of R sub C plus R sub EM equals negative one minus Mu R sub C plus R sub EM over the norm of R sub C plus R sub EM cubed. These terms can be linearized by means of a Taylor expansion to the first order around the target position. For the lunar gravitational acceleration term we have:

G sub M of R sub C approximately equals G sub M of R plus the partial derivative of G sub M of Q with respect to Q evaluated at Q equals R times R sub C minus R equals negative Mu R over R cubed minus Mu over R cubed times the identity matrix minus three times R R transpose over R squared, rho, whereas for the Earth gravitational acceleration term:

G sub E of R sub C plus R sub E M approximately equals G sub E of R plus R sub E M plus partial G sub E of Q with respect to Q evaluated at Q equals R plus R sub E M times R sub C minus R equals negative one minus mu times R plus R sub E M over norm of R plus R sub E M cubed minus one minus mu over norm of R plus R sub E M cubed times I minus three times R plus R sub E M R plus R sub E M transpose over norm of R plus R sub E M squared rho. Hence, the right-hand side of Equation fourteen can be approximated as follows:

Mu times R over R cubed minus R sub C over R sub C cubed plus one minus mu times R plus R sub E M over norm of R plus R sub E M cubed minus R sub C plus R sub E M over norm of R sub C plus R sub E M cubed approximately equals negative mu over R cubed times I minus three times R R transpose over R squared rho minus one minus mu over norm of R plus R sub E M cubed times I minus three times R plus R sub E M R plus R sub E M transpose over norm of R plus R sub E M squared rho obtaining a linear expression of the gravitation accelerations, with respect to the relative position vector.


## C. Relative Motion Equation Sets

The possible simplifications discussed in the previous section can be used to derive four equation sets, which describe the relative dynamics with different levels of accuracy.

In the following, the skew symmetric matrices associated with angular velocity and acceleration vectors o sub l slash i and dot a sub l slash i subscript script L, that is:

Omega sub l slash i equals matrix zero negative o sub l slash i superscript z o sub l slash i superscript y o sub l slash i superscript z zero negative o sub l slash i superscript x negative o sub l slash i superscript y o sub l slash i superscript x zero matrix zero negative dot o sub l slash i superscript z dot o sub l slash i superscript y dot o sub l slash i superscript z zero negative dot o sub l slash i superscript x negative dot o sub l slash i superscript y dot o sub l slash i superscript x zero matrix where

O sub l slash i equals o sub l slash i superscript x hat iota plus o sub l slash i superscript y hat j plus o sub l slash i superscript z hat k, dot o sub l slash i subscript script L equals dot o sub l slash i superscript x hat iota plus dot o sub l slash i superscript y hat j plus dot o sub l slash i superscript z hat k are introduced to express the equations of motion in a more compact form.


## One. ER three BP-Based Equations: ENERM and ELERM

If the ER three BP problem is considered, then the Moon motion is governed by the classical two-body problem equations, with the Earth as primary body. The quantities R sub E M, A sub M slash i, and evaluated at script M can then be obtained accordingly.

With the name of elliptic nonlinear equations of relative motion (ENERM) we will refer to the following equation set:

left double bracket rho double dot right double bracket subscript script cap L end script equals negative two Omega subscript L over I left double bracket rho dot right double bracket subscript script cap L end script minus left parenthesis left double bracket Omega dot subscript L over I right double bracket subscript script cap L end script plus Omega subscript L over I squared right parenthesis rho plus mu left parenthesis r over r cubed minus r plus rho over norm r plus rho cubed right parenthesis plus left parenthesis one minus mu right parenthesis left parenthesis r plus r subscript E M over norm r plus r subscript E M cubed minus r plus rho plus r subscript E M over norm r plus rho plus r subscript E M cubed right parenthesis characterized by the following time-varying parameters that depend on target and on Moon orbital motion:

one a subscript L over I equals a subscript L over M plus o subscript M over I two left double bracket a dot subscript L over I right double bracket subscript script cap L end script equals left double bracket a dot subscript L over M right double bracket subscript script cap L end script plus left double bracket a dot subscript M over I right double bracket subscript script cap M end script minus a subscript L over M times a subscript M over I semicolon left double bracket a dot subscript L over M right double bracket subscript script cap L end script given by Equation thirty two comma with left double bracket r dot right double bracket subscript script cap M end script as in Equation thirty If the chaser acceleration is controllable by means of the control vector U, then Equation thirty-five can be written as a nonlinear system affine in the control:

x dot equals f left parenthesis t comma x right parenthesis plus B U comma x equals left bracket begin array rho rho dot left double bracket cap L end bracket end array right bracket comma B equals left bracket begin array zero subscript three times three cap I subscript three end array right bracket comma where cap I subscript N end subscript is the N times N identity matrix comma and zero subscript N times M is the N times M zero matrix.

The gravitational acceleration can be linearized as discussed in Section Four.B, obtaining the elliptic linear equations of relative motion abbreviated E L E R M:

left double bracket rho double dot right double bracket subscript script cap L end script equals negative two Omega subscript L over I left double bracket rho dot right double bracket subscript script cap L end script minus left parenthesis left double bracket Omega dot subscript L over I right double bracket subscript script cap L end script plus Omega subscript L over I squared plus mu over r cubed left parenthesis cap I minus three r r superscript T over r squared right parenthesis right parenthesis plus one minus mu over norm r plus r subscript E M cubed left parenthesis cap I minus three left parenthesis r plus r subscript E M right parenthesis left parenthesis r plus r subscript E M right parenthesis superscript T over norm r plus r subscript E M squared right parenthesis right parenthesis rho with angular velocities and accelerations computed as for the E N E R M. Assuming the chaser controllable in acceleration, Equation thirty-six can be written in state-space form as follows:

x dot equals A left parenthesis t right parenthesis x plus B U with

A left parenthesis t right parenthesis equals left bracket begin array zero subscript three times three cap I subscript three A subscript rho dot rho left parenthesis t right parenthesis negative two Omega subscript L over I left parenthesis t right parenthesis end array right bracket A subscript rho dot rho equals negative left double bracket Omega dot subscript L over I right double bracket subscript script cap L end script minus Omega subscript L over I squared minus mu over r cubed left parenthesis cap I minus three r r superscript T over r squared right parenthesis minus one minus mu over norm r plus r subscript E M cubed left parenthesis cap I minus three left parenthesis r plus r subscript E M right parenthesis left parenthesis r plus r subscript E M right parenthesis superscript T over norm r plus r subscript E M squared right parenthesis right parenthesis where in the last equation dependence on time was omitted for notation compactness.


## Two. CR three BP-Based Equations: CNERM and CLERM

If the CR three BP is considered, then the computation of the angular velocities simplifies as follows:

One) A sub l over i equals A sub l over m plus A sub m over i (as for the elliptic case);

Two) dot A sub l over i bracket L equals dot A sub l over m bracket L minus A sub l over m times dot K sub m. Three) W sub l over m is given by Equation thirty-one, but with double dot R bracket M as in Equation thirty-three according to the CR three BP;

Four) Left bracket at left bracket M right bracket E quad I S quad given quad B Y right. Equation thirty-two, with the CR three BP simplified jerk

Double dot R bracket M. The set in Equation thirty-five with the CR three BP simplifications will be referred to as circular nonlinear equations of relative motion (CNERM),

whereas the set in Equation thirty-six under the same simplifications as circular linear equations of relative motion (CLERM).


## V. Equation Sets Comparison

A. Reference Mission Scenario

To assess and compare the accuracy of the derived equation sets, we considered a reference target orbit inspired by the HLEPP study. The study considers a human-assisted robotic mission on the lunar surface, where rovers are tele-operated by astronauts on board a station in lunar orbit, the DSG. Access to the station by vehicles incoming from both the Earth and the lunar surface is one of the most critical aspects of the mission. The study of the relative dynamics for this scenario, and the design of maneuvers for rendezvous and docking with the DSG will provide a step forward in the overall mission design.

The candidate family of orbits for the DSG is the Earth-Moon L one NRHO. An example of NRHO belonging to the south subfamily is shown in Figure three. The orbit was provided by ESA.

In Figure three the region of the orbit suitable for rendezvous, as suggested, is highlighted. To identify the rendezvous region, the mean anomaly of the NRHO must be introduced:

M of one equals two Mwhere, in analogy to the Keplerian orbits, t is the time from the periselene passage, and T is the orbit period. For the orbit in Figure three, the average period is T equals six point nine eight six seven days. The periselene is defined as the point where the orbit crosses the x-z plane of the Moon frame closest to the Moon, whereas the aposelene is defined as the point crossing the same plane farthest from the Moon. The analysis of the stable and central manifolds of the orbit as a function of the mean anomaly was used to identify the recommended rendezvous region M in the range of eighty to two hundred eighty degrees. In this region the existence of the central manifolds enables the design of hovering or station keeping trajectories that can be exploited in the waiting for the clearance for the final approach.


## B. Simulations Setup

The equation sets defined in Section four point C were tested and compared, in order to assess their accuracy for different initial spacecraft separations.

Spacecraft motion was simulated according to the ER three BP. The reference scenario discussed in Section five point A was used as a benchmark, and the presented NRHO orbit was chosen for selecting target initial states with respect to the Moon.

The three simplified equation sets previously defined, namely, the ELERM, the CNERM, and the CLERM, were implemented in MATLAB Simulink twenty fourteen B. The ENERM set was not included in the comparison because for the ER three BP it corresponds to the exact description of the relative motion. Two relative motion equation sets based on the two-body problem were also considered, in order to understand their applicability to restricted three-body scenarios:

One) the linear equations of relative motion (LERM):

x equals p of one minus two x minus twenty-one of two minus two

Eight y equals negative j y p

Two equals two left bracket x minus x right bracket plus j squared one plus two e) Hill's equations e) Hill's equations where p equals x i plus y j plus z k, p is the target orbit semilatus rectum, and f denotes the true anomaly rate. Both p and f were computed from the target initial position and velocity vectors as follows:

p equals h of p, j equals h of t o times h of t o squared where h of t o equals norm r of t o cross r of t o

Two) the Hill's or Clohessy-Wiltshire equations:

x equals two n z j equals negative n squared y z equals negative two n x plus three n squared z where n is the orbit mean anomaly, given by n equals two x over T, with T period of the NRHO orbit.

Two different Monte Carlo simulations were performed to assess the accuracy of the equation sets. The distance test analyzes the accuracy as the initial relative separation increases. In particular, for each target initial condition, a given number of relative distances were chosen. For each one, a random initial relative position vector with norm equal to the chosen distance was computed, and the equation sets were propagated. Relative velocity was kept fixed to zero for all the simulations. Conversely, in the speed test a set of initial relative speed was chosen, and associated relative velocity vectors were generated randomly. In both tests, target initial conditions were chosen in terms of mean anomaly M along the NRHO orbit. The equation sets were tested over an interval of twelve hours. MATLAB solver settings are listed in Table one. Monte Carlo test parameters are given in Table two.

e) Hill's equations

The following performance indexes were defined to compare the equation sets:

One) the maximum distance and speed errors over the simulation interval:

e v equals max norm p of t minus hat p of t e p equals max norm p of t minus p of t, t in the range from t o to t f t in the range from t o to t f where the hat denotes the relative position and velocities computed by the tested equation set, whereas the quantities without hat denote the true values.

Two) the aggregative performance index:

number

V equals max norm p of t minus hat p of t, t in the range from t o to t f xi n p where n is the NRHO mean motion. This index, used allows to characterize the overall accuracy of the set. The index V has dimension of length by adimensionalizing time in the relative velocity using the orbit mean motion.


## C. Distance Test Results

The results of the distance test are shown in Figures four through six. The ELERM is the most accurate set, with a position error in the order of the meter for almost all the simulated conditions. The CR3BP assumption introduces a significant error, as can be seen comparing the position error of ELERM and CNERM in Figure four. In particular, the position error is in the order of the meter only for initial relative distances lower than few kilometers. The linearization of the CNERM does not introduce a great difference in the results, except for target initial conditions near the periselene. This difference can be observed comparing the values of the error index near the mean anomalies M equals zero and M equals three hundred sixty degrees in Figures six B and six C.

The two-body-based equations perform worse than the other sets for all the analyzed initial conditions. However, LERM equations show an acceptable error in the order of the meter when the target starts its motion far from the periselene, for initial mean anomalies M between ten degrees and two hundred eighty degrees.

All the equation sets showed good accuracy in terms of relative velocities, with values of speed errors always below the meter per second, except for large separations in the case of two-body-based equation set (in particular for initial distances above ten kilometers, with target starting its motion near the periselene).


## D. Speed Test Results

The aim of this test is the analysis of the equations accuracy when the initial relative velocity is not zero, as in the distance test. The results are presented in Figures seven through nine.

The ELERM confirmed their higher accuracy compared with the other sets. The CR3BP assumption produces a significant growth in both the position and velocity errors, though in the latter case remain acceptable (below the meter for almost all the tested conditions). Again, there are no significant differences between the CNERM and the CLERM sets.

The two-body-based equation sets showed the worst accuracy, in both position and velocity computation. In particular, for all the test conditions, the position error is above one hundred meters for the LERM, and above one kilometer for the Hill's equations.

The analysis of the error index v surfaces in Figure nine confirms the overall higher accuracy of the ELERM, with respect to the other equation sets.


## E. General Remarks

One. Applicability of CR3BP at the Aposelene

From the analysis of the position accuracy of the equation sets based on the CR3BP assumption, Figures six B, six C, seven B, and seven C, a region can be found at the aposelene, where the error is small enough to provide a reliable estimation of the chaser relative state. This is highlighted in Figure ten, where the average position error for the distance and speed tests is evaluated in the rendezvous zone. In the distance test the position error at the aposelene is less than a centimeter for distances below one hundred meters; see Figures ten A and ten B. In the speed test, at the aposelene the position error is of the order of the meter for relative speeds below zero point one meters per second. Therefore, CNERM and CLERM equation sets are suitable for relative guidance system design for terminal rendezvous at the aposelene. In particular, CLERM equations are appealing for the design of classical robust controllers due to their linear nature and the reduced number of time-varying parameters, which are the target position with respect to the Moon and the LVLH angular velocity and acceleration vectors. These parameters can be modeled as bounded uncertainties, defined by a prior analysis of their values around the aposelene. Because of the reduced target velocity at the aposelene, the parameters' rate of change will be limited and robust control techniques can be successfully applied.


## Two. Linearization Error

The effects of the linearization are evident near the periselene. Considering, for instance, the distance test, the error index v at the periselene is larger for the linearized sets ELERM and CLERM than for the nonlinear set CNERM; see Figures six A through six C. In Figure eleven the values of the error index V for values of the mean anomaly near the first and the second periselene are shown. For distances above seventy to eighty meters the error is clearly larger for the linearized sets, compared with the C-N-E-R-M equations. For the rest of the target orbit the linearization error is negligible. The cause lies in the high velocity of the target at the periselene that results in a quick separation of the spacecraft, which exceeds the linearization domain of validity.


## Six. Conclusions

The relative dynamics in the local-vertical local-horizon frame for restricted three-body scenarios were characterized and described by means of a set of nonlinear time-varying equations. Possible simplifications were discussed and applied, obtaining simplified sets with a reduced number of time-varying parameters, and/or linear with respect to the relative motion state. The accuracy of the equation sets was analyzed by means of extensive Monte Carlo simulations, and compared against the two linear equation sets generally employed in Keplerian orbits, namely, linear equations of relative motion and Hill's equations. The tests confirmed that two-body-based equation sets are not suitable for restricted three-body scenarios, especially when the relative velocity becomes significant. The assumption of circular motion for the primaries introduces considerable error, at least for the Earth-Moon system and the orbit chosen as reference target trajectory. However, the error is reduced near the aposelene, making the circular nonlinear equations of relative motion and circular linear equations of relative motion sets suitable for relative guidance and navigation system design in this regions, provided that robust control techniques are adopted.