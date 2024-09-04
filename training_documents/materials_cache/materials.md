## Mathematical Crystal Chemistry

Efficient heuristics have predicted many functional materials such as high-temperature superconducting hydrides, while inorganic structural chemistry explains why and how the crystal structures are stabilized. Here we develop the paired mathematical programming formalism for searching and systematizing the structural prototypes of crystals. The first is the minimization of the volume of the unit cell under the constraints of only the minimum and maximum distances between pairs of atoms. We show the capabilities of linear relaxations of inequality constraints to optimize structures by the steepest-descent method, which is computationally very efficient. The second is the discrete optimization to assign five kinds of geometrical constraints including chemical bonds for pairs of atoms. Under the constraints, the two object functions, formulated as mathematical programming, are alternately optimized to realize the given coordination numbers of atoms. This approach successfully generates a wide variety of crystal structures of oxides such as spinel, pyrochlore-o, and K2 NiF4 structures.

Discovering advanced materials enables technological innovation in many areas such as batteries, photovoltaics, and catalysis. Since electronic structure depends on the spatial arrangements of atoms, predictions of unknown crystal structures have a major impact on the discovery of better materials. However, computational structure searching is still difficult despite the progress of computational power, since structure prediction is a large-scale nonconvex minimization problem of the total energy, which has a large number of local minima, concerning the atomic arrangement and crystal lattice.

Finding the global minimum essentially involves visiting every local minimum, but some heuristic approaches with more or less intelligent ways such as evolutionary algorithms and particle swarm-intelligence approach have predicted novel materials including binary hydrides that have been experimentally synthesized as high-temperature superconductors under high pressure. The drawbacks of these methods are that there are no guarantees that the most stable structure are found, and similarly, they can miss synthesizable unique structures. Furthermore, they cannot explain why and how the predicted structures are stabilized. This is also true of the deep learning approach and the random structure searching methods, while the latter may lead to peculiar structures without a priori knowledge.

The integer programming approach has been developed to deterministically find the lowest energy structure with guarantees. The global optimum of integer programming can be found deterministically by brute force with branch-and-cut algorithms that are capable of rapidly eliminating large parts of the optimization tion domain from consideration. To apply this universal method, all the atoms are placed at discrete positions within a fixed cubic unit cell, and the total energy is represented by the sum of two-body classical interaction potentials. This approach has successfully found complex crystals such as garnet structure, but the fixed unit cells and approximated total energies may limit its applicability. Instead of using approximated total energies, geometrical approaches may be effective to search crystal structures, for example, Yokoyama et al. have developed the dual periodic graph approach to generate structures composed of space-filling polyhedra.

Important structural principles for ionic crystals have been summarized by Pauling in the five rules. George et al. have shown the limited predictive power of the Pauling rules since a few oxides simultaneously satisfy them, but the rules offer the basic concepts for inorganic structural chemistry. For example, the crystal structures of oxides, chalcogenides, and mixed anion compounds are linked polyhedra with explicit chemical bonds, especially between anions and cations. Anions such as oxygen prefer to constitute the Barrow packings, which are the densest packings of spheres, and small cations are placed in the tetrahedral and octahedral sites, while large cations typically have a coordination number greater than six, and in some cases, constitutes the Barrow packings with anions. Small and large cations generally behave as hard and soft spheres, respectively. Highly polar bonds do not favor edge-sharing polyhedra and especially face-sharing polyhedra because of the increased electrostatic repulsion between central atoms.

The structure of amorphous semiconductors is well represented by continuous random network models which require a condition that each atom should satisfy fully its bonding needs. Two atoms interact only if they are explicitly bonded, and the total energy is given by the Keating potential. The network is reproduced periodically by bond transpositions accepted with the Metropolis acceptance probability, conserving four coordination. This approach can generate structurally and electronically good structures comparable with experiments from random initial structures.

In this study, we propose a paired mathematical programming approach that finds candidate structures of crystals satisfying a series of empirical rules. The first is the minimization problem of the volume of the unit cell within the constraints of minimum and maximum distances between pairs of atoms. The constraints represent linked polyhedra and simultaneously the packings of anionic spheres regardless of the kinds of chemical bonds. We approximate the inequality constraints as the linear potentials for the structural relaxation. The second is the maximization problem of the number of chemical bonds. The five kinds of geometrical constraints, which impose restrictions on the distances between every pair of atoms, are assigned by the network of chemical bonds. The two optimization problems are alternately solved to find a proper structure where every cation satisfies its bonding needs; the transpositions of geometrical constraints transform random initial structures into linked polyhedra as the sillium approach for amorphous silicons. We define a feasible solution as a structure satisfying all the constraints in the two optimization problems and all the bonding needs of atoms, and the other cases are denoted as infeasible solution. An optimal solution in this study is defined to be the feasible solution whose volume of the unit cell is minimized. The paired mathematical programming we propose is an efficient method which tries to find the optimal solution for a model system with a given composition.

Let us start our discussion by introducing the first object function in the paired mathematical programming formalism. The geometrical constraints are composed of the minimum and maximum distances between pairs of atoms. Suppose xi is the cartesian coordinate of atom i, and rijT is the distances between atoms i and jT given by

(one) where the atom jT corresponds to the atom j with the translational vector T of the crystal lattice. The object function is the volume § of the unit cell. The mathematical programming is given by

CijT equals x sub i plus T minus x sub i,

minimize §

subject to xijT greater than or equal to d min dijT,

(two) xijT less than or equal to d max where dijT min and d max lijT are the minimum and maximum distances between atoms i and jT, respectively. This model finds structural candidates of crystals without calculating the total energies.

To solve the problem, the equality and inequality constraints are relaxed as follows: The constraint of minimum distance between atoms i and jT:

KijT greater than or equal to d min,

is relaxed to the hard-spherical potential Umin xijT defined to be

Umin equals To open bracket negative k i open parenthesis Cir minus d min close parenthesis

CijT less than dijT min bijT less than WijT VI

, (four)

where k y is a common constant for the minimum constraints. Similarly, the constraint of maximum distance between atoms i and jT:

CijT less than or equal to d max.

is relaxed to the hard-spherical potential Umax defined to be

Umax less than HijT,

zero

XijT less than or equal to dijT Umax dijT

Umax equals kT (CijT minus Umax dijT)

where k plus is a common constant for the maximum constraints. The relaxations transform the problem of Eq. two into the minimization problem of the enthalpy H per unit cell formulated as minimize H equals E plus PQ,

where P is the pressure and E is given by E equals the sum of Umin and Umax,

and ai is the primitive translation vectors of crystal lattice. The displacement of each atom is calculated from the derivative of the enthalpy H per unit cell as

Axi equals negative Ki J the derivative of dH

The constant ki is scaled to ensure so that the norm of displacement does not exceed the given maximum value, Axmax, for each optimization step. Similarly, the primitive lattice vectors ai is optimized as

Aaj equals negative KL the derivative of dH

where kL is set to satisfy the condition:

Axmax squared plus Aaj squared plus Aa squared is less than or equal to Amax.

To reach the local optima of the problem given by Eq. seven, we gradually reduce Axmax and Aamax as

Axmax equals Q7-14xone Imax

Aajm equals Axmax "max four thousand where o is a constant and n is the number of geometrical optimization steps. The values of parameters such as a, ky, kj, and P are discussed in Supplementary Information. One may consider that structures are never relaxed due to the discontinuity in the first derivative of the potential. However, the structure converges to an optimal solution by gradually reducing the maximum Axmax and Aamax, even though there is the discontinuity. The effectiveness of linear relaxations of inequality constraints has already been shown in the previous studies on the densest sphere packings as iterative-balance method. The method enables the structures to reach a local optima precisely enough to calculate packing fractions. The inequality constraints are widely approximated by the logarithmic barrier functions, but the advantage of the linear potentials consists of the two folds: One is that the computational cost is the lowest and the other is that the potentials can impose hard penalties only when the constraints are not satisfied.

Next we turn our discussion to the second objective function in the paired mathematical programming formalism. The problem is how to determine the values of dair minimum and maximum. In the following discussion, we focus on the crystal structures of oxides. We introduce the five kinds of geometrical constraints as listed in Table one and illustrated in Fig. one. The minimum and maximum distances are determined as max p : s (p minimum)

minimum

SiiT ijT

ʹijT

maximum ijT equals maximum p SijT

p maximum p where Siir belongs to zero or one is a switch variable selecting one of the geometrical constraints, and p runs chemical bond , non-bonding constraint, anionic constraint, cationic constraint, and polyhedral constraint. The geometrical constraints for every pair of atoms are assigned depending on the network of CBs. CBs or NBCs are formed between every pair of an anion and a cation. ACs are formed between every pair of anions. Besides, if two coordination polyhedra around cations share some bridging anions, PC is formed between the two cations. Finally, CCs are formed between remained pairs of cations. To assist making coordination polyhedra, NBCs spatially separate the anion and cation when CB is not formed between them. ACs impose the hard-spherical constraint for every pair of anions; oxygen ions often constitute the Barrow-packings if the cationic radii are small. CCs are necessary to spatially separate two cations enough to avoid the condensation of cations, while a minimum distance of PC is smaller than that of CC to share a common edge or face as r(M) D(shared) plus D(shared)

otherwise N equals one,

PC minimum

'ijT

where D(shared) is the minimum distance from the cation i to the shared common edge or face as detailed in Supplementary Information.

Since any cation i has the desirable coordination number N for CBs, the feasible linked-polyhedra must satisfy the conditions of switch (N minus n equals zero,

where n n is the coordination number, which is counted by the number of CBs for atom i, and switch is a switch function for the atom i given by zero if the atom i is anion.

Most of random initial structures are infeasible solutions, and the analytic optimization methods such as the steepest-descent method cannot escape from the infeasible solution to a feasible solution. Therefore, we periodically update the values of D minimum and D maximum depending on the network of CBs that are also renewed periodically. The network is determined from the maximization problem of the number of CBs given by plus S Ein plus dot dot dot plus S M E M n M plus (CB)

maximize

CB is less than or equal to N CB

subject to

N I

CBA is less than or equal to N CBA

N I J T CB

S I J T T I J T less than or equal to two D CB, max plus CB S I S I I R J I J T less than or equal to min

C I J A T q where zero is less than E is the fixed bonding affinity, N I J T CBA is the number of common bridging atoms between the pair of atoms I and J T, N CBA is the default maximum number of common bridging atoms defined in Equation eighteen, and Q is an index for selecting N I indices of anions J T randomly. The third constraints define the formation ranges of CBs. The fourth constraints force cations to create CBs with the nearest N I anions. The optimization problem can be solved as follows: First, all the cations create as many CBs as possible with neighboring anions, and seconds, we erase CBs with maximizing the object function of Equation seventeen until all the number of common bridging atoms satisfy the second constraints. Note that two polyhedra are linked by sharing a common vertex, a common edge, or a common face that corresponds to sharing one, two, or more than two common bridging atoms, respectively.

To find the optimal solutions, we solve the problems of Equations two and seventeen alternately. The optimization scheme is shown in Figure two. A random initial structure can be infeasible solution, in fact, not all cations may not be surrounded by oxygen ions and may not have desirable coordination numbers. Besides, even if all the atoms have the desirable coordination numbers, the structure does not necessarily satisfy all the geometrical constraints such as the maximum number of common bridging atoms. Therefore, the global geometrical optimization is aimed at transforming the structure largely enough to create a different network of CBs by large Ax max. After the small number of global geometrical optimization steps,

CB, max equals R I plus R J

I

D I T

equals one point two R T plus R one

I plus R I

D I T

C

C

I plus R

D A I T

PC, max as discussed in main text we solve the problem of Equation seventeen once again to update the network of CBs. The mutable network and the other geometrical constraints assist cations making coordination polyhedra, and accordingly, the structure is transformed into a feasible solution. If the structure satisfies the condition of Equation fifteen, the structure is locally optimized by small Ax max to identify whether the structure can be the optimal solution of the geometrical optimization problem given by Equation two. If so, the structure is the optimal solution of the paired optimization problems. If not, the structure is globally optimized again after annealing. The parameters of global and local optimization are detailed in Supplementary Information.

To estimate the number of optimal solutions and coarsely classify the optimal solutions, we define a structural fingerprint as the bundle of the fingerprints by the lists of geometrical constraints LGCs in dictionary order. LGCs are defined as what kinds of geometrical constraints are formed with the adjacent atoms. The fingerprint of LGC enumerates the element symbols of the adjacent atoms linked by CBs, PCs, and ACs in dictionary order, respectively. Note that there is a possibility that the same structure fingerprint is assigned to different structures. For example, the fingerprint for the rutile structure and A P b O two is the case. See also Supplementary Information.

The paired mathematical programming approach is aimed at showcasting capabilities of simple rules to search structural prototypes of crystals. In this study, we introduce eleven kinds of cations shown in Table two to reproduce a wide variety of coordination polyhedra. The eleven cations are selected by considering closed packed polyhedra consisting of the centered cation and surrounding oxygen ions, and defined by R I, R J, N CB, and N CBA, where N CBA is the default maximum number of common bridging atoms. We determine N CBA in the second constraint of Equation seventeen as

N CBA equals min N CBA N CBA.

Eighteen

Cationic radius C N N in Nat corresponds to the minimum radius so that the cation can connect N oxygen ions, while C O corresponds to the ionic radius of oxygen ion. They are given in Supplementary Information. If the minimum and maximum cationic radii are the same, the cation is a hard sphere; if not, the cation is a soft sphere,

because the bonding lengths can vary within the two radii.

We apply our mathematical programming model to several compositions of cations, and find that a wide variety of real crystals are discovered in the optimal solutions by the paired mathematical programming. Table three shows the number of discovered optimal solutions for each composition, which seems to be much smaller than the number of local minima in the total energy by ab initio simulations, and corresponding real crystals found in them. We discuss here results by focusing on aspects of the generated coordination polyhedra.

The optimal solutions of H T y T M O N form a wide variety of linked-polyhedra composed of tetrahedra and octahedra as shown in Figure three. The cations T and H T are placed in the tetrahedral and octahedral sites, respectively, in the Barrow-packings consisting of oxygen ions. Many structures are rejected from the optimal solutions by the constraints of the maximum number of common bridging atoms of T. The spinel structure has the lowest number of LGCs and highest symmetry, found as one of the optimal solutions for both the H T four T two zero eight and H T eight T four zero one six, while the G A two O three structure, which is composed of five LGCs with the C two M symmetry, has more LGCs and lower symmetry than the structure shown in Figure three D. Real crystal structures are not necessarily the optimal solution composed of the lowest number of LGCs and highest symmetry, however, they are generally good indicators to assess expectations of the structures to be realized by real crystals. The optimal solution shown in Figure three C is similar to the crystal structure of L I two W O four; the difference comes from the sizes of the unit cells. The crystal structure of L I two W O four is composed of large tetrahedra and octahedra around lithiums, but this structure may be reproduced by using cations H T and T, which are placed in the octahedral and tetrahedral sites in the Barrow-packings consisting of oxygens, as the optimal solution of H T sixteen T eight O thirty-two. Figure three F shows the layered structure terminated by tetrahedra and octahedra. This optimal solution is composed of the lowest number of LGCs in H T five T three O twelve.

All the optimal solutions of D four Ht four O twelve correspond to the real crystals shown in Figures four (a), four (b), four (c), and four (d). The cation D makes coordination polyhedra of anticuboctahedron or cuboctahedron. Besides, we find that D three Ht six O fifteen has the optimal solution corresponding to the BaTi two O five structure shown in Figure four (f). The optimal solution consists of eleven LGCs, but we find another optimal solution consisting of only five LGCs with the Cmmm symmetry shown in Figure four (e).

Our results indicate that De four Ht two O eight and De nine Ht four O sixteen have only one optimal solution corresponding to the crystal structure of La two minus z Sr two CuO four as shown in Figure five (a). The cation De makes coordination polyhedron of capped square antiprism. Besides, our calculations indicate that D one De two Ht two O seven and D two De four Ht four O fourteen also have a unique optimal solution corresponding to the crystal structure of La two minus z Sr one plus two Cu two O seven which consists of three kinds of coordination polyhedra as shown in Figure five (b).

In the pyrochlore-o structure found as one of the optimal solutions for Do four Hd four O fourteen and Uo four Hd four O fourteen, one oxygen ion is placed in the center of the tetrahedron composed of large cations, and the distance of ionic bond must be smaller than those of the other ionic bonds, and thereby a large cation makes coordination polyhedron of distorted cubic as shown in Figure five (c). In fact, our calculations indicate that the pyrochlore-a structure is difficult to obtain without soft sphere, while both the Do four Hd four O fourteen and Uo four Hd four O fourteen have the optimal solution corresponding to the pyrochlore-o structure, which has the lowest number of LGCs with highest symmetry. Note that the interatomic distances can be as small as possible without attractive forces since the volume of the unit cell is minimized. The optimal solution consisting of the second lowest number of local geometric constraints for the U_O four H_D four O fourteen is the layer-by-layer structure of cubics and octahedra with the P one symmetry as shown in Figure 5(d).

The cubic coordination can also be realized by the cation E_O. E_O six O twelve has the optimal solution corresponding to the zirconia structure shown in Figure 5(e). The cation E_O can also make the coordination polyhedra of square antiprism as shown in Figure 5(f).

O_P four H_T four O twelve has the optimal solution corresponding to the crystal structure of Y_F_E_O three which is composed of coordination polyhedra of capped trigonal prisms as shown in Figure 6(a). Y_F_E_O three and the optimal solution shown in Figure 6(b) have the same symmetry, but the latter structure is composed of five local geometric constraints, and capped trigonal prisms in the structure share the faces. The manner of atomic distribution in Y_F_E_O three is the same as L_A_M_G_Ta one minus two O one plus three x N two minus three x which can be employed for overall water splitting at wavelengths of up to six hundred nanometers. The correspondence implies the applicability of our method to mixed anion compounds. On the other hand, we could not find the optimal solution corresponding to the crystal structure of S_R two P_D_O four in the optimal solutions of O_P four H_D O sixteen. However, the optimal solution, which has four local geometric constraints and the Pbam symmetry shown in Figure 6(c), is similar to the crystal structure of S_R two P_D_O four; they have the same symmetry, and the difference only comes from the kind of linking between octahedra and capped trigonal prisms. In the optimal solution, octahedra and capped trigonal prisms share the faces, while in the crystal structure of S_R two P_D_O four, they share edges. In general, our algorithm tends to generate polyhedra sharing as many common bridging atoms as possible.

Finally, P_E two S_H one O four has the optimal solution corresponding to the crystal structure of InGaZnO four. However, it may be difficult to form trigonal bipyramidal coordination polyhedra using the cation P_E, which possesses a hard cationic radius of C_five. Note that in the hexagonal closest packing of oxygen ions, the center of trigonal bipyramid is identical with the interstice between three atoms in the hexagonal layer, and accordingly, the axial atoms of the bipyramid are forty-one percent more distant than the equatorial atoms from the central atoms. Also, note that C five is the same as C six.

In summary, we propose a novel method to enumerate crystal structure prototypes using the paired mathematical programming, subject to a set of constraints on atomic distances, and demonstrate its applicability to find a broad range of crystal structures of oxides. The method consists of two optimization problems. The first is the minimization problem of the volume of the unit cell under the geometrical constraints that are the minimum and maximum distances between every pair of atoms, while the second is the maximization problem of the number of chemical bonds. The constraints of the two problems make every optimal solution satisfy a series of empirical rules systematized in inorganic structural chemistry. The two optimization problems are solved alternately to find a proper structure where every cation satisfies its bonding needs by transpositions of geometrical constraints as silicate approach for amorphous silicons. We find that the linear relaxations of inequality constraints are effective, and accordingly, the small computational cost enables the exhaustive search for the optimal solutions of large-scale systems. We apply the mathematical programming to cases with eighteen compositions, find the optimal solutions for each case successfully, and identify the corresponding real crystal structures. Our result strongly implies that the number of optimal solutions in the mathematical programming seems to be much smaller than the number of local minima in the total energy by ab-initio simulations. A small number of optimal solutions, identified through the mathematical programming, can be easily validated using ab-initio simulations to assess their stability. We anticipate that these optimal solutions may lead to the discovery of novel materials. The successful reproduction of a broad range of oxide crystal structures may suggest the emergence of a universal rule, potentially resulting from the precise refinement of the Pauling rules as demonstrated in this study. Given the proven success with oxide cases, it is anticipated that this method could be extended to other cases such as chalcogenides, mixed anionic compounds, intermetallic compounds, and borides, provided that effective principles are established.

ematical programming, subject to a set of constraints on atomic distances, and demonstrate its applicability to find a broad range of crystal structures of oxides. The method consists of two optimization problems. The first is the minimization problem of the volume of the unit cell under the geometrical constraints that are the minimum and maximum distances between every pair of atoms, while the second is the maximization problem of the number of chemical bonds. The constraints of the two problems make every optimal solution satisfy a series of empirical rules systematized in inorganic structural chemistry [24, 25]. The two optimization problems are solved alternately to find a proper structure where every cation satisfies its bonding needs by transpositions of ge- ometrical constraints as sillium approach for amorphous silicons [28-31]. We find that the linear relaxations of inequality constraints are effective, and accordingly, the small computational cost enables the exhaustive search for the optimal solutions of large-scale systems. We apply the mathematical programming to cases with 18 compo- sitions, find the optimal solutions for each case success- fully, and identify the corresponding real crystal struc- tures. Our result strongly implies that the number of op- timal solutions in the mathematical programming seems to be much smaller than the number of local minima in the total energy by ab-initio simulations. A small number of optimal solutions, identified through the mathemati- cal programming, can be easily validated using ab-initio simulations to assess their stability. We anticipate that these optimal solutions may lead to the discovery of novel materials. The successful reproduction of a broad range of oxide crystal structures may suggest the emergence of a universal rule, potentially resulting from the precise refinement of the Pauling rules as demonstrated in this study. Given the proven success with oxide cases, it is anticipated that this method could be extended to other cases such as chalcogenides, mixed anionic compounds, intermetallic compounds, and borides, provided that ef- fective principles are established.


## I. METHODS

Our mathematical programming formulation is based on inorganic structural chemistry that describes crystal structures. As references for our basic idea, see the textbooks.


## A. Geometrical constraints

Figure S1(a) shows the optimal solution of H_D four O_g corresponding to the rutile structure. Every oxygen makes three chemical bonds with H_D, while every H_D makes six chemical bonds with oxygens. Parallel linear strands of edge-sharing octahedra are joined by common octahedron vertices. Oxygen ions constitute the hexagonal closest-packings, and the structure is reproduced by the anionic constraints between every pair of oxygen ions. Figure S1(b) shows the optimal solution of H_D four O_g corresponding to the alpha-PbO two structure. The zigzag chains of edge-sharing octahedra are also joined by common vertices. If a pair of oxygen and H_D is not connected by a chemical bond, a non-bonding constraint connects them. Every H_D makes ten polyhedral constraints, and two of them correspond to edge-sharing. These two optimal solutions, which correspond to the rutile structure and the alpha-PbO two structure, respectively, have the same structural fingerprint, because the two structures have the same number of local geometric constraints of the same type, where a fingerprint of a local geometric constraint enumerates the element symbols of the adjacent atoms linked by chemical bonds, polyhedral constraints, and anionic constraints in dictionary order, respectively. Figures S1(c) shows the optimal solution H_T four O six corresponding to the corundum structure. There are pairs of face-sharing octahedra, and every octahedron shares three edges within a layer and three vertices with octahedra from the adjacent layer to which it has no face-sharing connection.

To share edges or faces of coordination polyhedra, the minimum distance between two cations is shortened compared to that of the cationic constraints. Suppose D_i is the minimum bonding distance given by

D_i equals r_i plus r_j.

(S1)

and then the minimum distance D(shared) from the cation i to the shared common edge or face is given by

V equals C three N_i_j (CBA) equals two.

D(shared) equals

N(CBA) equals three. (S2) N_i_j equals four.


## B. Initial structures

Initial structures are generated as follows: Suppose a one, a two and a three are the primitive lattice vectors. First, they are given by

(a one, a two, a three) equals (a one equals l one l two cosine theta two l three sine phi three cosine theta three l two sine theta two zero l three sine phi three sine theta three). (S3) l three cosine theta three where one is less than L i is less than or equal to two, ; less than or equal to zero ; } five twenty-three, and six P H i six six T T T T are randomly set. Second, the lattice is expanded until the sum of the volume of the atomic spheres becomes seventy percent of the volume of the unit cell, where the anionic and cationic radii are set to be zero point six and one point four, respectively. The cartesian coordinate of an atom is set to be

(S four)

x equals q one at one plus q two times A two plus q three at three where zero less than or equal to q i less than or equal to one are random values.


## C. Cationic Radii

The eleven cations, which are listed in Table two of the main article, are selected by considering closed packed polyhedra consisting of the centered cation and surrounding oxygen ions. Cationic radius C n (n belongs to natural numbers) corresponds to the minimum radius so that the cation can connect n oxygen ions, while C O corresponds to the ionic radius of oxygen ion. Table S one lists the value of C n and C O.

All cations have the same cationic repulsion radius r C equals one point four which is the same as the ionic radius of oxygen ion to avoid the condensation of cations.


## II. NUMERICAL ASPECTS

Table S two lists the common parameters for the global and local geometrical optimizations. The geometrical constraints are given by the minimum and maximum distances between atoms as x i j T greater than or equal to d y g n, L i j T less than or equal to d o max, (S five) but when we confirm the feasibility of the structure after local geometrical optimization, we permit five percent error as

T i j T greater than or equal to zero point nine five d i j one, (minimum) X i j T less than or equal to one point zero five d i j T (maximum)

E). (S six)

Besides, in this study, if the packing fraction is less than the minimum, we reject the sparse structure from the optimum solutions. O is calculated as a equals (A. x max, f A x max, i

, (S seven)

where A x max, i and A x max, f are the initial and final A x max, respectively, and N opt is the maximum number of optimization steps.

We generate one million samples for H t four T two O eight and H t four T four O sixteen. Table S five shows the number of H t four T two five and H t four T four O sixteen samples optimized to the spinel structure; about ten percent of H t four T two O eight are optimized to spinel structure, while zero point zero one percent of H t four T four O sixteen are optimized to spinel structure.

ture. Nine hundred thirty-eight thousand five hundred forty-two samples of eight H t four T four O sixteen cannot reach optimal solutions if we use the optimization parameters shown in Tables S two, S three, and S four.

Generally, not all the cations have the maximum number of chemical bonds. The global geometrical optimization is aimed at transforming the structure largely enough to create a different network of chemical bonds so that every cation satisfies its bonding needs. To analyze the optimization history, we monitor the rate of chemical bonds P c given by

E i sin (C B) E i plus N (C B)

Pc equals

(S-Eight)

where the numerator is the number of chemical bonds,

and the denominator is the total number of bonding needs. If every cation satisfies its bonding needs, the structure is locally optimized to identify whether the structure can be the optimal solution of the geometrical optimization problem. If so, all the interatomic distances satisfy the condition of Equation (S-Six), and we regard the chemical bonds satisfying Equation (S-Six) as the relaxed chemical bonds. We monitor the rate of relaxed chemical bonds Prc, where the numerator and the denominator are the total number of the relaxed chemical bonds and the total number of the chemical bonds of the constraint, respectively. We also monitor the packing fraction defined to be

(S-Nine)

Figure S-Two shows the changes of Pc, Pre and during the optimization process. The fluctuation of Pc indicates that a structure is transformed largely enough to change the network of chemical bonds. The small rate of Prc comes from the large displacement through the global optimization. If Pc reaches one point zero, the structure is locally optimized to identify whether the structure can be the optimal solution of the geometrical optimization problem within the five percent error. In local optimization, Pre shows larger value due to the small displacement, however, in some cases, Pre cannot reach one point zero due to the contradictions in the geometrical constraints. has the value around zero point five through the global optimization process.