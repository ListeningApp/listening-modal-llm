## What Is Entropy

Foreword

Once there was a thing called Twitter, where people exchanged short messages called 'tweets'. While it had its flaws, I came to like it and eventually decided to teach a short course on entropy in the form of tweets. This little book is a slightly expanded version of that course.

It's easy to wax poetic about entropy, but what is it? I claim it's the amount of information we don't know about a situation, which in principle we could learn. But how can we make this idea precise and quantitative? To focus the discussion I decided to tackle a specific puzzle: why does hydrogen gas at room temperature and pressure have an entropy corresponding to about twenty-three unknown bits of information per molecule? This gave me an excuse to explain these subjects:

· information

· Shannon entropy and Gibbs entropy

· the principle of maximum entropy

· the Boltzmann distribution

· temperature and coolness

· the relation between entropy, expected energy and temperature

· the equipartition theorem

· the partition function

· the relation between entropy, free energy and expected energy

· the entropy of a classical harmonic oscillator

· the entropy of a classical particle in a box

· the entropy of a classical ideal gas.

I have largely avoided the second law of thermodynamics, which says that entropy always increases. While fascinating, this is so problematic that a good explanation would require another book! I have also avoided the role of entropy in biology, black hole physics, etc. Thus, the aspects of entropy most beloved by physics popularizers will not be found here. I also never say that entropy is 'disorder'.

I have tried to say as little as possible about quantum mechanics, to keep the physics prerequisites low. However, Planck's constant shows up in the formulas for the entropy of the three classical systems mentioned above. The reason for this is fascinating: Planck's constant provides a unit of volume in position-momentum space, which is necessary to define the entropy of these systems. Thus, we need a tiny bit of quantum mechanics to get a good approximate formula for the entropy of hydrogen, even if we are trying our best to treat this gas classically.

Since I am a mathematical physicist, this book is full of math. I spend more time trying to make concepts precise and looking into strange counterexamples than an actual 'working' physicist would. If at any point you feel I am sinking into too many technicalities, don't be shy about jumping to the next tweet. The really important stuff is in the boxes. It may help to reach the end before going back and learning all the details. It's up to you.

In twenty ten, Chas A. Egan and Charles H. Lineweaver estimated the biggest contributors to the entropy of the observable universe. Measuring entropy in bits, these are:

· stars: ten to the eighty-first bits.

· interstellar and intergalactic gas and dust: ten to the eighty-second bits.

· gravitons: ten to the eighty-eighth bits.

· neutrinos: ten to the ninetieth bits.

· photons: ten to the ninetieth bits.

· stellar black holes: ten to the ninety-eighth bits.

· supermassive black holes: ten to the one hundred and fifth bits.

So, almost all the entropy is in supermassive black holes!

In twenty ten, Chas A. Egan and Charles H. Lineweaver estimated the entropy of the observable universe. Entropy corresponds to unknown information, so there's a heck of a lot we don't know! For stars, most of this unknown information concerns the details of every single electron and nucleus zipping around in the hot plasma. There's more entropy in interstellar and intergalactic gas and dust. Most of the gas here is hydrogen-some in molecular form H-two, some individual atoms, and some ionized. For all this stuff, the unknown information again mostly concerns the details, like the position and momentum, of each of these molecules, atoms and ions.

There's a lot more we don't know about the precise details of other particles whizzing through the universe, like gravitons, neutrinos and photons. But there's even more entropy in black holes! One reason Stephen Hawking is famous is that he figured out how to compute the entropy of black holes. To do that you need a combination of statistical mechanics, general relativity and quantum physics. Statistical mechanics is the study of physical systems where there's unknown information, which you study using probability theory. I'll explain some of that in these tweets. General relativity is Einstein's theory of gravity, and while I've explained that elsewhere, I don't want to get into it here so I will say nothing about the entropy of black holes.

Quantum physics was also necessary for Hawking's calculation, as witnessed by the fact that his answer involves Planck's constant, which sets the scale of quantum uncertainty in our universe. I will try to steer clear of quantum mechanics in these tweets, but in the end we'll need a tiny bit of it. There's a funny sense in which statistical mechanics is somewhat incomplete without quantum mechanics. You'll eventually see what I mean.


## THE ENTROPY OF HYDROGEN

At standard temperature and pressure, hydrogen gas has an entropy of

But a joule per kelvin of entropy is about

So the unknown information about the precise microscopic state of hydrogen is one hundred thirty point six eight. six point zero two two one times ten to the twenty-third

Egan and Lineweaver estimated the entropy of all the interstellar and intergalactic gas and dust in the observable universe. Entropy corresponds to information we don't know. Their estimate implies that there are ten to the eighty-second bits of information we don't know about all this gas and dust.

Most of this stuff is hydrogen. Hydrogen is very simple stuff. So it would be good to understand the entropy of hydrogen. You can measure changes in entropy by doing experiments. If you assume hydrogen has no entropy at absolute zero, you can do experiments to figure out the entropy of hydrogen under other conditions. From this you can calculate that each molecule in a container of hydrogen gas at standard temperature and pressure has about twenty-three bits of information that we don't know.

You can see a sketch of the calculation above. But everything about it is far from obvious! What does 'missing information' really mean here? Joules are a unit of energy; kelvin is a unit of temperature. So why is entropy measured in joules per kelvin? Why does one joule per kelvin correspond to one point zero four four nine times ten to the twenty-third bits of missing information? How can we do experiments to measure changes in entropy? And why is missing information the same as-or more precisely proportional to-entropy?

The good news: all these questions have answers! You can learn them here. However, you will have to persist. Since I'm starting from scratch it won't be quick. It takes some math-but luckily, nothing much more than calculus of several variables. When you can calculate the entropy of hydrogen from first principles, and understand what it means, that will count as true success.

See how it goes! Partial success is okay too.


## WHERE ARE WE GOING?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure?


## The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

S equals k N times the natural log of k T plus the natural log of approximately r divided by N V


## including the mysterious constant y.

The subgoal: compute the entropy of a single classical particle in a one-dimensional box.


## The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator.

To understand something deeply, it can be good to set yourself a concrete goal. To avoid getting lost in the theory of entropy, let's try to understand the entropy of hydrogen gas. This is a 'diatomic' gas since a hydrogen molecule has two atoms. At standard temperature and pressure it's close to 'ideal', meaning the molecules don't interact much. It's also close to 'classical', meaning we don't need to know quantum mechanics to do this calculation. Also, when the hydrogen is not extremely hot, its molecules don't vibrate much-but they do tumble around.

Given all this, we can derive a formula for the entropy S of some hydrogen gas as a function of its temperature T, the number N of molecules, the volume V, and a physical constant k called 'Boltzmann's constant'. This formula also involves a rather surprising constant which I'm calling y. We'll figure that out too. It's so weird I don't want to give it away!

As a warmup, we will derive the formula for the entropy of an ideal 'monatomic' gas a gas made of individual atoms, like helium or neon or argon. Sackur and Tetrode worked this out in nineteen twelve. Their result, called the Sackur-Tetrode equation, is similar to the one for a diatomic gas.

But before doing a monatomic gas, we'll figure out the entropy of a single atom of gas in a box. That turns out to be a good start, since in an ideal monatomic gas the atoms don't interact, and the entropy of N atoms-as we'll see is just N times the entropy of a single atom.

But before we can do any of this, we need to understand what entropy is, and how to compute it. It will take quite a bit of time to compute the entropy of a classical harmonic oscillator! But from then on, the rest is surprisingly quick.


## Five kinds of entropy

Entropy in thermodynamics: the change in entropy as we change a system's internal energy by an infinitesimal amount dE while keeping it in thermal equilibrium is dS equals dE divided by T, where T is the temperature.

Entropy in classical statistical mechanics: S equals negative k integral p(x) ln(p(x)) du(x) where p is a probability distribution on the measure space (X, u) of states and k is Boltzmann's constant.

Entropy in quantum statistical mechanics: S equals negative k times the trace of p ln p where p is a density matrix.

Entropy in information theory: H equals negative sum over x of p(x) log p(x) where p is a probability distribution on the set X.

Algorithmic entropy: the entropy of a string of symbols is the length of the shortest computer program that prints it out.

Before I actually start explaining entropy, a warning: it can be hard at first to learn about entropy because there are many kinds-and people often don't say which kind they're talking about. Here are five kinds. Luckily, they are closely related!

In thermodynamics we primarily have a formula for the change in entropy: if you change the internal energy of a system by an infinitesimal amount dE while keeping it in thermal equilibrium, the infinitesimal change in entropy is dS equals dE divided by T, where T is the temperature.

Later, in classical statistical mechanics, Gibbs explained entropy in terms of a prob- ability distribution p on the space of states of a classical system. In this framework, entropy is the integral of negative p ln p times a constant k called Boltzmann's constant.

Later von Neumann generalized Gibbs' formula for entropy from classical to quantum statistical mechanics! He replaced the probability distribution p by a so-called density matrix p, and the integral by a trace.

Later Shannon invented information theory, and a formula for the entropy of a probability distribution on a set (often a finite set). This is often called 'Shannon entropy'. It's just a special case of Gibbs' formula for entropy in classical statistical mechanics, but without the Boltzmann's constant.

Later still, Kolmogorov invented a formula for the entropy of a specific string of symbols. It's just the length of the shortest program, written in bits, that prints out this string. It depends on the computer language, but not too much.

There's a network of results connecting all these five concepts of entropy. I will first explain Shannon entropy, then entropy in classical statistical mechanics, and then entropy in thermodynamics. While this is the reverse of the historical order, it's the easiest way to go.

I will not explain entropy in quantum statistical mechanics: for that I would feel compelled to teach you quantum mechanics first. Nor will I explain algorithmic entropy.


## FROM PROBABILITY TO INFORMATION

How much information do you get when you learn an event of probability P has happened? It's

Negative log P where we can use any base for the logarithm, usually E or two.

Example: Suppose I flip three coins that you know are fair. I tell you the outcome: "heads, tails, heads". That's an event of probability one divided by two to the power of three, so the information you get is

Negative log of one divided by two to the power of three equals three log two or "three bits" for short, since log two of information is called a bit.

Here is the simplest link between probability and information: when you learn that an event of probability P has happened, how much information do you get? We say it's negative log P. We take a logarithm so that when you multiply probabilities, information adds. The minus sign makes information come out positive.

Beware: when I write 'log' I don't necessarily mean the logarithm base ten. I mean that you can use whatever base for the logarithm you want; this choice is like a choice of units. Whatever base B you decide to use, I'll call log base B two a 'bit'. For example, if I flip a single coin that you know is fair, and you see that it comes up heads, you learn of an event that's of probability one divided by two, so the amount of information you learn is

Negative log base B of one divided by two equals log base B two. That's one bit! Of course if you use base B equals two then this logarithm actually equals one, which is nice.

To understand the concept of information it helps to do some puzzles.

Puzzle one. First I flip two fair coins and tell you the outcome. Then I flip three more and tell you the outcome. How much information did you get?

Puzzle two. I roll a fair six-sided die and tell you the outcome. Approximately how much information do you get, using logarithms base two?


## Puzzle three. When you flip seven fair coins and tell me the outcome, how much information do I get?

Puzzle four. Every day I eat either a cheese sandwich, a salad, or some fried rice for lunch each with equal probability. I tell you what I had for lunch today. Approximately how many bits of information do you get?

Puzzle five. I have a trick coin that always lands heads up. You know this. I flip it five times and tell you the outcome. How much information do you receive?

Puzzle six. I have a trick coin that always lands heads up. You believe it's a fair coin. I flip it five times and tell you the outcome. How much information do you receive?

Puzzle seven. I have a trick coin that always lands with the same face up. You know this, but you don't know which face always comes up. I flip it five times and tell you the outcome. How much information do you receive?

These puzzles raise some questions about the nature of probability, like: is it subjective or objective? People like to argue about those questions. But once we get a probability P, we can convert it to information by computing negative log P.


## UNITS OF INFORMATION

An event of probability one divided by two carries one bit of information. An event of probability one divided by E carries one nat of information. An event of probability one divided by three carries one trit of information. An event of probability one divided by four carries one crumb of information. An event of probability one divided by ten carries one hartley of information. An event of probability one divided by sixteen carries one nibble of information. An event of probability one divided by two hundred fifty-six carries one byte of information. An event of probability one divided by two to the power of eight thousand one hundred ninety-two carries one kilobyte of information.

There are many units of information. Using information equals negative log P we can relate these to probabilities. For example if you see a number in base ten, and each digit shows up with probability one divided by ten, the amount of information you get from each digit is one 'hartley'.

How many bits are in a hartley? Remember: no matter what base you use, I call log ten a hartley and log two a bit. There are log ten divided by log two bits in a hartley. This number has the same value no matter what base you use for your logarithms! If you use base two, it's

Log base two ten divided by log base two two equals log base two ten approximately three point three two. So a hartley is about three point thirty-two bits.

If you flip eight fair coins and tell me what answers you got, I've learned of an event that has probability one divided by two to the power of eight equals one divided by two hundred fifty-six. We say I've received a 'byte' of information. This equals eight bits of information. Similarly, if you flip one thousand twenty-four multiplied by eight fair coins and tell me the outcome, I receive a kilobyte of information.

Or at least that's the old definition. Now many people define a kilobyte to be one thousand bytes rather than one thousand twenty-four bytes, in keeping with the usual meaning of the prefix. If you want one thousand twenty-four bytes you're supposed to ask for a 'kibibyte'. When we get to a terabyte, the new definition based on powers of ten is about ten percent less than the old one based on powers of two: ten to the twelve bytes rather than two to the forty approximately one point zero nine nine five times ten to the twelve. If you want the old larger amount of information you should ask for a 'tebibyte'.

Wikipedia has an article that lists many strange units of information. Did you know that two bits is a 'crumb'? Did you even need to know? No, but now you do.

Feel free to dispose of this unnecessary information! All this is just for fun-but I want you to get used to the formula information equals negative log P seven


## THE INFORMATION IN A LICENSE PLATE NUMBER

If there are N different possible license plate numbers, all equally likely, how many bits of information do you learn when you see one?

If you think N alternatives are equally likely, when you see which one actually occurs, you gain an amount of information equal to log N. Here the choice of base B is up to you: it's a choice of units. But what is this in bits? No matter what base you use,

log N equals log two N times log base two.

Since we call log base two a 'bit', this means you've learned log two N bits of information. Let's try it out!

Puzzle eight. Suppose a license plate has seven numbers and/or letters on it. If there are ten plus twenty-six choices of number and/or letter, there are three hundred sixty-seven possible license plate numbers. If all license plates are equally likely, what's the information in a license plate number in bits-approximately?

But wait! Suppose I tell you that all license plate numbers have a number, then three letters, then three numbers! You have just learned a lot of information. So the remaining information content of each license plate is presumably less. Let's work it out.

Puzzle nine. How much information is there in a license plate number if they all have a number, then three letters, then three numbers? Assume they're all equally probable and there are ten choices of each number and twenty-six choices of each letter.

The moral: when you learn more about the possible choices, the information it takes to describe a choice drops.


## THE INFORMATION IN A LICENSE PLATE

How much unknown information do the atoms in a license plate contain?

Aluminum has an entropy of about twenty-eight joules per kelvin per mole at standard temperature and pressure. A mole of aluminum weighs about twenty-seven grams. A typical license plate might weigh one hundred fifty grams, and thus have one hundred fifty grams times twenty-seven grams per mole times twenty-eight joules per kelvin per mole is approximately one hundred sixty joules per kelvin of entropy. But a joule per kelvin of entropy is about ten to the twenty-three bits of unknown information. Thus, the atoms in such a license plate contain about one hundred sixty times ten to the twenty-three bits is approximately one point six times ten to the twenty-five bits of unknown information.

Last time we talked about the information in a license plate number. A license plate number made of seven numbers and/or letters contains log two of three hundred sixty-seven is approximately thirty-six point one eight nine bits of information if all combinations are equally likely. How does this compare to the information in the actual metal of the license plate?

These days most license plates are made of aluminum, and they weigh roughly between one hundred and two hundred grams. Let's say one hundred fifty grams. If we work out the entropy of this much aluminum, and express it in bits of unknown information, we get an enormous number: roughly sixteen septillion bits!

Here is the point. While the information on the license plate and the information in the license plate can be studied using similar mathematics, the latter dwarfs the former. Thus, when we are doing chemistry and want to know, for example, how much the entropy of the license plate increases when we dissolve it in hydrochloric acid, the information in the writing on the license plate is irrelevant for all practical purposes.

Some people get fooled by this, in my opinion, and claim that "information" and "entropy" are fundamentally unrelated. I disagree.


## JUSTIFYING THE FORMULA FOR INFORMATION

Why do we say the information of an event of probability P is

I(P) equals negative log P

for some base B greater than one? Here's why:

Theorem. Suppose I: open zero, one close bracket to R is a function that is:

One. Decreasing: P less than Q implies I(P) greater than I(Q). This says less probable events have more information.

Two. Additive: I(PQ) equals I(P) plus I(Q). This says the information of the combination of two independent events is the sum of their separate informations.

Then for some B greater than one we have I(P) equals negative log P.

The information of an event of probability P is negative log P, where you get to choose the base of the logarithm. But why? This is the only option if we want less probable events to have more information, and information to add for independent events.

Proving this will take some math-but don't worry, you won't need to know this stuff for the rest of this 'course'.

Since we're trying to prove I(P) is a logarithm function, let's write and prove F has to be linear:

F of X equals C times X.

As we'll see, this gets the job done.

X less than Y implies F of X greater than F of Y for all X, Y less than or equal to zero.

Similarly, we can check that Condition two is equivalent to

F of X plus Y equals F of X plus F of Y for all X, Y less than or equal to zero.

Now what functions F have

F of X plus Y equals F of X plus F of Y

for all X, Y less than or equal to zero?

If we define F of negative X equals negative F of X, F will become a function from the whole real line to the real numbers, and it will still obey F of X plus Y equals F of X plus F of Y. So what functions obey this equation? The obvious solutions are

F of X equals C times X

for any real constant C. But are there any other solutions?

Yes, if you use the axiom of choice! Treat the reals as a vector space over the rationals. Using the axiom of choice, pick a basis. To get F from R to R that's linear over the rational numbers, just let F send each basis element to whatever real number you want and extend it to a linear function defined on all of R. This gives a function F that obeys F of X plus Y equals F of X plus F of Y.

However, no solutions of F of X plus Y equals F of X plus F of Y meet our other condition

X less than Y implies F of X greater than F of Y for all X, Y less than or equal to zero except for the familiar ones F of X equals C times X. For a proof see Wikipedia: they show all solutions except the familiar ones are so discontinuous their graphs are dense in the plane!

I(P) equals C times ln P

but this equals negative log P if we take B equals exp of negative one over C. And this number B can be any number greater than one. QED.

Thus, if we want a more general concept of the information associated to a probability, we need to drop Condition one or two. For example, we could replace additivity by some other rule. People have tried this! Indeed, there is a world of generalized entropy concepts including Tsallis entropies, Rényi entropies and others.


## WHAT IS PROBABILITY?

Since I've defined information in terms of probability, you may naturally wonder "what is probability?" I won't seriously try to answer this. This question has stirred up many debates over the centuries, and even today there's not a fully accepted answer. It deserves a whole book-and this is not that book. Luckily, we don't really need to know exactly what probability is to do calculations with it: we mainly need to set up some rules for working with it. This may seem like a cop-out. But it's a strange and wonderful feature of science that we can achieve great reliability in our results by sidestepping certain difficult questions, like someone who can make their way safely through a jungle by avoiding the quicksand and snakes.

One approach to probability goes like this. Suppose you repeat some experiment N times, doing your best to make the conditions the same each time. Suppose that M of these times some event E occurs. You may then say that the probability of event E happening under these conditions is M over N. This approach is called 'finite frequentism'. Unfortunately, this approach can lead you to say a coin has probability one of landing heads up if it does so the first time, or first three times, you flip it.

Another approach goes like this. You may say that some event E has probability p under some conditions if when you set up these conditions N times, and the event E happens M times, the fraction M over N approaches p in the limit N goes to infinity. This approach is called 'hypothetical frequentism', because in real experiments you can't take the limit N to infinity. But you can hope that when N becomes large enough, the fraction M over N usually becomes close to the limiting probability p-whatever that means.

Another approach, called 'Bayesianism', treats a probability of an event E under some specified conditions as a measure of your degree of belief that E will happen under these conditions. But what is 'degree of belief'? One answer involves bets. For example, perhaps to believe an event has probability one-half means you're willing to take a bet where you win more when the event happens than you lose if it does not.

Bayesians tend to focus on the rules for updating your probabilities as you learn new things, the most famous being 'Bayes' rule'. Even if agents start by assigning different probabilities to an event, if they follow the same rules for changing these probabilities as they learn new things, under certain circumstances we can prove their probabilities will converge to the same value.

For a passionate and intelligent discussion of these issues, I recommend E. T. Jaynes' book Probability Theory: the Logic of Science. Later we'll meet his 'principle of maximum entropy', another important approach to working with probabilities.


## PROBABILITY MEASURES

A measure on a set X is a function that assigns to certain so-called measurable subsets S of X a number p of S in the interval zero to one, obeying these rules:

. The empty set, X is a subset of X and are measurable.

m of the empty set equals zero.

. If S, T are subsets of X and S is a subset of T, then T minus S is measurable.

m of T equals m of S plus m of T minus S.

. If a countable collection of disjoint subsets S i are subsets of X and are measurable, then their union is measurable and m of the union of S i equals the sum of m of S i as i goes from one to infinity.

We say m is a probability measure if m of X equals one.

It is easier to do calculations with probabilities than say exactly what they mean! I will take a rough-and-ready approach to working with them, but first let's take a peek at how mathematicians do it. If you don't care, it's safe to move right on to the next tweet.

We start with any set. We call elements of X 'outcomes' and subsets of X 'events'. We can sometimes get into trouble trying to assign a probability to every subset of X. So, we'll only try to assign probabilities to events in some collection M with these properties:

· The empty set is in M and X is in M.

. If S, T are in M and S is a subset of T then the set of elements of T that are not in S, called T minus S, is in M.

. If S i are in M for i equals one, two, and so on, then the union of S i is in M.

We call elements of M measurable subsets of X. A measure is then a function m from M to the interval zero to one obeying these rules:

· m of the empty set equals zero.

· If S, T are in M and S is a subset of T then m of T equals m of S plus m of T minus S.

. If S i are in M then m of the union of S i equals the sum of m of S i as i goes from one to infinity.

If m also obeys m of X equals one then we say m is a probability measure, and for any S in M we say m of S is the probability of the event S. But we will also be interested in other measures, like the measure on the real line called 'Lebesgue measure'. This is closely connected to the symbol d x that shows up in integrals, because for any measurable set S subset of the real numbers, its Lebesgue measure is

The integral over all X of the characteristic function of S with respect to X dX where the characteristic function of S with respect to X is one for X in S and zero for X not in S. Indeed, people often get sloppy and say dX 'is' Lebesgue measure, and I may do that too. By the way, Lebesgue measure is one where we cannot take mathcal M to be the collection of all subsets of real numbers. There is an extensive theory of measures. We will not need it here, but if you're interested, you can try a book like Halsey Royden's Real Analysis, where I learned the basics myself, or Terry Tao's An Introduction to Measure Theory, which has a legal free version online.

Here are some puzzles about measures.

Puzzle ten. Let X be any set and define mathcal M to be the collection of all subsets of X. Show that there is a measure m from mathcal M to zero to infinity called counting measure such that for any S subset of X, m of S is the number of elements of S, infinity S is infinite.

Puzzle eleven. Let X be any set and define mathcal M as before. Suppose p is a probability distribution on X, meaning a function p from X to zero to infinity with the sum over i in X of p of i equals one. Show that there is a probability measure m from mathcal M to zero to infinity such that for any

S subset of X, m of S equals the sum over i in S of p of i. In this situation, we usually write p of i as p sub i and call it the probability of the outcome i in X. For any S subset of M we call m of S the probability of the event

S. In the next puzzles, X is any set, mathcal M obeys the three rules for a collection of measurable subsets of X, and m from mathcal M to zero to infinity is a measure.

Puzzle twelve. Show that if S, T in mathcal M then the union S cup T is in mathcal M. Puzzle thirteen. Show that if S, T in mathcal M then the intersection S cap T is in mathcal M. Puzzle fourteen. Show that if S sub i in mathcal M for i equals one, two, and so on then the intersection over i equals one to infinity S sub i is in mathcal M. Puzzle fifteen. Show that if S, T in mathcal M and S subset of T then m of S is less than or equal to m of T. Puzzle sixteen. Show that if S sub i in mathcal M for i equals one, two, and so on then m of the union over i equals one to infinity S sub i is less than or equal to the sum over i equals one to infinity m of S sub i. Puzzle seventeen. Show that if m is a probability measure and S in mathcal M then zero less than or equal to m of S less than or equal to one. One of the main uses of a measure m on a space X is that it lets us integrate certain functions f from X to real numbers. Alas, not all functions! It's only reasonable to try to integrate measurable functions f from X to real numbers, which have the property that if S subset of real numbers is measurable, its inverse image f inverse of S subset of X is measurable. And even measurable functions can cause trouble, because when we try to integrate them we might get positive infinity, negative infinity, or something even worse. For example, what's

The integral from negative infinity to infinity of x squared sine x d x. There's no good answer. We say a function f from X to R is integrable if it is measurable and its integral over X, defined in a certain way I won't explain here, gives a well-defined real number.


## SHANNON ENTROPY: A FIRST TASTE

When you learn an event of probability p has happened, the amount of information you get is negative log p.

Question. Suppose you know a coin lands heads up two-thirds of the time and tails up the rest of the time. What is the average or 'expected' amount of information you get when you learn which side landed up?

Answer. Two-thirds of the time you get negative log two-thirds of information, and the rest of the time you get negative log the rest. So, the expected amount of information you get is negative three times log two-thirds minus three times log the rest.

You can do the same thing whenever you have any number of probabilities that add to one. The expected information is called the Shannon entropy.

You flip a coin. You know the probability that it lands heads up. How much information do you get, on average, when you discover which side lands up? It's not hard to work this out. It's a simple example of 'Shannon entropy'. Roughly speaking, entropy is information that you don't know, that you could get if you did enough experiments. Here the experiment is simply flipping the coin and looking at it.

Puzzle eighteen. Suppose you know a coin lands heads up half the time and tails up the other half of the time. What is the expected amount of information you get from a coin flip? If you use base two for the logarithm, you get the expected information measured in bits. What do you get?

Puzzle nineteen. Suppose you know a coin lands heads up a third of the time and tails up the other two-thirds of the time. What is the expected amount of information you get from a coin flip?

Puzzle twenty. Suppose you know a coin lands heads up a quarter of the time and tails up three-quarters of the time. What is the expected amount of information you get from a coin flip, in bits?

If you solve these you'll see a pattern: the Shannon entropy is biggest when the coin is fair. As it becomes more and more likely for one side to land up than the other, the entropy drops. You're more sure about what will happen, so you learn less, on average, from seeing what happens!

We've been doing examples where your experiment has just two possible outcomes: heads up or down. But you can do Shannon entropy for any number of outcomes. It measures how ignorant you are of what will happen. That is: how much you learn on average when it does!


## SHANNON ENTROPY: A SECOND TASTE

According to the weather report there's a one-fourth chance that it will rain one centimeter, one-half chance it will rain two centimeters, and one-fourth chance it will rain three centimeters.

Question. What is the 'expected' amount of rainfall?

Answer. One-fourth times one plus one-half times two plus one-fourth times three equals two centimeters.

Question. What is the 'expected' amount of information you learn when you find out how much it rains?

Answer. Three-halves minus a fourth log a fourth minus one-half log one-half minus a fourth log a fourth equals three-halves log two, or in other words, three bits. This is the Shannon entropy of the weather report.

If the weather report tells you it'll rain different amounts with different probabilities, you can figure out the 'expected' amount of rain. You can also figure out the expected amount of information you'll learn when it rains. This is called the 'Shannon entropy'.

Shannon entropy is closely connected to information, but we can also think of it as a measure of ignorance. This may seem paradoxical. But it's not. Shannon entropy is the expected amount of information that you don't know when all you know is a probability distribution, which you will know when you see a specific outcome chosen according to this probability distribution.

For example, consider a weather report that says it will rain one centimeter with probability zero, two centimeters with probability one, and three centimeters with probability zero. The Shannon entropy of this weather report is negative zero log zero minus one log one minus zero log zero equals zero since by convention we set p log p equals zero when p equals zero, this being the limit of p natural log p as p approaches zero from above.

What does it mean that this weather report has zero Shannon entropy? It means that when we see a specific outcome chosen according to this probability distribution, we learn nothing! The weather report says it will rain two centimeters with probability one. When this happens, we learn nothing that the weather report didn't already tell us.

The Shannon entropy doesn't depend on the amounts of rain, or even whether the forecast is about centimeters of rain or dollars of income. It only depends on the probabilities of the various outcomes. So Shannon entropy is a universal, abstract concept.

Shannon entropy is closely connected to Gibbs entropy, which was already known in physics. But by lifting entropy to a more general level and connecting it to digital information, Shannon helped jump-start the information age. In fact a paper of his was the first to use the word 'bit'!


## THE DEFINITION OF SHANNON ENTROPY

Suppose you believe there are n possible outcomes with probabilities p one, ... , p n that are greater than or equal to zero that sum to one.

The average amount of information you learn when one of these outcomes happens, chosen according to this probability distribution, is the Shannon entropy:

H equals the sum over i from one to n of negative pi log pi.

Shannon entropy is larger for probability distributions that are more spread out, and smaller for probability distributions that are more sharply peaked.

I've been leading up to it with examples, but here it is in general: Shannon entropy! Gibbs had already used a similar formula in physics-but with base e for the logarithm, an integral instead of a sum, and multiplying the answer by Boltzmann's constant. Shannon applied it to digital information.

Here's where the formula for Shannon entropy comes from. We have some set of outcomes, say X. We have a probability distribution on this set, meaning a function p from X to the interval zero to one such that the sum of pi over all elements of X equals one.

If we have any function A from X to R, we define its expected value to be the sum over all elements i in the set X of pi times Ai.

It's a kind of average of A where each value A(i) is 'weighted', i.e. multiplied, by the probability of the ith outcome. We saw an example in the last tweet: the expected amount of rainfall.

We've seen that if you believe the ith outcome has probability pi, the amount of information you learn if the ith outcome actually occurs is negative log pi. Thus, the expected amount of information you learn is negative log P equals negative pi log pi.

And this is the Shannon entropy! We denote it by H, or more precisely H (p), so

H (p) equals negative pi log pi. In the box above I was taking X to be the set {one, ... , n}. This is often a good thing to do when there are finitely many outcomes.

Let's get to know the Shannon entropy a little better.

Puzzle twenty-one. Let X equals one, two so that we know a probability distribution P on X if we know P sub one, since P sub two equals one minus P sub one. Graph the Shannon entropy H of P as a function of P sub one. Show that it has a maximum at P sub one equals one-half and minima at P sub one equals zero and

P sub one equals one. This makes sense: if you believe P sub one equals one then you learn nothing when an outcome happens chosen according to the probability distribution P: you are sure outcome one will occur, and it does (with probability one). Similarly, if you believe P sub one equals zero you learn nothing when an outcome happens according to this probability distribution, since you are sure outcome two will occur. On the other hand, if P sub one equals one-half, you are maximally undecided about what will happens, and you learn one bit of information when it does.

Puzzle twenty-two. Let X equals one, two, three. Draw the set of probability distributions on X as an equilateral triangle whose corners are the probability distributions (one, zero, zero), (zero, one, zero), and (zero, zero, one). Sketch contour lines of H of P as a function on this triangle. Show it has a maximum at P equals (one-third, one-third, one-third) and minima at the corners of the triangle.

Again this should make intuitive sense. Here is a harder puzzle along the same lines:

Puzzle twenty-three. Let X equals { one, to, n }. Show that H of P has a maximum at P equals (one over n, to, one over n) and minima at the probability distributions where P sub i equals one for some particular i in X. Here is one of the big lessons from all this:

Shannon entropy is larger for probability distributions that are more spread out, and smaller for probability distributions that are more sharply peaked.

Indeed, you can think of Shannon entropy as a measure of how spread out a probability distribution is! The more spread out it is, the more you learn when an outcome occurs, drawn from that distribution.


## THE PRINCIPLE OF MAXIMUM ENTROPY

Suppose there are n possible outcomes. At first you have no reason to think any is more probable than any other.

Then you learn some facts about the correct probability distribution-but not enough to determine it uniquely! Which probability distribution P one, to, P n should you choose?

The principle of maximum entropy says:

H equals negative sum from i equals one to n Pi log pi.

What's Shannon entropy good for? For starters, it gives a principle for choosing the 'best' probability distribution consistent with what you know. Choose the one that maximizes the Shannon entropy!

This is called the 'principle of maximum entropy'. This principle first arose in statistical mechanics, which is the application of probability theory to physics-but we can use it elsewhere too.

For example: suppose you have a die with faces numbered one, two, three, four, five, six. At first you think it's fair. But then you somehow learn that the average of the numbers that comes up when you roll it is five. Given this, what's the probability that if you roll it, a six comes up?

Sounds like an unfair question! But you can figure out the probability distribution on {one, two, three, four, five, six} that maximizes Shannon entropy subject to the constraint that the mean is five. According to the principle of maximum entropy, you should use this to answer my question!

But is this correct?

The problem is figuring out what 'correct' means! But in statistical mechanics we use the principle of maximum entropy all the time, and it seems to work well. The brilliance of E. T. Jaynes was to realize it's a general principle of reasoning, not just for physics.

The principle of maximum entropy is widely used outside physics, though still controversial. But I think we should use it to figure out some basic properties of a gas-like its energy or entropy per molecule, as a function of pressure and temperature.

To do this, we should generalize Shannon entropy to 'Gibbs entropy', replacing the sum by an integral. Or else we should 'discretize' the gas, assuming each molecule has a finite set of states. It sort of depends on whether you prefer calculus or programming. Either approach is okay if we study our gas using classical statistical mechanics.

Quantum statistical mechanics gives a more accurate answer. It uses a more general definition of entropy-but the principle of maximum entropy still applies!

I won't dive into any calculations just yet. Before doing a gas, we should do some simpler examples-like the die whose average roll is five. But I can't resist mentioning one philosophical point. In the box above I was hinting that maximum entropy works when your 'prior' is uniform:

Suppose there are n possible outcomes. At first you have no reason to think any is more probable than any other.

This is an important assumption: when it's not true, the principle of maximum entropy as we've stated it does not apply. But what if our set of events is something like a line? There's no obvious best probability measure on the line! And even good old Lebesgue measure dx depends on our choice of coordinates. To handle this, we need a generalization of the principle of maximum entropy, called the principle of maximum relative entropy.

In short, a deeper treatment of the principle of maximum entropy pays more attention to our choice of 'prior': what we believe before we learn new facts. And it brings in the concept of 'relative entropy': entropy relative to that prior. But we won't get into this here, because we will always be using a very bland prior, like assuming that each of finitely many outcomes is equally likely.


## ADMITTING YOUR IGNORANCE

Suppose you describe your knowledge of a system with n states using a probability distribution P1, . . . , Pn. Then the Shannon information

H equals negative Pi log Pi i equals one measures your ignorance of the system's state.

So, choosing the maximum-entropy probability distribution consistent with the facts you know amounts to not pretending to know more than you do.

Remember: if we describe our knowledge using a probability distribution, its Shannon entropy says how much we expect to learn when we find out what's really going on. We can roughly say it measures our 'ignorance'-though ordinary language can be misleading here.

At first you think this ordinary six-sided die is fair. But then you learn that no, the average of the numbers that come up is five. What are the probabilities P1, . . . , Pn for the different faces to come up?

This is tricky: you can imagine different answers!

You could guess the die lands with five up every time. In other words, P5 equals one. This indeed gives the correct average. But the entropy of this probability distribution is zero. So you're claiming to have no ignorance at all of what happens when you roll the die!

Next you might guess that it lands with four up half the time and six up half the time. In other words, P4 equals P6 equals two. This probability distribution has one bit of entropy. Now you are admitting more ignorance. But how can you be so sure that five never comes up?

Next you might guess that P4 equals P6 equals four and P5 equals two. We can compute the entropy of this probability distribution. It's higher: one point five bits. Good, you're being more honest now! But how can you be sure that one, two, or three never come up? You are still pretending to know stuff!

Keep improving your guess, finding probability distributions with mean five with bigger and bigger entropy. The bigger the entropy gets, the more you're admitting your ignorance! If you do it right, your guess will converge to the unique maximum-entropy solution.

But there's a more systematic way to solve this problem.


## THE BOLTZMANN DISTRIBUTION

Suppose you want to maximize the Shannon entropy negative Pi log Pi i equals one of a probability distribution P1, . . . , Pn, subject to the constraint that the expected value of some quantity Ai is some number c:

PiAi equals C (star) i equals one n

Then try the Boltzmann distribution:

n exp(negative Beta Ai) Pi

Lexp(negative Beta Ai)

If you can find Beta that makes (star) hold, this is the answer you seek!

How do you actually use the principle of maximum entropy?

If you know the expected value of some quantity and want to maximize entropy given this, there's a great formula for the probability distribution that usually does the job! It's called the 'Boltzmann distribution'. In physics it also goes by the names 'Gibbs distribution' or 'canonical ensemble', and in statistics it's called an 'exponential family'.

In the Boltzmann distribution, the probability Pi is proportional to exp(negative Beta A) where A is the quantity whose expected value you know. Since probabilities must sum to one, we must have n exp(negative Beta Ai) i equals one Lexp(negative Beta Ai)

Pi equals

It is then easy to find the expected value of A as a function of the number Beta: just plug these probabilities into the formula

(A) equals Ai Pi i equals one n

The hard part is inverting this process and finding Beta if you know what you want (A) to be.

When and why does the Boltzmann distribution actually work? That's a bit of a long story, so I'll explain it later. First, let's use the Boltzmann distribution to solve the puzzle I mentioned last time:

At first you think this ordinary six-sided die is fair. But then you learn that no, the average of the numbers that come up is five. What are the probabilities P1, . . . , Pn for the different faces to come up? You can use the Boltzmann distribution to solve this puzzle!

To do it, take one is less than or equal to i is less than or equal to six and Ai equals i. Stick the Boltzmann distribution Pi into the formula Ci Ai Pi equals five and get a polynomial equation for exp(negative Beta). You can solve this with a computer and get exp(negative Beta) approximately one point eight seven seven.

So, the probability of rolling the die and getting the number one to six is proportional to exp(negative Beta i) approximately one point eight seven seven. You can figure out the constant of proportionality by demanding that the probabilities sum to one-or just look at the formula for the Boltzmann distribution. You should get these probabilities:

You can compute the entropy of this probability distribution, and you get roughly one point nine seven bits. You'll remember that last time we got entropies up to one point five bits just by making some rather silly guesses.

So, using the Boltzmann distribution, you can find the maximum-entropy die that rolls five on average. Later, we'll see how the same math lets us find the maximum-entropy state of a box of gas that has some expected value of energy!


## MAXIMIZATION SUBJECT TO A CONSTRAINT

To maximize a smooth function F of several variables subject to a constraint on some smooth function G, look for a point where for some number X.

When we're trying to maximize entropy subject to a constraint, we're doing a problem of the above sort. If you don't know how to do problems like this, it's time to learn about Lagrange multipliers. You can find this in any book on calculus of several variables. But the idea is in the picture above. Say we've got two smooth functions f, g: Rn maps to R and we have a point on the surface g equals constant where f is as big as it gets on this surface. The gradient of f must be perpendicular to the surface at this point. Otherwise, we could move along the surface in a way that made f bigger! For the same reason, the gradient of g is always perpendicular to the surface g equals constant. So Vf and Vg must point in the same or opposite directions at this point. Thus, as long as the gradient of g is nonzero, we must have

Vf equals lambda Vg for some number lambda, called a Lagrange multiplier. So, solving this equation along with g equals constant is a way to find the point we're looking for-though we still need to check we've found a maximum, not a minimum or something else.

We can write a formula that means the exact same thing as Vf equals lambda Vg using differentials:

df equals lambda dg

This is what we'll do from now on. Gradients are vector fields while differentials are one-forms. If you don't know what this means, you can probably ignore this for now: the difference, while ultimately quite important, will not be significant for anything we're doing.


## MAXIMIZING ENTROPY SUBJECT TO A CONSTRAINT

To maximize the entropy

H equals negative summation i equals one to n of pi ln pi subject to a constraint on the expected value subject to a constraint on the expected value summation of Ai pi equals c it's good to look for a probability distribution such that dH equals lambda d(A)

for some number lambda. This will then be a Boltzmann distribution:

exp of negative lambda Ai

Pi equals one over the summation of exp of negative lambda Ai

We've seen how to maximize a function subject to a constraint. Now let's do the case we're interested in: maximizing entropy subject to a constraint on the expected value of some quantity.

Suppose we have a finite set of outcomes, say one to n. Our 'quantity' A is just a number A1 to An depending on the outcome. For any probability distribution p on the set of outcomes, we can define its Shannon entropy and the expected value of A:

H equals negative summation i equals one to n of pi ln pi, and expected value of A equals summation i equals one to n of Ai pi.

Here we are using base e for the Shannon entropy, to simplify the calculations. Let's try to find the probability distribution that maximizes H on the surface where the expected value of A equals c. We'll show that if such a probability distribution p exists, and none of the pi are zero, then p must be a Boltzmann distribution

Pi equals exp of negative lambda Ai divided by summation i equals one to n of exp of negative lambda Ai for some lambda in R. If you're willing to trust me on this, you can skip this calculation.

for some \ E R. If you're willing to trust me on this, you can skip this calculation.

To use the method from last time-the Lagrange multiplier method-we'd like to use the probabilities pi as coordinates on the space of probability distributions. But they aren't independent, since summation i equals one to n of pi equals one. To get around this, let's use all but one of the pi as coordinates, and remember that the remaining one is a function of those. Let's use p2, p3, and so on, to pn as coordinates, so that p1 equals 1 minus the summation of p2 and so on to pn. Furthermore, the space of all probability distributions on our finite set is the closed interval from zero to one for all pi where the summation i equals one to n of pi equals one. It looks like a closed interval when n equals two, or a triangle when n equals three, or a tetrahedron when n equals four, or some higher-dimensional version of a tetrahedron when n is larger. In its interior this space looks locally like Rn minus one, so we can use the Lagrange multiplier method, but it also has a boundary where one or more of the pi vanish, and then this method no longer applies. We'll see an example of that later.

So, let's assume p is a probability distribution maximizing the Shannon entropy H on the surface where the expected value of A equals c, and also suppose p has p1 to pn greater than zero. Suppose that not all the values Ai are equal, since that makes the problem too easy see why? Then the expected value of A is never zero, so from what I said last time, we must have dH equals lambda d(A)

at the point p. So let's see what this equation actually says.

Since

H equals negative summation i equals one to n of pi ln pi we have dH equals negative summation i equals one to n of (1 plus ln pi) dpi.

Similarly, since expected value of A equals summation i equals one to n of Ai pi we have d(A) equals summation i equals one to n of Ai dpi.

So, our equation dH equals lambda d(A) says that negative (1 plus ln pi) dpi equals lambda summation i equals one to n of Ai dpi.

For these to be equal, the coefficients of dpi must agree for each of our coordinates p2 to pn. But we have to remember that p1 equals one minus the summation of p2 to pn and thus dp1 equals negative of the summation of dp2 to dpn. Thus, for each i from 2 to n we have

(1 plus ln p1) minus (1 plus ln pi) equals lambda times (negative A1 plus Ai)

and fiddling around we get exp of negative lambda times A1 divided by exp of negative Ai times P1 equals Pi.

This says something cool: the probabilities pi are proportional to the exponentials exp of negative lambda Ai. And since the probabilities must sum to one, it's obvious what the constant of proportionality must be: pi equals the exp of negative lambda Ai divided by the summation i equals one to n of exp of negative lambda Ai. So yes: pi must be given by the Boltzmann distribution!

In summary, we've seen that if there exists a probability distribution p that maximizes the Shannon entropy among probability distributions with expected value of A equals c, and if all the pi are positive, then p must be a Boltzmann distribution. But this raises other questions. When does such a probability distribution exist? If it exists, is it unique? And what if not all the pi are positive?

In what follows we'll dive down this rabbit hole and get to the bottom of it. I'll just state some facts-you may enjoy trying to see if you can prove them. First, there exists a probability distribution p1 to pn with expected value of A equals c if and only if

A sub min is less than or equal to C is less than or equal to A sub max where A sub min is the minimum value and A sub max is the maximum value of the numbers from A sub one to A sub N. Second, whenever

A sub min is less than C is less than A sub max, there exists a unique probability distribution from P sub one to P sub N maximizing Shannon entropy subject to the constraint expectation of A equals C. Third, this unique maximizer P has P sub I greater than zero for all I, and is thus a Boltzmann distribution, whenever

A sub min is less than C is less than A sub max. When C equals A sub min, the unique maximizer assigns the same probability P sub I to each outcome I with A sub I equals A sub min, while P sub I equals zero for all other outcomes. Similarly, when C equals A sub max, the unique maximizer assigns the same probability P sub I to each outcome I with A sub I equals A sub max, while P sub I equals zero for all other outcomes.

It's good to look at an example:

Puzzle twenty-four. Suppose there are only two outcomes, with A sub one equals negative one and A sub two equals one. Work out the Boltzmann distribution P maximizing Shannon entropy subject to the constraint expectation of A equals C for negative one is less than less than one. Show that as lambda approaches positive infinity this Boltzmann distribution has

P sub one approaches one, P sub two approaches zero while as lambda approaches negative infinity it has

P sub one approaches zero, P sub two approaches one. Show the probability distribution P sub one equals one, P sub two equals zero maximizes Shannon entropy subject to the constraint expectation of A equals negative one, while P sub one equals zero, P sub two equals one maximizes it subject to the constraint expectation of A equals one. Show these two probability distributions are not Boltzmann distributions.


## THERMAL EQUILIBRIUM

Suppose a system has finitely many states I equals one, two, up to N with energies E sub j. If the probability P sub I that it's in the ith state maximizes entropy subject to a constraint on its expected energy:

expectation of E equals sum from I equals one to N of P sub I times E sub I

we say it is in thermal equilibrium. In this case P sub I is given by a Boltzmann distribution

P sub I equals greater than exp of negative E sub I

at least if all the probabilities P sub I are positive.

Don't worry: the substance of what I'm saying here is almost the same as in the last box. I'm merely attaching new words to the concepts, to make them sound more like physics:

Before I said we had a set of N 'outcomes' numbered one, two, up to N. Now I'm talking about 'states'. If we have a system with N states, it means there are N outcomes when we do a measurement to completely determine which state it's in. A 'state' is some way for a physical system to be that's vague but it's all we can say until we consider some specific kind of system. In classical physics the states form a set, usually infinite but sometimes finite.

Before I said we had a 'quantity' A that depends on the outcome, taking the value A sub I in the ith outcome. Now I'm calling this quantity the 'energy' E. Energy is a particularly interesting quantity in physics, so we'll focus on that, without demanding that you know anything about it: for our present purposes, we can take any quantity and dub it 'energy'.

Before I called the Lagrange multiplier. Now I'm calling it Beta, because that's what physicists do in this particular context.

When a system maximizes entropy subject to a constraint on the expected value of its energy, and perhaps also some other quantities, we say the system is in thermal equilibrium. This is meant to suggest that an object just sitting there, not heating up or cooling down, is often best modeled this way.

You may have noticed the annoying clause "at least if all the probabilities P sub I are positive". I only said that because I cannot tell a lie. In Puzzle twenty-four we saw that as Beta goes to infinity, the Boltzmann distribution can converge to a non-Boltzmann probability distribution where some of the probabilities P sub I vanish. This still counts as thermal equilibrium, because it's still maximizing entropy subject to a constraint on expected energy. We'll learn more about this when we study the concept of 'absolute zero'.


## COOLNESS

If a probability distribution P sub I maximizes entropy subject to a constraint on the expected value of the energy E sub j, then

P sub I is proportional to exp of Beta times E sub I

where Beta is the coolness, inversely proportional to temperature. So:

The cooler a system is, the less likely it is to be in a high-energy state!

Say a system with finitely many states maximizes entropy subject to a constraint on the expected value of some quantity E that we choose to call 'energy'. Then its probability of being in the ith state is proportional to exp(-BE;) for some number.

When B is big and positive, the probability of being in a state of high energy is tiny, since exp(-BE;) gets very small for large energies Ej. This means our system is cold.

Conversely when B is small and positive, exp(-BE;) drops off very slowly as the energy Ej gets bigger. So, high-energy states become quite likely when B is small and positive. This means our system is hot.

It turns out B is inversely proportional to the temperature more about that later. But in modern physics B is just as important as temperature. It comes straight from the principle of maximum entropy!

So B deserves a name. And its name is 'coolness'.

By the way, the formula

Pi exp(BEi)

is only strictly true when B is finite. There's also a limiting case B approaches positive zero, when pi equals zero except for states of the very lowest energy. And there's a limiting case B approaches negative zero, where Pi equals zero except for states of the very highest energy. I'll say a bit about these oddities later. First I'll say more about what coolness has to do with temperature.


## COOLNESS VERSUS TEMPERATURE

Coolness B is inversely proportional to temperature T:

where k is Boltzmann's constant.

Coolness is measured in joules to the negative one, temperature is measured in kelvin, and Boltzmann's constant is a conversion factor:

k equals one point three eight zero six four nine times ten to the negative twenty-third joules per kelvin.

In statistical mechanics, coolness is inversely proportional to temperature. But coolness has units of energy to the negative one, not temperature to the negative one. So we need a constant to convert between coolness and inverse temperature! And this constant is very interesting.

Remember: when a system maximizes entropy with a constraint on its expected energy, the probability of it having energy E is proportional to exp(-BE) where B is its coolness. But we can only exponentiate dimensionless quantities! So B has dimensions of one over energy.

Since coolness is inversely proportional to temperature, we must have B equals one over kT where k is some constant with dimensions of energy per temperature. This constant k is called 'Boltzmann's constant'. It's tiny:

k equals one point three eight zero six four nine times ten to the negative twenty-third joules per kelvin.

This is mainly because we use units of energy, joules, suited to macroscopic objects like a cup of hot water. Boltzmann's constant being tiny reveals that such things have enormously many microscopic states!

Later we'll see that a single classical point particle, in empty space, has energy three kT divided by two when it's maximizing entropy at temperature T. The three here is because the atom can move in three directions, the one half because we integrate x squared to get this result. The important part is kT. The kT says: if an ideal gas is made of atoms, each atom contributes just a tiny bit of energy per kelvin, or degree Celsius: roughly ten to the negative twenty-third joules. So a little bit of gas, like a gram of hydrogen, must have roughly ten to the twenty-third atoms in it. This is a very rough estimate, but it's a big deal.

Indeed, the number of atoms in a gram of hydrogen is about six times ten to the twenty-third. You may have heard of Avogadro's number-this is quite close to that. So Boltzmann's constant gives a hint that matter is made of atoms-and even better, a nice rough estimate of how many per gram!

Later we will see that Boltzmann's constant has another important meaning: it's a fundamental unit of entropy, a nat, expressed in joules per kelvin.


## TEMPERATURE

If a system has finitely many states with energies Ei, in thermal equilibrium at temperature T the probability that it's in the ith state is Pi proportional to exp(-Ei/kT).

where k is Boltzmann's constant and T can be positive, negative, or even infinite.

T equals infinity.

T is less than zero.

T is greater than zero.

A system with finitely many states can be pretty weird. It can have negative temperature! Even weirder: as you heat it up, its temperature becomes large and positive, then it reaches infinity, and then it 'wraps around' and becomes large and negative.

The reason: coolness is more fundamental than temperature. The coolness B is inversely proportional to the temperature T:

B equals one over kT.

When the temperature goes up to infinity and then suddenly becomes a large negative number, it's really just the coolness going down to zero and becoming negative. Temperatures 'wrap around' infinity, as shown in the picture.

A system with finitely many states can have negative or infinite temperature because in thermal equilibrium, its probability of being in the ith state is exp(-BEi) divided by the sum from i equals one to n of exp(-BEi)

Pi where Ei is the energy of the ith state, and this makes sense for any B in the reals. Moreover, the probability pi depends continuously on B, even as B passes through zero. This means a large positive temperature is almost like a large negative temperature!

But the circle of temperature can be misleading. Temperatures wrap around T equals infinity but not T equals zero. A system with a small positive temperature is very different from one with a small negative temperature! That's because pi for B much greater than zero is very different than it is for B less than zero.

For a system with finitely many states we can take the limit of the Boltzmann distribution when B approaches positive zero; then the system will only occupy its lowest-energy state or states. We can also take the limit when B approaches negative infinity; then the system will only occupy its highest-energy state or states. In terms of temperature, this means that the limit where T approaches zero from above is very different than the limit where T approaches zero from below.

So, for a system with finitely many states, the best picture of possible thermal equilibria is not a circle of temperatures but a closed interval of coolness: the coolness B can be anything in the interval from negative infinity to positive infinity, which topologically is a closed interval. In terms of coolness, positive zero is different from negative zero, but approaching zero from above is the same as approaching it from below. But in terms of temperature, approaching zero from above is different from approaching zero from below, while a temperature of positive infinity is the same as a temperature of negative infinity.

Now, if all this seems very weird, here's why: we often describe physical systems using infinitely many states, with a lowest possible energy but no highest possible energy. In this case the sum in the Boltzmann distribution can't converge for B less than zero, so negative temperatures are ruled out.

However, some physical systems can be approximately described using a finite set of states (or in quantum theory, a finite-dimensional Hilbert space of states). Then the things I just said hold true! And people enjoy studying these systems, and their strange properties, in the lab.

It's good to look at a simple example, and work everything out explicitly:

Puzzle twenty-five. Suppose a system has two states with energies E one and E two. Compute the probabilities pi that it is in either of these states in thermal equilibrium as a function of the coolness B. Then express these probabilities as a function of the temperature T. Using these functions pi of T:

Show that when zero is less than T is less than positive infinity the system is more likely to be in the lower-energy state: P one of T is greater than P two of T.

. Show that when negative infinity is less than T and T is less than zero the system is more likely to be in the higher-energy state: P one of T is less than p two of T.

· Show that

T approaches positive infinity, limit pi of T equals limit pi of T as T approaches negative infinity so we can speak unambiguously of the probabilities pi at infinite temperature.

· Show that at infinite temperature the system has an equal probability of being in either state.

· Show that as T approaches zero from above, the probability of the system being in the lower energy state approaches one.

· Show that as T approaches zero from below, the probability of the system being in the higher energy state approaches one.


## INFINITE TEMPERATURE

If a system has finitely many states with energies E i, in thermal equilibrium at temperature T the probability that it's in the i-th state is

Pi is proportional to e to the power of B times E i where B equals one over k times T and k is Boltzmann's constant.

When B equals zero the system's temperature becomes infinite, and all states become equally probable!

The probability of finding a system in a particular state decays exponentially with energy when the coolness beta is positive. But for a system with finitely many states, beta can be zero. Then it becomes equally probable for the system to be in any state!

Zero coolness means 'utter randomness': that is, maximum entropy.

Here's why. The probability distribution with the largest entropy is the one where all probabilities pi are all equal. This happens at zero coolness! When beta equals zero we get exp of negative B times Ei equals one for all i. The probabilities pi are proportional to these numbers exp of negative beta times Ei equals one, so they're all equal.

It seems zero coolness is impossible for a system with infinitely many states. With infinitely many states, all equally probable, the probability of being in any state would be zero. In other words, there's no uniform probability distribution on an infinite set.

One way out: replace sums with integrals. For the usual measure on zero to one, called the Lebesgue measure dx, we have the integral from zero to one of dx equals one. So this is a 'probability measure' that we could use to describe a system at zero coolness, whose space of states is zero to one.

But replacing sums by integrals raises all sorts of interesting issues. For example, there's a unique way to sum over a finite set of states, but an integral over an infinite set of states depends on a choice of measure. So a choice of measure is a significant extra structure we're slapping on our set of states.

We'll need to think about these issues later, since to compute the entropy of a classical ideal gas we'll need integrals. But we'll encounter difficulties, which are ultimately resolved using quantum mechanics.

Anyway: infinite temperature is really zero coolness, and at least for systems with finitely many states, the entropy becomes as large as possible at zero coolness.


## NEGATIVE TEMPERATURE

If a system has finitely many states with energies E i, in thermal equilibrium at temperature T the probability that it's in the i-th state is p i is proportional to e to the power of negative beta E i, where beta equals one over k times T and k is Boltzmann's constant.

When beta is less than zero the system becomes 'hotter than infinitely hot'. Its temperature is negative, but the higher the energy of a state, the more probable it is!

A system with finitely many states can reach infinite temperature. It can get even hotter, but then its temperature 'wraps around' and becomes negative!

The possibility of negative temperatures was first discussed by the physicist Lars Onsager in nineteen forty-nine, and they have been created in the lab with a variety of systems that-within some approximation-can be described as having finitely many states. In quantum theory, this happens for systems that have finite basis of 'energy eigenstates': states with well-defined energies E i. For example, the nucleus of an atom may have just two spin states, and if we put it in a magnetic field these will have different energies. The result is the system we studied in Puzzle twenty-five.

Here is a generalization with more energy states, all equally spaced:

Puzzle twenty-six. Consider a system with two N plus one states labeled by an integer n with negative N less than or equal to n and n less than or equal to N, where the nth state has energy E n equals alpha n for some energy alpha greater than zero. Compute the Boltzmann distribution for this system at coolness beta for all beta in the set of real numbers. Compute the expected energy E as a function of beta. What is the qualitative difference in your result between the case of positive temperature beta greater than zero and negative temperature beta less than zero. For more, try this:


## ABSOLUTE ZERO: THE LIMIT OF INFINITE COOLNESS

If a system with finitely many states having energies E i is in thermal equilibrium, the probability p i that it's in the i-th state is proportional to exp of negative beta E i where beta is the coolness.

In the limit of infinite coolness, beta approaches positive infinity, these probabilities go to zero except for the states of lowest energy, which all become equally probable.

The limit beta approaches positive infinity is also the limit where T approaches zero from above, commonly called absolute zero.

The limit where T approaches zero from above is often called absolute zero. Why? First people made up various temperature scales like Celsius, where zero was the freezing point of water, and Fahrenheit, where zero is the freezing point of a mixture of water, ice, and ammonium chloride. But researchers discovered that nature had a more fundamental concept of zero temperature: the limit of infinite coolness! This happens as the temperature approaches negative two hundred seventy-three point one five degrees Celsius, or roughly negative four hundred fifty-nine point six seven degrees Fahrenheit. This discovery led Kelvin to propose a shifted version of Celsius where zero is absolute zero. This was originally called 'absolute Celsius', but now it is called the Kelvin scale. This is the scale of temperature I'll always use here. The size of the degrees is a somewhat arbitrary convention, but the zero is not: it's absolute zero.


## THE HAGEDORN TEMPERATURE

If a system has a countable infinity of states N equals one, two, three, etc. with energies E sub N, the Boltzmann distribution

P sub N equals the fraction with exp left parenthesis negative E sub N over k T right parenthesis in the numerator and the sum from N equals one to infinity exp left parenthesis negative E sub N over k T right parenthesis in the denominator is either:

One, defined for all

Zero less than T less than positive infinity. Two, undefined for all

Zero less than T less than positive infinity. Three, defined for all zero less than T less than T sub H but not for T sub H less than T less than positive infinity, where T sub H is some temperature called the Hagedorn temperature.

We've been discussing systems with finitely many states, but many physical systems have a countable infinity of states. So let's think a bit about those. We can copy everything we've done so far, but we have to be careful. For thermal equilibrium to be possible at some temperature T, we need the Boltzmann distribution

P sub N equals the fraction with exp left parenthesis negative E sub N over k T right parenthesis in the numerator and the sum from N equals one to infinity exp left parenthesis negative E sub N over k T right parenthesis in the denominator to make sense. But it might not. Sometimes the sum fails to converge! This happens when the terms exp left parenthesis negative E sub N over k T right parenthesis don't go to zero fast enough as

N approaches positive infinity. Let's investigate this issue. We'll assume that

The sum from N equals one to infinity exp left parenthesis negative E sub N over k T right parenthesis converges for some T greater than zero. Then the energies E sub N must be bounded below: otherwise the terms exp left parenthesis negative E sub N over k T right parenthesis will get bigger and bigger. Furthermore for any E in the real numbers there can be at most finitely many E sub N less than E: otherwise we'd be adding up infinitely many terms greater than exp left parenthesis negative E over k T right parenthesis. As a result, we can reorder the states so their energies are nondecreasing:

E sub one less than or equal to E sub two less than or equal to E sub three less than or equal to dot dot dot and

E sub N approaches positive infinity. Reordering a sum can't change its convergence or value if fits gamma s a sum of nonnegative numbers, like the sum we have here. So we might as well assume we've listed the energies in nondecreasing order as above. Then there are two cases:

One. The energies E sub N approach positive infinity so fast that the sum from N equals one to infinity exp left parenthesis negative E sub N over k T right parenthesis converges for all zero less than T less than positive infinity. Then our system can be in thermal equilibrium at any finite positive temperature. This is the nicest situation, and the one we typically expect.

Two. The energies E sub N approach positive infinity slowly enough that the sum from N equals one to infinity exp left parenthesis negative E sub N over k T right parenthesis converges when T is small enough, but not otherwise. In this case there is some temperature T sub H, called the Hagedorn temperature, such that our system can be in thermal equilibrium at positive temperatures T below T sub H, but not above

T sub H. In both cases, the sum from N equals one to infinity exp left parenthesis negative E sub N over k T right parenthesis diverges for all negative infinity less than or equal to T less than zero and T equals positive infinity. So, for a system with a countable infinity of states, if thermal equilibrium exists for some positive temperature, it cannot exist for negative or infinite temperatures.

The second case is weird and interesting. It's named after Rolf Hagedorn, who in nineteen sixty-four noticed that this was a possibility in nuclear physics. He considered a model of nuclear matter where the energies E sub N approach plus infinity in a roughly logarithmic way. As you heat it, its expected energy keeps increasing, but its temperature can never exceed T sub H. This model turned out to be incorrect, but it is interesting anyway.

Now let's solve some puzzles on systems with a countable infinity of states. Some of these show up in quantum mechanics, but you don't need to know quantum mechanics to do these puzzles.

Puzzle twenty-seven. Show that for a system with a countable infinity of states, if thermal equilibrium is possible for some negative temperature, it is impossible for positive or infinite temperatures.

Puzzle twenty-eight. Work out the Boltzmann distribution when E sub N equals N E for some energy E, and show that it is well-defined for all temperatures zero is less than T which is less than plus infinity. The next puzzle is a lot like the previous one a bit more messy, but worthwhile because of its great importance in physics.

Puzzle twenty-nine. For a system called the quantum harmonic oscillator of frequency omega we have E sub N equals N plus one-half times h-bar omega, where h-bar is the reduced Planck's constant. Work out the Boltzmann distribution in this case, and show it is well-defined for all temperatures zero is less than T which is less than plus infinity. Puzzle thirty. For a system called the primon gas we have E sub N equals E ln N for some energy E. Show that the Boltzmann distribution is well-defined for small enough positive temperatures, but there is a Hagedorn temperature. Give a formula for the Boltzmann distribution in terms of the Riemann zeta function:

zeta of s equals the sum from N equals one to infinity of N to the power of negative s. You can show that for the primon gas the sum of the N equals one to infinity of exp of negative E sub N over k T diverges at the Hagedorn temperature. But it can go the other way, too:

Puzzle thirty-one. Find energies E sub N with a Hagedorn temperature such that the sum from N equals one to infinity of exp of negative E sub N over k T converges at the Hagedorn temperature.

Various other strange things can happen, as you should expect when dealing with infinite series. For example, it's possible that the Boltzmann distribution is well-defined at some temperature but the expected value of the energy is infinite! But I'll resist the lure of these rabbit holes and turn to something much more important: systems with a continuum of states. We will need to get good at these to compute the entropy of hydrogen. Now our sums become integrals, and various new things happen.


## THE FINITE VERSUS THE CONTINUOUS

THE FINITE


## THE CONTINUOUS

You can switch from finite sums to integrals in the definition of entropy, and we'll need to do this to compute the entropy of hydrogen. But be careful: a bunch of things change!

We need to switch from finite sums to integrals when we switch from a finite set of states to a measure space of states. I'll illustrate the ideas with the real line, R. We define a probability distribution on R to be an integrable function p: R -> [zero, zero) with

Such a probability distribution has a Gibbs entropy given by

S(p) equals negative k integral from zero to infinity of p(x) ln p(x) dx.

We can also define Shannon entropy, where we leave out Boltzmann's constant k and use whatever base we want for the logarithm:

H (p) equals negative integral from zero to infinity of p(x) log p(x) dx.

I should warn you that many writers reserve the term 'Shannon entropy' only for a sum

H (p) equals negative sum of pi log pi.

While that convention has advantages, I want to use the term 'Shannon entropy' to signal that I'm leaving out the factor of k.

Unlike the entropy for a probability distribution on a finite set, the entropy of a probability distribution on R can be negative! This is disturbing. Earlier I said that the Shannon entropy of a probability distribution is the expected amount of information you learn when an outcome is chosen according to that distribution. How can this be negative?

The answer is that this interpretation of entropy, valid for probability distributions on a finite or even a countably infinite set, is not true in the continuous case! We have to adapt our intuitions.

Look at an example. Let Pe be the probability distribution on R given by

P(x) equals zero otherwise.

For small e it's a tall thin spike near zero. Let's work out its Shannon entropy: I(p) equals negative p(x) log p(x) dx equals negative integral from e to one over e of log one over e dx equals log e.

We're just integrating a constant here, so it's easy. When e equals one the entropy is zero, and when e becomes smaller than one the entropy becomes negative!

Why? We need a distance scale to define the entropy of a probability distribution on the real line. If I measure distance in centimeters, I'll think the entropy of a probability distribution is bigger than you, who measures it in meters. And if I measure it in kilometers, I'll think the entropy is smaller-and possibly even negative.

Let's see how this works. If I measure distance in different units from you, my coordinate y on the real line will not equal your coordinate x: instead we'll have y equals c times x for some c greater than zero. Then my probability distribution, say q, will have q(y) dy equals q(c x) dx equals c q(x) dx so we must have q(c x) equals p(x) over c to make this integral equal one. In other words, stretching out a probability distribution must also flatten it out, making it less 'tall'-and its entropy increases. Indeed:


## Puzzle thirty-two. Show that H(q) equals H(p) plus ln c.

Thanks to this formula choosing zero less than c less than one compresses a probability distribution and makes it taller, reducing its entropy. Inevitably, this can make the entropy negative if c is small enough.

In summary: in the continuous case, entropy is not invariant under reparametrizations: our choice of coordinates matters! And this can make entropy negative. This applies not only to R but many other measure spaces we'll be considering, like R. This issue will be very important.

After learning this, it should be less of a shock that the entropy of a probability distribution on R can be infinite, or even undefined:

Puzzle thirty-three. Find three probability distributions p on the real line that have entropy plus infinity, minus zero, and undefined because it's of the form plus infinity minus infinity.


## ENTROPY, ENERGY AND TEMPERATURE

Suppose a system has some measure space X of states with energy E : X maps to R. In thermal equilibrium the probability distribution on states, p: X maps to R, maximizes the Gibbs entropy S equals negative k times the integral of p of x times the natural log of p of x dx subject to a constraint on the expected value of energy: the expected value of E equals the integral of p of x times E of x dx

Typically when this happens p is the Boltzmann distribution e to the power of negative E of x divided by kT dx where T is the temperature and k is Boltzmann's constant.

Then as we vary the expected value of E we have


## d of the expected value of E equals T dS

We can now generalize a lot of our work from a finite set of states to a general measure space. I won't redo all the arguments, just state the results and point out a couple of caveats.

For any measure space X we say a function p: X maps to [zero, infinity) is a probability distribution if it's measurable and the integral of p of x dx equals one.

We can define a version of Shannon entropy for p by

H equals negative the integral of p of x times the log of p of x dx,

but physicists mainly use the Gibbs entropy, defined by

S equals negative k times the integral of p of x times the natural log of p of x dx.

As I warned you last time, this can take values in [negative infinity, infinity], though we are mainly interested in cases when it's finite. If we think of X as the space of states of some system, we can pick any measurable function E : X maps to R and call it the 'energy'. Its expected value is then the expected value of E equals the integral of E of x times p of x dx at least when this integral converges.

We say the probability distribution p describes thermal equilibrium if it maximizes S subject to a constraint of the expected value of E equals c. Typically when this happens p is a Boltzmann distribution p of x equals one divided by Z times e to the power of negative beta times E of x dx where beta is called the coolness. I say 'typically' because even when X is a finite set, we saw in Puzzle twenty-four that there can be thermal equilibria that are not Boltzmann distributions, but only limits of Boltzmann distributions as beta approaches positive infinity or negative infinity. This can also happen for other measure spaces X. I will not delve into this, because my goal now is to get to some physics.

As before, we can write beta equals one over kT, at least if beta is not zero, and then write the Boltzmann distribution as

X times e to the power of negative E of x divided by kT dx p of x equals

Also as before, the Boltzmann distributions obey the crucial relation dH equals beta times the differential of the expected value of E.

Rewriting this in terms of Gibbs entropy S equals kH and temperature T equals one divided by k beta, it becomes this famous relation between temperature, entropy and the expected energy: TdS equals the differential of the expected value of E.

Notice that the units match here. The Shannon entropy H is dimensionless, but since k has units of energy per temperature, the Gibbs entropy S equals kH has units of energy per temperature. Thus TdS has units of energy, as does the differential of the expected value of E.


## THE CHANGE IN ENTROPY

As we change the temperature of a system from T one to T two while keeping it in thermal equilibrium, the change in its entropy is

S of T one minus S of T zero equals the integral from T zero to T one of the differential of the expected value of E divided by T

where the expected value of E is its expected energy at temperature T.

Last time we saw that as we change the expected energy of E of a system while keeping it in thermal equilibrium, this fundamental relation holds:

TdS equals the differential of the expected value of E.

We can rewrite this as


## dS equals the differential of the expected value of E divided by T

and then integrate this from one temperature to another-remember, as the expected energy changes, so does the temperature. We get the integral from T zero to T one of the differential of the expected value of E divided by T equals S of T one minus S of T zero.

This is the main way people do experiments to 'measure entropy'. Slowly heat something up, keeping track of how much energy it takes to increase its temperature each little bit. Using this data you can approximately calculate the integral at left and that gives the change in entropy!

This is the main way people do experiments to 'measure entropy'. Slowly heat something up, keeping track of how much energy it takes to increase its temperature each little bit. Using this data you can approximately calculate the integral at left and that gives the change in entropy!

But so far we're just measuring changes in entropy. How can you figure out the actual value of the entropy? One way is to assume the Third Law of Thermodynamics, which says that in thermal equilibrium the entropy approaches zero as the temperature approaches zero from above. This gives the integral from T zero to T one of the differential of the expected value of E divided by T equals S of T

This is how people often 'measure the entropy' of a system in thermal equilibrium. They heat it up starting from absolute zero, very slowly so they hope it is close to thermal equilibrium at every moment-and they take data on how much energy is used, and approximately calculate the integral at left!

But this relies on the Third Law of Thermodynamics. So where does that come from?


## THE THIRD LAW OF THERMODYNAMICS

If a system has countably many states, with just one of lowest energy, and thermal equilibrium is possible for this system for some temperature T greater than zero, then its entropy in thermal equilibrium approaches zero as T approaches zero from above:

the limit as T approaches zero from above of S of T equals zero

Some people say the Third Law of Thermodynamics this way: "entropy is zero at absolute zero". But it's not really that simple indeed, other people say it's impossible to reach absolute zero. Above I've stated a version of the Third Law that's actually a theorem. Let's prove it!

Actually, let's prove it now for systems with only finitely many states. It'll be easier to handle systems with a countably infinite number of states later, when we've developed more tools. And by the way, we'll see the Third Law isn't always true for systems with a continuum of states. It will fail for all three of the problems on our big to-do list: the classical harmonic oscillator, the classical particle in a box and the classical ideal gas. This is often taken as a failure of classical mechanics, since switching to quantum mechanics makes the Third Law hold for these systems.

Let's show that for a system with finitely many states i = one, and so on, with energies Ei, as the temperature T approaches zero from above, the entropy of the system in thermal equilibrium approaches k ln N where N is the number of lowest-energy states. In thermal equilibrium

Pi xe negative Ei divided by kT.

Thus, all states with the lowest energy have the same probability, while as the temperature approaches zero from above, any higher-energy states have pi approaching zero. So, as the temperature approaches zero from above, the probability of the system being in any one of its N lowest-energy states approaches one divided by N, and we get as T approaches zero from above, the limit of S(T) equals the negative summation from i equals one to N of k times pi times ln pi.

ln N equals k ln N.

In particular, if the system has just one lowest-energy state, we get the Third Law of Thermodynamics:

the limit of S(T) as T approaches zero equals zero.

Here T approaching zero from above means that T is approaching zero from above.

But beware: for systems with lots of lowest-energy states, their entropy in thermal equilibrium can be large even near absolute zero! Also, a related problem: systems may take a ridiculously long time to reach equilibrium! This is especially true for systems that have many states whose energies are very near the lowest energy, like a piece of glass. You can put a piece of glass in a fancy refrigerator and try to cool it to near absolute zero. If it has one lowest-energy state, its entropy should approach zero. If this happened, the glass would change from glass to a crystal, which has less entropy. But nobody has seen glass turn into a crystal when they cool it down. If this happens, it probably does so only after an absurdly long time, much longer than the age of the Universe. This phenomenon is called 'frustration'. People like to argue about frustration and the Third Law, so I am not trying to give you the final word here, just alert you to the issue. You can learn a bit more here:

By the way: for systems with finitely many states, it's possible to have negative temperatures, and the Third Law has a counterpart saying what happens when the temperature approaches zero from below:


## Puzzle thirty-four. Show that for a system with finitely many states,

the limit of S(T) as T approaches zero equals k ln M

where M is the number of states of highest energy.

However, most systems we'll be studying won't have a state of highest energy.


## MEASURING ENTROPY

If we assume the entropy of a system approaches zero as T approaches zero from above, we have the integral from zero to T sub one of d average E over T equals S of T sub one. Using this assumption, we can do experiments to measure the entropy of different substances at standard temperature and pressure:

· iron: approximately five bits per atom

· water: approximately twelve bits per molecule

· hydrogen: approximately twenty-three bits per molecule

People actually do experiments and use the above formula to figure out the entropy of many substances in thermal equilibrium assuming their entropy vanishes as the temperature approaches absolute zero. They slowly heat up a substance and keep track of how much energy is needed to raise its temperature as they go, so they can approximately calculate the integral shown. They usually report the answers in joules per kelvin per mole, but I enjoy 'bits per molecule'.

As you can see, liquids tend to have more entropy than solids, and gases tend to have even more. My goal in this course is to teach you how to approximately compute some of these entropies from first principles. Unfortunately the only substances that are simple enough for us to handle are gases.

This is a good opportunity to explain some conventions. A mole is defined to be exactly six point zero two two one four zero seven six times ten to the twenty-third; this is called Avogadro's number, and it's close to the number of hydrogen atoms in a gram. A joule per kelvin of Gibbs entropy corresponds to about seven point two four two two nine seven times ten to the twenty-second nats of Shannon entropy: the number here is the reciprocal of Boltzmann's constant, which is defined to be exactly one point three eight zero six four nine times ten to the negative twenty-third joules per kelvin. A bit is ln two nats. From these three facts, we see one joule per kelvin of Gibbs entropy per mole corresponds to about zero point one seven three five one six bits per molecule of Shannon entropy.

By the way, what is 'standard temperature and pressure'? Annoyingly, this phrase means different things to different organizations. I will try to always use it to mean a temperature of two hundred ninety-eight point one five kelvin and a pressure of one bar. The temperature here equals twenty-five degrees Celsius, which seems a bit random compared to zero degrees Celsius - but convenient, because it's close to room temperature. A pressure of one bar, or more officially one hundred kilopascals, is slightly less than a 'standard atmosphere', which is a unit of pressure intended to equal the average air pressure at sea level. A pascal is an official SI unit: it's a pressure of one newton per square meter.


## THE EQUIPARTITION THEOREM

Suppose the energy of a system with n degrees of freedom is a positive definite quadratic form E from R to R, for example

E of x equals the summation from i equals one to n of C_i times x_i squared divided by two.

C_i is greater than zero.

Then in thermal equilibrium at temperature T, the expected value of the energy is average E equals n k T divided by two.

where k is Boltzmann's constant.

Temperature is very different from energy. But sometimes, not very often, but sometimes, the expected energy of a system in thermal equilibrium is proportional to its temperature. The equipartition theorem says this happens when the energy depends quadratically on several real variables, defining a positive definite quadratic form on R. For example, it happens for a classical harmonic oscillator.

Some people get confused and try to apply the equipartition theorem where it doesn't apply. They foolishly conclude that temperature is always proportional to energy.

This theorem does not apply to quantum systems. Indeed, when people tried to apply the equipartition theorem to a mirrored box of light they ran into a problem called the ultraviolet catastrophe. Classically the box of light is a system where the energy is a positive definite quadratic form, but n equals zero, so they got an infinite expected value of the energy! Quantum mechanics saves the day and makes the answer finite.


## Radiation

Visible

The equipartition theorem also doesn't apply to classical systems unless the energy is quadratic. So it's very limited in its applicability, but still useful.

Let's prove this result! To prove a theorem, you have to understand the definitions. We'll start with some background.


## THE EQUIPARTITION THEOREM-BACKGROUND

Suppose the energy of a system with n degrees of freedom is some function E from R to R

Let k be Boltzmann's constant. Suppose p from R to R is a probability distribution maximizing the entropy

S equals negative k times the integral over R of p(x) ln p(x) d"x subject to a constraint on the expected energy average E equals the integral over R of E(x)p(x) d"x.

Then p must be a Boltzmann distribution:

p of x equals e to the power of - B E(x) divided by the integral over R of e to the power of - B E(x) d"x p(x) equals for some number B greater than zero.

The temperature T is defined so that B equals one divided by kT.

We're defining entropy with an integral now, unlike a sum as before, and sticking Boltzmann's constant into the definition of entropy, as physicists do, so that entropy has units of energy over temperature.

Given the formula for the energy E as a function on R^n, we'll have to find the Boltzmann distribution and then compute the expected energy as a function of temperature.


## PROOF OF THE EQUIPARTITION THEOREM: One

Special case: a system with one degree of freedom where the energy E : R -> R is E of x equals x squared over two.

The Boltzmann distribution is e to the power of negative B x squared over two p of x equals so the expected energy is integral from negative infinity to infinity r squared e to the power of negative B x squared over two

B x squared e to the negative B x squared over two dx e to the power of negative B x squared over two dx the expected energy equals the integral from negative infinity to infinity of E of x times p of x dx e to the power of negative B x squared over two dx so doing a substitution with u squared equals B x squared:

the expected energy equals one hundred e to the power of negative u squared over two du u squared e to the power of negative u squared over two du since integral of e to the power of negative u squared over two du equals negative infinity to infinity u squared e to the power of negative u squared over two du equals the square root of pi over two

We'll do two special cases before proving the general result. First let's do a system with one degree of freedom where the energy is E of x equals x squared over two. In this case, after a change of variables, the Gibbs distribution becomes a Gaussian with mean zero and variance one, and that gives the desired result. Or just do the integrals and see what you get! The expected energy is one half k T.


## PROOF OF THE EQUIPARTITION THEOREM: Two

More general case: a system with n degrees of freedom where the energy E: R^n > R is F of x equals the norm of x squared over two

We can reduce this to the case with one degree of freedom:

the expected energy equals R^n two T

e to the power of negative B the norm of x squared over two dn x e to the power of negative B the norm of x squared over two dn x

J integral over R^n

Next we do a system with n degrees of freedom where the energy is a sum of n terms of the form x squared over two. It's no surprise that each degree of freedom contributes one half k T to the expected energy, giving the expected energy equals five n k T

But make sure you follow my calculation above. I skipped a couple of steps!


## PROOF OF THE EQUIPARTITION THEOREM: Three

General case: a system with n degrees of freedom where the energy E : R^n to R is any positive definite quadratic form. Then

E of x equals one half the norm of A x squared for some invertible n by n matrix A . When A is a diagonal matrix this gives

E of x equals the sum from i equals one to n of c sub i x sub i squared over two for positive c sub i. We can reduce the general case to the previous case by a change of variables y equals A x

Q of x equals the sum from i,j equals one to n of q sub i j x sub i x sub j for some numbers q sub i j in R. We say it's positive definite if x not equal to zero implies Q of x greater than zero. One can prove that a quadratic form Q : R^n to R is positive definite if and only if

Q of x equals one half the norm of A x squared for some invertible n by n matrix A . The factor of one half here is just to make our calculations easier.

Thanks to this, if we have a system whose space of states is R^n and its energy function E : R^n to R is a positive definite quadratic form, we can compute the expected energy equals the integral over R^n E of x times the exponential of negative beta E of x d x divided by the integral over R^n of the exponential of negative beta E of x d x by reducing it to the previous case using a change of variables. We get the expected energy equals one half n k T

So, each degree of freedom still contributes one half k T to the expected energy. That's the equipartition theorem!

But be careful. The equipartition theorem doesn't apply when the energy is an arbitrary function of n variables. It also fails when we switch from classical to quantum statistical mechanics.

People sometimes memorize the conclusion of the equipartition theorem, E equals two n k T, without learning that it holds only for classical systems whose energy is a positive definite quadratic form. These people sometimes get fooled into thinking expected value of E is always proportional to T. Some of these poor benighted souls go around saying that temperature is just a measure of energy per degree of freedom. This completely ignores the subtlety of the concept of temperature.

As we've seen, the truly general relation between temperature and energy, for systems in thermal equilibrium, also involves entropy:

T d S equals d E.


## THE AVERAGE ENERGY OF AN ATOM

Since an atom of helium gas can move in three directions, and its energy depends quadratically on its velocity and not on position, the equipartition theorem says that classically its expected energy should be

Expected value of E equals negative k T two thirds where T is temperature and k is Boltzmann's constant, about one point three eight times ten to the negative twenty-third joules per kelvin.

So, heating an atom of helium gas one degree Celsius should take

This is very close to the truth.

We can finally start reaping the rewards of all our thoughts about entropy! The equipartition theorem lets us estimate how much energy it takes to heat up one atom of helium one degree Celsius. And it works!

Of course we don't heat up an individual atom: we heat up a bunch. A mole of helium is about six point zero two times ten to the twenty-third atoms, so heating up a mole of helium one degree Celsius equals one kelvin should take about six point zero two times ten to the twenty-third times two point zero seven times ten to the negative twenty-third approximately twelve point four six joules

And this is very close to correct! It seems the experimentally measured answer is twelve point six joules.

What are the sources of error? Most importantly, our calculation neglects the interaction between helium atoms. Luckily this is very small at standard temperature and pressure. We're also neglecting quantum mechanics. Luckily for helium this too gives only small corrections at standard temperature and pressure.

It's important here that helium is a monatomic gas. In hydrogen, which is a diatomic gas, we get extra energy because this molecule can tumble around, not just move along. We'll try that next.


## THE ENERGY OF HYDROGEN

If we treat a molecule of hydrogen as a dumbbell whose position takes three numbers and whose axis takes two numbers to describe, we can try to use the equipartition theorem to estimate its expected energy as

Expected value of E equals negative k T five where T is temperature and k equals one point three eight times ten to the negative twenty-third joules per kelvin.

In this approximation, heating a molecule of hydrogen gas one kelvin takes

In reality it takes three point three nine times ten to the negative twenty-third joules at standard temperature and pressure. Not bad!

A molecule of hydrogen gas is a blurry quantum thing, but let's pretend it's a classical solid dumbbell that can move and tumble but not spin around its axis. Then it has three plus two equals five degrees of freedom, and we can use the equipartition theorem to estimate its energy.

For T significantly less than six thousand kelvin, hydrogen molecules don't vibrate with the two atoms moving toward and away from each other. They don't spin around their axis until even higher temperatures. But they tumble like a dumbbell as soon as T exceeds about ninety kelvin.

We need quantum mechanics to compute these things. But at room temperature and pressure, we can pretend a hydrogen gas is made of classical solid dumbbells that can move around and tumble but not spin around their axes! In this approximation the equipartition theorem tells us expected value of E equals five k T.

This is fine as far as it goes-but our goal in this course is to compute the entropy of hydrogen. We'll start with a useful warmup: the classical harmonic oscillator.


## ENTROPY OF THE HARMONIC OSCILLATOR ONE

A classical harmonic oscillator has energy equals p squared k g squared divided by two m where q is its position, p its momentum, m its mass and « its spring constant.

By the equipartition theorem, in thermal equilibrium at temperature T it has expected energy expected value of E equals k T where k is Boltzmann's constant.

So, using d E equals T d S, its entropy is

S equals J a s minus J a equals k absolute value minus k open parenthesis log

Since this does not approach zero as T approaches zero from above, the Third Law of Thermodynamics doesn't hold for the classical harmonic oscillator.

But what is this constant C? For that we must think harder.

What's the entropy of a classical harmonic oscillator in thermal equilibrium? Using the equipartition theorem and the formula d E equals T d S, we can show it's

So, the entropy grows logarithmically with temperature. And it does not go to zero as T approaches zero: instead, it goes to negative infinity. So the Third Law of Thermodynamics does not hold for the classical harmonic oscillator!

That may seem shocking, but it actually makes sense. The Third Law holds only for certain special systems. Furthermore, we've seen that the entropy of a sharply peaked probability distribution on a continuous state space is negative. We'll see that the Boltzmann distribution for the classical oscillator gets more and more sharply peaked near q equals p equals zero as the temperature approaches zero from above. So in fact, it makes perfect sense that the entropy approaches negative zero.

However, the classical harmonic oscillator is just an approximation to the quantum harmonic oscillator, which does obey the Third Law. It's a good approximation at high temperatures, but bad at low temperatures. In fact, this business of negative entropies at low temperature is not something that happens in the real world. It's just a defect of classical mechanics. It's trying to tell us that quantum mechanics is better.

Another point: you'll have noticed that constant C here. What is it? We can make progress with a bit of dimensional analysis. The quantity ln T is a funny thing: if we change our units of temperature, it doesn't get multiplied by a constant factor, the way physical quantities usually do. It changes by adding a constant! So k log T doesn't have dimensions of entropy. But must have dimensions of entropy. The constant C must somehow save the day! How does that work? Let's see.


## ENTROPY OF THE HARMONIC OSCILLATOR TWO

Classically, a harmonic oscillator at temperature T has entropy

S equals K open parenthesis L N T plus C close parenthesis. Writing C equals negative L N T sub zero for some constant T sub zero, this gives S equals K L N open parenthesis T over T sub zero close parenthesis. Dimensional analysis implies T sub zero must have units of temperature!

But what is this temperature T sub zero? For that we must think harder.

The formula S equals K open parenthesis L N T plus C close parenthesis is a bit scary from the viewpoint of dimensional analysis. We usually avoid working with the logarithm of a dimensionful quantity, like L N T, because it transforms in a funny way when we change our units. But if we write C equals negative L N T sub zero then we get S equals K L N open parenthesis T over T sub zero close parenthesis, and we see the solution to our problem! If T sub zero has units of temperature, then T over T sub zero is dimensionless, so L N open parenthesis T over T sub zero close parenthesis doesn't change at all when we change our units. In other words: now L N open parenthesis T over T sub zero close parenthesis is dimensionless, so S equals K L N open parenthesis T over T sub zero close parenthesis has units of entropy as it should.

So, the constant C must equal negative L N T sub zero for some temperature T sub zero that we can compute for any harmonic oscillator. What is it? We could just compute it. But it's more fun to use dimensional analysis.

What could it depend on? Obviously the mass M, the spring constant K and Boltzmann's constant K. But there's no way to form a quantity with units of temperature from just M, K and K. So we need an extra ingredient.

And we've seen this already: to define the entropy of a probability distribution on the Q, P plane and get something with the right units, we need a quantity with units of action! The obvious candidate is Planck's constant H, and this is actually right. The entropy we're after is given by an integral with respect to D P D Q over H where H equals H over two pi. So the temperature T sub zero can depend on H as well as M, K and K.

We can compute a quantity with units of temperature from M, K, K and H. The frequency of our oscillator is omega equals the square root of K over M, and it's a famous fact that H omega has units of energy. K has units of energy over temperature ... so H omega over K has units of temperature!

Thus, our temperature T sub zero must be H omega over K times some dimensionless purely mathematical constant, which I'll call one over A. A must be something like seven or two, or if we're really unlucky, E six six six - though in practice we usually get numbers fairly close to one, not huge or tiny numbers.

So, the entropy of a classical harmonic oscillator must be

S equals K L N open parenthesis A K T over H omega close parenthesis.

This is far as I can get without breaking down and doing some real work. Later we will compute Q.


## Entropy of the harmonic oscillator: three

We've seen a classical harmonic oscillator with frequency omega has entropy

S equals K L N open parenthesis A K T over H omega close parenthesis when it's in thermal equilibrium at temperature T.

Here K is Boltzmann's constant, H is Planck's constant,

and A is some dimensionless mathematical constant. We'll figure it out later.

Even though we don't know A, this formula is already very interesting! K T is known to be the typical energy scale of thermal fluctuations at temperature T. H omega is the spacing between energy levels of a quantum harmonic oscillator with frequency omega. The ratio K T over H omega is therefore roughly the number of energy eigenstates in which we may find a quantum harmonic oscillator with high probability when it's at temperature T.

Thus, S is roughly K times the logarithm of the number of states that we're likely to find a quantum harmonic oscillator in, when it's at temperature T. This may seem mysterious. After all, we weren't trying to do quantum mechanics, much less count quantum states. But there are other examples of this pattern, where the entropy of a classical system in thermal equilibrium at temperature T is roughly K times the logarithm of the number of quantum states that are accessible at temperature T.

We'll learn a bit more about this later, when we relate entropy to something called the 'partition function', which can be understood as the 'number of accessible states'. This viewpoint will also explain the constant Q. But now let's calculate this constant.


## Entropy of the harmonic oscillator: four

A classical harmonic oscillator has energy

P, Q equals two plus K G squared over two M

where P is its momentum, Q its position, M its mass and K its spring constant.

At temperature T, the probability density of its momentum and position is the Boltzmann distribution:

E to the negative B E open parenthesis P, Q close parenthesis P open parenthesis P, Q close parenthesis equals integral E to the negative B E open parenthesis P, Q close parenthesis D P D Q over H

where B equals one over K T, K is Boltzmann's constant, and H equals two pi H is the original 'unreduced' Planck's constant.

The oscillator's entropy at temperature T is thus integral P open parenthesis P, Q close parenthesis L N P open parenthesis P, Q close parenthesis D P D Q over H

S equals negative K integral L N open parenthesis P open parenthesis P, Q close parenthesis over zero close parenthesis.

Last time we found a formula for the entropy of a classical harmonic oscillator ... which includes a mysterious purely mathematical dimensionless constant Q. Now let's figure out A.

We'll grit our teeth and actually do the integral needed to calculate the entropy-but only in one easy case! Combining this with our formula, we'll get A.

First, recall the basics. The energy E open parenthesis P, Q close parenthesis of our harmonic oscillator at momentum P and position Q determines its Boltzmann distribution at temperature T, which I'll call P open parenthesis P, Q close parenthesis now since the letter P is already being used. Integrating negative P L N P using the measure D P D Q over H we get the Shannon entropy. In physics we multiply this by Boltzmann's constant K to get the Gibbs entropy.


## Entropy of the harmonic oscillator: five

We can choose units of length, time, mass and temperature to make a classical harmonic oscillator's mass M, its spring constant K, Boltzmann's constant K and Planck's constant H all equal one.

Then at T equals one the Boltzmann distribution of the oscillator is

E to the negative open parenthesis P squared plus Q squared close parenthesis over two

P open parenthesis P, Q close parenthesis equals integral E to the negative open parenthesis P squared plus Q squared close parenthesis over two D P D Q equals E to the negative open parenthesis P squared plus Q squared close parenthesis over two so its entropy is S = negative integral e to the power of negative open parenthesis p squared plus two close parenthesis over two ln open parenthesis e to the power of negative open parenthesis p squared plus two close parenthesis over two close parenthesis d p d q negative zero zero negative zero zero.

Let's do this integral!

Let's compute the Boltzmann distribution p(p, q) and the entropy S. To keep the formulas clean, we'll work in units where m equals K equals k equals h equals one, and compute everything at one special temperature: T equals one.

In this setup h equals twenty-seven, and e to the power of negative B E (p,q) equals e to the power of negative open parenthesis p squared plus q squared close parenthesis over two is a beautiful Gaussian with integral integral e to the power of negative open parenthesis p squared plus q squared close parenthesis over two equals twenty-seven pi.

These two factors of twenty-seven cancel when we compute the denominator of the probability distribution p(p, q):

d p d q twenty-seven pi twenty-seven pi equals one.

Thus, we get simply p(p,q) equals e to the power of negative open parenthesis p squared plus q squared close parenthesis over two.

The entropy of the harmonic oscillator is thus d p d q when K equals k equals h equals T equals one. Next let's do this integral.

S equals negative e to the power of negative open parenthesis p squared plus two close parenthesis over two ln open parenthesis e to the power of negative open parenthesis p squared plus two close parenthesis over two close parenthesis negative infinity negative zero zero.


## ENTROPY OF THE HARMONIC OSCILLATOR: six

When m equals k equals k equals h equals T equals one the entropy of a classical harmonic oscillator is integral integral e to the power of negative open parenthesis p squared plus q squared close parenthesis over two ln open parenthesis e to the power of negative open parenthesis p squared plus q squared close parenthesis over two close parenthesis d p d q.

S equals integral from zero to one hundred e to the power of negative r squared over two r d r d theta open parenthesis switching to polar close parenthesis equals one hundred fifty-two plus one-half r c.

(doing the integral)

equals integral u e to the power of negative u d u.

(substituting u equals r squared over two)

equals one.

Now let's do the integral to compute the entropy of the harmonic oscillator. We copy a famous trick for computing the integral of a Gaussian. First we switch to polar coordinates in the p q plane, where r squared equals p squared plus q squared and d p d q equals r d r d theta.

Then we integrate with respect to theta, which cancels out the factor of one-half pi. Then we do a substitution u equals r squared over two. But for us r squared over two is minus the logarithm of the Gaussian:

minus open parenthesis p plus zero squared over two close parenthesis equals one.

so we're left with

S equals integral u e to the power of negative u d u.

which we can do with integration by parts.

After all this work, we get an incredibly simple answer:

S equals one.

So in the special case where m equals K equals k equals h equals T equals one, the entropy of a classical harmonic oscillator in thermal equilibrium is one.

Now let's return to the general case, and finish the job.


## ENTROPY OF THE HARMONIC OSCILLATOR: seven

A classical harmonic oscillator with frequency w has entropy

S equals k ln open parenthesis a k T over h w close parenthesis.

for some dimensionless constant alpha.

But when m equals K equals k equals h equals T equals one we have w equals one and S equals one, so we must have and thus finally k T over h w plus one.

S equals k ln open parenthesis k T over h w plus one close parenthesis.

Knowing the entropy in one special case, we can figure out the constant a in our general formula for the entropy. Our general formula says

S equals k ln open parenthesis a k T over h w close parenthesis.

But when m equals k equals T equals h equals one we get w equals k over m equals one, and we saw last time that in this special case we get

S equals one.

So a must equal e.

Thus, the entropy of an oscillator with frequency w at temperature T is

S equals k ln open parenthesis e k T over h w close parenthesis equals k k open parenthesis ln open parenthesis A T close parenthesis plus one close parenthesis.

The extra one here is fascinating to me. If we had slacked off, ignored the possibility of a dimensionless constant alpha, and crudely used dimensional analysis to guess S approximately the way people often do, we might have gotten

S equals k ln open parenthesis k T over h w close parenthesis.

This would be off by one nat.

What does the one extra nat mean? It seems pretty mysterious now. But later we'll understand it! I already mentioned that often entropy is roughly k times the logarithm of something called the 'number of accessible states'. But that formula is not exactly right: there's also an extra term related to energy, and that accounts for the one extra nat here. Be patient, and you'll see what I mean.


## WHERE ARE WE NOW?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure?

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

equals A N V N plus three ln K I plus seven including the mysterious constant y.

The subgoal: compute the entropy of a single classical particle in a one-dimensional box.

The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator:

S equals k ln open parenthesis k T plus one close parenthesis.

Okay, so we've gotten somewhere! By doing the right integral, we've figured out that the entropy S of a classical harmonic oscillator of frequency w in thermal equilibrium at temperature T is

S equals k open parenthesis k T plus one close parenthesis.

where k is Boltzmann's constant and h is Planck's constant.

We could compute the entropy of a single particle in a box the same way, and also the entropy of a classical ideal diatomic gas. But the integrals get a bit hairy, so people prefer to use a clever trick called the 'partition function'. It's definitely worth learning. It's not merely a clever trick, it gives new insights on the relation between entropy, energy and temperature. So let's talk about it.


## THE PARTITION FUNCTION

If a system has a set of states X with measure d x and its energy is a function E from X to R, its partition function is

Z of B equals integral e to the power of negative B E of x d x.

where beta is the coolness.

I want to compute the entropy of a particle in a box, and ultimately the entropy of a box of hydrogen. We could do it directly, but that's a bit ugly. It's better to use the 'partition function'. This amazing function knows everything about statistical mechanics. From it you can get the entropy-and much more!


## THE PARTITION FUNCTION AND THE BOLTZMANN DISTRIBUTION

If a system has a set of states X with measure d x and its energy is E from X to R, in thermal equilibrium at coolness beta its probability distribution of states is the Boltzmann distribution:

p(x) equals S x e to the power of negative B E of x d x e to the power of negative B E of x equals e to the power of negative B E of x over Z of B.

where Z of B equals integral e to the power of negative B F of x d x is its partition function.

In fact we've already seen the partition function: it's the thing you have to divide e to the power of negative B E of x by to get a function whose integral is one. And that function whose integral is one is the Boltzmann distribution: the probability distribution of states in thermal equilibrium at coolness. So the partition function is a humble normalizing factor! And yet we'll see that it's incredibly powerful. It's kind of surprising.

Like Lagrangians in classical mechanics, it's fairly easy to use partition functions, but it's harder to understand what they 'really mean'. We will try. But first let's see how to use them.

sixty-five.


## THE PARTITION FUNCTION KNOWS ALL!

If a system has partition function

Z of B equals integral e to the power of negative B E of x d x then in thermal equilibrium at coolness beta its expected energy is

E equals negative one ln Z and its entropy is k open parenthesis ln Z minus B d ln Z close parenthesis.

Here's how you can compute the expected energy E and the entropy S of any system starting from its partition function Z as a function of the coolness beta. I'll show you why these formulas are true, and then we'll test them out on the harmonic oscillator, where we have already computed the expected energy and entropy by other methods.

sixty-six


## THE PARTITION FUNCTION KNOWS THE EXPECTED ENERGY

If a system has partition function Z equals the integral of E(x) exp(-beta E(x)) dx, then the derivative of the natural log of Z with respect to beta equals the integral over x of the derivative of E(x) exp(-beta E(x)) divided by Z.

the integral over x of E(x) exp(-beta E(x)), divided by the integral over x of exp(-beta E(x)).

the integral over x of exp(-beta E(x)) dx equals the expected value of E

In short, the expected energy is the derivative of the natural log of Z with respect to beta

The partition function is all-powerful! For starters, if you know the partition function of a physical system, you can figure out its expected energy. The expected energy is minus the derivative of the natural log of Z with respect to the coolness beta equals one over k T.

How do we show this? Easy: just look at the calculation above! We get a fraction, which is the expected value of E with respect to the Gibbs distribution.

By the way, this trick of taking the derivative of the logarithm of a function is famous: it's called a 'logarithmic derivative'. Notice that f prime of x divided by f of x

Thus the logarithmic derivative says how fast a function is growing compared to the value of the function itself-like the interest rate in compound interest.


## THE PARTITION FUNCTION KNOWS THE ENTROPY

If a system has Boltzmann distribution p(x) equals exp(-beta E(x)) divided by Z, where Z equals the integral over x of exp(-beta E(x)) dx,

then its entropy in thermal equilibrium is

S equals negative k times the integral over x of p(x) natural log of p(x) dx, which equals negative k times the integral over x of p(x) natural log of exp(-beta E(x)) divided by Z dx.

equals k times the integral over x of p(x) natural log Z plus beta E(x) dx.

equals k natural log Z plus beta times the expected value of E.

But since the expected value of E equals negative the derivative of the natural log of Z, this gives

S equals k natural log Z minus beta times the derivative of the natural log of Z with respect to beta.

The entropy is a bit more complicated. But don't be scared! The Boltzmann distribution p(x) is a fraction, so the log of this fraction breaks into two parts:

the natural log of p(x) equals the natural log of exp(-beta E(x)), minus the natural log of Z, which equals negative the natural log of Z plus beta E(x).

Thus our integral for entropy breaks into two parts:

S equals negative k times the integral over x of p(x) natural log p(x) dx, which equals k times the integral over x of p(x) natural log Z dx plus k times beta times the integral over x of p(x) E(x) dx.

The first part is just k natural log Z since the integral of p(x) is one. The second part is k times beta times the expected value of E. If we use what we just learned about the expected value of E:

the expected value of E equals negative the derivative of the natural log of Z.

we get this formula for entropy in terms of the partition function:

This formula seems hard to understand at first. To extract its inner meaning, we need a new concept: 'free energy'.


## sixty-eight

THE PARTITION FUNCTION KNOWS THE FREE ENERGY

To maximize entropy while holding expected energy constant, you can just minimize the free energy

F equals the expected value of E minus T S. We've seen the expected value of E equals negative the derivative of the natural log of Z with respect to beta and S equals k times the natural log of Z minus beta times the derivative of the natural log of Z with respect to beta.

so with beta equals one over k T, a little algebra shows

F equals negative the natural log of Z.

We can understand the relation between entropy, energy and the partition function if we bring in a concept I haven't mentioned yet: the free energy

F equals the expected value of E minus T S.

Since we know formulas for the expected value of E and S in terms of the partition function, we can work out a formula for F. And it's really simple! Much simpler than S, for example. It's just

F equals negative the natural log of Z.

But what's the meaning of free energy? Remember: to maximize the Shannon entropy H subject to a constraint on expected energy, we introduced the Lagrange multiplier beta equals one over k T and maximized the quantity H minus beta times the expected value of E. But if you multiply this quantity by negative k T, you get free energy:

negative k T times the quantity H minus beta times the expected value of E, which equals the expected value of E minus T S, which equals F.

So, as long as T is greater than zero, maximizing entropy subject to a constraint on expected energy is equivalent to minimizing free energy!

Thus, free energy turns a problem of maximizing entropy subject to a constraint into a minimization problem without a constraint. The point is not that we've turned maximization into minimization: that's just an arbitrary business with signs. The point is that free energy lets us stop thinking about the constraint.

There's a huge amount to say about the free energy, which is also called the 'Helmholtz free energy', since there are other kinds. You can think of T S as the amount of energy in useless random form, since it comes from entropy. Since the expected value of E is the total expected energy, F equals the expected value of E minus T S is the amount of 'useful' energy. More precisely, the free energy is the maximum amount of work obtainable from a system at a constant temperature. But showing this would take us out of our way.


## THE PARTITION FUNCTION KNOWS ALL: REVISITED

If Z is the partition function of a system, in thermal equilibrium at coolness beta, its expected energy is the expected value of E equals negative the derivative of the natural log of Z

and its free energy is

F equals negative the natural log of Z

We can compute its entropy from these using

F equals the expected value of E minus T S and we get

S equals k natural log Z minus the derivative of natural log of Z with respect to beta.

Now we can tell a simpler story, which is easier to remember. Free energy, being the energy in useful form, is the expected energy minus the useless energy, which is temperature times entropy. Thus

F equals the expected value of E minus T S.

so

S equals the expected value of E minus F divided by T.

equals k beta times the quantity negative F plus the expected value of E.

and using our formulas for F and the expected value of E in terms of the partition function Z, we get

S equals k natural log Z minus beta times the derivative of natural log of Z.

The story here is more of a mnemonic than a true explanation, because I'm not saying much what it means for energy to be 'useful' or 'useless'. I've only given this hint: when a system is in thermal equilibrium, its free energy is minimized. For more on the meaning of free energy, try a good book on thermodynamics, like this:

Right now I'd rather say a bit about the meaning of the partition function.


## THE MEANING OF THE PARTITION FUNCTION

Say X is a set where each point i has an 'energy' E; E R. Its partition function is

Z equals De-exp negative BEi IEX.

where B E R is the coolness.

The partition function counts the points of X but it counts points with large energy less, since they're less likely to be 'occupied'.

If ß equals one over kT, points with energy E; much greater than kT count for very little.

But as T approaches positive infinity, all points get fully counted and Z approaches the cardinality of X. In physics we call Z the number of accessible states.

Say we have a system with some countable set of states X. In thermal equilibrium at temperature T, the probability that the system is in its ith state is proportional to exp of negative BE;, where E; is the energy of that state and ß is the coolness. Thus, physicists say the partition function

Z equals sum over i EX of exp negative BEi.

is the number of accessible states: roughly, the number of states the system can easily be in at temperature T, where ß equals one over kT.

This is a funny thing to say, because being 'accessible' is not a yes-or-no matter. A more precise statement is that the partition function counts states weighted by their accessibility exp negative ßE;. States whose energy is low compared to kT are highly accessible, or probable, because exp negative BE; is close to one if E; is less than kT. States of high energy are more inaccessible, or improbable, since exp negative BE; is close to zero if E; is much greater than kT.

Calling the partition function the 'number of accessible states' emphasizes how it generalizes the cardinality of X, meaning its number of points. Let's make this precise! Let's call a set X with a function E: X to R an energetic set. I will write it merely as X, so you need to remember it comes with an energy function. I will call its partition function Z of X:

Z of X equals sum over i EX of exp negative BEi.

If X is finite we don't have to worry about the convergence of this sum. My main message is this:

The partition function Z of X does for energetic sets what the cardinality of X does for sets.

For example, just like the cardinality, the partition function adds when you take disjoint unions, and multiplies when you take products! Let's see why.

Puzzle thirty-five. The disjoint union X plus X prime of energetic sets E from X to R and E prime from X prime to R is again an energetic set: for points in X we use the energy function E, while for points in X prime we use the function E prime. Show that the partition function obeys the law Z of X plus X prime equals Z of X plus Z of X prime, at least for finite energetic sets.

Puzzle thirty-six. The cartesian product X cross X prime of energetic sets E from X to R and E prime from X prime to R is again an energetic set: define the energy of (x, x prime) in X cross X prime to be E(x) plus E(x prime). This is how it really works in physics. Show that the partition function obeys the law Z of X cross X prime equals Z of X multiplied by Z of X prime, at least for finite energetic sets.

Puzzle thirty-seven. Show that if X is a finite energetic set, its partition function Z of X approaches its cardinality of X as T approaches positive infinity.

The key virtue of cardinality is that two sets are isomorphic that is, there exists a one-to-one and onto function between them if and only if they have the same cardinality. This generalizes to energetic sets if we use the partition function instead of the cardinality! Let's say two energetic sets with energy functions E from X to R and E prime from X prime to R are isomorphic if there is a one-to-one and onto f from X to X prime which is compatible with their energy functions, meaning

E prime of f(x) equals E(x)

for all x in X.

Puzzle thirty-eight. Show that two finite energetic sets are isomorphic if and only if they have the same partition function. Hint: the key is to show that the functions exp of negative E over kT for various energies E in R are linearly independent. As a step toward this, show that a finite linear combination can only be zero if ci equals zero for the smallest energy Ej.

Puzzle thirty-nine. Make up a category of energetic sets, where morphism are maps that are compatible with their energy functions. Prove that it is a category.

Puzzle forty. Show the disjoint union of energetic sets is the coproduct in this category. Puzzle forty-one. Show that what I called the cartesian product of energetic sets is not the product in this category.

Puzzle forty-two. Show that what I called the 'cartesian product' of energetic sets gives a symmetric monoidal structure on the category of energetic sets. So we should really write it as a tensor product X tensor X prime, not X cross X prime.

Puzzle forty-three. Show this tensor product distributes over coproducts: X tensor (Y plus Z) is isomorphic to X tensor Y plus X tensor Z.

We can go even further and define not only a partition function for energetic sets, but also an expected energy, free energy, and entropy, using the formulas we've seen earlier. These obey a bunch of rules like this:

Puzzle forty-four. Define the entropy of an energetic set by

S of X equals k times ln of Z of X plus B times ln of Z of X.

Show that

S of X tensor Y equals S of X plus S of Y.

seventy-two.

Entropy comes in two parts.

The entropy of a system in thermal equilibrium is always the sum of two parts:

One. The free energy part:

negative F over T equals k ln Z.

This is Boltzmann's constant times the logarithm of the number of accessible states.

Two. The expected energy part:

(E) over T.

This equals ln(kT) if the system has n degrees of freedom and its energy is a positive definite quadratic form.

Before we dive into examples, it's good to think one last time about the entropy of a system in thermal equilibrium. We've seen that this entropy is always the sum of two parts, which we could call the free energy part negative F over T and the expected energy part (E) over T. But there are various ways to think about this. One is simply that it follows from F equals (E) minus TS: the free energy is the expected energy minus the useless energy. But here is another way to think about it.

In his early work, Boltzmann said the entropy of a system is k times the logarithm of the number of states it can occupy. This is true if all these states are equally probable. But typically some states are more probable than others. We could try to address this by replacing the number of states with the number of accessible states

Z equals sum over i EX of exp negative BEi.

Here we count states weighted by their accessibility exp negative BE;. If we try to follow Boltzmann's prescription with this adjustment we get k ln Z equals F over T. This is the free energy part of the entropy.

In many situations this is close to the true entropy. But this clearly can't be all there is to it. After all, suppose we add the same constant c to the energy of each state. Then the probability of each state in thermal equilibrium is unchanged, so the entropy must stay the same! But the accessibility of each state gets multiplied by exp negative ßc, so we have to subtract kfc from the free energy part of the entropy. There must be some compensating term and this is the expected energy part of the entropy, (E) over T. When we add c to the energy of each state, this goes up by c over T equals kBc.

Thus, in thermal equilibrium we can think of entropy as k times the log of the number of accessible states, 'corrected' so that the result doesn't change when we add a constant to the energy of every state.


## THE POWER OF THE PARTITION FUNCTION

A classical harmonic oscillator with mass m and spring constant k has energy p, q) = twelve plus K g squared over two m.

K g squared.

Its partition function is d p d q h.

Z beta equals the integral from zero to infinity of e to the negative beta E of p,q.

where beta is coolness and h is Planck's constant.

From this we can find its expected energy and free energy in thermal equilibrium:

F equals negative one times the natural log of Z.

The expected value of E equals negative the partial derivative of the natural log of Z with respect to beta.

and then its entropy:

S equals the expected value of E minus F over T where T is temperature: beta equals one over k T where k is Boltzmann's constant.

To test the power of the partition function, let's use it to figure out the entropy of a classical harmonic oscillator. Here's the game plan. First we'll compute the partition function by doing the integral in bright red. Then we'll use it to compute the oscillator's expected energy and free energy. Then we'll subtract those and divide by temperature to get the entropy.

In fact, we've already worked out the answer to this problem:

S equals k times the natural log of beta h over two pi T plus one.

Our earlier approach led to some cool insights. But it was 'tricky', not systematic. The partition function method is systematic, so it's good for harder problems. It will also give new insight into that pesky plus one.

When we compute the entropy using a partition function, all the pain is concentrated at one point: computing the partition function! So let's get that over with.


## HARMONIC OSCILLATOR: PARTITION FUNCTION

A classical harmonic oscillator has energy E(p, q) equals p squared plus k g squared over two and frequency omega equals the square root of K over m, so its partition function is

V m equals the square root of m.

the integral from zero to infinity of e to the negative beta r squared over two r d r d theta.

(switching to polar)

u equals r squared over two.

equals one over beta h omega.

The partition function equals one over beta h omega.

Z beta equals one over beta h omega.

beta h omega.

For the harmonic oscillator, the partition function is the integral of a Gaussian in two variables. A change of variables makes the Gaussian 'round', and then we use polar coordinates to do the integral.

The physicist Kelvin is said to have written

The integral from negative infinity to infinity of e to the negative x squared d x equals the square root of pi.

on the blackboard and said "A mathematician is one to whom that is as obvious as that twice two makes four is to you." I find that rather obnoxious, but when I heard the story as a kid, I made damn sure I knew how to do this integral. The usual trick is to compute the square of this integral using polar coordinates.

Now we're seeing something interesting. The harmonic oscillator, whose energy depends quadratically on two degrees of freedom, is physically more important than a system whose energy depends quadratically on just one degree of freedom. And when beta equals h equals omega equals one, the partition function of the harmonic oscillator is the integral from negative infinity to infinity of e to the negative x squared d x d y equals the integral from zero to infinity of r times e to the negative r squared over two d r d theta equals two pi times one over two equals pi.

which is more fundamental than the integral Kelvin wrote down.


## HARMONIC OSCILLATOR: EXPECTED ENERGY

A classical harmonic oscillator has partition function

Z equals beta h omega.

so its expected energy in thermal equilibrium is

The expected value of E equals negative the partial derivative of the natural log of Z with respect to beta.

The expected value of E equals k T.

just as the equipartition theorem says it must be!

Once we know the partition function of the classical harmonic oscillator, it's easy to compute its expected energy: just use

The expected value of E equals negative the partial derivative of the natural log of Z with respect to beta.

and get

The expected value of E equals negative the partial derivative of the natural log of beta h omega with respect to beta.

beta equals one over k T.

We can also figure this out using the equipartition theorem. Remember, the equipartition theorem applies to a classical system whose energy is quadratic. If it has n degrees of freedom, then at temperature T it has

The expected value of E equals k T.

Our harmonic oscillator has n equals two, so we get the expected value of E equals k T. Good, this matches the partition function approach!


## HARMONIC OSCILLATOR: FREE ENERGY

A classical harmonic oscillator has partition function

Z beta equals one over beta h omega.

so its free energy in thermal equilibrium is

F equals negative the natural log of Z equals negative the natural log of one over beta h omega

F equals negative k T natural log of beta h omega.

equals one over beta h omega.

The partition function lets us do more! It lets us compute the free energy, too, using

F equals negative k T natural log of Z.

Unlike the expected energy, the free energy involves Planck's constant:

F equals negative k T natural log of beta h omega.

Note k T and h omega both have units of energy, so k T over h omega is dimensionless, which is good because we're taking its logarithm. Also note that the free energy is negative at high temperatures! That may seem weird, but it turns out to be good when we compute the entropy.


## HARMONIC OSCILLATOR: ENTROPY

In thermal equilibrium at temperature T, a classical harmonic oscillator has k T over h omega so its entropy is expected energy E equals k T and free energy F equals negative k T natural log of beta h omega.

k T over h omega.

negative k T plus k T natural log T.

S equals the expected value of E minus F over T.

k T

plus one over h omega.

To compute the entropy of a classical harmonic oscillator, we just use

S equals the expected value of E minus F over T.

We get the answer we got before, of course:

S equals k natural log of beta h over two pi T plus one.

But now we can finally understand the puzzling extra plus one.


## As we've seen, the entropy of any system in thermal equilibrium consists of two parts:

One. The free energy part, negative F over T. For the classical harmonic oscillator this is

Two. The expected energy part, the expected value of E over T. For the classical harmonic oscillator this is the expected value of E over T.

k.

The free energy part of the entropy is always k times the logarithm of the number of accessible states. For the classical harmonic oscillator, the expected energy part of the entropy must equal k by the equipartition theorem, since the oscillator's energy depends on two degrees of freedom. This is small compared to the free energy part when h omega is less than k T: that is, when quantum effects are small compared to thermal effects.


## PARTICLE IN A BOX: PARTITION FUNCTION

The energy of a classical free particle of mass m in a one-dimensional box depends only on its momentum p:

p squared over two m.

Its position q is trapped in the interval zero to L.

Its partition function is therefore

Z beta equals the integral from negative infinity to infinity of e to the negative beta E of p,q d p d q over h.

The integral from negative infinity to infinity of e to the negative beta p squared over two m d p equals two pi m over beta.

beta.

Now let's turn to our ultimate goal: computing the entropy of a box of gas. As a warmup, let's figure out the entropy of a single particle in a box. In fact, let's start with a free classical particle in a one-dimensional box: that is, in some interval zero to L.

The first step is to compute its partition function. As you can see, this is easy enough. But the whole idea raises some questions. Some people get freaked out by the concept of entropy for a single particle I guess because it involves probability theory for a single particle, and they think probability only applies to large numbers of things.

I sometimes ask these people "how large counts as large?" In fact the foundations of probability theory are just as mysterious for large numbers of things as for just one thing. What do probabilities really mean? We could argue about this all day: Bayesian versus frequentist interpretations of probability, etc. I said a tiny bit about this before, and I won't say more now.

Large numbers of things tend to make large deviations less likely. For example, the chance of having all the gas atoms in a box all on the left side is less if you have one thousand atoms than if you have just two. This makes us worry less about using averages and probability.

But the math of probability works the same for small numbers of particles-even one particle! Even better, knowing the entropy of one particle in a box will help us understand the entropy of a million particles in a box-at least if they don't interact, as we assume for an ideal gas.

But why just a one-dimensional box? The answer is that particle in a three-dimensional box is mathematically the same as three noninteracting distinguishable particles in a one-dimensional box! The x, y, and z coordinates of the three d particle act like positions of three one d particles.


## PARTICLE IN A BOX: EXPECTED ENERGY

A classical free particle of mass m in a one d box of length L has partition function

Z equals L divided by h times the square root of two pi m divided by beta. The expected energy of any system in thermal equilibrium is expected value of E equals negative d divided by d beta of ln Z. So, by the miracle of basic calculus, we get expected value of E equals one divided by two beta equals one divided by two k T as we'd expect from the equipartition theorem!

We worked out the partition function of a classical free particle in a one-dimensional box. From this we can work out its expected energy. Look how simple it is! It's just one divided by two k T, where k is Boltzmann's constant and T is the temperature!

Why is the final answer so simple? We can use the chain rule d divided by d beta of ln Z equals one divided by Z d Z divided by d beta to see that only the power of beta in

Z equals L divided by h times the square root of two pi m divided by beta matters, not all the constants: these constants show up in d Z divided by d beta, but also in one divided by Z, and they cancel. The length L, the mass m, Planck's constant h, the factor of two pi none of this junk matters! Not for the expected energy, anyway. Because Z is proportional to beta to the power of negative one half, we simply get expected value of E equals one divided by two k T. More generally, if the partition function of a system is proportional to beta to the power of negative c, its expected energy will be c k T. Z proportional to beta to the power of negative c implies expected value of E equals c k T. But when is the partition function of a system proportional to beta to the power of negative c? It's enough for the system's energy to be a positive definite quadratic form in n real variables-which physicists call 'degrees of freedom'. Then c equals n divided by two. We've already seen an example with two degrees of freedom: the classical harmonic oscillator. We saw that in this example Z proportional to one divided by beta. This gives expected value of E equals k T. But the result is quite general:

Puzzle forty-five. Suppose we have a system with state space R to the power of n and energy function E from R to the power of n to R that is a positive definite quadratic form, so that

E of x equals one divided by two norm of A x squared for some invertible n times n matrix A. Show that its partition function is proportional to beta to the power of negative c where c equals n divided by two. In fact, this is just a new outlook on our friend the equipartition theorem.

Here's another thing to consider. While our particle in a one dimensional box has two degrees of freedom-position and momentum-its energy depends on just one of these, and quadratically on that one. So its expected energy is one divided by two n k T where n equals one, not n equals two. So here's another puzzle for you:

Puzzle forty-six. Say we have a harmonic oscillator with spring constant K. As long as Kappa is greater than zero, the energy depends quadratically on two degrees of freedom so expected energy equals k T. But when Kappa equals zero it depends on just one, and suddenly expected energy equals one-half k T. How is such a discontinuity possible? In other words: how can a particle care so much about the difference between an arbitrarily small positive spring constant and a spring constant that's exactly zero, making its expected energy twice as much in the first case?

I'll warn you: this puzzle is deliberately devilish. In a way it's a trick question!


## PARTICLE IN A BOX: FREE ENERGY

A classical free particle of mass m in a one-dimensional box of length L has partition function

Z equals one divided by two times temperature times mass times length minus beta

The free energy of any system is given by F equals negative natural logarithm Z, so B one

F equals negative natural logarithm

Using one divided by kT and fiddling around a bit, we can rewrite this as

F equals negative k T (natural logarithm L plus negative natural logarithm kT plus negative natural logarithm one-half natural logarithm constant K T plus one-half two times mass times constant H squared

From the partition function of a classical free particle in a one-dimensional box we can also compute its free energy!


## PARTICLE IN A BOX: ENTROPY

We've shown that in thermal equilibrium, a classical particle of mass m in a one-dimensional box of length L has expected energy expected energy equals k T one and free energy

F equals negative k T (natural logarithm L plus negative natural logarithm kT plus negative natural logarithm one-half times one-half times two times mass times constant H squared

But entropy S is always (expected energy minus F) divided by T, so

S equals k natural logarithm L plus one-half natural logarithm kT plus natural logarithm one plus one-half

Having worked out the expected energy expected energy and free energy F for a single classical particle in thermal equilibrium in a one-dimensional box, it is easy to work out its entropy. We just subtract the free energy from the expected energy and divide by temperature:

S : (expected energy minus F T .

The formula we get is not very snappy:

S equals k (natural logarithm L plus five natural logarithm kT plus natural logarithm one divided by two times mass times constant H squared plus two) .

We will get a better formula later, and ponder its meaning. For now, let's just make these observations:

When we make the length L of the box larger, the entropy becomes larger.

When we increase the temperature T, the entropy becomes larger.

When we increase the mass m of the particle, the entropy becomes larger.

The first two facts should feel intuitively obvious. When we increase the box's length, there is more unknown information about the position of the particle in thermal equilibrium. When we increase the particle's temperature, there is more unknown information about its momentum. The third fact is less obvious. When we introduce the concept of 'thermal wavelength', we will see that increasing the particle's mass decreases its thermal wavelength, which in turn increases its entropy in thermal equilibrium.


## WHERE ARE WE NOW?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure?

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

N (natural logarithm ) volume three N plus negative natural logarithm kT plus unknown constant two including the mysterious constant y.


## The subgoal: compute the entropy of a single classical particle in a one-dimensional box:

S equals k natural logarithm L plus negative natural logarithm kT plus natural logarithm T plus two one


## The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator:

how kT one checkmark

Let's pause to remember where we are in our game plan. First we computed the entropy of a classical harmonic oscillator. Now we've computed the entropy of a single classical particle in a one-dimensional box. The answer looks a bit like the entropy of an ideal gas! That's no coincidence we're almost there now.

In case you wanted to know the entropy of a particle in a three-dimensional box, don't worry. It's the same as the entropy of three particles of the same mass in three one-dimensional boxes of appropriate lengths: the length L, width W and height H of our three-dimensional box. So we can just sum those three entropies and get our answer. Since natural logarithm L plus natural logarithm W plus natural logarithm H equals natural logarithm volume where volume is the volume of our three-dimensional box, we get

S equals k natural logarithm volume plus natural logarithm kT plus two natural logarithm three H squared two plus three).

Later we'll do this calculation more rigorously and more generally for a box of any shape.

But you may have another question: what's the meaning of our formula for the entropy of a classical particle in a one-dimensional box? It's pretty complicated, after all, and we'll need to understand it to have any chance of understanding the mysterious constant y in the formula for a classical ideal monatomic gas.

We can understand our formula better if we delve into a tiny bit of quantum mechanics, and the concept of 'thermal wavelength'. So let's do that.


## THE WAVELENGTH OF A PARTICLE

In quantum mechanics particles are waves! A particle with momentum p has wavelength h one equals p where h is the unreduced Planck's constant, exactly

For example, the wavelength of an electron moving at one meter per second is about zero point seven millimeters.

One of the most amazing discoveries of twentieth-century physics: particles are waves. The wavelength of a particle is Planck's constant divided by its momentum! This was first realized by Louis de Broglie in his nineteen twenty-four Ph.D. thesis, so it's called the 'de Broglie wavelength'.

Why am I telling you this? Because I want to explain and simplify the formula for the entropy of a particle in a box. Even though I derived it classically, it contains Planck's constant! So, it will become more intuitive if we think a tiny bit about quantum mechanics.

A good explanation of quantum mechanics would require a whole other course. But it's good to know that in quantum mechanics, a particle with a given momentum has a wavelength associated to it: we shouldn't imagine it as having a definite location; it's a bit 'blurry'.

This will give a more intuitive explanation for our complicated formula of the entropy of a particle in a one-dimensional box. We'll use this intuition to simplify our formula. That will make it easier to generalize to N particles in a three-dimensional box that is, a classical monatomic ideal gas!


## THE WAVELENGTH OF A WARM PARTICLE

In thermal equilibrium, the average energy of a classical free particle in three-dimensional space is

The expected value of E equals three k T.

where T is the temperature and k is Boltzmann's constant.

If the particle has mass m,

E equals m v squared, p equals m v equals p equals square root of two m E equals square root of three m k T.

In quantum mechanics, a particle of momentum p has wavelength X equals h over p where h is the unreduced Planck's constant. So, at temperature T, the typical wavelength of a free particle of mass m is roughly square root of three m k T.

Particles are waves! Their wavelength is shorter when their momentum is bigger. And the warmer they are, the bigger their momentum tends to be. So there should be a formula for the typical wavelength of a warm particle. And here it is! It helps us visualize the world: particles are a bit blurry, with a characteristic wavelength that depends on temperature.

We get this formula from a blend of ideas. Classical mechanics says kinetic energy is E equals p squared over two m. Classical statistical mechanics says E equals two k T. Quantum mechanics says X equals h over p. It's pretty optimistic to put these formulas together and see what we get. But the result is approximately correct, though subject to limitations.

We derived E equals k T using classical statistical mechanics. But it's close to correct for a single quantum particle in a big enough box at high enough temperatures. Otherwise quantum effects kick in.

Another problem is that the expected value of E equals two k T and E equals p squared over two m do not imply the expected value of p equals square root of three m k T, even if p here means the magnitude of the momentum vector. The arithmetic mean of a square is not the square of the arithmetic mean! Really the 'root mean square' of p is square root of three m k T. Similarly, even if the root mean square of p is square root of three m k T and quantum mechanically X equals h over p, we cannot conclude that the root mean square of X is h over square root of three m k T. Again, you cannot pass a root mean square through a reciprocal!

So, our derivation above is dodgy-but it's okay as an order-of-magnitude approximation for a warm enough particle in a big enough box.


## THE PARTITION FUNCTION AND THE THERMAL WAVELENGTH

The partition function of a classical free particle of mass m in a one-dimensional box of length L is

Z equals integral from negative infinity to infinity integral from negative infinity to infinity the length L e to the power of negative beta p squared over two m dp dq over h.

equals L

divided by square root of two pi m divided by beta.

where

Lambda equals h over square root of two m pi.

two pi m.

is called the 'thermal wavelength'.

Last time we saw that at temperature T, the typical wavelength of a free particle of mass m is roughly h over square root of three m k T equals h y over beta times three m.

But the partition function of a classical particle of mass m in a box simplifies a lot if we introduce a slightly different distance scale, which people call the thermal wavelength.

Lambda equals h over square root of two pi m k T equals hv over square root of two pi m k T.

Then the partition function is just the length of the box divided by Lambda. The thermal wavelength Lambda is a bit smaller than X: we have Lambda approximately zero point six nine. But we probably shouldn't worry about this too much, since our calculation of X was so rough. Of course, all these details are worth thinking about. But the thermal wavelength will turn out to be very useful!


## FREE ENERGY AND THE THERMAL WAVELENGTH

In thermal equilibrium, a classical free particle of mass m in a one-dimensional box of length L has free energy

F equals negative k times T times natural logarithm of

L divided by h square root of two pi m over beta.

beta.

F equals negative k T natural logarithm of where two pi m over beta.

A equals h y.

is the thermal wavelength.

Since the partition function of the classical free particle in a one-dimensional box is and free energy is related to the partition function by

F equals negative k times natural logarithm of Z,

we have

Expressing this in terms of temperature rather than coolness, we have

F equals negative k T natural logarithm of


## ENTROPY AND THE THERMAL WAVELENGTH

In thermal equilibrium, a classical free particle of mass m in a one-dimensional box of length L has expected energy

The expected value of E equals k T.

and free energy

F equals negative k T natural logarithm of Lambda L.

where Lambda equals h over square root of two pi m k T is the thermal wavelength.

But entropy S is the expected value of E minus F divided by T, so

S equals k natural logarithm of

Now that we have clean formulas for the expected energy and free energy of the classical free particle in a one-dimensional box, we can get a nice formula for its entropy. This is equivalent to the formula we saw before, but it's easier to understand. It's a sum of two terms:

S equals k times the natural logarithm of Lambda plus two.

Let's make sure we understand this! We've seen that for any system in thermal equilibrium, the entropy is the sum of two parts:

1. The free energy part. For the classical particle in a one-dimensional box, this is

S equals k times natural logarithm of L over Lambda.

divided by

2. The expected energy part. For the classical particle in a one-dimensional box, this is

The expected value of E.

equals two k.

The free energy part is always k times the logarithm of the number of accessible states, and for the particle in a one-dimensional box the number of accessible states is L over Lambda. The expected energy part is two k, by the equipartition theorem, because the particle's expected energy depends on one degree of freedom.

Let us think a bit more about why the number of accessible states is L over Lambda. The most rigorous approach is simply to compute the number of accessible states that is,

the partition function:

Z equals equals L times equals L divided by h times square root of two pi m over beta.

equals L divided by Lambda.

A more hand-wavy approach is to imagine the space of states of the particle, meaning the space of position-momentum pairs (q, p) inside the range zero to L times R. When it comes to counting accessible states, each region of area h holds one state. The 'accessible' states are those where the energy is not too big compared to k T, so the probability density e to the power of negative E divided by k T is fairly large. This is a bit vague, as it must be, because 'accessibility' is not really a yes-or-no matter. But let's just pretend it is, and demand E is less than or equal to k T. Then the 'accessible' region of state space is where p squared over two m is less than or equal to k T, or p is less than or equal to square root of two m k T over beta.

This region is the set of all (q, p) such that zero is less than or equal to q is less than or equal to L, and negative square root of two m k T over beta is less than or equal to p is less than or equal to square root of two m k T over beta.

It has area L times two times square root of m k T over beta, so the number of states it holds is this divided by h, or two L

square root of two m over h beta.

This is just thirteen percent more than the exact value of Z. More importantly, I hope this calculation gives you a mental picture of number of accessible states for the particle in a one-dimensional box. A mental picture can be helpful even if it's oversimplified. I like to imagine counting the little rectangles of area h that can fit into the 'accessible' region of state space.

In fact, this idea is related to Bohr and Sommerfeld's early approach to quantum physics, the 'old quantum theory', which was later subsumed by the theory of 'geometric quantization'. In Bohr and Sommerfeld's approach, when we quantize a classical system with one position and one momentum degree of freedom, there should be approximately one quantum state for each region of area h in the qp plane. More generally, when we quantize a classical system with n position and n momentum degrees of freedom, there should be approximately one quantum state for each region R inside R to the power of two n with the integral over R of dp dq is equal to h to the power of n.

So, delving into more quantum mechanics, and geometric quantization, would shed more light on the calculations we're doing now.


## PARTICLE IN A three D BOX: PARTITION FUNCTION

The partition function of a classical free particle of mass m in a three-dimensional box B of volume V is

B e-ßp.p/2m ď3pd3q h3

where B equals one over kT is the coolness.

This result becomes prettier using the thermal wavelength A equals h(8 over two mm) to the power of one-half.

Then we get simply

V over A cubed

Z equals

Now that we've worked out the statistical mechanics of a classical particle in a one-dimensional box, it's easy to copy everything for a three-dimensional box of any shape. We start with the partition function. The energy of a free particle of mass m is p. p over two m, so the partition function is the integral of exp(-p . p over two m) over all possible positions and momenta. Integrate over momentum and you get

- e-B(p?+p3+p3)/2m dp1dp2dp3 h3 (ten - thirty over two m Ap) equals h two mm beta cubed

In terms of the thermal wavelength this is just one over A cubed. Integrate over position and you multiply this by the volume of the box, say V. So we get an incredibly simple final answer:

Z equals X- V

And this sort of calculation works in any dimension: there's nothing special about the number three here.


## PARTICLE IN A THREE-D BOX: ENTROPY

In thermal equilibrium, a classical free particle of mass m in a three-dimensional box of volume V has expected energy

(E) equals kT times two-thirds and free energy

A cubed V

F equals negative kT ln where A equals h over V two xmkT is the thermal wavelength. But entropy S is ((E) minus F) over T, so

S equals k ln (MAS plus three)

The entropy of a particle in thermal equilibrium in a three-dimensional box works very much like our earlier calculation for a one-dimensional box, with a couple of adjustments due to the dimension. Since the particle's energy is now a quadratic function of three variables, the equipartition theorem now says its expected energy is

〈 E〉 equals kT.

We can work out its free energy from its partition function, which we computed in the last tweet:

V

F equals- kT ln Z equals- k ln

Thirteen.

Thus its entropy is

S equals (E) minus F over T

The meaning of the two terms here is very similar to that for the particle in the one-dimensional box. The first term is k times the logarithm of the number of accessible states, as always for the Gibbs entropy of a system in thermal equilibrium. Here the number of accessible states is V over A cubed. The second term is two k thanks to the equipartition theorem, since the particle's expected energy depends quadratically on three degrees of freedom. When V is much greater than A cubed this second term is a small correction to the first. As this ceases to be true, the second term becomes more important-and when A cubed is comparable to V, quantum corrections to our calculation also become significant.


## A TALE OF TWO GASES

The entropy of an ideal gas of N distinguishable classical particles of mass m in a box of volume V is

Sa equals kN (ln V plus ln kT plus ln kI plus ln Im plus two mm two while for indistinguishable particles it's

Si approximately equals KN ln plus ln kT plus ln m plus two two where the corrections are small compared to N as N greater than zero.

Now we are finally ready to tackle the entropy of a gas. We start with a 'monatomic ideal gas', which means N free point particles bouncing around in a box. But there's a subtlety! We'll get different answers depending on whether we think of these particles as distinguishable or indistinguishable. That is: do we count the state of the gas as different if we switch two particles, or not?

The formulas look very similar. There are three differences:

· For distinguishable particles we'll get an exact formula, while for indistinguishable particles we'll get an approximate one, where the corrections are small compared to N when N becomes large.

· The entropy for distinguishable particles has a term equal to two kN, while for indistinguishable particles it has a term equal to two kN.

· Most importantly, there's a huge difference in the volume dependence! Where the distinguishable particles have a term in the entropy equal to kN ln V, the indistinguishable ones have a term equal to kN ln, so their entropy is considerably smaller for large volumes.

The last difference makes the entropy behave strangely for distinguishable particles, so in practice the physically important case is the gas of indistinguishable particles. But we'll do the calculations in both cases, because the distinguishable case is easier, and interesting.


## GAS OF DISTINGUISHABLE PARTICLES: PARTITION FUNCTION

The partition function of an ideal gas of N distinguishable classical particles of mass m in a three-dimensional box B of volume V is

Za equals JBN J 1. IRON e -B i=1 N two m d3 p1 . . . d3PN d3 q1 . . . d3 qN

pi· pi h3N

two pi m β three N over two equals VN h3N

Thus Za equals three N A cubed N VN

where A equals h(8 over two pi m) to the power of one-half is the thermal wavelength.

Suppose we have a system of N distinguishable classical free particles in a three-dimensional box B of volume V. The state of this system is described by N positions q1, ... , qN E B and N momenta pi, ... , pN E R cube. If each particle has mass m, the energy of the ith particle is equal to

Ei equals pi· pi over two m and the energy of the system is

E equals sum over i equals one to N of Ei. Let's call the partition function of this system Za. To compute this we integrate exp(-BE) over the space of states, obtaining

Za equals LAN JARON BN JR cubed N exp(-ßE) d3 p1 . . . d3pNd3q1 . . . d3qN h3N.

Above, I proceeded to compute Za directly by doing the Gaussian integral over momenta and integrating each position over the box. Here's a slightly different way. Because exp(-(E) equals exp(-ßE1) ... exp(-ßEN),

the partition function Za is a product of integrals which are all equal:

BJR cubed e-Bp·p over two m d3pd3q h3 .

Za equals

The integral in the parentheses is the partition function of a single particle in a box. We have already seen that this equals

JB JR cubed e - Bp.p over two m ď3pd3q _V h3

A cubed where A is the thermal wavelength. Thus we have

Za equals

We can also do this calculation with a lot less work using Puzzle thirty-six. This implies that when we build a new system from N identical noninteracting copies of some old system, the partition function of the new system is the Nth power of the partition function of the old system. What I just did is show this in a special case.


## GAS OF DISTINGUISHABLE PARTICLES: ENTROPY

In thermal equilibrium, an ideal gas of N distinguishable classical particles of mass m in a three-dimensional box of volume V has expected energy

(Ed) equals kNT over three and free energy

A cubed N VN

Fa equals negative kT ln where A equals h over V two TmkT is the thermal wavelength. Its entropy Sa is ((Ea) minus Fa) over T, so

Sa equals kN ln N (ln N plus three)

We use the subscript d for a gas of N distinguishable particles. Since the energy is a quadratic function of three N variables, the equipartition theorem says the expected energy is expected energy equals kNT.

The free energy F is minus Boltzmann's constant times the logarithm of the partition function, which we just computed:

Fa equals negative kln Za equals negative kln

Thus the entropy of the gas is

Sa equals expected energy minus Fa T V( 3 +2). h equals

A equals square root of two pi m k T three two Tm h squared plus two

If we expand this out using we get the formula I promised earlier:

Sa equals kN (lnV +lnkT +ln

The only advantage of this messier formula is that it separates out the temperature dependence and the volume dependence.


## THE GIBBS "PARADOX"

For the ideal gas of N distinguishable classical particles in a box of volume V, the entropy

Sa equals kN ln V plus ln kT plus ln three two three two Tm plus three h squared two more than doubles if we double both N and V while keeping everything else the same. This confused people for a while, so it's called the 'Gibbs paradox'.

Start with a box B containing an ideal gas of distinguishable classical particles. Then double the volume of the box to get a new box B', and double the number of particles in the box too, while keeping the temperature and everything else the same.

We might expect the entropy to double. After all, we could take the doubled box and slip a thin wall down the middle to get two identical copies of the original box. So the entropy should be twice as big now. Right?

Apparently not! Instead of just doubling the kN ln V term in the original entropy, we are replacing it with two kN ln( 2V ), which is more than twice as big. The reason is that in the doubled box B' each individual particle has twice as much room to roam than if you put a wall down the middle. Thus, it takes more information to say where all the particles are.

While there's no real paradox here, people found this result deeply counterintuitive, so they called it the 'Gibbs paradox'. And in fact they had a good reason for being suspicious of this result. It would be correct if gas molecules were distinguishable. But in fact molecules of the same kind are not distinguishable they don't have little labels on them that let you recognize which is which. And if we take this fact into account, our formula for the entropy changes. Let's see how!


## GAS OF INDISTINGUISHABLE PARTICLES: PARTITION FUNCTION

The partition function of an ideal gas of N indistinguishable classical particles of mass M in a three-dimensional box B of volume V is

Zi(B) equals Za(B) divided by N factorial beta cubed N over two equals one VN N factorial h cubed N

Thus

Zi(B) equals N factorial A cubed N one VN

where A equals h square root of eight over two pi m

The partition function Zi for a gas of N indistinguishable particles is one over N factorial times that for a gas of distinguishable particles. Why? We got Za by integrating exp negative beta E over the space of ordered N-tuples of position-momentum pairs. The energy E here does not change if we permute our N-tuple, so we can also think of it as a function of unordered N-tuples. Then we get Zi by integrating exp negative beta E over the space of such unordered tuples. Notice that there are N factorial ordered N-tuples for each unordered N-tuple, except for N-tuple with repeated entries, which form a set of measure zero and thus contribute nothing to the integral. Thus, we should not be surprised that

Zi(B) equals Za(B) divided by N factorial.

But we've seen

Za(B)= A cubed N VN

where A is the thermal wavelength, so

Zi(B) equals N factorial A cubed N divided by VN

Making this sketchy argument precise requires more notation. I think carefully doing the case N equals two is the best way for you to see what's going on.


## GAS OF INDISTINGUISHABLE PARTICLES: ENTROPY

In thermal equilibrium, an ideal gas of N indistinguishable classical particles of mass M in a three-dimensional box of volume V has expected energy expected energy equals three over two k N T and free energy free energy equals minus k T ln one over N factorial V to the N over lambda cubed N where lambda equals h over square root of two pi m k T is the thermal wavelength.

Its entropy Si is expected energy minus free energy divided by T, so

Si equals k N ln V over lambda cubed plus three over two minus k ln N factorial. We use the subscript i for a gas of N indistinguishable particles. Since the energy is a quadratic function of the three N momentum variables, the equipartition theorem says the expected energy of this gas is expected energy equals three over two k N T. The free energy F is minus Boltzmann's constant times the logarithm of the partition function, which we just computed:

F sub i equals negative k ln Z sub i equals negative k ln left parenthesis one over N factorial times V to the power of N divided by Lambda to the power of three N right parenthesis. Thus the entropy of the gas is

S sub i equals left parenthesis expected value of E sub i minus F sub i right parenthesis divided by T equals k N left parenthesis ln fraction V over Lambda cubed plus three halves right parenthesis minus k ln N factorial. In short, it is k ln N less than for the gas of distinguishable particles. This makes beautiful intuitive sense: there are N factorial permutations of the particles that we no longer care about in the indistinguishable case.


## STIRLING'S FORMULA

Stirling's formula says approximately equal to square root of two pi N left parenthesis N divided by e right parenthesis to the power of N

N factorial and it gives ln N factorial approximately equal to left parenthesis ln N minus one right parenthesis N plus one half ln two pi N where the error goes to zero as

N approaches positive infinity. Now we need a bit of math: Stirling's formula for the factorial function. In one form this says limit as N approaches positive infinity of the fraction square root of two pi N left parenthesis N divided by e right parenthesis to the power of N divided by N factorial equals one. We abbreviate this fact, that the ratio of two quantities approaches one as N approaches positive infinity, by saying N factorial is asymptotic to square root of two pi N left parenthesis N divided by e right parenthesis to the power of N. We also write

N factorial asymptotic to square root of two pi N left parenthesis N divided by e right parenthesis to the power of N. where the symbol asymptotic to means 'asymptotic to'.

If we take the logarithm of both sides we get ln N factorial approximately equal to left parenthesis ln N minus one right parenthesis N plus one half ln two pi N. The symbol approximately equal has a vaguer meaning: 'approximately equal to'. But it turns out that in this instance the approximation is extremely good: the difference between the left and right sides goes to zero as N approaches positive infinity. In fact we will content ourselves with a cruder approximation:

ln N factorial approximately equal to left parenthesis ln N minus one right parenthesis N because in the entropy entropy of an ideal gas N is typically huge, so the term we have discarded here is dwarfed by the others.

N approximately equal to six times ten to the power of twenty-three. What is the ratio of fraction one half ln two pi N to

N? While deriving Stirling's formula is fascinating and not at all trivial, doing so would take us rather far afield. So I will resist, and refer you instead to this:


## THE SACKUR-TETRODE EQUATION

In thermal equilibrium, an ideal gas of N indistinguishable classical particles in a three-dimensional box of volume V has entropy

S sub i equals k N left parenthesis ln fraction V over Lambda cubed plus three halves right parenthesis minus k ln N factorial where Lambda equals Planck's constant divided by square root of two pi mass Boltzmann constant T is the thermal wavelength.

Using Stirling's formula ln N factorial approximately equal to left parenthesis ln N minus one right parenthesis N we get the Sackur-Tetrode equation:

S sub i approximately equal to k N left parenthesis ln fraction V over N Lambda cubed plus five halves right parenthesis Taking our formula

S sub i equals k N left parenthesis ln fraction V over Lambda cubed plus three halves right parenthesis minus k ln N factorial and using a simple version of Stirling's formula, ln N factorial asymptotic to left parenthesis ln N minus one right parenthesis N, we get the famous Sackur-Tetrode equation:

S sub i asymptotic to k N left parenthesis ln fraction V over Lambda cubed plus three halves right parenthesis minus k left parenthesis ln N minus one right parenthesis N asymptotic to k N left parenthesis ln fraction V over N Lambda cubed plus five halves right parenthesis. Note that with this formula, if we multiply both V and N by the same constant, the entropy also gets multiplied by that constant. In this situation we say the entropy is 'extensive'.

For a better approximation, we can use natural log of N factorial approximates as the natural log of N minus one times N plus one half times the natural log of two pi N where the error goes to zero as N approaches infinity. This gives a correction to the Sackur-Tetrode equation:

entropy aproximately equals k N times the natural log of volume over N lambda cubed plus five halves minus one half times the natural log of two pi N. Here if we multiply both volume and N by a constant c, we don't just multiply the entropy by c: we also have to subtract one half natural log of two pi c. So the entropy is not quite extensive but this effect is tiny when you've got a mole of gas.


## THE ENTROPY OF AN IDEAL MONATOMIC GAS

In thermal equilibrium, an ideal gas of N indistinguishable classical particles in a three-dimensional box of volume V has entropy given approximately by the Sackur-Tetrode equation:

But the thermal wavelength A is

A =

V2TmkT

so we can rewrite this as three halves KT plus three one half mm plus five entropy approximately equals K N natural log of V over N

We've done it: we've figured out the entropy of a gas of N indistinguishable classical free particles in a three-dimensional box of volume V. Above I've written it in two different ways. Let's mull over the meaning of each term in each formula.

The first formula says

Like the entropy of the classical harmonic oscillator and the classical free particle in a box, this breaks up into two parts, thanks to the formula

S equals E minus F T.

But it does so a bit subtly. The two parts are not what you might naively think! They are:

One. The free energy part:

T F and k N (natural log of one over N A cubed V plus one).

Two. The expected energy part:

E

T equals K N.

As usual, the free energy part of the entropy is k times the logarithm of the number of accessible states. The expected energy part of the entropy is N times k by the equipartition theorem, since there are N particles each of whose energy depends on three momentum degrees of freedom.

The expected energy part of the entropy is small compared to the free energy part when V over N is greater than A cubed: that is, when the volume available per particle greatly exceeds the cube of its thermal wavelength. This happens for a gas that is sufficiently warm and dilute, made of sufficiently massive particles. We will see that this is true for helium at standard temperature and pressure. It's even more true for the heavier monatomic gases: the noble gases like neon, argon, and krypton.

The surprise is the extra "plus one" in the first part of the entropy-the free energy part. It's telling us that the logarithm of the number of accessible states, divided by the number of particles, is natural log of N A cubed plus one over V.

What's the physical origin of this mysterious extra nat?

Mathematically it comes from Stirling's formula, which showed up when we switched from a gas of distinguishable particles to a gas of indistinguishable particles. It may seem odd that indistinguishability would increase the entropy by one nat per particle, but don't be confused: as we've seen, it greatly reduces it. For a gas of distinguishable particles the log of the number of accessible states, divided by the number of particles, is natural log of V over A cubed. When we switch to indistinguishable particles this drops to natural log of V over N A cubed plus one.

Here is a rough heuristic explanation of what's going on. For a single particle in a box of volume V, the number of accessible states is V over A cubed. In a gas of distinguishable free particles, each roams independently around the whole volume V. Thus, the log of the number of accessible states is natural log of V over A cubed per particle.

For a gas of indistinguishable particles, the story changes. For starters, we can crudely pretend each particle is trapped in its own tiny box of volume V over N. After all, if it leaves this tiny box by trading places with another particle in another tiny box, nothing really changes. In this approximation, the log of the number of accessible states is natural log of V over N A cubed per particle.

But it's not really true that each particle can only leave its tiny box by trading places with another. We can have more than one particle in the same tiny box-or none. That is, our gas can have density fluctuations. An exact treatment of the problem gives, not natural log of V over N A cubed nats per particle, but natural log of V over A cubed minus natural log of N factorial.

Stirling's formula says this is approximately natural log of V over A cubed minus natural log of N minus one equals natural log of V over N A cubed plus one.

This explains the mysterious extra nat. The extra nat of entropy per particle is due to density fluctuations!

As we've seen, even this is an oversimplification. A still better approximation, again coming from Stirling's formula, says natural log of V over A cubed minus natural log of N factorial approximates natural log of V over N A cubed plus one minus two natural log of two T N over N.

But as we saw in Puzzle forty-seven, this further correction is negligible for a mole of gas. It only becomes interesting for microscopic systems.

Now let's look at our second formula for the entropy of a gas of N indistinguishable classical free particles:

entropy approximately equals K N (natural log plus plus natural log of k T plus natural log of two T m over h squared plus three) .

Not only is this harder to remember, it's generally less friendly to physical intuition. First of all, three of the terms involve the logarithm of dimensionful quantities. Thus, when we change units they change, not by rescaling in the usual way, but by addition or subtraction. Secondly, the important role of the thermal wavelength is concealed in this formula.

The main advantage of this formula is that it separates out three contributors to the entropy per particle:

The volume available per particle, V over N. The bigger this is, the more entropy the gas has per particle.

The temperature, T. The bigger this is, the more entropy per particle.

The particle mass, m. The bigger this is, the more entropy per particle.

The first two should be rather intuitive. But what about the third? We need to combine V over N and T with the particle mass m and some constants of nature to get a dimensionless quantity, which we can then take the logarithm of. This leads us straight to the thermal wavelength:

natural log V plus, natural log k T plus, minus natural log of three two T m over h squared equals natural log of N A cubed V.

Thus, my best explanation of why a gas of heavier particles has more entropy per particle is that they have a shorter thermal wavelength, so we can specify their position more accurately, and it takes more information to do so.


## WHERE ARE WE NOW?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure?

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

N natural log plus, natural log k T plus y two thirds.

Y equals twenty-one halves plus two.


## The subgoal: compute the entropy of a single classical particle in a one-dimensional box:

entropy equals k natural log L plus, minus natural log k T plus one twelve plus two


## The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator:

k natural log K a k T plus one how

Okay, now we know the entropy of a classical ideal monatomic gas! We even know what it means. Unfortunately we're trying to figure out the entropy of hydrogen, which is diatomic. But we can do helium, which is monatomic ... and then we'll do hydrogen.


## ENTROPY PER MOLE VERSUS BITS PER MOLECULE

A nat of unknown information is one point three eight zero six four nine times ten to the negative twenty-three joules per kelvin of entropy: this is Boltzmann's constant.

There are six point zero two two one four zero seven six times ten to the twenty-three molecules per mole: this is Avogadro's number.

Thus, one nat of unknown information per molecule corresponds to one point three eight zero six four nine times ten to the negative twenty-three times six point zero two two one four zero seven six times ten to the twenty-three approximately eight point three one four four six three joules per kelvin of entropy per mole.

A bit is ln two approximately zero point six nine three one five nats, so one bit of unknown information per molecule corresponds to about zero point six nine three one five times eight point three one four four six three approximately five point seven six three one four six joules per kelvin of entropy per mole.

By the way, the values of Boltzmann's constant and Avogadro's number here are exact, fixed by the definition of SI units. So there is no experimental uncertainty in any of the numbers on this page.


## THE ENTROPY OF HELIUM: THEORY

The Sackur-Tetrode equation says that assuming helium is a classical ideal monatomic gas, its entropy is

S sub i approximately k N left parenthesis ln fraction V over N Lambda cubed plus fraction five over two right parenthesis which corresponds to ln fraction V over N Lambda cubed plus fraction five over two nats of unknown information per atom. At standard temperature and pressure, this gives about fifteen point zero four one nats or fraction fifteen point zero four one over ln two approximately twenty-one point seven zero zero bits of unknown information per atom.

Now let's calculate the entropy of helium in its gaseous state. NIST has tabulated its entropy at standard temperature and pressure, specifically temperature T equals two hundred ninety-eight point one five K and pressure P equals one bar, so that's what we'll try to calculate. An atom of helium has a mass of m equals six point six four six four seven seven times ten to the negative twenty-seven kilograms, so at standard temperature its thermal wavelength is

Lambda equals fraction h over square root of two pi m k T approximately fraction over square root of two pi times six point six four six four seven seven times ten to the negative twenty-seven kilograms times one point three eight zero six four nine times ten to the negative twenty-three joules per kelvin times two hundred ninety-eight point one five kelvin approximately five point zero five three seven two one times ten to the negative eleven meters. six point six two six zero seven times ten to the negative thirty-four joule seconds

For a mole of an ideal gas we have N equals six point zero two two one four zero seven six times ten to the twenty-three (this is Avogadro's number), and at standard temperature and pressure a mole of ideal gas has V approximately zero point zero two four seven eight nine six cubic meters: this is called its 'molar volume'. The molar volume of helium is actually slightly different from this, because helium is not an ideal gas: the atoms interact. But since we're doing a calculation assuming helium is a classical ideal gas, let's ignore that for now. We then get fraction V over N Lambda cubed approximately fraction zero point zero two four seven eight nine six cubic meters over six point zero two two one four zero seven six times ten to the twenty-three times left parenthesis five point two seven nine nine two nine one times ten to the negative eleven meters right parenthesis cubed approximately two hundred seventy-nine thousand six hundred sixty-three. We thus have ln fraction V over N Lambda cubed approximately ln two hundred seventy-nine thousand six hundred sixty-three approximately twelve point five four one. As explained earlier, this means that the logarithm of the number of accessible states of each helium atom would be twelve point five four one if it were trapped in its own small box of volume V over N. But density fluctuations contribute one extra nat of entropy per atom. Thus, the free energy part of the entropy per atom is thirteen point five four one nats. On the other hand, the expected energy part of the entropy per atom is two, coming from the atom's three momentum degrees of freedom. The total entropy per atom is thus

In A cubed plus one plus N A cubed

To impress our friends we can convert this to bits: we divide by ln two and get about zero point six nine three one five approximately twenty-one point seven zero zero bits of unknown information per atom of helium.

I've kept only five significant figures in the later stages of these calculations, since that's how precise the experimental data is. Next let's compare the final result to experiment!


## THE ENTROPY OF HELIUM: EXPERIMENT

The entropy of helium at standard temperature and pressure has been measured to be one hundred twenty-six point one five joules per kelvin per mole.

One bit of unknown information per atom corresponds to about five point seven six three one joules per kelvin of entropy per mole.

Thus, each atom of helium at standard temperature and pressure carries about one hundred twenty-six point one five approximately twenty-one point eight eight nine bits of unknown information.

Experimentally, the entropy of helium at standard temperature and pressure is one hundred twenty-six point one five joules per kelvin per mole. Converting this to bits per atom we get twenty-one point eight eight nine, very close to our theoretical result of twenty-one point seven zero zero, but about zero point nine percent higher.

There are a couple of possible reasons for this slight discrepancy. First, while our theoretical calculation assumed that helium is an ideal gas of noninteracting point particles, this is not true. The helium atoms interact!

Second, our computation ignored quantum effects-except for using Planck's constant to determine the thermal wavelength. Even for an ideal gas, quantum effects become important when Volume over N A cubed ceases to be large. This happens at high densities Volume over N, low temperatures T, or for particles of small mass m. Helium has a low mass as molecules of gas go-and our ultimate goal, hydrogen, is even worse.

Now let's tackle the final summit: hydrogen. This is a diatomic gas, so it works differently.


## THE IDEAL DIATOMIC GAS

In thermal equilibrium, a classical ideal diatomic gas of N indistinguishable molecules of mass m in a three-dimensional box of volume V has expected energy five times E equals kNT

and free energy

F equals negative kT ln N factorial A cubed N over V N

where A equals h over sqrt twenty-two pi mkT is the thermal wavelength.

Its entropy S is E minus F over T, so E N A cubed plus two negative k ln N factorial and using Stirling's formula ln N factorial approximately equals (ln N minus one) N we get S as kN E N (ln A cubed plus three) over N A cubed

It's easy to repeat our computation of entropy for a diatomic gas if we recall that the tumbling of the molecules add two degrees of freedom to the three for position, giving E equals two kNT. Tracking the effects of this change we see the entropy is higher than for a monatomic gas. To be precise, the entropy of a classical ideal diatomic gas is approximately E N (ln A S plus two) over N A cubed

So, it has one more nat of Shannon entropy per molecule than an ideal monatomic gas! Let's see how this plays out for hydrogen.


## THE ENTROPY OF HYDROGEN: THEORY

Assuming hydrogen is a classical ideal diatomic gas, its entropy is

E N (ln A S plus two) over N A cubed which corresponds to ln N A cubed V plus seven nats of unknown information per molecule. At standard temperature and pressure, this gives fifteen point one four four nats or ln two fifteen point one four four approximately twenty-one point eight four eight bits of unknown information per molecule.

A hydrogen molecule has m equals three point three four seven zero six times ten to the negative twenty-seventh kg, so at a temperature T equals two hundred ninety-eight point one five K its thermal wavelength is six point six two six zero seven times ten to the negative thirty-fourth J s approximately equals two pi times three point three four seven zero six times ten to the negative twenty-seventh kg times one point three eight zero six four nine times ten to the negative twenty-third J per K times two hundred ninety-eight point one five K

approximately seven point one two one five six times ten to the negative eleventh m.

For a mole of an ideal gas at standard temperature and pressure, N equals six point zero two two one four zero seven six times ten to the twenty-third and V approximately zero point zero two four seven eight nine six cubic meters, so approximately one hundred thirteen thousand nine hundred seventy-one N A cubed V approximately equals six point zero two two one four zero seven six times ten to the twenty-third times (seven point one two one five six times ten to the negative eleventh m) cubed over zero point zero two four seven eight nine six cubic meters

We thus have ln N A cubed V approximately equals ln one hundred thirteen thousand nine hundred seventy-one approximately equals eleven point six four four

Thanks to our previous work we know this means that the logarithm of the number of accessible states of each molecule would be eleven point six four four if it were trapped in its own small box of volume V over N. There is also a correction to this simplified picture due to density fluctuations, which gives one extra nat of entropy. These add up to give the free energy contribution to the entropy per molecule: twelve point six four four nats. This is less than we got for helium. But the expected energy contribution to the entropy per molecule is larger: we again get two nats from the molecule's three momentum degrees of freedom,

but now we get one extra nat due to its two extra tumbling degrees of freedom. The total number of nats of unknown information per hydrogen molecule is thus ln V over N A cubed plus one plus three halves plus one approximately equals fifteen point one four four. Finally, the number of bits of unknown information per hydrogen molecule is fifteen point one four four over zero point six nine three one five approximately equals twenty-one point eight four eight. This is slightly more than for helium, where the number was twenty-one point seven zero zero.

As a sanity check, let's do this calculation a different way. A hydrogen molecule is close to half the mass of a helium atom, so its thermal wavelength should be sqrt two times as large. In our calculation we're treating V over N as the same for both gases, so hydrogen's V over N A cubed should be two to the power of negative three-halves times as large as that for helium. Since ultimately we compute bits by taking a logarithm in base two, this reduces its entropy per molecule by three halves bits. However, hydrogen's two tumbling degrees of freedom increase its entropy per molecule by one nat, or one over ln two bits. We have negative three halves plus one over ln two approximately equals negative one point five plus one point four four three approximately equals negative zero point zero five seven. This suggests that each hydrogen molecule should carry zero point zero five seven fewer bits of unknown information than each helium atom. Why did our more careful calculation say hydrogen should have about twenty-one point eight four eight minus twenty-one point seven zero zero approximately equals zero point one four eight more bits of unknown information per molecule? What's the mistake?

The slight discrepancy arises solely from the fact that a hydrogen molecule is not exactly half the mass of a helium atom! It's a bit heavier. It's actually more like zero point five zero three five eight times the mass of a helium. This makes its thermal wavelength a bit smaller than our estimate in the last paragraph, which boosts its entropy. It's nice that such subtleties, ultimately due to nuclear physics, are showing up here.

By the way, all our calculations have been for the most common isotopes of hydrogen and helium: hydrogen whose nucleus consists of a single proton, and helium whose nucleus consists of two protons and two neutrons. Other isotopes have significantly different mass, and this changes the entropy values significantly.


## THE ENTROPY OF HYDROGEN: EXPERIMENT

The entropy of hydrogen at standard temperature and pressure has been measured to be one hundred thirty point six eight joules per kelvin per mole.

One bit of unknown information per molecule corresponds to about five point seven six three one joules per kelvin of entropy per mole.

Thus, each molecule of hydrogen at standard temperature and pressure has about one hundred thirty point six eight approximately twenty-two point six seven five five point seven six three one bits of unknown information.

Okay, let's compare our theoretical prediction to experiment.

The experimental figure for the entropy of hydrogen at standard temperature and pressure is one hundred thirty point six eight joules per kelvin per mole, which translates into twenty-two point six seven five bits per molecule. This is larger than our theoretical prediction of twenty-one point eight four eight bits per molecule by about three point eight percent.

That's not bad. We can say we solved our original problem fairly well. But the percentage error here is about four times worse than it was for calculation for helium. Why is it worse?

I haven't studied this, but I can imagine two reasons. First, remember that quantum effects kick in when V over N A cubed ceases to be large. This quantity is a bit smaller for hydrogen than for helium. Remember, for helium it was two hundred seventy-nine thousand six hundred sixty-three at standard temperature and pressure, while for hydrogen it's one hundred thirteen thousand nine hundred seventy-one. But that's still very large, so I imagine quantum effects are still quite tiny.

Second, hydrogen molecules are not chemically inert like helium atoms, and they're larger, and diatomic rather than monatomic. So I'd expect them to interact more, making the ideal gas approximation worse. This feels like a more plausible explanation for the three point eight percent discrepancy.


## WHERE DID WE GO?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure? V

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

negative W N of M plus three over two Log M plus negative Log k T plus Y

including the mysterious constant Y:

Two M over N squared

Y equals two over twelve plus two


## The subgoal: compute the entropy of a single classical particle in a one-dimensional box:

S equals k times Log L plus negative Log k T plus negative Log twelve plus two times Log twenty-two plus one half


## The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator:

S equals k Log of plus one times Log of k T

We're done! Or at least we reached our stated goal. But there is a lot more to say about entropy. In a way we've scarcely scratched the surface. For more on the mathematics of entropy, I recommend these books:

The second one has an intense focus on our friend the box of gas. And for the principle of maximum entropy, I again recommend this insightful and opinionated text:


## THE FIRST LAW OF THERMODYNAMICS

Suppose a system has some measure space X of states with functions called energy E of X to R and volume V of X to R.

Consider probability distributions on X maximizing the Gibbs entropy S subject to constraints on E and V.

Then as we vary E and V we have d of E equals T d S minus P d of V

where T is called temperature and P is called pressure.

I said we were done. But what kind of course on entropy doesn't cover the three laws of thermodynamics? I talked a bit about the Third Law, but I haven't even mentioned the other two yet.

Here's why: this wasn't a course on thermodynamics. In 'classical thermodynamics' there's a tradition of taking concepts such as energy, work and heat as primitive, and treating the laws of thermodynamics as axioms. I've instead been explaining a bit of 'classical statistical mechanics', where we start with probability theory and attempt to derive classical thermodynamics. In this approach the laws of thermodynamics are not fundamental. They actually look a bit odd: they become results that hold under various conditions, so each one becomes a collection of theorems and conjectures.

I'll state versions of the three laws of thermodynamics in the language we've developed here. But please be aware that my versions are idiosyncratic and will make some people raise their eyebrows. I'm afraid you'll have to go elsewhere, like Reif's book, to learn these laws in their traditional form!

We've been maximizing entropy subject to a constraint on the expected value of one quantity. What if we do two or more? Everything works the same way, but the fundamental relation between temperature, energy and entropy, d(E) equals TDs, gets one extra term for each constraint. The resulting equation is a version of the 'First Law of Thermodynamics'.

I'll explain the case with one extra constraint. Suppose we've got a measure space X whose points are states of some system. Choose two functions on it. They could be anything, but let's call them energy and volume and write them as E: X goes to R and V: X goes to R. These terms are favored because thermodynamics arose in part from the study of steam engines, where you've got a cylinder of steam with some energy and some volume. For any probability distribution p: X goes to zero comma zero, we can write down a formula for its Shannon entropy

H equals negative the integral of p of x times the natural log of p of x dx and also the expected values

(E) equals the integral of E of x dx, (V) equals the integral of V of x dx.

Let's not worry now about whether these integrals converge.

Suppose we only know (E) and (V), and we are trying to choose the 'best' probability distribution p with these expected values. What should we do? Following the principle of maximum entropy, we seek the probability distribution p that maximizes H subject to our constraints on (E) and (V). If we do this, we are led to a Lagrange multipliers problem, much as in the simpler case of one constraint. But now we need two Lagrange multipliers: let's call them beta and gamma. We get this equation:

dH equals beta d(E) plus gamma d(V).

This is the First Law!

But this isn't the way physicists usually write it. To get the First Law in its usual form, first let's switch to using Gibbs entropy S equals kH, and emphasize the role of energy by solving for d(E):

d(E) equals TdS minus Pd(V).

Then, to simplify the look of this equation, let's introduce variables called temperature and pressure:

T equals k beta inverse, P equals beta.

Now the First Law of Thermodynamics looks like this:

d(E) equals TdS minus Pd(V).

It says that as we move around among probability distributions that maximize entropy subject to constraints on expected energy and volume, the change in expected energy is the sum of two terms:

heat, meaning TdS

work, meaning minus Pd(V).

For example, if we have a cylinder of steam with pressure P and we increase its expected volume by a little bit deltaV, its expected energy goes down by about P deltaV: that's how we understand the minus sign. In this situation, the external world has done an amount of work minus P deltaV on the cylinder of steam, but most people say the cylinder of steam has done an amount of work P deltaV on the external world.

Here are a few puzzles if you want to dig deeper. In the first two, I ask you to generalize ideas from our earlier work on maximizing entropy subject to a single constraint.

(E) equals e, (V) equals v,

and also suppose p1 and so on up to pn greater than zero. Show that at p we have dH equals beta d(E) plus gamma d(V)

for some beta, gamma in R. (Hint: first do the case where not all the E_i are equal and not all the V_i are equal. This guarantees that d(E) and d(V) are nonzero. You can handle the other cases separately.)

n exp minus beta E_i minus gamma V_i

P_i sum exp minus beta E_i minus gamma V_i


## THE SECOND LAW OF THERMODYNAMICS

Suppose a system has some measure space X of states and at any time t there is a probability distribution p of t on X.

We say the second law of thermodynamics holds if t1 is less than or equal to t2 implies S of p of t1 is less than or equal to S of p of t2.

This seems to be widely true, yet the conditions under which it holds are subtle and much argued.

The Second Law of Thermodynamics, as commonly stated, says that the entropy of a closed system never decreases. This appears to be a profound fact about our universe. A huge challenge to physics is to understand where this law comes from. Can it be derived from some realistic assumptions? One problem is that the laws of classical mechanics are invariant under time-reversal. Thus, if we evolve probability distributions on some space of states according to these laws, for any probability distribution whose entropy is nondecreasing, there is a time-reversed one whose entropy is nonincreasing.

This is called the problem of the arrow of time: briefly, why does the future look so different from the past? Quantum mechanics makes the problem subtler but does not provide an easy resolution. The solution may be that we happen to live in a universe a particular solution of the laws of physics where entropy was very low at the Big Bang, making it easy for entropy to increase after that. But if you get ten physicists in a room and ask them to explain the arrow of time, you are likely to hear ten different opinions. Thus, I will not attempt to resolve it here. For more on that, I recommend this book:

Instead, let's see how the Second Law sheds light on the meaning of temperature. You'll notice that in our course I never talked about systems evolving in time, and I never talked about two systems interacting: always just a single system. Now let's imagine two systems, each in thermal equilibrium, but at possibly different temperatures. Say the first has entropy S1, expected energy (E1) and temperature T1. As usual, these are related by dS1 equals d(E1) over T1.

Say the second system works similarly, with dS2 equals d(E2) over T2.

We can define the total entropy of the two systems by

S equals S1 plus S2.

and the total expected energy by

(E) equals (E1) plus (E2).

Suppose now that the two systems can exchange energy with each other, but in a slow and gentle way, so we can approximately treat each one as in thermal equilibrium at any moment. If no energy flows in or out of the combined system, the total expected energy is conserved, so d(E) over dt equals zero and thus d(E1) over dt

What does the Second Law give us in this situation? It implies dS over dt greater than or equal to zero or

S1 plus S2 greater than dS2 over dt over dt dS1

It follows that one over T1 d(E1) over dt plus one over T2 d(E2) is greater than zero or

T1 over dt one over d(E1)

T2 over dt one over d(E1) is greater than or equal to zero.

We can rewrite this as

T1 inverse minus T2 inverse.

Now suppose both T1 and T2 are positive. Then we get a remarkable consequence: as two systems exchange energy, with each staying in thermal equilibrium at every moment, expected energy can only flow from the system with higher temperature to the system with lower temperature!

Now suppose both T1 and T2 are positive. Then we get a remarkable consequence: as two systems exchange energy, with each staying in thermal equilibrium at every moment, expected energy can only flow from the system with higher temperature to the system with lower temperature!


## THE THIRD LAW OF THERMODYNAMICS: REVISITED

If a system has countably many states, with just one of lowest energy, and thermal equilibrium is possible for this system for some temperature T greater than zero, then its entropy in thermal equilibrium approaches zero exponentially fast as a function of one over T as T approaches zero from above.

In our earlier work on the Third Law, we only studied systems with finitely many states. Later we saw how to compute entropy from the free energy and expected energy. This makes it a bit easier to handle systems with a countable infinity of states. In the following puzzles, which are only for the most devoted readers, let's use these ideas to prove and improve the Third Law for systems with countably many states.

Earlier we worked with temperature, but it's cooler to use coolness. For all the following puzzles, let's suppose we have a system with a countable infinity of states n equals one, two, three, and so on with energies En. Also suppose thermal equilibrium is possible for some Bo greater than zero, i.e., the sum

Z of Bo equals the sum of exp of negative BoEn from n equals one to infinity converges. Our arguments also apply to systems with finitely many states, where this convergence condition is automatic.

En equals En plus c we get a new 'shifted' system whose partition function, expected energy, free energy, and entropy are related to those of our original system by

Z equals exp of negative ßc times Z, the expected value of E equals the expected value of E plus c, F equals F plus c, and S equals S

for all B greater than Bo.

Now further suppose that our original system has just one state of least energy. Earlier we saw that we could reindex the states so that E one is less than E two is less than or equal to E three is less than or equal to and so on and En approaches positive infinity. The same is true of our new shifted system, and let's choose c equals negative E one so that the lowest energy of the shifted system is zero. With this shift we have zero equals E one is less than E two is less than three is less than and En approaches positive infinity.

using this equation show and thus for some constant independent of beta. Use the fact that the expected value of F as a function of beta equals negative one over beta times the natural logarithm of Z as a function of beta to show that for large enough beta, the absolute value of the expected value of F as a function of beta is less than a constant times exp of negative the quantity beta minus beta sub zero times E two possibly for a different constant independent of beta. Using Puzzle fifty-seven, conclude that the absolute value of F as a function of beta minus E one is less than a constant times exp of negative the quantity beta minus beta sub zero times the quantity E two minus E one. Voilà! This shows that for a system with countably many states and just one state of lowest energy, if thermal equilibrium is possible at some positive temperature, then the free energy must approach this lowest energy exponentially fast as beta approaches positive infinity. Now let's show something similar for the expected energy. Again we use the shifted system to simplify the calculations. I'll leave more work to you this time.

the partial derivative with respect to beta of Z as a function of beta equals negative the sum from n equals two of E tilde sub n times exp of negative beta E tilde sub n. Use this to show that the partial derivative with respect to beta of Z as a function of beta goes to zero exponentially fast as beta approaches positive infinity. Using the expected value of E tilde as a function of beta equals negative the partial derivative with respect to beta of the natural logarithm of Z as a function of beta equals negative one over Z as a function of beta times the partial derivative with respect to beta of Z as a function of beta and Puzzle fifty-eight, show that the expected value of E tilde as a function of beta goes to zero exponentially fast as beta approaches positive infinity. Using Puzzle fifty-seven, conclude that the expected value of E as a function of beta approaches E sub one exponentially fast as beta approaches positive infinity. Finally, since

S equals k times beta times the quantity F minus the expected value of E and both F and the expected value of E approach E sub one exponentially fast as beta approaches positive infinity, conclude that S approaches zero exponentially fast as beta approaches positive infinity. Let's summarize! Suppose we have a system with a countable infinity of states and just one state of lowest energy. If thermal equilibrium is possible for this system for some T greater than zero, the Third Law of Thermodynamics says its entropy in thermal equilibrium goes to zero as T approaches zero from above. But in fact we can say more: for some a and b greater than zero we have the absolute value of S as a function of beta is less than a times the exponential of negative b times beta for all large enough