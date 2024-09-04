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

I have largely avoided the second law of thermodynamics, which says that entropy always increases. While fascinating, this is so problematic that a good explanation would require another book! I have also avoided the role of entropy in biology, black hole physics, et cetera. Thus, the aspects of entropy most beloved by physics popularizers will not be found here. I also never say that entropy is 'disorder'.

I have tried to say as little as possible about quantum mechanics, to keep the physics prerequisites low. However, Planck's constant shows up in the formulas for the entropy of the three classical systems mentioned above. The reason for this is fascinating: Planck's constant provides a unit of volume in position-momentum space, which is necessary to define the entropy of these systems. Thus, we need a tiny bit of quantum mechanics to get a good approximate formula for the entropy of hydrogen, even if we are trying our best to treat this gas classically.

Since I am a mathematical physicist, this book is full of math. I spend more time trying to make concepts precise and looking into strange counterexamples than an actual 'working' physicist would. If at any point you feel I am sinking into too many technicalities, don't be shy about jumping to the next tweet. The really important stuff is in the boxes. It may help to reach the end before going back and learning all the details. It's up to you.

In twenty ten, Chas A. Egan and Charles H. Lineweaver estimated the biggest contributors to the entropy of the observable universe. Measuring entropy in bits, these are:

· stars: ten to the eighty-one bits.

· interstellar and intergalactic gas and dust: ten to the eighty-two bits.

· gravitons: ten to the eighty-eight bits.

· neutrinos: ten to the ninety bits.

· photons: ten to the ninety bits.

· stellar black holes: ten to the ninety-eight bits.

· supermassive black holes: ten to the one hundred five bits.

So, almost all the entropy is in supermassive black holes!

In twenty ten, Chas A. Egan and Charles H. Lineweaver estimated the entropy of the observable universe. Entropy corresponds to unknown information, so there's a heck of a lot we don't know! For stars, most of this unknown information concerns the details of every single electron and nucleus zipping around in the hot plasma. There's more entropy in interstellar and intergalactic gas and dust. Most of the gas here is hydrogen-some in molecular form H-two, some individual atoms, and some ionized. For all this stuff, the unknown information again mostly concerns the details, like the position and momentum, of each of these molecules, atoms and ions.

There's a lot more we don't know about the precise details of other particles whizzing through the universe, like gravitons, neutrinos and photons. But there's even more entropy in black holes! One reason Stephen Hawking is famous is that he figured out how to compute the entropy of black holes. To do that you need a combination of statistical mechanics, general relativity and quantum physics. Statistical mechanics is the study of physical systems where there's unknown information, which you study using probability theory. I'll explain some of that in these tweets. General relativity is Einstein's theory of gravity, and while I've explained that elsewhere, I don't want to get into it here so I will say nothing about the entropy of black holes.

Quantum physics was also necessary for Hawking's calculation, as witnessed by the fact that his answer involves Planck's constant, which sets the scale of quantum uncertainty in our universe. I will try to steer clear of quantum mechanics in these tweets, but in the end we'll need a tiny bit of it. There's a funny sense in which statistical mechanics is somewhat incomplete without quantum mechanics. You'll eventually see what I mean.


## THE ENTROPY OF HYDROGEN

At standard temperature and pressure, hydrogen gas has an entropy of

One hundred thirty point six eight joule per kelvin per mole

But a joule per kelvin of entropy is about

One point zero four four nine times ten to the twenty-three bits of unknown information and a mole of any chemical is about

Six point zero two two one times ten to the twenty-three molecules

So the unknown information about the precise microscopic state of hydrogen is

One point zero four four nine times ten to the twenty-three approximately equals twenty-three bits per molecule!

One hundred thirty point six eight times six point zero two two one times ten to the twenty-three

Egan and Lineweaver estimated the entropy of all the interstellar and intergalactic gas and dust in the observable universe. Entropy corresponds to information we don't know. Their estimate implies that there are ten to the eighty-two bits of information we don't know about all this gas and dust.

Most of this stuff is hydrogen. Hydrogen is very simple stuff. So it would be good to understand the entropy of hydrogen. You can measure changes in entropy by doing experiments. If you assume hydrogen has no entropy at absolute zero, you can do experiments to figure out the entropy of hydrogen under other conditions. From this you can calculate that each molecule in a container of hydrogen gas at standard temperature and pressure has about twenty-three bits of information that we don't know.

You can see a sketch of the calculation above. But everything about it is far from obvious! What does 'missing information' really mean here? Joules are a unit of energy; kelvin is a unit of temperature. So why is entropy measured in joules per kelvin? Why does one joule per kelvin correspond to one point zero four four nine times ten to the twenty-three bits of missing information? How can we do experiments to measure changes in entropy? And why is missing information the same as-or more precisely proportional to-entropy?

The good news: all these questions have answers! You can learn them here. However, you will have to persist. Since I'm starting from scratch it won't be quick. It takes some math-but luckily, nothing much more than calculus of several variables. When you can calculate the entropy of hydrogen from first principles, and understand what it means, that will count as true success.

See how it goes! Partial success is okay too.


## WHERE ARE WE GOING?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure?

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

S equals kN times the natural log of kT plus the natural log of approximate plus r parentheses over N times V

including the mysterious constant y.


## The subgoal: compute the entropy of a single classical particle in a one-dimensional box.

The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator.

To understand something deeply, it can be good to set yourself a concrete goal. To avoid getting lost in the theory of entropy, let's try to understand the entropy of hydrogen gas. This is a 'diatomic' gas since a hydrogen molecule has two atoms. At standard temperature and pressure it's close to 'ideal', meaning the molecules don't interact much. It's also close to 'classical', meaning we don't need to know quantum mechanics to do this calculation. Also, when the hydrogen is not extremely hot, its molecules don't vibrate much—but they do tumble around.

Given all this, we can derive a formula for the entropy S of some hydrogen gas as a function of its temperature T, the number N of molecules, the volume V, and a physical constant k called 'Boltzmann's constant'. This formula also involves a rather surprising constant which I'm calling y. We'll figure that out too. It's so weird I don't want to give it away!

As a warmup, we will derive the formula for the entropy of an ideal 'monatomic' gas a gas made of individual atoms, like helium or neon or argon. Sackur and Tetrode worked this out in nineteen twelve. Their result, called the Sackur-Tetrode equation, is similar to the one for a diatomic gas.

But before doing a monatomic gas, we'll figure out the entropy of a single atom of gas in a box. That turns out to be a good start, since in an ideal monatomic gas the atoms don't interact, and the entropy of N atoms—as we'll see is just N times the entropy of a single atom.

But before we can do any of this, we need to understand what entropy is, and how to compute it. It will take quite a bit of time to compute the entropy of a classical harmonic oscillator! But from then on, the rest is surprisingly quick.


## Five kinds of entropy

Entropy in thermodynamics: the change in entropy as we change a system's internal energy by an infinitesimal amount dE while keeping it in thermal equilibrium is dS equals dE divided by T, where T is the temperature.

Entropy in classical statistical mechanics: S equals negative k integral of P of x l n of P of x du of x where P is a probability distribution on the measure space (X, u) of states and k is Boltzmann's constant.

Entropy in quantum statistical mechanics: S equals negative k trace of P l n of P where P is a density matrix.

Entropy in information theory: H equals negative summation of P sub i log P sub i where P is a probability distribution on the set X.

Algorithmic entropy: the entropy of a string of symbols is the length of the shortest computer program that prints it out.

Before I actually start explaining entropy, a warning: it can be hard at first to learn about entropy because there are many kinds—and people often don't say which kind they're talking about. Here are five kinds. Luckily, they are closely related!

In thermodynamics we primarily have a formula for the change in entropy: if you change the internal energy of a system by an infinitesimal amount dE while keeping it in thermal equilibrium, the infinitesimal change in entropy is dS equals dE divided by T where T is the temperature.

Later, in classical statistical mechanics, Gibbs explained entropy in terms of a probability distribution P on the space of states of a classical system. In this framework, entropy is the integral of negative P l n P times a constant k called Boltzmann's constant.

Later von Neumann generalized Gibbs' formula for entropy from classical to quantum statistical mechanics! He replaced the probability distribution p by a so-called density matrix p, and the integral by a trace.

Later Shannon invented information theory, and a formula for the entropy of a probability distribution on a set (often a finite set). This is often called 'Shannon entropy'. It's just a special case of Gibbs' formula for entropy in classical statistical mechanics, but without Boltzmann's constant.

Later still, Kolmogorov invented a formula for the entropy of a specific string of symbols. It's just the length of the shortest program, written in bits, that prints out this string. It depends on the computer language, but not too much.

There's a network of results connecting all these five concepts of entropy. I will first explain Shannon entropy, then entropy in classical statistical mechanics, and then entropy in thermodynamics. While this is the reverse of the historical order, it's the easiest way to go.

I will not explain entropy in quantum statistical mechanics: for that I would feel compelled to teach you quantum mechanics first. Nor will I explain algorithmic entropy.


## FROM PROBABILITY TO INFORMATION

How much information do you get when you learn an event of probability P has happened? It's

Negative log P where we can use any base for the logarithm, usually E or two.

Example: Suppose I flip three coins that you know are fair. I tell you the outcome: "heads, tails, heads". That's an event of probability one over two to the power of three, so the information you get is

Negative log of one over two to the power of three equals three log two or "three bits" for short, since log two of information is called a bit.

Here is the simplest link between probability and information: when you learn that an event of probability P has happened, how much information do you get? We say it's negative log P. We take a logarithm so that when you multiply probabilities, information adds. The minus sign makes information come out positive.

Beware: when I write 'log' I don't necessarily mean the logarithm base ten. I mean that you can use whatever base for the logarithm you want; this choice is like a choice of units. Whatever base B you decide to use, I'll call log base B two a 'bit'. For example, if I flip a single coin that you know is fair, and you see that it comes up heads, you learn of an event that's of probability one over two, so the amount of information you learn is

Negative log base B of one over two equals log base B two. That's one bit! Of course if you use base B equals two then this logarithm actually equals one, which is nice.

To understand the concept of information it helps to do some puzzles.

Puzzle one. First I flip two fair coins and tell you the outcome. Then I flip three more and tell you the outcome. How much information did you get?

Puzzle two. I roll a fair six-sided die and tell you the outcome. Approximately how much information do you get, using logarithms base two?

Puzzle three. When you flip seven fair coins and tell me the outcome, how much information do I get?

Puzzle four. Every day I eat either a cheese sandwich, a salad, or some fried rice for lunch- each with equal probability. I tell you what I had for lunch today. Approximately how many bits of information do you get?

Puzzle five. I have a trick coin that always lands heads up. You know this. I flip it five times and tell you the outcome. How much information do you receive?

Puzzle six. I have a trick coin that always lands heads up. You believe it's a fair coin. I flip it five times and tell you the outcome. How much information do you receive?

Puzzle seven. I have a trick coin that always lands with the same face up. You know this, but you don't know which face always comes up. I flip it five times and tell you the outcome. How much information do you receive?

These puzzles raise some questions about the nature of probability, like: is it sub- jective or objective? People like to argue about those questions. But once we get a probability P, we can convert it to information by computing negative log P.


## UNITS OF INFORMATION

An event of probability one over two carries one bit of information. An event of probability one over E carries one nat of information. An event of probability one over three carries one trit of information. An event of probability one over four carries one crumb of information. An event of probability one over ten carries one hartley of information. An event of probability one over sixteen carries one nibble of information. An event of probability one over two hundred fifty-six carries one byte of information. An event of probability one over two to the power of eight one nine two carries one kilobyte of information.

There are many units of information. Using information equals negative log P we can relate these to probabilities. For example if you see a number in base ten, and each digit shows up with probability one over ten, the amount of information you get from each digit is one ‘hartley'.

How many bits are in a hartley? Remember: no matter what base you use, I call log ten a hartley and log two a bit. There are log ten over log two bits in a hartley. This number has the same value no matter what base you use for your logarithms! If you use base two, it's

Log base two ten over log base two two equals log base two ten approximately three point three two. So a hartley is about three point three two bits.

If you flip eight fair coins and tell me what answers you got, I've learned of an event that has probability one over two to the power of eight equals one over two hundred fifty-six. We say I've received a 'byte' of information. This equals eight bits of information. Similarly, if you flip one thousand twenty-four times eight fair coins and tell me the outcome, I receive a kilobyte of information.

Or at least that's the old definition. Now many people define a kilobyte to be one thousand bytes rather than one thousand twenty-four bytes, in keeping with the usual meaning of the prefix. If you want one thousand twenty-four bytes you're supposed to ask for a 'kibibyte'. When we get to a terabyte, the new definition based on powers of ten is about ten percent less than the old one based on powers of two: ten to the twelve bytes rather than two to the forty approximately one point zero nine nine five times ten to the twelve. If you want the old larger amount of information you should ask for a 'tebibyte'.

Wikipedia has an article that lists many strange units of information. Did you know that two bits is a 'crumb'? Did you even need to know? No, but now you do.

Feel free to dispose of this unnecessary information! All this is just for fun-but I want you to get used to the formula

Information equals negative log P


## THE INFORMATION IN A LICENSE PLATE NUMBER

California two thousand twelve! F two million fifteen thousand four hundred thirty-eight six T R J two four four

If there are N different possible license plate numbers, all equally likely, how many bits of information do you learn when you see one?

If you think N alternatives are equally likely, when you see which one actually occurs, you gain an amount of information equal to log N. Here the choice of base B is up to you: it's a choice of units. But what is this in bits? No matter what base you use,

log N equals log base two N times log base six two.

Since we call log base two a 'bit', this means you've learned log base two N bits of information. Let's try it out!

Puzzle eight. Suppose a license plate has seven numbers and or letters on it. If there are ten plus twenty-six choices of number and or letter, there are three hundred sixty-seven possible license plate numbers. If all license plates are equally likely, what's the information in a license plate number in bits approximately?

California six T K J seven five zero and two thousand seventeen

November

But wait! Suppose I tell you that all license plate numbers have a number, then three letters, then three numbers! You have just learned a lot of information. So the remaining information content of each license plate is presumably less. Let's work it out.

Puzzle nine. How much information is there in a license plate number if they all have a number, then three letters, then three numbers? Assume they're all equally probable and there are ten choices of each number and twenty-six choices of each letter.

The moral: when you learn more about the possible choices, the information it takes to describe a choice drops.


## THE INFORMATION IN A LICENSE PLATE

How much unknown information do the atoms in a license plate contain?

Aluminum has an entropy of about twenty-eight joules per kelvin per mole at standard temperature and pressure. A mole of aluminum weighs about twenty-seven grams. A typical license plate might weigh one hundred fifty grams, and thus have one hundred fifty grams times twenty-seven grams per mole twenty-eight joules per kelvin per mole equals approximately one hundred sixty joules per kelvin of entropy. But a joule per kelvin of entropy is about ten to the twenty-three bits of unknown information. Thus, the atoms in such a license plate contain about one hundred sixty times ten to the twenty-three bits approximately one point six times ten to the twenty-five bits of unknown information.

Last time we talked about the information in a license plate number. A license plate number made of seven numbers and or letters contains log base two of three hundred sixty-seven approximately thirty-six point one eight nine bits of information if all combinations are equally likely. How does this compare to the information in the actual metal of the license plate?

These days most license plates are made of aluminum, and they weigh roughly between one hundred and two hundred grams. Let's say one hundred fifty grams. If we work out the entropy of this much aluminum, and express it in bits of unknown information, we get an enormous number: roughly sixteen septillion bits!

Here is the point. While the information on the license plate and the information in the license plate can be studied using similar mathematics, the latter dwarfs the former. Thus, when we are doing chemistry and want to know, for example, how much the entropy of the license plate increases when we dissolve it in hydrochloric acid, the information in the writing on the license plate is irrelevant for all practical purposes.

Some people get fooled by this, in my opinion, and claim that "information" and "entropy" are fundamentally unrelated. I disagree.


## JUSTIFYING THE FORMULA FOR INFORMATION

Why do we say the information of an event of probability P is

I of P equals negative log P

for some base B greater than one? Here's why:

Theorem. Suppose I of zero to one maps to the real numbers is a function that is:

One. Decreasing: P less than Q implies I of P greater than I of Q. This says less probable events have more information.

Two. Additive: I of P times Q equals I of P plus I of Q. This says the information of the combination of two independent events is the sum of their separate informations.

Then for some base B greater than one we have I of P equals negative log P.

The information of an event of probability P is negative log P, where you get to choose the base of the logarithm. But why? This is the only option if we want less probable events to have more information, and information to add for independent events.

Proving this will take some math-but don't worry, you won't need to know this stuff for the rest of this course.

Since we're trying to prove I of P is a logarithm function, let's write and prove F has to be linear:

F of X equals C X.

As we'll see, this gets the job done.

X less than Y implies F of X greater than F of Y for all X, Y less than or equal to zero.

Similarly, we can check that Condition Two is equivalent to

F of X plus Y equals F of X plus F of Y for all X, Y less than or equal to zero.

Now what functions F have

F of X plus Y equals F of X plus F of Y

for all X, Y less than or equal to zero?

If we define F of negative X equals negative F of X, F will become a function from the whole real line to the real numbers, and it will still obey F of X plus Y equals F of X plus F of Y. So what functions obey this equation? The obvious solutions are

F of X equals C X

for any real constant C. But are there any other solutions?

Yes, if you use the axiom of choice! Treat the reals as a vector space over the rationals. Using the axiom of choice, pick a basis. To get F maps the real numbers to the real numbers that's linear over the rational numbers, just let F send each basis element to whatever real number you want and extend it to a linear function defined on all of the real numbers. This gives a function F that obeys F of X plus Y equals F of X plus F of Y.

However, no solutions of F of X plus Y equals F of X plus F of Y meet our other condition

X less than Y implies F of X greater than F of Y for all X, Y less than or equal to zero except for the familiar ones F of X equals C X. For a proof see Wikipedia: they show all solutions except the familiar ones are so discontinuous their graphs are dense in the plane!

I of P equals C l n P

but this equals negative log P if we take B equals exp of negative one divided by C. And this number B can be any number greater than one. QED.

Thus, if we want a more general concept of the information associated to a probability, we need to drop Condition one or two. For example, we could replace additivity by some other rule. People have tried this! Indeed, there is a world of generalized entropy concepts including Tsallis entropies, Renyi entropies and others.


## WHAT IS PROBABILITY?

Since I've defined information in terms of probability, you may naturally wonder "what is probability?" I won't seriously try to answer this. This question has stirred up many debates over the centuries, and even today there's not a fully accepted answer. It deserves a whole book-and this is not that book. Luckily, we don't really need to know exactly what probability is to do calculations with it: we mainly need to set up some rules for working with it. This may seem like a cop-out. But it's a strange and wonderful feature of science that we can achieve great reliability in our results by sidestepping certain difficult questions, like someone who can make their way safely through a jungle by avoiding the quicksand and snakes.

One approach to probability goes like this. Suppose you repeat some experiment N times, doing your best to make the conditions the same each time. Suppose that M of these times some event E occurs. You may then say that the probability of event E happening under these conditions is M over N. This approach is called 'finite frequentism'. Unfortunately, this approach can lead you to say a coin has probability one of landing heads up if it does so the first time, or first three times, you flip it.

Another approach goes like this. You may say that some event E has probability p under some conditions if when you set up these conditions N times, and the event E happens M times, the fraction M over N approaches p in the limit N goes to infinity. This approach is called 'hypothetical frequentism', because in real experiments you can't take the limit N to infinity. But you can hope that when N becomes large enough, the fraction M over N usually becomes close to the limiting probability p-whatever that means.

Another approach, called 'Bayesianism', treats a probability of an event E under some specified conditions as a measure of your degree of belief that E will happen under these conditions. But what is 'degree of belief'? One answer involves bets. For example, perhaps to believe an event has probability one half means you're willing to take a bet where you win more when the event happens than you lose if it does not.

Bayesians tend to focus on the rules for updating your probabilities as you learn new things, the most famous being 'Bayes' rule'. Even if agents start by assigning different probabilities to an event, if they follow the same rules for changing these probabilities as they learn new things, under certain circumstances we can prove their probabilities will converge to the same value.

For a passionate and intelligent discussion of these issues, I recommend E. T. Jaynes' book Probability Theory: the Logic of Science. Later we'll meet his 'principle of maximum entropy', another important approach to working with probabilities.


## PROBABILITY MEASURES

A measure on a set X is a function that assigns to certain so-called measurable subsets S of X a number p of S in the interval from zero to one, obeying these rules:

. The empty set and X are measurable and m of the empty set equals zero

. If S, T in X are measurable and S is a subset of T, then T minus S is measurable and m of T equals m of S plus m of T minus S

. If a countable collection of disjoint subsets Si of X are measurable, then their union is measurable and m of the union of Si equals the sum of m of Si i equals one to infinity

We say m is a probability measure if m of X equals one.

It is easier to do calculations with probabilities than say exactly what they mean! I will take a rough-and-ready approach to working with them, but first let's take a peek at how mathematicians do it. If you don't care, it's safe to move right on to the next tweet.

We start with any set. We call elements of X 'outcomes' and subsets of X 'events'. We can sometimes get into trouble trying to assign a probability to every subset of X. So, we'll only try to assign probabilities to events in some collection M with these properties:

· The empty set is in M and X is in M.

. If S, T are in M and S is a subset of T then the set of elements of T that are not in S, called T minus S, is in M.

. If Si is in M for i equals one, two, and so on then the union Si is in M.

We call elements of M measurable subsets of X. A measure is then a function m from M to zero to one obeying these rules:

· m of the empty set equals zero

· If S, T are in M and S is in M then m of T equals m of S plus m of T minus S.

. If Si is in M then m of the union Si equals the sum of m of Si.

If M also obeys m of X equals one then we say M is a probability measure, and for any S in M we say m of S is the probability of the event S. But we will also be interested in other measures, like the measure on the real line called 'Lebesgue measure'. This is closely connected to the symbol d x that shows up in integrals, because for any measurable set S is a subset of the reals, its Lebesgue measure is

The integral from negative infinity to infinity chi sub S of x d x where chi sub S of x is one for x in S and zero for x not in S. Indeed, people often get sloppy and say d x "is" Lebesgue measure, and I may do that too. By the way, Lebesgue measure is one where we cannot take script M to be the collection of all subsets of the set of real numbers. There is an extensive theory of measures. We will not need it here, but if you're interested, you can try a book like Halsey Royden's Real Analysis, where I learned the basics myself, or Terry Tao's An Introduction to Measure Theory, which has a legal free version online.

Here are some puzzles about measures.

Puzzle ten. Let X be any set and define script M to be the collection of all subsets of X. Show that there is a measure m from script M to open zero to infinity closed called counting measure such that for any S subset X, m of S is the number of elements of S, infinity if S is infinite.

Puzzle eleven. Let X be any set and define script M as before. Suppose P is a probability distribution on X, meaning a function P from X to open zero to infinity closed with the sum over i in X P of i equals one. Show that there is a probability measure m from script M to open zero to infinity closed such that for any

S subset X, m of S equals the sum over i in S P of i. In this situation we usually write P of i as P sub i and call it the probability of the outcome i in X. For any S subset or equal to M we call m of S the probability of the event

S. In the next puzzles X is any set, script M obeys the three rules for a collection of measurable subsets of X, and m from script M to open zero to infinity closed is a measure.

Puzzle twelve. Show that if S, T in script M then the union S union T is in script M. Puzzle thirteen. Show that if S, T in script M then the intersection S intersection T is in script M. Puzzle fourteen. Show that if S sub i in script M for i equals one, two, and so on then the intersection from i equals one to infinity S sub i is in script M. Puzzle fifteen. Show that if S, T in script M and S subset or equal to T then m of S less than or equal to m of T. Puzzle sixteen. Show that if S sub i in script M for i equals one, two, and so on then m of the union from i equals one to infinity S sub i less than or equal to the sum from i equals one to infinity m of S sub i. Puzzle seventeen. Show that if m is a probability measure and S in script M then zero less than or equal to m of S less than or equal to one. One of the main uses of a measure m on a space X is that it lets us integrate certain functions f from X to the set of real numbers. Alas, not all functions! It's only reasonable to try to integrate measurable functions f from X to the set of real numbers, which have the property that if S subset or equal to the set of real numbers is measurable, its inverse image f inverse of S subset or equal to X is measurable. And even measurable functions can cause trouble, because when we try to integrate them we might get positive infinity, negative infinity, or something even worse. For example, what's

The integral from negative infinity to infinity of x squared sine x d x ? There's no good answer. We say a function f from X to the real numbers is integrable if it is measurable and its integral over X, defined in a certain way I won't explain here, gives a well-defined real number.


## Shannon Entropy: A First Taste

When you learn an event of probability P has happened, the amount of information you get is negative log P.

Question. Suppose you know a coin lands heads up two thirds of the time and tails up one third of the time. What is the average or 'expected' amount of information you get when you learn which side landed up?

Answer. Two thirds of the time you get negative log two thirds of information, and one third of the time you get negative log one third. So, the expected amount of information you get is negative two thirds log two thirds, and negative one third log one third.

You can do the same thing whenever you have any number of probabilities that add to one. The expected information is called the Shannon entropy.

You flip a coin. You know the probability that it lands heads up. How much information do you get, on average, when you discover which side lands up? It's not hard to work this out. It's a simple example of Shannon entropy. Roughly speaking, entropy is information that you don't know, that you could get if you did enough experiments. Here the experiment is simply flipping the coin and looking at it.

Puzzle eighteen. Suppose you know a coin lands heads up half of the time and tails up half of the time. What is the expected amount of information you get from a coin flip? If you use base two for the logarithm, you get the expected information measured in bits. What do you get?

Puzzle nineteen. Suppose you know a coin lands heads up one third of the time and tails up two thirds of the time. What is the expected amount of information you get from a coin flip?

Puzzle twenty. Suppose you know a coin lands heads up one fourth of the time and tails up three fourths of the time. What is the expected amount of information you get from a coin flip, in bits?

If you solve these you'll see a pattern: the Shannon entropy is biggest when the coin is fair. As it becomes more and more likely for one side to land up than the other, the entropy drops. You're more sure about what will happen, so you learn less, on average, from seeing what happens!

We've been doing examples where your experiment has just two possible outcomes: heads up or down. But you can do Shannon entropy for any number of outcomes. It measures how ignorant you are of what will happen. That is: how much you learn on average when it does!


## Shannon Entropy: A Second Taste

According to the weather report there's a one fourth chance that it will rain one centimeter, one half chance it will rain two centimeters, and one fourth chance it will rain three centimeters.

Question. What is the 'expected' amount of rainfall?

Answer. One fourth times one plus one half times two plus one fourth times three equals two centimeters.

Question. What is the 'expected' amount of information you learn when you find out how much it rains?

Answer. Three halves minus one fourth log one fourth minus one half log one half minus one fourth log one fourth equals three halves log two, or in other words, three bits. This is the Shannon entropy of the weather report.

If the weather report tells you it'll rain different amounts with different probabilities, you can figure out the 'expected' amount of rain. You can also figure out the expected amount of information you'll learn when it rains. This is called the 'Shannon entropy'.

Shannon entropy is closely connected to information, but we can also think of it as a measure of ignorance. This may seem paradoxical. But it's not. Shannon entropy is the expected amount of information that you don't know when all you know is a probability distribution, which you will know when you see a specific outcome chosen according to this probability distribution.

For example, consider a weather report that says it will rain one centimeter with probability zero, two centimeters with probability one, and three centimeters with probability zero. The Shannon entropy of this weather report is

Negative zero log zero minus one log one minus zero log zero equals zero since by convention we set P log P equals zero when P equals zero, this being the limit of P ln P as P approaches zero from above.

What does it mean that this weather report has zero Shannon entropy? It means that when we see a specific outcome chosen according to this probability distribution, we learn nothing! The weather report says it will rain two centimeters with probability one. When this happens, we learn nothing that the weather report didn't already tell us.

The Shannon entropy doesn't depend on the amounts of rain, or even whether the forecast is about centimeters of rain or dollars of income. It only depends on the probabilities of the various outcomes. So Shannon entropy is a universal, abstract concept.

Shannon entropy is closely connected to Gibbs entropy, which was already known in physics. But by lifting entropy to a more general level and connecting it to digital information, Shannon helped jump-start the information age. In fact a paper of his was the first to use the word 'bit'!


## The Definition of Shannon Entropy

Suppose you believe there are n possible outcomes with probabilities P1, P2, up to Pn greater than or equal to zero that sum to one.

The average amount of information you learn when one of these outcomes happens, chosen according to this probability distribution, is the Shannon entropy:

H equals negative sum of P i log P i for i equals one to n.

Shannon entropy is larger for probability distributions that are more spread out, and smaller for probability distributions that are more sharply peaked.

I've been leading up to it with examples, but here it is in general: Shannon entropy! Gibbs had already used a similar formula in physics-but with base e for the logarithm, an integral instead of a sum, and multiplying the answer by Boltzmann's constant. Shannon applied it to digital information.

Here's where the formula for Shannon entropy comes from. We have some set of outcomes, say X. We have a probability distribution on this set, meaning a function P from X to the interval from zero to one such that

The sum of P i from i in X equals one.

If we have any function A from X to the real numbers, we define its expected value to be the sum of P i A i for i in X.

It's a kind of average of A where each value A(i) is 'weighted', i.e. multiplied, by the probability of the ith outcome. We saw an example in the last tweet: the expected amount of rainfall.

We've seen that if you believe the ith outcome has probability p_i, the amount of information you learn if the ith outcome actually occurs is negative log p_i. Thus, the expected amount of information you learn is negative sum of p_i log p_i.

And this is the Shannon entropy! We denote it by H, or more precisely H of p, so

H of p equals negative sum of p_i log p_i. In the box above I was taking X to be the set {1, ... , n}. This is often a good thing to do when there are finitely many outcomes.

Let's get to know the Shannon entropy a little better.

Puzzle twenty-one. Let X equal one, two so that we know a probability distribution p on X if we know p sub one, since p sub two equals one minus p sub one. Graph the Shannon entropy H of p as a function of p sub one. Show that it has a maximum at p sub one equals one half and minima at p sub one equals zero and p sub one equals one. This makes sense: if you believe p sub one equals one then you learn nothing when an outcome happens chosen according to the probability distribution p: you are sure outcome one will occur, and it does (with probability one). Similarly, if you believe p sub one equals zero you learn nothing when an outcome happens according to this probability distribution, since you are sure outcome two will occur. On the other hand, if p sub one equals one half you are maximally undecided about what will happen, and you learn one bit of information when it does.

Puzzle twenty-two. Let X equal one, two, three. Draw the set of probability distributions on X as an equilateral triangle whose corners are the probability distributions (one, zero, zero), (zero, one, zero), and (zero, zero, one). Sketch contour lines of H of p as a function on this triangle. Show it has a maximum at p equals (one third, one third, one third) and minima at the corners of the triangle.

Again this should make intuitive sense. Here is a harder puzzle along the same lines:

Puzzle twenty-three. Let X equal {one, ..., n}. Show that H of p has a maximum at p equals (one over n, ..., one over n) and minima at the probability distributions where p sub i equals one for some particular i in X. Here is one of the big lessons from all this:

Shannon entropy is larger for probability distributions that are more spread out, and smaller for probability distributions that are more sharply peaked.

Indeed, you can think of Shannon entropy as a measure of how spread out a probability distribution is! The more spread out it is, the more you learn when an outcome occurs, drawn from that distribution.


## THE PRINCIPLE OF MAXIMUM ENTROPY

Suppose there are n possible outcomes. At first you have no reason to think any is more probable than any other.

Then you learn some facts about the correct probability distribution-but not enough to determine it uniquely! Which probability distribution P one, ..., P n should you choose?

The principle of maximum entropy says:

Of all the probability distributions consistent with the facts you've learned, choose the one with the largest Shannon entropy

H equals negative sum of P_i log P_i.

What's Shannon entropy good for? For starters, it gives a principle for choosing the 'best' probability distribution consistent with what you know. Choose the one that maximizes the Shannon entropy!

This is called the 'principle of maximum entropy'. This principle first arose in statistical mechanics, which is the application of probability theory to physics-but we can use it elsewhere too.

For example: suppose you have a die with faces numbered one, two, three, four, five, six. At first you think it's fair. But then you somehow learn that the average of the numbers that comes up when you roll it is five. Given this, what's the probability that if you roll it, a six comes up?

Sounds like an unfair question! But you can figure out the probability distribution on {one, two, three, four, five, six} that maximizes Shannon entropy subject to the constraint that the mean is five. According to the principle of maximum entropy, you should use this to answer my question!

But is this correct?

The problem is figuring out what 'correct' means! But in statistical mechanics we use the principle of maximum entropy all the time, and it seems to work well. The brilliance of E. T. Jaynes was to realize it's a general principle of reasoning, not just for physics.

The principle of maximum entropy is widely used outside physics, though still controversial. But I think we should use it to figure out some basic properties of a gas-like its energy or entropy per molecule, as a function of pressure and temperature.

To do this, we should generalize Shannon entropy to 'Gibbs entropy', replacing the sum by an integral. Or else we should 'discretize' the gas, assuming each molecule has a finite set of states. It sort of depends on whether you prefer calculus or programming. Either approach is okay if we study our gas using classical statistical mechanics.

Quantum statistical mechanics gives a more accurate answer. It uses a more general definition of entropy-but the principle of maximum entropy still applies!

I won't dive into any calculations just yet. Before doing a gas, we should do some simpler examples-like the die whose average roll is five. But I can't resisting mentioning one philosophical point. In the box above I was hinting that maximum entropy works when your 'prior' is uniform:

Suppose there are N possible outcomes. At first you have no reason to think any is more probable than any other.

This is an important assumption: when it's not true, the principle of maximum entropy as we've stated it does not apply. But what if our set of events is something like a line? There's no obvious best probability measure on the line! And even good old Lebesgue measure D X depends on our choice of coordinates. To handle this, we need a generalization of the principle of maximum entropy, called the principle of maximum relative entropy.

In short, a deeper treatment of the principle of maximum entropy pays more attention to our choice of 'prior': what we believe before we learn new facts. And it brings in the concept of 'relative entropy': entropy relative to that prior. But we won't get into this here, because we will always be using a very bland prior, like assuming that each of finitely many outcomes is equally likely.


## ADMITTING YOUR IGNORANCE

Suppose you describe your knowledge of a system with N states using a probability distribution P one, P two, dot, dot, dot, P N. Then the Shannon information

H equals negative summation P I log P I measures your ignorance of the system's state.

So, choosing the maximum-entropy probability distribution consistent with the facts you know amounts to not pretending to know more than you do.

Remember: if we describe our knowledge using a probability distribution, its Shannon entropy says how much we expect to learn when we find out what's really going on. We can roughly say it measures our 'ignorance'-though ordinary language can be misleading here.

At first you think this ordinary six-sided die is fair. But then you learn that no, the average of the numbers that come up is five. What are the probabilities P one, dot, dot, dot, P N for the different faces to come up?

This is tricky: you can imagine different answers!

You could guess the die lands with five up every time. In other words, P five equals one. This indeed gives the correct average. But the entropy of this probability distribution is zero. So you're claiming to have no ignorance at all of what happens when you roll the die!

Next you might guess that it lands with four up half the time and six up half the time. In other words, P four equals P six equals point five. This probability distribution has one bit of entropy. Now you are admitting more ignorance. But how can you be so sure that five never comes up?

Next you might guess that P four equals P six equals point four and P five equals point two. We can compute the entropy of this probability distribution. It's higher: one point five bits. Good, you're being more honest now! But how can you be sure that one, two, or three never come up? You are still pretending to know stuff!

Keep improving your guess, finding probability distributions with mean five with bigger and bigger entropy. The bigger the entropy gets, the more you're admitting your ignorance! If you do it right, your guess will converge to the unique maximum-entropy solution.

But there's a more systematic way to solve this problem.


## THE BOLTZMANN DISTRIBUTION

Suppose you want to maximize the Shannon entropy negative summation P I log P I

of a probability distribution P one, dot, dot, dot, P N, subject to the constraint that the expected value of some quantity A I is some number C:

summation P I A I equals C (*) for I equals one to N

Then try the Boltzmann distribution:

P I proportional to exp(negative beta A I)

where beta is some parameter.

If you can find beta that makes (*) hold, this is the answer you seek!


## How do you actually use the principle of maximum entropy?

If you know the expected value of some quantity and want to maximize entropy given this, there's a great formula for the probability distribution that usually does the job! It's called the 'Boltzmann distribution'. In physics it also goes by the names 'Gibbs distribution' or 'canonical ensemble', and in statistics it's called an 'exponential family'.

In the Boltzmann distribution, the probability P I is proportional to exp(negative beta A I) where A is the quantity whose expected value you know. Since probabilities must sum to one, we must have summation exp(negative beta A I) for I equals one to N in the denominator.

P I equals this expression scaled so that the total probability is one.

It is then easy to find the expected value of A as a function of the number beta: just plug these probabilities into the formula expected value of A equals summation A I P I for I equals one to N.

The hard part is inverting this process and finding beta if you know what you want the expected value of A to be.

When and why does the Boltzmann distribution actually work? That's a bit of a long story, so I'll explain it later. First, let's use the Boltzmann distribution to solve the puzzle I mentioned last time:

At first you think this ordinary six-sided die is fair. But then you learn that no, the average of the numbers that come up is five. What are the probabilities P one, dot, dot, dot, P N for the different faces to come up? You can use the Boltzmann distribution to solve this puzzle!

To do it, take one less than or equal to I less than or equal to six and A I equals I. Stick the Boltzmann distribution P I into the formula summation A I P I equals five and get a polynomial equation for exp(negative beta). You can solve this with a computer and get exp(negative beta) approximately one point eight seven seven.

So, the probability of rolling the die and getting the number one through six is proportional to exp(negative beta I) approximately one point eight seven seven to the power I. You can figure out the constant of proportionality by demanding that the probabilities sum to one-or just look at the formula for the Boltzmann distribution. You should get these probabilities:

You can compute the entropy of this probability distribution, and you get roughly one point nine seven bits. You'll remember that last time we got entropies up to one point five bits just by making some rather silly guesses.

So, using the Boltzmann distribution, you can find the maximum-entropy die that rolls five on average. Later, we'll see how the same math lets us find the maximum-entropy state of a box of gas that has some expected value of energy!


## MAXIMIZATION SUBJECT TO A CONSTRAINT

To maximize a smooth function F of several variables subject to a constraint on some smooth function G, look for a point where the gradient of F is equal to lambda times the gradient of G for some number lambda.

When we're trying to maximize entropy subject to a constraint, we're doing a problem of the above sort. If you don't know how to do problems like this, it's time to learn about Lagrange multipliers. You can find this in any book on calculus of several variables. But the idea is in the picture above. Say we've got two smooth functions f, g: RN maps to R and we have a point on the surface g equals constant where f is as big as it gets on this surface. The gradient of f must be perpendicular to the surface at this point. Otherwise we could move along the surface in a way that made f bigger! For the same reason, the gradient of g is always perpendicular to the surface g equals constant. So gradient f and gradient g must point in the same or opposite directions at this point. Thus, as long as the gradient of g is nonzero, we must have gradient f equals lambda gradient g for some number lambda, called a Lagrange multiplier. So, solving this equation along with g equals constant is a way to find the point we're looking for-though we still need to check we've found a maximum, not a minimum or something else.

We can write a formula that means the exact same thing as gradient f equals lambda gradient g using differentials:

df equals lambda dg

This is what we'll do from now on. Gradients are vector fields while differentials are one-forms. If you don't know what this means, you can probably ignore this for now: the difference, while ultimately quite important, will not be significant for anything we're doing.


## MAXIMIZING ENTROPY SUBJECT TO A CONSTRAINT

To maximize the entropy

H equals negative the sum from i equals one to n of pi ln pi

Pi In pi subject to a constraint on the expected value

A equals the sum from i equals one to n of pi Ai it's good to look for a probability distribution such that dH equals lambda dA

for some number lambda. This will then be a Boltzmann distribution:

exp of negative lambda times Ai

Pi equals the sum from j equals one to n of exp of negative lambda times Aj

We've seen how to maximize a function subject to a constraint. Now let's do the case we're interested in: maximizing entropy subject to a constraint on the expected value of some quantity.

Suppose we have a finite set of outcomes, say one, two, ..., n. Our 'quantity' A is just a number A1, A2, ..., An depending on the outcome. For any probability distribution p on the set of outcomes, we can define its Shannon entropy and the expected value of A:

H equals negative the sum from i equals one to n of pi ln pi, A equals the sum from i equals one to n of pi Ai.

Here we are using base e for the Shannon entropy, to simplify the calculations. Let's try to find the probability distribution that maximizes H on the surface A equals c. We'll show that if such a probability distribution p exists, and none of the pi are zero, then p must be a Boltzmann distribution the sum from j equals one to n of exp of negative lambda times Aj

Pi equals the sum from i equals one to n of exp of negative lambda times Ai for some lambda in R. If you're willing to trust me on this, you can skip this calculation.

To use the method from last time the Lagrange multiplier method-we'd like to use the probabilities pi as coordinates on the space of probability distributions. But they aren't independent, since the sum from i equals one to n of pi equals one. To get around this, let's use all but one of the pi as coordinates, and remember that the remaining one is a function of those. Let's use p2, P3, ..., Pn as coordinates, so that P1 equals one minus the sum of p2, ..., Pn. Furthermore, the space of all probability distributions on our finite set is the set of P such that zero is less than or equal to Pi is less than or equal to one, and the sum from i equals one to n of P equals one. It looks like a closed interval when n equals two, or a triangle when n equals three, or a tetrahedron when n equals four, or some higher-dimensional version of a tetrahedron when n is larger. In its interior this space looks locally like RN minus one, so we can use the Lagrange multiplier method, but it also has a boundary where one or more of the pi vanish, and then this method no longer applies. (We'll see an example of that later.)

So, let's assume p is a probability distribution maximizing the Shannon entropy H on the surface A equals c, and also suppose p has p1, ..., Pn greater than zero. Suppose that not all the values Ai are equal, since that makes the problem too easy-see why? Then dA is never zero, so from what I said last time, we must have dH equals lambda dA

at the point p. So let's see what this equation actually says.

Since

H equals negative the sum from i equals one to n of pi ln pi we have dH equals negative the sum from i equals one to n of d(pi ln pi) equals negative the sum from i equals one to n of (one plus ln pi) dpi.

Similarly, since

A equals the sum from i equals one to n of pi Ai we have dA equals the sum from i equals one to n of Ai dpi.

So, our equation dH equals lambda dA says negative the sum from i equals one to n of (one plus ln pi) dpi equals lambda times the sum from i equals one to n of Ai dpi.

For these to be equal, the coefficients of dpi must agree for each of our coordinates P2, ..., Pn. But we have to remember that p1 equals one minus (p2 plus ... plus Pn) and thus dp1 equals negative (dp2 plus ... plus dpn). Thus, for each i equals two, ..., n we have

(one plus ln p1) minus (one plus ln pi) equals lambda times negative A1 plus Ai and fiddling around we get exp of negative lambda times A1 over exp of negative lambda times Ai equals P1 over Pi

This says something cool: the probabilities p sub i are proportional to the exponentials exp of negative lambda Ai. And since the probabilities must sum to one, it's obvious what the constant of proportionality must be:

p sub i equals exp of negative lambda Ai over the sum from i equals one to n of exp of negative lambda Ai. So yes: p sub i must be given by the Boltzmann distribution!

In summary, we've seen that if there exists a probability distribution p that maximizes the Shannon entropy among probability distributions with expected value A equals c, and if all the p sub i are positive, then p must be a Boltzmann distribution. But this raises other questions. When does such a probability distribution exist? If it exists, is it unique? And what if not all the p sub i are positive?

In what follows we'll dive down this rabbit hole and get to the bottom of it. I'll just state some facts-you may enjoy trying to see if you can prove them. First, there exists a probability distribution p sub one, ..., p sub n with expected value A equals c if and only if

A sub min is less than or equal to c is less than or equal to A sub max where A sub min is the minimum value and A sub max is the maximum value of the numbers A sub one through A sub n. Second, whenever

A sub min is less than c is less than A sub max, there exists a unique probability distribution P sub one through P sub n maximizing Shannon entropy subject to the constraint expected value A equals c. Third, this unique maximizer P has P sub i greater than zero for all i, and is thus a Boltzmann distribution, whenever

A sub min is less than c is less than A sub max. When c equals A sub min, the unique maximizer assigns the same probability P sub i to each outcome i with A sub i equals A sub min, while P sub i equals zero for all other outcomes. Similarly, when c equals A sub max, the unique maximizer assigns the same probability P sub i to each outcome i with A sub i equals A sub max, while P sub i equals zero for all other outcomes.

It's good to look at an example:

Puzzle twenty-four. Suppose there are only two outcomes, with A sub one equals negative one and A sub two equals one. Work out the Boltzmann distribution P maximizing Shannon entropy subject to the constraint expected value A equals c for negative one is less than c is less than one. Show that as lambda approaches positive infinity this Boltzmann distribution has

P sub one approaches one, P sub two approaches zero while as lambda approaches negative infinity it has

P sub one approaches zero, P sub two approaches one. Show the probability distribution P sub one equals one, P sub two equals zero maximizes Shannon entropy subject to the constraint expected value A equals negative one, while P sub one equals zero, P sub two equals one maximizes it subject to the constraint expected value A equals one. Show these two probability distributions are not Boltzmann distributions.


## THERMAL EQUILIBRIUM

Suppose a system has finitely many states i equals one through n with energies E sub i. If the probability P sub i that it's in the i-th state maximizes entropy subject to a constraint on its expected energy:

expected value of E equals sum of P sub i times E sub i from i equals one to n we say it is in thermal equilibrium. In this case P sub i is given by a Boltzmann distribution

P sub i equals greater than exp(negative E sub i)

at least if all the probabilities P sub i are positive.

Don't worry: the substance of what I'm saying here is almost the same as in the last box. I'm merely attaching new words to the concepts, to make them sound more like physics:

Before I said we had a set of n 'outcomes' numbered one, two, and so on, up to n. Now I'm talking about 'states'. If we have a system with n states, it means there are n outcomes when we do a measurement to completely determine which state it's in. A 'state' is some way for a physical system to be that's vague but it's all we can say until we consider some specific kind of system. In classical physics the states form a set, usually infinite but sometimes finite.

Before I said we had a 'quantity' A that depends on the outcome, taking the value A sub i in the i-th outcome. Now I'm calling this quantity the 'energy' E. Energy is a particularly interesting quantity in physics, so we'll focus on that, without demanding that you know anything about it: for our present purposes, we can take any quantity and dub it 'energy'.

Before I called the Lagrange multiplier lambda. Now I'm calling it beta, because that's what physicists do in this particular context.

When a system maximizes entropy subject to a constraint on the expected value of its energy, and perhaps also some other quantities, we say the system is in thermal equilibrium. This is meant to suggest that an object just sitting there, not heating up or cooling down, is often best modeled this way.

You may have noticed the annoying clause "at least if all the probabilities P sub i are positive". I only said that because I cannot tell a lie. In Puzzle twenty-four we saw that as beta approaches infinity, the Boltzmann distribution can converge to a non-Boltzmann probability distribution where some of the probabilities P sub i vanish. This still counts as thermal equilibrium, because it's still maximizing entropy subject to a constraint on expected energy. We'll learn more about this when we study the concept of 'absolute zero'.


## COOLNESS

If a probability distribution P sub i maximizes entropy subject to a constraint on the expected value of the energy E sub j, then

P sub i equals beta E sub i where beta is the coolness, inversely proportional to temperature. So:

The cooler a system is, the less likely it is to be in a high-energy state!

Say a system with finitely many states maximizes entropy subject to a constraint on the expected value of some quantity E that we choose to call 'energy'. Then its probability of being in the ith state is proportional to exp(negative B E i) for some number.

When B is big and positive, the probability of being in a state of high energy is tiny, since exp(negative B E i) gets very small for large energies E j. This means our system is cold.

Conversely when B is small and positive, exp(negative B E i) drops off very slowly as the energy E i gets bigger. So, high-energy states become quite likely when B is small and positive. This means our system is hot.

It turns out B is inversely proportional to the temperature more about that later. But in modern physics, B is just as important as temperature. It comes straight from the principle of maximum entropy!

So B deserves a name. And its name is 'coolness'.

By the way, the formula

Pi equals B E i is only strictly true when B is finite. There's also a limiting case B approaches plus zero, when pi equals zero except for states of the very lowest energy. And there's a limiting case B approaches negative zero, where Pi equals zero except for states of the very highest energy. I'll say a bit about these oddities later. First I'll say more about what coolness has to do with temperature.


## COOLNESS VERSUS TEMPERATURE

Coolness B is inversely proportional to temperature T:

where k is Boltzmann's constant.

Coolness is measured in joules to the negative one, temperature is measured in kelvin, and Boltzmann's constant is a conversion factor:

k equals one point three eight zero six four nine times ten to the negative twenty-three joules kelvin

In statistical mechanics, coolness is inversely proportional to temperature. But coolness has units of energy to the negative one, not temperature to the negative one. So we need a constant to convert between coolness and inverse temperature! And this constant is very interesting.

Remember: when a system maximizes entropy with a constraint on its expected energy, the probability of it having energy E is proportional to exp(negative B E) where B is its coolness. But we can only exponentiate dimensionless quantities! (Why?) So B has dimensions of one over energy.

Since coolness is inversely proportional to temperature, we must have B equals one over k T where k is some constant with dimensions of energy over temperature. This constant k is called 'Boltzmann's constant'. It's tiny:

k equals one point three eight zero six four nine times ten to the negative twenty-three joules per kelvin,

This is mainly because we use units of energy, joules, suited to macroscopic objects like a cup of hot water. Boltzmann's constant being tiny reveals that such things have enormously many microscopic states!

Later we'll see that a single classical point particle, in empty space, has energy three k T divided by two when it's maximizing entropy at temperature T. The three here is because the atom can move in three directions, the one half because we integrate x squared to get this result. The important part is k T. The k T says: if an ideal gas is made of atoms, each atom contributes just a tiny bit of energy per kelvin, or degree Celsius: roughly ten to the negative twenty-three joules. So a little bit of gas, like a gram of hydrogen, must have roughly ten to the twenty-three atoms in it. This is a very rough estimate, but it's a big deal.

Indeed, the number of atoms in a gram of hydrogen is about six times ten to the twenty-three. You may have heard of Avogadro's number-this is quite close to that. So Boltzmann's constant gives a hint that matter is made of atoms-and even better, a nice rough estimate of how many per gram!

Later we will see that Boltzmann's constant has another important meaning: it's a fundamental unit of entropy, a nat, expressed in joules per kelvin.


## TEMPERATURE

If a system has finitely many states with energies E i, in thermal equilibrium at temperature T the probability that it's in the ith state is Pi propotional to exp(negative E i over k T)

where k is Boltzmann's constant and T can be positive, negative, or even infinite:

T equals infinity

T is less than zero

T is greater than zero

A system with finitely many states can be pretty weird. It can have negative temperature! Even weirder: as you heat it up, its temperature becomes large and positive, then it reaches infinity, and then it 'wraps around' and becomes large and negative.

The reason: coolness is more fundamental than temperature. The coolness B is inversely proportional to the temperature T:

B equals one over k T.

When the temperature goes up to infinity and then suddenly becomes a large negative number, it's really just the coolness going down to zero and becoming negative. Temperatures 'wrap around' infinity, as shown in the picture.

A system with finitely many states can have negative or infinite temperature because in thermal equilibrium, its probability of being in the ith state is proportional to exp(negative B E i) over the sum of exp(negative B E i) from i equals one to n.

Pi where E i is the energy of the ith state, and this makes sense for any B in the reals. Moreover, the probability pi depends continuously on B, even as B passes through zero. This means a large positive temperature is almost like a large negative temperature!

But the circle of temperature can be misleading. Temperatures wrap around T equals infinity but not T equals zero. A system with a small positive temperature is very different from one with a small negative temperature! That's because pi for B is much greater than zero is very different than it is for B is less than zero.

For a system with finitely many states we can take the limit of the Boltzmann distribution when B approaches plus zero; then the system will only occupy its lowest-energy state or states. We can also take the limit when B approaches negative infinity; then the system will only occupy its highest-energy state or states. In terms of temperature, this means that the limit where T approaches zero from above is very different than the limit where T approaches zero from below.

So, for a system with finitely many states, the best picture of possible thermal equilibria is not a circle of temperatures but a closed interval of coolness: the coolness B can be anything in negative zero to plus infinity, which topologically is a closed interval. In terms of coolness, plus zero is different from negative zero, but approaching zero from above is the same as approaching it from below. But in terms of temperature, approaching zero from above is different from approaching zero from below, while a temperature of infinity is the same as a temperature of negative zero.

Now, if all this seems very weird, here's why: we often describe physical systems using infinitely many states, with a lowest possible energy but no highest possible energy. In this case the sum in the Boltzmann distribution can't converge for B is less than zero, so negative temperatures are ruled out.

However, some physical systems can be approximately described using a finite set of states (or in quantum theory, a finite-dimensional Hilbert space of states). Then the things I just said hold true! And people enjoy studying these systems, and their strange properties, in the lab.

It's good to look at a simple example, and work everything out explicitly:

Puzzle twenty-five. Suppose a system has two states with energies E one and E two. Compute the probabilities pi that it is in either of these states in thermal equilibrium as a function of the coolness B. Then express these probabilities as a function of the temperature T. Using these functions pi(T):

Show that when zero is less than T and T is less than infinity, the system is more likely to be in the lower-energy state: P one of T is greater than p two of T.

. Show that when negative infinity is less than T is less than zero the system is more likely to be in the higher-energy state: P one of T is less than p two of T.

· Show that

T approaches positive infinity, the limit pi of T equals the limit pi of T as T approaches negative infinity.

so we can speak unambiguously of the probabilities p at infinite temperature.

· Show that at infinite temperature the system has an equal probability of being in either state.

· Show that as T approaches zero from above, the probability of the system being in the lower energy state approaches one.

· Show that as T approaches zero from below, the probability of the system being in the higher energy state approaches one.


## INFINITE TEMPERATURE

If a system has finitely many states with energies E i, in thermal equilibrium at temperature T the probability that it's in the i-th state is

Pi proportional to e to the power of B E i.

where B equals one divided by k T and k is Boltzmann's constant.

When B equals zero the system's temperature becomes infinite, and all states become equally probable!

The probability of finding a system in a particular state decays exponentially with energy when the coolness beta is positive. But for a system with finitely many states, beta can be zero. Then it becomes equally probable for the system to be in any state!

Zero coolness means 'utter randomness': that is, maximum entropy.

Here's why. The probability distribution with the largest entropy is the one where all probabilities pi are all equal. This happens at zero coolness! When beta equals zero we get exp of negative beta E i equals one for all i. The probabilities pi are proportional to these numbers exp of negative beta E i equals one, so they're all equal.

It seems zero coolness is impossible for a system with infinitely many states. With infinitely many states, all equally probable, the probability of being in any state would be zero. In other words, there's no uniform probability distribution on an infinite set.

One way out: replace sums with integrals. For the usual measure on zero to one, called the Lebesgue measure dx, we have the integral from zero to one of dx equals one. So this is a 'probability measure' that we could use to describe a system at zero coolness, whose space of states is zero to one.

But replacing sums by integrals raises all sorts of interesting issues. For example, there's a unique way to sum over a finite set of states, but an integral over an infinite set of states depends on a choice of measure. So a choice of measure is a significant extra structure we're slapping on our set of states.

We'll need to think about these issues later, since to compute the entropy of a classical ideal gas we'll need integrals. But we'll encounter difficulties, which are ultimately resolved using quantum mechanics.

Anyway: infinite temperature is really zero coolness, and at least for systems with finitely many states, the entropy becomes as large as possible at zero coolness.


## NEGATIVE TEMPERATURE

If a system has finitely many states with energies E sub i, in thermal equilibrium at temperature T the probability that it's in the i-th state is p sub i proportional to e to the power of negative beta E sub i where beta equals one divided by k T and k is Boltzmann's constant.

When beta is less than zero the system becomes 'hotter than infinitely hot'. Its temperature is negative-but the higher the energy of a state, the more probable it is!

A system with finitely many states can reach infinite temperature. It can get even hotter, but then its temperature 'wraps around' and become negative!

The possibility of negative temperatures was first discussed by the physicist Lars Onsager in nineteen forty-nine, and they have been created in the lab with a variety of systems that-within some approximation-can be described as having finitely many states. In quantum theory, this happens for systems that have finite basis of 'energy eigenstates': states with well-defined energies E sub i. For example, the nucleus of an atom may have just two spin states, and if we put it in a magnetic field these will have different energies. The result is the system we studied in Puzzle twenty-five.

Here is a generalization with more energy states, all equally spaced:

Puzzle twenty-six. Consider a system with two N plus one states labeled by an integer n with negative N less than or equal to n less than or equal to N, where the n-th state has energy E sub n equals alpha n for some energy alpha greater than zero. Compute the Boltzmann distribution for this system at coolness beta for all beta in the real numbers. Compute the expected energy E as a function of beta. What is the qualitative difference in your result between the case of positive temperature beta greater than zero and negative temperature beta less than zero. For more, try this:


## ABSOLUTE ZERO: THE LIMIT OF INFINITE COOLNESS

If a system with finitely many states having energies E; is in thermal equilibrium, the probability p that it's in the i-th state is proportional to exp of negative beta E i where beta is the coolness.

In the limit of infinite coolness, beta approaches positive infinity, these probabilities go to zero except for the states of lowest energy, which all become equally probable.

The limit beta approaches positive infinity is also the limit where T approaches zero from above, commonly called absolute zero.

The limit where T approaches zero from above is often called absolute zero. Why? First people made up various temperature scales like Celsius, where zero was the freezing point of water, and Fahrenheit, where zero is the freezing point of a mixture of water, ice, and ammonium chloride. But researchers discovered that nature had a more fundamental concept of zero temperature: the limit of infinite coolness! This happens as the temperature approaches negative two hundred seventy-three point one five degrees Celsius, or roughly negative four hundred fifty-nine point six seven degrees Fahrenheit. This discovery led Kelvin to propose a shifted version of Celsius where zero is absolute zero. This was originally called 'absolute Celsius', but now it is called the Kelvin scale. This is the scale of temperature I'll always use here. The size of the degrees is a somewhat arbitrary convention, but the zero is not: it's absolute zero.


## THE HAGEDORN TEMPERATURE

If a system has a countable infinity of states n equals one, two, three, and so on, with energies E sub n, the Boltzmann distribution

P sub n equals frac left exp left, negative E sub n over k T right over sum sub n equals one to infinity exp left, negative E sub n over k T right,

One. defined for all zero less than T less than plus infinity Two. undefined for all zero less than T less than plus infinity Three. defined for all zero less than T less than T sub H but not for T sub H less than T less than plus infinity, where T sub H is some temperature called the Hagedorn temperature.

We've been discussing systems with finitely many states, but many physical systems have a countable infinity of states. So let's think a bit about those. We can copy everything we've done so far, but we have to be careful. For thermal equilibrium to be possible at some temperature T, we need the Boltzmann distribution

P sub n equals frac left exp left, negative E sub n over k T right over sum sub n one to infinity exp left, negative E sub n over k T right, to make sense. But it might not. Sometimes the sum fails to converge! This happens when the terms exp left, negative E sub n over k T right don't go to zero fast enough as n approaches plus infinity. Let's investigate this issue. We'll assume that sum sub n equals one to infinity exp left, negative E sub n over k T right converges for some T greater than zero. Then the energies E sub n must be bounded below: otherwise the terms exp left, negative E sub n over k T right will get bigger and bigger. Furthermore for any E in R there can be at most finitely many E sub n less than E: otherwise we'd be adding up infinitely many terms greater than exp left, negative E over k T. As a result, we can reorder the states so their energies are non-decreasing:

E sub one less than or equal to E sub two less than or equal to E sub three less than or equal to and so on, and

E sub n approaches plus infinity. Reordering a sum can't change its convergence or value if it's a sum of nonnegative numbers, like the sum we have here. So we might as well assume we've listed the energies in non-decreasing order as above. Then there are two cases:

One. The energies E sub n approach plus infinity so fast that sum sub n equals one to infinity exp left, negative E sub n over k T right converges for all zero less than T less than plus infinity. Then our system can be in thermal equilibrium at any finite positive temperature. This is the nicest situation, and the one we typically expect.

Two. The energies E sub n approach plus infinity slowly enough that sum sub n equals one to infinity exp left, negative E sub n over k T right converges when T is small enough, but not otherwise. In this case there is some temperature T sub H, called the Hagedorn temperature, such that our system can be in thermal equilibrium at positive temperatures T below T sub H, but not above

T sub H. In both cases, sum sub n equals one to infinity exp left, negative E sub n over k T right diverges for all negative infinity less than or equal to T less than zero and T equals plus infinity. So, for a system with a countable infinity of states, if thermal equilibrium exists for some positive temperature, it cannot exist for negative or infinite temperatures.

The second case is weird and interesting. It's named after Rolf Hagedorn, who in nineteen sixty-four noticed that this was a possibility in nuclear physics. He considered a model of nuclear matter where the energies E sub n approach positive infinity in a roughly logarithmic way. As you heat it, its expected energy keeps increasing, but its temperature can never exceed T sub H. This model turned out to be incorrect, but i t super gamma varsigma interesting anyway.

Now let's solve some puzzles on systems with a countable infinity of states. Some of these show up in quantum mechanics, but you don't need to know quantum mechanics to do these puzzles.

Puzzle twenty-seven. Show that for a system with a countable infinity of states, if thermal equilibrium is possible for some negative temperature, it is impossible for positive or infinite temperatures.

Puzzle twenty-eight. Work out the Boltzmann distribution when E sub n equals n E for some energy E, and show that it is well-defined for all temperatures zero is less than T is less than positive infinity. The next puzzle is a lot like the previous one a bit more messy, but worthwhile because of its great importance in physics.

Puzzle twenty-nine. For a system called the quantum harmonic oscillator of frequency omega we have E sub n equals open parenthesis n plus one-half close parenthesis h-bar omega, where h-bar is the reduced Planck's constant. Work out the Boltzmann distribution in this case, and show it is well-defined for all temperatures zero is less than T is less than positive infinity. Puzzle thirty. For a system called the primon gas we have E sub n equals E ln n for some energy E. Show that the Boltzmann distribution is well-defined for small enough positive temperatures, but there is a Hagedorn temperature. Give a formula for the Boltzmann distribution in terms of the Riemann zeta function:

zeta open parenthesis s close parenthesis equals the sum from n equals one to infinity of n to the power negative s. You can show that for the primon gas the sum of the series from n equals one to infinity of exp open parenthesis negative E sub n divided by k T close parenthesis diverges at the Hagedorn temperature. But it can go the other way, too:

Puzzle thirty-one. Find energies E sub n with a Hagedorn temperature such that the sum of the series from n equals one to infinity of exp open parenthesis negative E sub n divided by k T close parenthesis converges at the Hagedorn temperature.

Various other strange things can happen, as you should expect when dealing with infinite series. For example, it's possible that the Boltzmann distribution is well-defined at some temperature but the expected value of the energy is infinite! But I'll resist the lure of these rabbit holes and turn to something much more important: systems with a continuum of states. We will need to get good at these to compute the entropy of hydrogen. Now our sums become integrals, and various new things happen.


## THE FINITE VERSUS THE CONTINUOUS

THE FINITE


## THE CONTINUOUS

p a probability distribution on open curly brace one, two, up to n close curly brace Gibbs entropy Gibbs entropy p a probability distribution on R

S(p) equals negative k sum of i equals one to n of p sub i ln p sub i equals negative k integral of p of x ln p of x dx

S(p) always greater than or equal to zero S(p) not always greater than or equal to zero

S(p) always finite S(p) not always finite

S(p) invariant under permutations of open curly brace one, two, up to n close curly brace

S(p) not invariant under reparametrizations of R

You can switch from finite sums to integrals in the definition of entropy, and we'll need to do this to compute the entropy of hydrogen. But be careful: a bunch of things change!

We need to switch from finite sums to integrals when we switch from a finite set of states to a measure space of states. I'll illustrate the ideas with the real line, R. We define a probability distribution on R to be an integrable function p colon R arrow open square bracket zero, infinity close square bracket with

Such a probability distribution has a Gibbs entropy given by

S(p) equals negative k integral of p of x ln p of x dx from negative infinity to positive infinity.

We can also define Shannon entropy, where we leave out Boltzmann's constant k and use whatever base we want for the logarithm:

H (p) equals negative integral of p of x log p of x dx from negative infinity to positive infinity.

I should warn you that many writers reserve the term 'Shannon entropy' only for a sum

H (p) equals negative sum of p sub i log p sub i as i varies over some index set.

While that convention has advantages, I want to use the term 'Shannon entropy' to signal that I'm leaving out the factor of k.

Unlike the entropy for a probability distribution on a finite set, the entropy of a probability distribution on R can be negative! This is disturbing. Earlier I said that the Shannon entropy of a probability distribution is the expected amount of information you learn when an outcome is chosen according to that distribution. How can this be negative?

The answer is that this interpretation of entropy, valid for probability distributions on a finite or even a countably infinite set, is not true in the continuous case! We have to adapt our intuitions.

Look at an example. Let P sub epsilon be the probability distribution on R given by

P of x equals one divided by two epsilon if x is between negative epsilon and positive epsilon and P of x equals zero otherwise. For small epsilon it's a tall thin spike near zero. Let's work out its Shannon entropy: H(p) equals negative integral of p of x log p of x dx from negative infinity to positive infinity equals negative integral from negative epsilon to positive epsilon of one divided by two epsilon ln one divided by two epsilon dx equals log epsilon.

We're just integrating a constant here, so it's easy. When epsilon equals one the entropy is zero, and when epsilon becomes smaller than one the entropy becomes negative!

Why? We need a distance scale to define the entropy of a probability distribution on the real line. If I measure distance in centimeters, I'll think the entropy of a probability distribution is bigger than you, who measures it in meters. And if I measure it in kilometers, I'll think the entropy is smaller-and possibly even negative.

Why? We need a distance scale to define the entropy of a probability distribution on the real line. If I measure distance in centimeters, I'll think the entropy of a probability distribution is bigger than you, who measures it in meters. And if I measure it in kilometers, I'll think the entropy is smaller-and possibly even negative.

Let's see how this works. If I measure distance in different units from you, my coordinate y on the real line will not equal your coordinate x: instead we'll have y equals c times x for some c greater than zero. Then my probability distribution, say q, will have q of y dy equals q of c x d of x equals c q of x dx so we must have q of c x equals one divided by c p of x to make this integral equal to one. In other words, stretching out a probability distribution must also flatten it out, making it less 'tall'-and its entropy increases. Indeed:

Puzzle thirty-two. Show that H of q equals H of p plus ln c.

Thanks to this formula choosing zero is less than c is less than one compresses a probability distribution and makes it taller, reducing its entropy. Inevitably, this can make the entropy negative if c is small enough.

In summary: in the continuous case, entropy is not invariant under reparametrizations: our choice of coordinates matters! And this can make entropy negative. This applies not only to R but many other measure spaces we'll be considering, like R. This issue will be very important.

After learning this, it should be less of a shock that the entropy of a probability distribution on R can be infinite, or even undefined:

Puzzle thirty-three. Find three probability distributions P on the real line that have entropy positive infinity, negative zero, and undefined because it's of the form positive infinity minus infinity.


## ENTROPY, ENERGY AND TEMPERATURE

Suppose a system has some measure space X of states with energy E: X to R. In thermal equilibrium the probability distribution on states, P: X to R, maximizes the Gibbs entropy S equals negative k integral of P(x) ln P(x) dx subject to a constraint on the expected value of energy: (E) equals integral of P(x) E(x) dx

Typically when this happens P is the Boltzmann distribution e to the power of negative E(x)/kT

P(x) =

integral of e to the power of negative E(x)/kT dx where T is the temperature and k is Boltzmann's constant.

Then as we vary (E) we have d(E) equals TdS

We can now generalize a lot of our work from a finite set of states to a general measure space. I won't redo all the arguments, just state the results and point out a couple of caveats.

For any measure space X we say a function P: X to [zero, zero) is a probability distribution if it's measurable and integral of P(x) dx equals one.

We can define a version of Shannon entropy for P by

H equals negative integral of P(x) log P(x) dx,

but physicists mainly use the Gibbs entropy, defined by

S equals negative k integral of P(x) ln P(x) dx.

As I warned you last time, this can take values in [negative infinity, zero], though we are mainly interested in cases when it's finite. If we think of X as the space of states of some system, we can pick any measurable function E: X to R and call it the 'energy'. Its expected value is then

(E) equals integral of E(x)P(x) dx at least when this integral converges.

We say the probability distribution P describes thermal equilibrium if it maximizes S subject to a constraint (E) equals c. Typically when this happens P is a Boltzmann distribution

P(x) equals one over x e to the power of negative beta E(x) times e to the power of negative beta E(x) dx where beta is called the coolness. I say 'typically' because even when X is a finite set, we saw in Puzzle twenty-four that there can be thermal equilibria that are not Boltzmann distributions, but only limits of Boltzmann distributions as beta approaches positive infinity or approaches negative infinity. This can also happen for other measure spaces X. I will not delve into this, because my goal now is to get to some physics.

As before, we can write beta equals one over kT, at least if beta does not equal zero, and then write the Boltzmann distribution as

X to the power of negative E(x)/kT dx e to the power of negative E(x)/kT

P(x) =

Also as before, the Boltzmann distributions obey the crucial relation dH equals beta d(E).

Rewriting this in terms of Gibbs entropy S equals kH and temperature T equals one over k beta, it becomes this famous relation between temperature, entropy and the expected energy: TdS equals d(E).

Notice that the units match here. The Shannon entropy H is dimensionless, but since k has units of energy over temperature, the Gibbs entropy S equals kH has units of energy over temperature. Thus TdS has units of energy, as does d(E).


## THE CHANGE IN ENTROPY

As we change the temperature of a system from T one to T two while keeping it in thermal equilibrium, the change in its entropy is

S(T one) minus S(T zero) equals integral from T zero to T one d(E) over T

where (E) is its expected energy at temperature T.

Last time we saw that as we change the expected energy (E) of a system while keeping it in thermal equilibrium, this fundamental relation holds:

TdS equals d(E).

We can rewrite this as dS equals d(E) over T

and then integrate this from one temperature to another-remember, as the expected energy changes, so does the temperature. We get integral from T zero to T one d(E) over T equals S(T one) minus S(T zero).

This is the main way people do experiments to 'measure entropy'. Slowly heat something up, keeping track of how much energy it takes to increase its temperature each little bit. Using this data you can approximately calculate the integral at left and that gives the change in entropy!

This is the main way people do experiments to 'measure entropy'. Slowly heat something up, keeping track of how much energy it takes to increase its temperature each little bit. Using this data you can approximately calculate the integral at left and that gives the change in entropy!

But so far we're just measuring changes in entropy. How can you figure out the actual value of the entropy? One way is to assume the Third Law of Thermodynamics, which says that in thermal equilibrium the entropy approaches zero as the temperature approaches zero from above. This gives integral from T zero to T one d(E) over T equals S(T)

This is how people often 'measure the entropy' of a system in thermal equilibrium. They heat it up starting from absolute zero, very slowly so they hope it is close to thermal equilibrium at every moment-and they take data on how much energy is used, and approximately calculate the integral at left!

But this relies on the Third Law of Thermodynamics. So where does that come from?


## THE THIRD LAW OF THERMODYNAMICS

If a system has countably many states, with just one of lowest energy, and thermal equilibrium is possible for this system for some temperature T greater than zero, then its entropy in thermal equilibrium approaches zero as T approaches zero from above:

limit S(T) equals zero as T approaches zero from above.

Some people say the Third Law of Thermodynamics this way: "entropy is zero at absolute zero". But it's not really that simple indeed, other people say it's impossible to reach absolute zero. Above I've stated a version of the Third Law that's actually a theorem. Let's prove it!

Actually, let's prove it now for systems with only finitely many states. It'll be easier to handle systems with countably infinite number of states later, when we've developed more tools. And by the way, we'll see the Third Law isn't always true for systems with a continuum of states. It will fail for all three of the problems on our big to-do list: the classical harmonic oscillator, the classical particle in a box and the classical ideal gas. This is often taken as a failure of classical mechanics, since switching to quantum mechanics makes the Third Law hold for these systems.

Let's show that for a system with finitely many states i equals one, ... , n with energies E i, as the temperature T approaches zero from above, the entropy of the system in thermal equilibrium approaches k ln N where N is the number of lowest-energy states. In thermal equilibrium

P i equals e to the power of negative E i over kT.

Thus, all states with the lowest energy have the same probability, while as the temperature approaches zero from above, any higher-energy states have P i approaches zero. So, as the temperature approaches zero from above, the probability of the system being in any one of its N lowest-energy states approaches one over N, and we get limit as T approaches zero from above S(T) equals limit as T approaches zero from above negative k sum from i equals one to n P i ln P i equals negative k sum from i equals one to N of one over N ln of one over N.

ln N equals k ln N.

In particular, if the system has just one lowest-energy state, we get the Third Law of Thermodynamics:

limit as T approaches zero from above S(T) equals zero.

Here T approaches zero from above means that T is approaching zero from above.

But beware: for systems with lots of lowest-energy states, their entropy in thermal equilibrium can be large even near absolute zero! Also, a related problem: systems may take a ridiculously long time to reach equilibrium! This is especially true for systems that have many states whose energies are very near the lowest energy, like a piece of glass. You can put a piece of glass in a fancy refrigerator and try to cool it to near absolute zero. If it has one lowest-energy state, its entropy should approach zero. If this happened, the glass would change from glass to a crystal, which has less entropy. But nobody has seen glass turn into a crystal when they cool it down. If this happens, it probably does so only after an absurdly long time, much longer than the age of the Universe. This phenomenon is called 'frustration'. People like to argue about frustration and the Third Law, so I am not trying to give you the final word here, just alert you to the issue. You can learn a bit more here:

By the way: for systems with finitely many states, it's possible to have negative temperatures, and the Third Law has a counterpart saying what happens when the temperature approaches zero from below:


## Puzzle thirty-four. Show that for a system with finitely many states,

the limit as T approaches zero from below of S(T) equals k log M

where M is the number of states of highest energy.

However, most systems we'll be studying won't have a state of highest energy.


## MEASURING ENTROPY

If we assume the entropy of a system approaches zero as T approaches zero from above, we have the integral from zero to T sub one of d expected value of E over T equals S of T sub one. Using this assumption, we can do experiments to measure the entropy of different substances at standard temperature and pressure:

iron: approximately five bits per atom water: approximately twelve bits per molecule hydrogen: approximately twenty-three bits per molecule

People actually do experiments and use the above formula to figure out the entropy of many substances in thermal equilibrium assuming their entropy vanishes as the temperature approaches absolute zero. They slowly heat up a substance and keep track of how much energy is needed to raise its temperature as they go, so they can approximately calculate the integral shown. They usually report the answers in joules per kelvin per mole, but I enjoy 'bits per molecule'.

As you can see, liquids tend to have more entropy than solids, and gases tend to have even more. My goal in this course is to teach you how to approximately compute some of these entropies from first principles. Unfortunately the only substances that are simple enough for us to handle are gases.

This is a good opportunity to explain some conventions. A mole is defined to be exactly six point zero two two one four zero seven six times ten to the power of twenty-three this is called Avogadro's number, and it's close to the number of hydrogen atoms in a gram. A joule per kelvin of Gibbs entropy corresponds to about seven point two four two two nine seven times ten to the power of twenty-two nats of Shannon entropy: the number here is the reciprocal of Boltzmann's constant, which is defined to be exactly one point three eight zero six four nine times ten to the negative twenty-three joules per kelvin. A bit is log base two of e nats. From these three facts, we see one joule per kelvin of Gibbs entropy per mole corresponds to about zero point one seven three five one six bits per molecule of Shannon entropy.

By the way, what is 'standard temperature and pressure'? Annoyingly, this phrase means different things to different organizations. I will try to always use it to mean a temperature of two hundred ninety-eight point one five kelvin and a pressure of one bar. The temperature here equals twenty-five degrees Celsius, which seems a bit random compared to zero degrees Celsius but convenient, because it's close to room temperature. A pressure of one bar, or more officially one hundred kilopascals, is slightly less than a 'standard atmosphere', which is a unit of pressure intended to equal the average air pressure at sea level. A pascal is an official SI unit: it's a pressure of one newton per square meter.


## THE EQUIPARTITION THEOREM

Suppose the energy of a system with n degrees of freedom is a positive definite quadratic form E from R to R, for example

E of x equals the sum from i equals one to n of C sub i x sub i squared over two

C sub i greater than zero

Then in thermal equilibrium at temperature T, the expected value of the energy is the expected value of E equals n k T over two where k is Boltzmann's constant.

Temperature is very different from energy. But sometimes not very often, but sometimes the expected energy of a system in thermal equilibrium is proportional to its temperature. The equipartition theorem says this happens when the energy depends quadratically on several real variables, defining a positive definite quadratic form on R. For example, it happens for a classical harmonic oscillator.

Some people get confused and try to apply the equipartition theorem where it doesn't apply. They foolishly conclude that temperature is always proportional to energy.

This theorem does not apply to quantum systems. Indeed, when people tried to apply the equipartition theorem to a mirrored box of light they ran into a problem called the ultraviolet catastrophe. Classically the box of light is a system where the energy is a positive definite quadratic form, but n equals infinity, so they got an infinite expected value of the energy! Quantum mechanics saves the day and makes the answer finite.


## Radiation

Visible

The equipartition theorem also doesn't apply to classical systems unless the energy is quadratic. So it's very limited in its applicability, but still useful.


## Let's prove this result! To prove a theorem, you have to understand the definitions. We'll start with some background.

THE EQUIPARTITION THEOREM-BACKGROUND

Suppose the energy of a system with n degrees of freedom is some function E from R to R

Let k be Boltzmann's constant. Suppose p from R to R is a probability distribution maximizing the entropy

S equals negative k times the integral over R of p of x log p of x d n x subject to a constraint on the expected energy the expected value of E equals the integral over R of E of x p of x d n x

Then p must be a Boltzmann distribution:

the integral over R of e to the power of negative beta E of x d n x times e to the power of negative beta E of x p of x equals for some number beta greater than zero.

The temperature T is defined so that beta equals one over k T.

We're defining entropy with an integral now, unlike a sum as before, and sticking Boltzmann's constant into the definition of entropy, as physicists do, so that entropy has units of energy over temperature.

Given the formula for the energy E as a function on R-N, we'll have to find the Boltzmann distribution and then compute the expected value of E as a function of temperature.


## PROOF OF THE EQUIPARTITION THEOREM: One

Special case: a system with one degree of freedom where the energy E: R maps to R is E of x equals x squared over two.

The Boltzmann distribution is

E to the negative B x squared over two

P of x equals so the expected energy is

Integral from negative infinity to infinity of r squared e to the negative B x squared over two dx

One over zero Eight B x squared e to the negative B x squared over two dx from negative infinity to infinity

Integral from negative infinity to infinity of e to the negative B x squared over two dx

Integral from negative infinity to infinity of E of x times P of x dx equals

Integral from negative infinity to infinity of e to the negative B x squared over two dx over two so doing a substitution with u squared equals B x squared:

Integral from negative infinity to infinity of E equals one over zero

Integral from zero to infinity of e to the negative u squared over two du times u squared e to the negative u squared over two du

Integral from negative infinity to infinity of one

Integral from negative infinity to infinity of two

Integral from zero to infinity of two since

Integral from zero to infinity of e to the negative u squared over two du equals

We'll do two special cases before proving the general result. First let's do a system with one degree of freedom where the energy is E of x equals x squared over two. In this case, after a change of variables, the Gibbs distribution becomes a Gaussian with mean zero and variance one, and that gives the desired result. Or just do the integrals and see what you get! The expected energy E is k-T.


## PROOF OF THE EQUIPARTITION THEOREM: Two

More general case: a system with n degrees of freedom where the energy E: R-N maps to R is F of x equals M l-squared over two

We can reduce this to the case with one degree of freedom:

The expected value of E equals R-N

two T

Integral from negative infinity to infinity of e to the negative B l squared over two dn x

Integral from negative infinity to infinity of e to the negative B l squared over two dn x

JIR-N

Next we do a system with n degrees of freedom where the energy is a sum of n terms of the form x squared over two. It's no surprise that each degree of freedom contributes k-T to the expected energy, giving

Expected value of E equals five n k T

But make sure you follow my calculation above. I skipped a couple of steps!


## PROOF OF THE EQUIPARTITION THEOREM: Three

General case: a system with n degrees of freedom where the energy E: R-N maps to R is any positive definite quadratic form. Then

E of x equals one half norm A x squared for some invertible n by n matrix A. When A is a diagonal matrix this gives

E of x equals the sum from i equals one to n of c-sub-i x-sub-i squared over two where c-sub-i is greater than zero. We can reduce the general case to the previous case by a change of variables y equals A x: The expected value of E equals the integral over R-N of one half norm A x squared e to the negative beta norm A x squared over two d-n x divided by the integral over R-N of e to the negative beta norm A x squared over two d-n x equals the integral over R-N of one half norm y squared e to the negative beta norm y squared over two d-n y divided by the integral over R-N of e to the negative beta norm y squared over two d-n y equals n over two k T. Finally let's do the general case. A quadratic form on R-N is a map Q: R-N maps to R such that

Q of x equals the sum from i equals j equals one to n of q-sub-i-j x-sub-i x-sub-j for some numbers q-sub-i-j in R. We say it's positive definite if x not equal to zero implies Q of x is greater than zero. One can prove that a quadratic form Q: R-N maps to R is positive definite if and only if

Q of x equals one half norm A x squared for some invertible n by n matrix A. The factor of one half here is just to make our calculations easier.

Thanks to this, if we have a system whose space of states is R-N and its energy function E: R-N maps to R is a positive definite quadratic form, we can compute the average energy equals the integral over R superscript n of E of x times the exponential of negative beta times E of x d x divided by the integral over R superscript n of the exponential of negative beta times E of x d x by reducing it to the previous case using a change of variables. We get the average energy equals one-half n k T

So, each degree of freedom still contributes a k T to the expected energy. That's the equipartition theorem!

But be careful. The equipartition theorem doesn't apply when the energy is an arbitrary function of n variables. It also fails when we switch from classical to quantum statistical mechanics.

People sometimes memorize the conclusion of the equipartition theorem, E equals two n k T, without learning that it holds only for classical systems whose energy is a positive definite quadratic form. These people sometimes get fooled into thinking the average energy is always proportional to T. Some of these poor benighted souls go around saying that temperature is just a measure of energy per degree of freedom. This completely ignores the subtlety of the concept of temperature.

As we've seen, the truly general relation between temperature and energy, for systems in thermal equilibrium, also involves entropy:

T d S equals d E.


## THE AVERAGE ENERGY OF AN ATOM

Since an atom of helium gas can move in three directions, and its energy depends quadratically on its velocity and not on position, the equipartition theorem says that classically its expected energy should be the average energy equals negative k T two-thirds where T is temperature and k is Boltzmann's constant, about one point three eight times ten to the negative twenty-three joules per kelvin.

So, heating an atom of helium gas one degree Celsius should take three times one point three eight times ten to the negative twenty-three joules equals two point zero seven times ten to the negative twenty-three joules two

This is very close to the truth.

We can finally start reaping the rewards of all our thoughts about entropy! The equipartition theorem lets us estimate how much energy it takes to heat up one atom of helium one degree Celsius. And it works!

Of course we don't heat up an individual atom: we heat up a bunch. A mole of helium is about six point zero two times ten to the twenty-third atoms, so heating up a mole of helium one degree Celsius equals one kelvin should take about six point zero two times ten to the twenty-third times two point zero seven times ten to the negative twenty-three is approximately twelve point four six joules

And this is very close to correct! It seems the experimentally measured answer is twelve point six joules.

What are the sources of error? Most importantly, our calculation neglects the interaction between helium atoms. Luckily this is very small at standard temperature and pressure. We're also neglecting quantum mechanics. Luckily for helium this too gives only small corrections at standard temperature and pressure.

It's important here that helium is a monatomic gas. In hydrogen, which is a diatomic gas, we get extra energy because this molecule can tumble around, not just move along. We'll try that next.


## THE ENERGY OF HYDROGEN

If we treat a molecule of hydrogen as a dumbbell whose position takes three numbers and whose axis takes two numbers to describe, we can try to use the equipartition theorem to estimate its expected energy as the average energy equals negative k T five-halves where T is temperature and k equals one point three eight times ten to the negative twenty-three joules per kelvin.

In this approximation, heating a molecule of hydrogen gas one kelvin takes two times one point three eight times ten to the negative twenty-three joules equals three point four five times ten to the negative twenty-three joules

In reality it takes three point three nine times ten to the negative twenty-three joules at standard temperature and pressure. Not bad!

A molecule of hydrogen gas is a blurry quantum thing, but let's pretend it's a classical solid dumbbell that can move and tumble but not spin around its axis. Then it has three plus two equals five degrees of freedom, and we can use the equipartition theorem to estimate its energy.

For T significantly less than six thousand kelvin, hydrogen molecules don't vibrate with the two atoms moving toward and away from each other. They don't spin around their axis until even higher temperatures. But they tumble like a dumbbell as soon as T exceeds about ninety kelvin.

We need quantum mechanics to compute these things. But at room temperature and pressure, we can pretend a hydrogen gas is made of classical solid dumbbells that can move around and tumble but not spin around their axes! In this approximation the equipartition theorem tells us the average energy equals five k T.

This is fine as far as it goes—but our goal in this course is to compute the entropy of hydrogen. We'll start with a useful warmup: the classical harmonic oscillator.


## ENTROPY OF THE HARMONIC OSCILLATOR: ONE

A classical harmonic oscillator has energy equals p squared over two m where q is its position, p its momentum, m its mass and k its spring constant.

By the equipartition theorem, in thermal equilibrium at temperature T it has expected energy the average energy equals k T where k is Boltzmann's constant.

By the equipartition theorem, in thermal equilibrium at temperature T it has expected energy (E) = kT where k is Boltzmann's constant.

So, using d E equals T d S, its entropy is

S equals integral of d E over T equals k times the integral of one over T.

Since this does not approach zero as T approaches zero from above, the Third Law of Thermodynamics doesn't hold for the classical harmonic oscillator.

But what is this constant C? For that we must think harder.

What's the entropy of a classical harmonic oscillator in thermal equilibrium? Using the equipartition theorem and the formula d E equals T d S, we can show it's

So, the entropy grows logarithmically with temperature. And it does not go to zero as T approaches zero: instead, it goes to negative infinity. So the Third Law of Thermodynamics does not hold for the classical harmonic oscillator!

That may seem shocking, but it actually makes sense. The Third Law holds only for certain special systems. Furthermore, we've seen that the entropy of a sharply peaked probability distribution on a continuous state space is negative. We'll see that the Boltzmann distribution for the classical oscillator gets more and more sharply peaked near q equals p equals zero as the temperature approaches zero from above. So in fact, it makes perfect sense that the entropy approaches negative zero.

However, the classical harmonic oscillator is just an approximation to the quantum harmonic oscillator, which does obey the Third Law. It's a good approximation at high temperatures, but bad at low temperatures. In fact, this business of negative entropies at low temperature is not something that happens in the real world. It's just a defect of classical mechanics. It's trying to tell us that quantum mechanics is better.

Another point: you'll have noticed that constant C here. What is it? We can make progress with a bit of dimensional analysis. The quantity ln T is a funny thing: if we change our units of temperature, it doesn't get multiplied by a constant factor, the way physical quantities usually do. It changes by adding a constant! So k ln T doesn't have dimensions of entropy. But must have dimensions of entropy. The constant C must somehow save the day! How does that work? Let's see.


## ENTROPY OF THE HARMONIC OSCILLATOR: Two

Classically, a harmonic oscillator at temperature T has entropy

S equals K times the natural logarithm of T plus C. Writing C equals negative natural logarithm of T subscript zero for some constant T subscript zero, this gives S equals K times the natural logarithm of T divided by T subscript zero. Dimensional analysis implies T subscript zero must have units of temperature!

But what is this temperature T subscript zero? For that we must think harder.

The formula S equals K times the natural logarithm of T plus C is a bit scary from the viewpoint of dimensional analysis. We usually avoid working with the logarithm of a dimensionful quantity, like the natural logarithm of T, because it transforms in a funny way when we change our units. But if we write C equals negative natural logarithm of T subscript zero then we get S equals K times the natural logarithm of T divided by T subscript zero, and we see the solution to our problem! If T subscript zero has units of temperature, then T divided by T subscript zero is dimensionless, so the natural logarithm of T divided by T subscript zero does not change at all when we change our units. In other words, now the natural logarithm of T divided by T subscript zero is dimensionless, so S equals K times the natural logarithm of T divided by T subscript zero has units of entropy as it should.

So, the constant C must equal negative natural logarithm of T subscript zero for some temperature T subscript zero that we can compute for any harmonic oscillator. What is it? We could just compute it. But it is more fun to use dimensional analysis.

What could it depend on? Obviously the mass M, the spring constant K and Boltzmann's constant K. But there is no way to form a quantity with units of temperature from just M, K and K. So we need an extra ingredient.

And we have seen this already: to define the entropy of a probability distribution on the Q, P plane and get something with the right units, we need a quantity with units of action! The obvious candidate is Planck's constant H, and this is actually right. The entropy we are after is given by an integral with respect to DP DQ divided by H where H equals H divided by two pi. So, the temperature T subscript zero can depend on H as well as M, K and K.

We can compute a quantity with units of temperature from M, K, K and H. The frequency of our oscillator is omega equals K divided by M, and it is a famous fact that it has units of energy. K has units of energy divided by temperature, so H times omega divided by K has units of temperature!

Thus, our temperature T subscript zero must be H times omega divided by K times some dimensionless purely mathematical constant, which I will call one divided by alpha. Alpha must be something like seven or two, or if we are really unlucky, E six six six, though in practice we usually get numbers fairly close to one, not huge or tiny numbers.

So, the entropy of a classical harmonic oscillator must be

S equals K times the natural logarithm of T divided by T subscript zero equals K times the natural logarithm of alpha times K times T divided by H times omega.

This is as far as I can get without breaking down and doing some real work. Later we will compute Q.


## ENTROPY OF THE HARMONIC OSCILLATOR: Three

We have seen a classical harmonic oscillator with frequency omega has entropy

S equals K times the natural logarithm of alpha times K times T divided by H times omega when it is in thermal equilibrium at temperature T.

Here K is Boltzmann's constant, H is Planck's constant,

and alpha is some dimensionless mathematical constant. We will figure it out later.

Even though we do not know alpha, this formula is already very interesting! K times T is known to be the typical energy scale of thermal fluctuations at temperature T. H times omega is the spacing between energy levels of a quantum harmonic oscillator with frequency omega. The ratio K times T divided by H times omega is therefore roughly the number of energy eigenstates in which we may find a quantum harmonic oscillator with high probability when it is at temperature T.

Thus, S is roughly K times the logarithm of the number of states that we are likely to find a quantum harmonic oscillator in, when it is at temperature T. This may seem mysterious. After all, we were not trying to do quantum mechanics, much less count quantum states. But there are other examples of this pattern, where the entropy of a classical system in thermal equilibrium at temperature T is roughly K times the logarithm of the number of quantum states that are accessible at temperature T.

We will learn a bit more about this later, when we relate entropy to something called the 'partition function', which can be understood as the 'number of accessible states'. This viewpoint will also explain the constant Q. But now let us calculate this constant.


## ENTROPY OF THE HARMONIC OSCILLATOR: Four

A classical harmonic oscillator has energy

P, Q equals P squared divided by two M plus K times Q squared divided by two where P is its momentum, Q its position, M its mass and K its spring constant.

At temperature T, the probability density of its momentum and position is the Boltzmann distribution:

E raised to the power of negative beta times E of P, Q divided by P of P, Q equals zero to infinity E raised to the power of negative beta times E of P, Q, DP DQ divided by H

where beta equals one divided by K T, K is Boltzmann's constant, and H equals two pi times H is the original 'unreduced' Planck's constant.

The oscillator's entropy at temperature T is thus zero to infinity P of P, Q times the natural logarithm of P of P, Q, DP DQ divided by H

S equals negative K from negative infinity to positive infinity

Last time we found a formula for the entropy of a classical harmonic oscillator ... which includes a mysterious purely mathematical dimensionless constant Q. Now let us figure out alpha.

We will grit our teeth and actually do the integral needed to calculate the entropy, but only in one easy case! Combining this with our formula, we will get alpha.

First, recall the basics. The energy E of P, Q of our harmonic oscillator at momentum P, and position Q determines its Boltzmann distribution at temperature T, which I will call P of P, Q now since the letter P is already being used. Integrating negative P times the natural logarithm of P using the measure DP DQ divided by H we get the Shannon entropy. In physics we multiply this by Boltzmann's constant K to get the Gibbs entropy.


## ENTROPY OF THE HARMONIC OSCILLATOR: Five

We can choose units of length, time, mass and temperature to make a classical harmonic oscillator's mass M, its spring constant K, Boltzmann's constant K and Planck's constant H all equal one.

Then at T equals one the Boltzmann distribution of the oscillator is

E raised to the power of negative P squared plus Q squared divided by two

P of P, Q equals from zero to infinity E raised to the power of negative P squared plus Q squared divided by two, DP DQ equals E raised to the power of negative P squared plus Q squared divided by two so its entropy is S equals negative integral E to the power of negative P squared plus two divided by two, ln of E to the power of negative P squared plus two divided by two, dP dQ from negative infinity to infinity.

Let's do this integral!

Let's compute the Boltzmann distribution P of P and Q and the entropy S. To keep the formulas clean, we'll work in units where M equals K equals K equals H equals one, and compute everything at one special temperature: T equals one.

In this setup H equals two pi, and

E to the power of negative BE of P and Q equals E to the power of negative P squared plus Q squared divided by two is a beautiful Gaussian with integral integral from negative infinity to infinity E to the power of negative P squared plus Q squared divided by two equals two pi.

These two factors of two pi cancel when we compute the denominator of the probability distribution P of P and Q:

dp dq two pi times two pi equals one.

Thus, we get simply

P of P and Q equals E to the power of negative P squared plus Q squared divided by two.

The entropy of the harmonic oscillator is thus integral dp dq when K equals K equals H equals T equals one. Next let's do this integral.

S equals negative integral E to the power of negative P squared plus two divided by two ln of E to the power of negative P squared plus two divided by two from negative infinity to infinity.


## ENTROPY OF THE HARMONIC OSCILLATOR: Six

When M equals K equals K equals H equals T equals one the entropy of a classical harmonic oscillator is integral from negative infinity to infinity E to the power of negative P squared plus Q squared divided by two ln of E to the power of negative P squared plus Q squared divided by two dP dQ

S equals one over two integral zero to infinity R squared times E to the negative R squared divided by two dR dTheta (switching to polar) equals one half times two plus one half R squared

(doing the zero integral)

equals integral U E to the negative U du

(substituting U equals R squared divided by two)

equals one

Now let's do the integral to compute the entropy of the harmonic oscillator. We copy a famous trick for computing the integral of a Gaussian. First we switch to polar coordinates in the P Q plane, where

R squared equals P squared plus Q squared and dP dQ equals R dR dTheta.

Then we integrate with respect to Theta, which cancels out the factor of one over two pi. Then we do a substitution U equals R squared divided by two. But for us R squared divided by two is minus the logarithm of the Gaussian:

negative P plus zero squared divided by two equals one.

so we're left with

S equals integral U E to the negative U du which we can do with integration by parts.

After all this work, we get an incredibly simple answer:

S equals one.

So in the special case where M equals K equals K equals H equals T equals one, the entropy of a classical harmonic oscillator in thermal equilibrium is one.


## Now let's return to the general case, and finish the job.

ENTROPY OF THE HARMONIC OSCILLATOR: Seven

A classical harmonic oscillator with frequency w has entropy

S equals k ln of A k T divided by H w for some dimensionless constant A.

But when M equals K equals K equals H equals T equals one we have w equals one and S equals one, so we must have and thus finally k T divided by H w plus one

S equals k ln

Knowing the entropy in one special case, we can figure out the constant A in our general formula for the entropy. Our general formula says

S equals k ln of A k T divided by H w.

But when M equals K equals T equals H equals one we get w equals K divided by M equals one, and we saw last time that in this special case we get

S equals one.

So A must equal E.

Thus, the entropy of an oscillator with frequency w at temperature T is

S equals k ln of E k T divided by H w equals k ln of k T plus one.

The extra one here is fascinating to me. If we had slacked off, ignored the possibility of a dimensionless constant A, and crudely used dimensional analysis to guess S approximately the way people often do, we might have gotten

S equals k ln of k T divided by H w

This would be off by one nat.

What does the one extra nat mean? It seems pretty mysterious now. But later we'll understand it! I already mentioned that often entropy is roughly k times the logarithm of something called the 'number of accessible states'. But that formula is not exactly right: there's also an extra term related to energy, and that accounts for the one extra nat here. Be patient, and you'll see what I mean.


## WHERE ARE WE NOW?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure?

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

equals N V to the power of N plus three ln K plus seven including the mysterious constant gamma.

The subgoal: compute the entropy of a single classical particle in a one-dimensional box.

The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator:

S equals k ln minus k T plus one

Okay, so we've gotten somewhere! By doing the right integral, we've figured out that the entropy S of a classical harmonic oscillator of frequency w in thermal equilibrium at temperature T is

S equals k ln of k T plus one.

where k is Boltzmann's constant and h is Planck's constant.

We could compute the entropy of a single particle in a box the same way, and also the entropy of a classical ideal diatomic gas. But the integrals get a bit hairy, so people prefer to use a clever trick called the 'partition function'. It's definitely worth learning. It's not merely a clever trick, it gives new insights on the relation between entropy, energy and temperature. So let's talk about it.


## THE PARTITION FUNCTION

If a system has a set of states X with measure dX and its energy is a function E of X to R, its partition function is

Z of beta equals integral E to the power of negative beta E of X dX

where beta is the coolness.

I want to compute the entropy of a particle in a box, and ultimately the entropy of a box of hydrogen. We could do it directly, but that's a bit ugly. It's better to use the 'partition function'. This amazing function knows everything about statistical mechanics. From it you can get the entropy-and much more!


## THE PARTITION FUNCTION AND THE BOLTZMANN DISTRIBUTION

If a system has a set of states X with measure dX and its energy is E: X to R, in thermal equilibrium at coolness beta its probability distribution of states is the Boltzmann distribution:

P of X equals S sub X E to the power of negative beta E of X dX E to the power of negative beta E of X equals E to the power of negative beta E of X Z of beta where Z of beta equals integral E to the power of negative beta F of X dX

is its partition function.

In fact we've already seen the partition function: it's the thing you have to divide E to the power of negative beta E of X by to get a function whose integral is one. And that function whose integral is one is the Boltzmann distribution: the probability distribution of states in thermal equilibrium at coolness beta. So the partition function is a humble normalizing factor! And yet we'll see that it's incredibly powerful. It's kind of surprising.

Like Lagrangians in classical mechanics, it's fairly easy to use partition functions, but it's harder to understand what they 'really mean'. We will try. But first let's see how to use them.


## THE PARTITION FUNCTION KNOWS ALL!

If a system has partition function

Z of beta equals integral E to the power of negative beta E of X dX

then in thermal equilibrium at coolness beta its expected energy is

E equals negative one over Z ln Z and its entropy is k times ln Z minus beta d ln Z

Here's how you can compute the expected energy (E) and the entropy S of any system starting from its partition function Z of Beta as a function of the coolness Beta. I'll show you why these formulas are true, and then we'll test them out on the harmonic oscillator, where we have already computed the expected energy and entropy by other methods.


## THE PARTITION FUNCTION KNOWS THE EXPECTED ENERGY

If a system has partition function Z of six equals E to the power of negative Beta E of x d x then d over d Beta ln Z equals negative one over Z d over d Beta Z d beta Jx equals negative one over Z d over d Beta E to the power of negative Beta E of x d x equals E of x E to the power of negative Beta E of x d x over Z Jx

Jx E of x E to the power of negative Beta E of x d x

Jx E to the power of negative Beta E of x d x equals E

In short, the expected energy is E equals negative d over d Beta d ln Z

The partition function is all-powerful! For starters, if you know the partition function of a physical system, you can figure out its expected energy. The expected energy E is minus the derivative of ln Z with respect to the coolness Beta equals one over k T.

How do we show this? Easy: just look at the calculation above! We get a fraction, which is the expected value of E with respect to the Gibbs distribution.

By the way, this trick of taking the derivative of the logarithm of a function is famous: it's called a 'logarithmic derivative'. Notice that f prime of x f of x

Thus the logarithmic derivative says how fast a function is growing compared to the value of the function itself-like the interest rate in compound interest.


## THE PARTITION FUNCTION KNOWS THE ENTROPY

If a system has Boltzmann distribution p of x equals E to the power of negative Beta E of x over Z where Z equals the integral of E to the power of negative Beta E of x d x then its entropy in thermal equilibrium is

S equals negative k integral of p of x ln p of x d x equals negative k integral of p of x ln E to the power of negative Beta E of x over Z d x equals k integral of p of x ln Z plus Beta E of x d x equals k ln Z plus Beta E

But since E equals minus ln Z, this gives

S equals k ln Z minus Beta ln Z over d Beta

The entropy is a bit more complicated. But don't be scared! The Boltzmann distribution p of x is a fraction, so the log of this fraction breaks into two parts:

ln p of x equals ln E to the power of negative Beta E of x over Z equals negative ln Z plus Beta E of x.

Thus our integral for entropy breaks into two parts:

S equals negative k integral of p of x ln p of x d x equals k integral of p of x ln Z d x plus k Beta integral of p of x E of x d x.

The first part is just k ln Z since the integral of p of x is one. The second part is k Beta E. If we use what we just learned about E:

E equals negative d over d Beta ln Z

we get this formula for entropy in terms of the partition function:

This formula seems hard to understand at first. To extract its inner meaning, we need a new concept: 'free energy'.


## THE PARTITION FUNCTION KNOWS THE FREE ENERGY

To maximize entropy while holding expected energy constant, you can just minimize the free energy

F equals E minus T S We've seen

E equals negative d over d Beta ln Z and S equals k ln Z minus Beta ln Z over d Beta so with Beta equals one over k T a little algebra shows

F equals negative ln Z

Three

We can understand the relation between entropy, energy and the partition function if we bring in a concept I haven't mentioned yet: the free energy

F equals E minus T S.

Since we know formulas for E and S in terms of the partition function, we can work out a formula for F. And it's really simple! Much simpler than S, for example. It's just

F equals negative ln Z.

But what's the meaning of free energy? Remember: to maximize the Shannon entropy H subject to a constraint on expected energy, we introduced the Lagrange multiplier Beta equals one over k T and maximized the quantity H minus Beta E. But if you multiply this quantity by negative k T, you get free energy:

negative k T times H minus Beta E equals E minus T S equals F.

So, as long as T is greater than zero, maximizing entropy subject to a constraint on expected energy is equivalent to minimizing free energy!

Thus, free energy turns a problem of maximizing entropy subject to a constraint into a minimization problem without a constraint. The point is not that we've turned maximization into minimization: that's just an arbitrary business with signs. The point is that free energy lets us stop thinking about the constraint.

There's a huge amount to say about the free energy, which is also called the 'Helmholtz free energy', since there are other kinds. You can think of T S as the amount of energy in useless random form, since it comes from entropy. Since E is the total expected energy, F equals E minus T S is the amount of 'useful' energy. More precisely, the free energy is the maximum amount of work obtainable from a system at a constant temperature. But showing this would take us out of our way.


## THE PARTITION FUNCTION KNOWS ALL: REVISITED

If Z of three is the partition function of a system, in thermal equilibrium at coolness Beta its expected energy is E equals negative d over d Beta ln Z

and its free energy is

F equals negative ln Z

We can compute its entropy from these using

F equals E minus T S and we get

S equals k ln Z minus Beta ln Z over d Beta

Now we can tell a simpler story, which is easier to remember. Free energy, being the energy in useful form, is the expected energy minus the useless energy, which is temperature times entropy. Thus

F equals E minus T S

so

S equals E minus F over T

equals k Beta times negative F plus E

and using our formulas for F and E in terms of the partition function Z, we get

S equals k ln Z minus Beta ln Z

The story here is more of a mnemonic than a true explanation, because I'm not saying much what it means for energy to be 'useful' or 'useless'. I've only given this hint: when a system is in thermal equilibrium, its free energy is minimized. For more on the meaning of free energy, try a good book on thermodynamics, like this:

Right now I'd rather say a bit about the meaning of the partition function.


## THE MEANING OF THE PARTITION FUNCTION

Say X is a set where each point i has an 'energy' E sub i; E R. Its partition function is

Z equals the sum of E to the power of negative Beta E sub i for i in X

where Beta E R is the coolness.

The partition function counts the points of X-but it counts points with large energy less, since they're less likely to be 'occupied'.

If Beta equals one over k T, points with energy E sub i much greater than k T count for very little.

But as T approaches plus infinity, all points get fully counted and Z approaches the absolute value of X. In physics we call Z the number of accessible states.

Say we have a system with some countable set of states X. In thermal equilibrium at temperature T, the probability that the system is in its i-th state is proportional to the exponential of negative Beta E sub i, where E sub i is the energy of that state and Beta is the coolness. Thus, physicists say the partition function

Z equals the sum of E to the power of negative Beta E sub i for i in X

is the number of accessible states: roughly, the number of states the system can easily be in at temperature T, where Beta equals one over k T.

This is a funny thing to say, because being 'accessible' is not a yes-or-no matter. A more precise statement is that the partition function counts states weighted by their accessibility exp(negative beta E sub i). States whose energy is low compared to kT are highly accessible, or probable, because exp(negative beta E sub i) is close to one if E sub i is less than kT. States of high energy are more inaccessible, or improbable, since exp(negative beta E sub i) is close to zero if E sub i is much greater than kT.

Calling the partition function the 'number of accessible states' emphasizes how it generalizes the cardinality of an ordinary set X, meaning its number of points. Let's make this precise! Let's call a set X with a function E: X to R an energetic set. I will write it merely as X, so you need to remember it comes with an energy function. I will call its partition function Z of X:

Z of X equals the sum of e to the negative beta E sub i for i in X

If X is finite we don't have to worry about the convergence of this sum. My main message is this:

The partition function Z of X does for energetic sets what the cardinality does for sets.

For example, just like the cardinality, the partition function adds when you take disjoint unions, and multiplies when you take products! Let's see why.

Puzzle thirty-five. The disjoint union X plus X' of energetic sets E: X to R and E': X' to R is again an energetic set: for points in X we use the energy function E, while for points in X' we use the function E'. Show that the partition function obeys the law Z of (X + X') equals Z of (X) plus Z of (X'), at least for finite energetic sets.

Puzzle thirty-six. The cartesian product X times X' of energetic sets E: X to R and E': X' to R is again an energetic set: define the energy of (x, x') in X times X' to be E of x plus E' of x'. This is how it really works in physics. Show that the partition function obeys the law Z of (X times X') equals Z of (X) times Z of (X'), at least for finite energetic sets.

Puzzle thirty-seven. Show that if X is a finite energetic set, its partition function Z of (X) approaches its cardinality as T approaches positive infinity.

The key virtue of cardinality is that two sets are isomorphic that is, there exists a one-to-one and onto function between them if and only if they have the same cardinality. This generalizes to energetic sets if we use the partition function instead of the cardinality! Let's say two energetic sets with energy functions E: X to R and E': X' to R are isomorphic if there is a one-to-one and onto f: X to X' which is compatible with their energy functions, meaning

E' of f of x equals E of x for all x in X.

Puzzle thirty-eight. Show that two finite energetic sets are isomorphic if and only if they have the same partition function. (Hint: the key is to show that the functions exp(negative E over kT) for various energies E in R are linearly independent. As a step toward this, show that a finite linear combination can only be zero if c sub i equals zero for the smallest energy E sub j.) The sum of c sub i exp(negative E sub i over kT)

If you're into category theory, here are some ways to go further. If you're not, please skip to the next page.

Puzzle thirty-nine. Make up a category of energetic sets, where morphisms are maps that are compatible with their energy functions. Prove that it is a category.

Puzzle forty. Show the disjoint union of energetic sets is the coproduct in this category. Puzzle forty-one. Show that what I called the cartesian product of energetic sets is not the product in this category.

Puzzle forty-two. Show that what I called the 'cartesian product' of energetic sets gives a symmetric monoidal structure on the category of energetic sets. So we should really write it as a tensor product X tensor X', not X times X'.


## Puzzle forty-three. Show this tensor product distributes over coproducts: X tensor (Y plus Z) is isomorphic to (X tensor Y) plus (X tensor Z).

We can go even further and define not only a partition function for energetic sets, but also an expected energy, free energy, and entropy, using the formulas we've seen earlier. These obey a bunch of rules like this:


## Puzzle forty-four. Define the entropy of an energetic set by

S of X equals k times ln of Z of X plus beta ln of Z of X

Show that

S of X tensor Y equals S of X plus S of Y.


## ENTROPY COMES IN TWO PARTS

The entropy of a system in thermal equilibrium is always the sum of two parts:


## One. The free energy part:

negative F over T equals k ln Z

This is Boltzmann's constant times the logarithm of the number of accessible states.


## Two. The expected energy part:

(E) over T

This equals ln kT if the system has n degrees of freedom and its energy is a positive definite quadratic form.

Before we dive into examples, it's good to think one last time about the entropy of a system in thermal equilibrium. We've seen that this entropy is always the sum of two parts, which we could call the free energy part negative F over T and the expected energy part (E) over T. But there are various ways to think about this. One is simply that it follows from F equals (E) minus TS: the free energy is the expected energy minus the useless energy. But here is another way to think about it.

In his early work, Boltzmann said the entropy of a system is k times the logarithm of the number of states it can occupy. This is true if all these states are equally probable. But typically some states are more probable than others. We could try to address this by replacing the number of states with the number of accessible states

Z equals the sum of e to the negative beta E sub i for i in X

Here we count states weighted by their accessibility exp(negative beta E sub i). If we try to follow Boltzmann's prescription with this adjustment we get k ln Z equals F over T. This is the free energy part of the entropy.

In many situations this is close to the true entropy. But this clearly can't be all there is to it. After all, suppose we add the same constant c to the energy of each state. Then the probability of each state in thermal equilibrium is unchanged, so the entropy must stay the same! But the accessibility of each state gets multiplied by exp(negative beta c), so we have to subtract k times c from the free energy part of the entropy. There must be some compensating term and this is the expected energy part of the entropy, (E) over T. When we add c to the energy of each state, this goes up by c over T equals k times beta c.

Thus, in thermal equilibrium we can think of entropy as k times the log of the number of accessible states, "corrected" so that the result doesn't change when we add a constant to the energy of every state.


## THE POWER OF THE PARTITION FUNCTION

A classical harmonic oscillator with mass m and spring constant k has energy p, q) = one half plus Kg squared divided by two m

Kg squared

Its partition function is dp dq divided by h

Z of beta equals integral from zero to infinity e to the power of negative beta E of p, q where beta is coolness and h is Planck's constant.

From this we can find its expected energy and free energy in thermal equilibrium:

F equals negative kT ln Z

expected energy equals negative ln Z d beta and then its entropy:

S equals expected energy minus free energy divided by T where T is temperature, beta equals one divided by kT where k is Boltzmann's constant.

To test the power of the partition function, let's use it to figure out the entropy of a classical harmonic oscillator. Here's the game plan. First we'll compute the partition function by doing the integral in bright red. Then we'll use it to compute the oscillator's expected energy and free energy. Then we'll subtract those and divide by temperature to get the entropy.

In fact, we've already worked out the answer to this problem:

S equals k ln beta h divided by T plus one.

Our earlier approach led to some cool insights. But it was tricky, not systematic. The partition function method is systematic, so it's good for harder problems. It will also give new insight into that pesky plus one.

When we compute the entropy using a partition function, all the pain is concentrated at one point: computing the partition function! So let's get that over with.


## HARMONIC OSCILLATOR: PARTITION FUNCTION

A classical harmonic oscillator has energy E of p, q equals p squared divided by two m plus K squared q squared divided by two and frequency omega equals square root of K divided by m, so its partition function is square root of two pi m divided by beta to the power of one half integral from zero to infinity e to the power of negative beta r squared divided by two r d r d theta switching to polar u equals r squared divided by two equals one divided by beta h omega how beta

Z of beta equals beta h omega

For the harmonic oscillator, the partition function is the integral of a Gaussian in two variables. A change of variables makes the Gaussian round, and then we use polar coordinates to do the integral.

The physicist Kelvin is said to have written integral from negative infinity to infinity e to the power of negative x squared dx equals square root of pi on the blackboard and said "A mathematician is one to whom that is as obvious as that twice two makes four is to you." I find that rather obnoxious, but when I heard the story as a kid, I made damn sure I knew how to do this integral. The usual trick is to compute the square of this integral using polar coordinates.

Now we're seeing something interesting. The harmonic oscillator, whose energy depends quadratically on two degrees of freedom, is physically more important than a system whose energy depends quadratically on just one degree of freedom. And when beta equals h equals omega equals one, the partition function of the harmonic oscillator is integral from zero to infinity e to the power of negative r squared divided by two r d r d theta equals integral zero to infinity e to the power of negative u d u equals one half pi which is more fundamental than the integral Kelvin wrote down.


## HARMONIC OSCILLATOR: EXPECTED ENERGY

A classical harmonic oscillator has partition function

Z equals beta h omega so its expected energy in thermal equilibrium is expected energy equals negative two divided by partition function equals derivative of ln Z with respect to beta expected energy equals kT

just as the equipartition theorem says it must be!

Once we know the partition function of the classical harmonic oscillator, it's easy to compute its expected energy: just use expected energy equals derivative with respect to beta of ln Z

and get expected energy equals kT

beta equals one

We can also figure this out using the equipartition theorem. Remember, the equipartition theorem applies to a classical system whose energy is quadratic. If it has n degrees of freedom, then at temperature T it has expected energy equals n divided by two kT.

Our harmonic oscillator has n equals two, so we get expected energy equals kT. Good, this matches the partition function approach!


## HARMONIC OSCILLATOR: FREE ENERGY

A classical harmonic oscillator has partition function

Z of beta equals so its free energy in thermal equilibrium is

F equals negative kT ln Z equals negative kT ln beta h omega

F equals negative kT ln how

The partition function lets us do more! It lets us compute the free energy, too, using

F equals kT ln Z

Unlike the expected energy, the free energy involves Planck's constant:

F equals negative kT ln

Note kT and h omega both have units of energy, so kT divided by h omega is dimensionless, which is good because we're taking its logarithm. Also note that the free energy is negative at high temperatures! That may seem weird, but it turns out to be good when we compute the entropy.


## HARMONIC OSCILLATOR: ENTROPY

In thermal equilibrium at temperature T, a classical harmonic oscillator has kT divided by h omega so its entropy is expected energy equals kT and free energy F equals negative kT ln kT divided by h omega negative kT plus kT ln T

S equals expected energy minus F divided by T

kT

plus one divided by h omega

To compute the entropy of a classical harmonic oscillator, we just use

S equals expected energy minus F divided by T.

We get the answer we got before, of course:

S equals k ln beta h divided by T plus one.

But now we can finally understand the puzzling extra plus one.

As we've seen, the entropy of any system in thermal equilibrium consists of two parts:


## One. The free energy part, negative F divided by T. For the classical harmonic oscillator this is

Two. The expected energy part, expected energy divided by T. For the classical harmonic oscillator this is


## expected energy divided by T

k.

The free energy part of the entropy is always k times the logarithm of the number of accessible states. For the classical harmonic oscillator, the expected energy part of the entropy must equal k by the equipartition theorem, since the oscillator's energy depends on two degrees of freedom. This is small compared to the free energy part when h omega is much less than kT: that is, when quantum effects are small compared to thermal effects.


## PARTICLE IN A BOX: PARTITION FUNCTION

The energy of a classical free particle of mass m in a one-dimensional box depends only on its momentum p:

E equals p squared divided by two m

Its position q is trapped in the interval [zero, L].

Its partition function is therefore

Z of beta equals integral from zero to L integral from negative infinity to infinity e to the power of negative beta E of p, q dp dq divided by h h integral from zero to L integral from negative infinity to infinity e to the power of negative beta p squared divided by two m dp equals square root of two pi m divided by beta

Now let's turn to our ultimate goal: computing the entropy of a box of gas. As a warmup, let's figure out the entropy of a single particle in a box. In fact, let's start with a a free classical particle in a one-dimensional box: that is, in some interval [zero, L].

The first step is to compute its partition function. As you can see, this is easy enough. But the whole idea raises some questions. Some people get freaked out by the concept of entropy for a single particle I guess because it involves probability theory for a single particle, and they think probability only applies to large numbers of things.

I sometimes ask these people "how large counts as large?" In fact the foundations of probability theory are just as mysterious for large numbers of things as for just one thing. What do probabilities really mean? We could argue about this all day: Bayesian versus. frequentist interpretations of probability, etc. I said a tiny bit about this before, and I won't say more now.

Large numbers of things tend to make large deviations less likely. For example the chance of having all the gas atoms in a box all on the left side is less if you have one thousand atoms than if you have just two. This makes us worry less about using averages and probability.

But the math of probability works the same for small numbers of particles-even one particle! Even better, knowing the entropy of one particle in a box will help us understand the entropy of a million particles in a box-at least if they don't interact, as we assume for an 'ideal gas'.

But why just a one-dimensional box? The answer is that a particle in a three-dimensional box is mathematically the same as three noninteracting distinguishable particles in a one-dimensional box! The x, y, and z coordinates of the three-dimensional particle act like positions of three one-dimensional particles.


## PARTICLE IN A BOX: EXPECTED ENERGY

A classical free particle of mass M in a one-dimensional box of length L has partition function

Z equals the fraction with numerator L and denominator h times the square root of the fraction with numerator two pi times m and denominator beta The expected energy of any system in thermal equilibrium is the expected value of E equals the negative of the fraction with numerator d and denominator d beta of the natural logarithm of Z So, by the miracle of basic calculus, we get the expected value of E equals the fraction with numerator one and denominator two beta equals the fraction with numerator one and denominator two times k T as we'd expect from the equipartition theorem!

We worked out the partition function of a classical free particle in a one-dimensional box. From this we can work out its expected energy. Look how simple it is! It's just the fraction with numerator one and denominator two times k T where k is Boltzmann's constant and T is the temperature!

Why is the final answer so simple? We can use the chain rule the fraction with numerator d and denominator d beta of the natural logarithm of Z equals the fraction with numerator one and denominator Z times the fraction with numerator d Z and denominator d beta to see that only the power of beta in

Z equals the fraction with numerator L and denominator h times the square root of the fraction with numerator two pi times m and denominator beta matters, not all the constants: these constants show up in d Z divided by d beta but also in one divided by Z and they cancel. The length L, the mass m, Planck's constant h, the factor of two pi... none of this junk matters! Not for the expected energy, anyway. Because Z is proportional to beta to the power of negative one half, we simply get the expected value of E equals the fraction with numerator one and denominator two times k T More generally, if the partition function of a system is proportional to beta to the power of negative c its expected energy will be c times k T Z proportional to beta to the power of negative c implies the expected value of E equals c times k T But when is the partition function of a system proportional to beta to the power of negative c It's enough for the system's energy to be a positive definite quadratic form in n real variables-which physicists call 'degrees of freedom'. Then c equals n divided by two. We've already seen an example with two degrees of freedom: the classical harmonic oscillator. We saw that in this example Z is proportional to one divided by beta. This gives the expected value of E equals k T. But the result is quite general:

Puzzle forty-five. Suppose we have a system with state space R to the power of n and energy function E from R to the power of n to R that is a positive definite quadratic form, so that

E of x equals the fraction with numerator one and denominator two times the norm of A x squared for some invertible n by n matrix A Show that its partition function is proportional to beta to the power of negative c where c equals n divided by two In fact, this is just a new outlook on our friend the equipartition theorem.

Here's another thing to consider. While our particle in a one dimensional box has two degrees of freedom-position and momentum-its energy depends on just one of these, and quadratically on that one. So its expected energy is the fraction with numerator one and denominator two times n times k T where n equals one, not n equals two. So here's another puzzle for you:

Puzzle forty-six. Say we have a harmonic oscillator with spring constant K. As long as Kappa is greater than zero, the energy depends quadratically on two degrees of freedom so the expected value of energy equals K T. But when Kappa equals zero it depends on just one, and suddenly the expected value of energy equals one-half K T. How is such a discontinuity possible? In other words: how can a particle care so much about the difference between an arbitrarily small positive spring constant and a spring constant that's exactly zero, making its expected energy twice as much in the first case?

I'll warn you: this puzzle is deliberately devilish. In a way it's a trick question!


## PARTICLE IN A BOX: FREE ENERGY

A classical free particle of mass m in a one-dimensional box of length L has partition function

Z equals one divided by two T m h over L h minus beta

The free energy of any system is given by F equals minus the natural logarithm of Z, so B one

F equals minus the natural logarithm

Using one over kT and fiddling around a bit, we can rewrite this as

F equals minus kT times the natural logarithm of L plus minus the natural logarithm of kT plus minus the natural logarithm of one-half n kET plus one-half two m h squared

From the partition function of a classical free particle in a one-dimensional box we can also compute its free energy!


## PARTICLE IN A BOX: ENTROPY

We've shown that in thermal equilibrium, a classical particle of mass m in a one-dimensional box of length L has expected energy equals kT one and free energy

F equals minus kT times the natural logarithm of L plus minus the natural logarithm of kT plus minus the natural logarithm of one-half one two T m h squared

But entropy S is always the expected value of energy minus F divided by T, so

S equals k ln L plus one-half the natural logarithm of kT plus the natural logarithm of one plus one-half

Having worked out the expected energy and free energy F for a single classical particle in thermal equilibrium in a one-dimensional box, it is easy to work out its entropy. We just subtract the free energy from the expected energy and divide by temperature:

S equals the expected value of energy minus F divided by T.

The formula we get is not very snappy:

S equals k times the natural logarithm of L plus five times the natural logarithm of kT plus the natural logarithm of one-half T m h squared plus two.

We will get a better formula later, and ponder its meaning. For now, let's just make these observations:

When we make the length L of the box larger, the entropy becomes larger.

When we increase the temperature T, the entropy becomes larger.

When we increase the mass m of the particle, the entropy becomes larger.

The first two facts should feel intuitively obvious. When we increase the box's length, there is more unknown information about the position of the particle in thermal equilibrium. When we increase the particle's temperature, there is more unknown information about its momentum. The third fact is less obvious. When we introduce the concept of 'thermal wavelength', we will see that increasing the particle's mass decreases its thermal wavelength, which in turn increases its entropy in thermal equilibrium.


## WHERE ARE WE NOW?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure?

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

N times the natural logarithm of V plus three N plus minus the natural logarithm of kT plus Y two including the mysterious constant y.

The subgoal: compute the entropy of a single classical particle in a one-dimensional box:

S equals k times ln L plus minus the natural logarithm of kT plus the natural logarithm of T plus two

Check

The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator:

how kT one check

Let's pause to remember where we are in our game plan. First we computed the entropy of a classical harmonic oscillator. Now we've computed the entropy of a single classical particle in a one-dimensional box. The answer looks a bit like the entropy of an ideal gas! That's no coincidence we're almost there now.

In case you wanted to know the entropy of a particle in a three-dimensional box, don't worry. It's the same as the entropy of three particles of the same mass in three one-dimensional boxes of appropriate lengths: the length L, width W and height H of our three-dimensional box. So we can just sum those three entropies and get our answer. Since ln L plus ln W plus ln H equals ln V where V is the volume of our three-dimensional box, we get

S equals k times ln V plus the natural logarithm of kT plus two times ln three h squared plus three.

Later we'll do this calculation more rigorously and more generally for a box of any shape.

But you may have another question: what's the meaning of our formula for the entropy of a classical particle in a one-dimensional box? It's pretty complicated, after all, and we'll need to understand it to have any chance of understanding the mysterious constant y in the formula for a classical ideal monatomic gas.

We can understand our formula better if we delve into a tiny bit of quantum mechanics, and the concept of 'thermal wavelength'. So let's do that.


## THE WAVELENGTH OF A PARTICLE

In quantum mechanics particles are waves! A particle with momentum p has wavelength h

Lambda equals p where h is the unreduced Planck's constant, exactly

For example, the wavelength of an electron moving at one meter per second is about zero point seven millimeters.

One of the most amazing discoveries of twentieth-century physics: particles are waves. The wavelength of a particle is Planck's constant divided by its momentum! This was first realized by Louis de Broglie in his nineteen twenty-four Ph.D. thesis, so it's called the 'de Broglie wavelength'.

Why am I telling you this? Because I want to explain and simplify the formula for the entropy of a particle in a box. Even though I derived it classically, it contains Planck's constant! So, it will become more intuitive if we think a tiny bit about quantum mechanics.

A good explanation of quantum mechanics would require a whole other course. But it's good to know that in quantum mechanics, a particle with a given momentum has a wavelength associated to it: we shouldn't imagine it as having a definite location; it's a bit 'blurry'.

This will give a more intuitive explanation for our complicated formula of the entropy of a particle in a one-dimensional box. We'll use this intuition to simplify our formula. That will make it easier to generalize to N particles in a three-dimensional box that is, a classical monatomic ideal gas!


## THE WAVELENGTH OF A WARM PARTICLE

In thermal equilibrium, the average energy of a classical free particle in three-dimensional space is

(E) = CkT three where T is the temperature and k is Boltzmann's constant.

If the particle has mass m,

E equals m v squared, p equals m v equals p equals square root two m E equals square root three m k T

In quantum mechanics, a particle of momentum p has wavelength X equals h over p where h is the unreduced Planck's constant. So, at temperature T, the typical wavelength of a free particle of mass m is roughly square root three m k T

Particles are waves! Their wavelength is shorter when their momentum is bigger. And the warmer they are, the bigger their momentum tends to be. So there should be a formula for the typical wavelength of a warm particle. And here it is! It helps us visualize the world: particles are a bit blurry, with a characteristic wavelength that depends on temperature.

We get this formula from a blend of ideas. Classical mechanics says kinetic energy is E equals p squared over two m. Classical statistical mechanics says E equals two k T. Quantum mechanics says X equals h over p. It's pretty optimistic to put these formulas together and see what we get. But the result is approximately correct, though subject to limitations.

We derived E equals k T using classical statistical mechanics. But it's close to correct for a single quantum particle in a big enough box at high enough temperatures. Otherwise quantum effects kick in.

Another problem is that (E) equals two k T and E equals p squared over two m do not imply (p) equals square root three m k T, even if p here means the magnitude of the momentum vector. The arithmetic mean of a square is not the square of the arithmetic mean! Really the 'root mean square' of p is square root three m k T. Similarly, even if the root mean square of p is square root three m k T and quantum mechanically X equals h over p, we cannot conclude that the root mean square of X is h over square root three m k T. Again, you cannot pass a root mean square through a reciprocal!

So, our derivation above is dodgy- but it's okay as an order-of-magnitude approximation for a warm enough particle in a big enough box.


## THE PARTITION FUNCTION AND THE THERMAL WAVELENGTH

The partition function of a classical free particle of mass m in a one-dimensional box of length L is

Z equals integral negative infinity to infinity e to the power of negative beta p squared over two m d p d q over h equals L

square root two pi m over beta where lambda equals h over square root two pi m k T

square root two pi m over k T

is called the 'thermal wavelength'.

Last time we saw that at temperature T, the typical wavelength of a free particle of mass m is roughly h over square root three m k T

But the partition function of a classical particle of mass m in a box simplifies a lot if we introduce a slightly different distance scale, which people call the thermal wavelength.

lambda equals h over square root two pi m k T

Then the partition function is just the length of the box divided by lambda. The thermal wavelength lambda is a bit smaller than the previous calculation: we have lambda approximately equals zero point sixty-nine times the previous value. But we probably shouldn't worry about this too much, since our calculation of the previous value was so rough. Of course all these details are worth thinking about. But the thermal wavelength will turn out to be very useful!

Then the partition function is just the length of the box divided by A. The thermal wavelength A is a bit smaller than X: we have A ~ 0.69). But we probably shouldn't worry about this too much, since our calculation of \ was so rough. Of course all these details are worth thinking about. But the thermal wavelength will turn out to be very useful!


## FREE ENERGY AND THE THERMAL WAVELENGTH

In thermal equilibrium, a classical free particle of mass m in a one-dimensional box of length L has free energy

F equals negative k T ln

L over lambda plus k T times pi beta

F equals negative k T ln where lambda equals h over square root two pi m k T

is the thermal wavelength.

is the thermal wavelength.

Since the partition function of the classical free particle in a one-dimensional box is and free energy is related to the partition function by

F equals negative k T ln Z,

we have

Expressing this in terms of temperature rather than coolness, we have

F equals negative k T ln


## ENTROPY AND THE THERMAL WAVELENGTH

In thermal equilibrium, a classical free particle of mass m in a one-dimensional box of length L has expected energy

(E) equals k T

and free energy

F equals negative k T ln lambda over L

where lambda equals h over square root two pi m k T is the thermal wavelength.

But entropy S is (expected energy minus free energy) over T, so

S equals k ln

Now that we have clean formulas for the expected energy and free energy of the classical free particle in a one-dimensional box, we can get a nice formula for its entropy. This is equivalent to the formula we saw before, but it's easier to understand. It's a sum of two terms:

S equals k (ln lambda over L plus two).

Let's make sure we understand this! We've seen that for any system in thermal equilibrium, the entropy is the sum of two parts:

One. The free energy part. For the classical particle in a one-dimensional box, this is

S equals k ln lambda over L

plus

Two. The expected energy part. For the classical particle in a one-dimensional box, this is

(E)

equals two k.

The free energy part is always k times the logarithm of the number of accessible states, and for the particle in a one-dimensional box the number of accessible states is L over lambda. The expected energy part is two k, by the equipartition theorem, because the particle's expected energy depends on one degree of freedom.

Let us think a bit more about why the number of accessible states is L over lambda. The most rigorous approach is simply to compute the number of accessible states that is,

the partition function:

Z equals zero to L

equals L over lambda equals L over lambda.

A more hand-wavy approach is to imagine the space of states of the particle, meaning the space of position-momentum pairs (q, p) in the range zero to L times R. When it comes to counting accessible states, each region of area h holds one state. The 'accessible' states are those where the energy is not too big compared to k T, so the probability density e to the power of negative E over k T is fairly large. This is a bit vague, as it must be, because 'accessibility' is not really a yes or no matter. But let's just pretend it is, and demand E less than or equal to k T. Then the 'accessible' region of state space is where p squared over two m is less than or equal to k T, or p is less than or equal to square root two m k T over m.

This region is

{(q, p) | zero is less than or equal to q which is less than or equal to L, negative square root two m k T over m is less than or equal to p which is less than or equal to square root two m k T over m} in the range [0, L] times R.

It has area L times square root four m k T over m, so the number of states it holds is this divided by h, or two L

times square root two m k T over h.

This is just thirteen percent more than the exact value of Z. More importantly, I hope this calculation gives you a mental picture of number of accessible states for the particle in a one-dimensional box. A mental picture can be helpful even if it's oversimplified. I like to imagine counting the little rectangles of area h that can fit into the 'accessible' region of state space.

In fact this idea is related to Bohr and Sommerfeld's early approach to quantum physics, the 'old quantum theory', which was later subsumed by the theory of 'geometric quantization'. In Bohr and Sommerfeld's approach, when we quantize a classical system with one position and one momentum degree of freedom, there should be approximately one quantum state for each region of area h in the q p plane. More generally, when we quantize a classical system with n position and n momentum degrees of freedom, there should be approximately one quantum state for each region R in R to the power of two n with

R times Δ p times Δ q equals h to the power of n.


## PARTICLE IN A THREE-DIMENSIONAL BOX: PARTITION FUNCTION

The partition function of a classical free particle of mass m in a three-dimensional box B of volume V is

B exp(-p dot p divided by two m) differential three p differential three q divide h cubed where B equals one divide kT is the coolness.

This result becomes prettier using the thermal wavelength A equals h open parenthesis eight divide two m m close parenthesis to the power of one half

Then we get simply

V divide A cubed

Z equals

Now that we've worked out the statistical mechanics of a classical particle in a one-dimensional box, it's easy to copy everything for a three-dimensional box of any shape. We start with the partition function. The energy of a free particle of mass m is p dot p divided by two m, so the partition function is the integral of exp negative p dot p divided by two m over all possible positions and momenta. Integrate over momentum and you get exp negative B open parenthesis p one square plus p two square plus p three square close parenthesis divided by two m differential p one differential p two differential p three divide h cubed equals h divided by two m m beta to the power of three

In terms of the thermal wavelength this is just one divide A cubed. Integrate over position and you multiply this by the volume of the box, say V. So we get an incredibly simple final answer:

Z equals V divide A cubed

And this sort of calculation works in any dimension: there's nothing special about the number three here.


## PARTICLE IN A THREE-DIMENSIONAL BOX: ENTROPY

In thermal equilibrium, a classical free particle of mass m in a threed box of volume V has expected energy

E equals kT divided by two times three and free energy

A cubed V

F equals negative kT Ln where A equals h divided by V to the power of two times m kT is the thermal wavelength. But entropy S is E minus F divided by T, so

S equals k ln V divided by A cubed plus three

The entropy of a particle in thermal equilibrium in a three-dimensional box works very much like our earlier calculation for a one-dimensional box, with a couple of adjustments due to the dimension. Since the particle's energy is now a quadratic function of three variables, the equipartition theorem now says its expected energy is

E equals kT.

We can work out its free energy from its partition function, which we computed in the last tweet:

V

F equals negative kT ln Z equals negative k ln

V divided by A cubed.

Thus its entropy is

S equals E minus F divided by T

The meaning of the two terms here is very similar to that for the particle in the one-dimensional box. The first term is k times the logarithm of the number of accessible states, as always for the Gibbs entropy of a system in thermal equilibrium. Here the number of accessible states is V divide A cubed. The second term is two k thanks to the equipartition theorem, since the particle's expected energy depends quadratically on three degrees of freedom. When V is much greater than A cubed this second term is a small correction to the first. As this ceases to be true, the second term becomes more important and when A cubed is comparable to V, quantum corrections to our calculation also become significant.


## A TALE OF TWO GASES

The entropy of an ideal gas of N distinguishable classical particles of mass m in a box of volume V is

S equals kN open parenthesis ln V plus three halves ln kT plus three halves ln k plus ln I m plus three halves close parenthesis.

while for indistinguishable particles it's

S equals kN ln open parenthesis V divide N close parenthesis plus three halves ln kT plus three halves ln m plus three halves.

where the corrections are small compared to N as N gets larger.

Now we are finally ready to tackle the entropy of a gas. We start with a monatomic ideal gas, which means N free point particles bouncing around in a box. But there's a subtlety! We'll get different answers depending on whether we think of these particles as distinguishable or indistinguishable. That is: do we count the state of the gas as different if we switch two particles, or not?

The formulas look very similar. There are three differences:

For distinguishable particles, we'll get an exact formula, while for indistinguishable particles, we'll get an approximate one, where the corrections are small compared to N when N becomes large.

The entropy for distinguishable particles has a term equal to two kN, while for indistinguishable particles it has a term equal to zero.

Most importantly, there's a huge difference in the volume dependence! Where the distinguishable particles have a term in the entropy equal to kN ln V, the indistinguishable ones have a term equal to kN ln open parenthesis V divide N close parenthesis, so their entropy is considerably smaller for large volumes.

The last difference makes the entropy behave strangely for distinguishable particles, so in practice the physically important case is the gas of indistinguishable particles. But we'll do the calculations in both cases, because the distinguishable case is easier, and interesting.


## GAS OF DISTINGUISHABLE PARTICLES: PARTITION FUNCTION

The partition function of an ideal gas of N distinguishable classical particles of mass m in a three-dimensional box B of volume V is

Z equals integral over B to the power of N exponential negative B times sum from i equals one to N pi dot pi divide two m differential three p one dot dot dot differential three p N differential three q one dot dot dot differential three q N

equals pi squared times pi h to the power of three hundred N

equals two pi m beta to the power of three N divide by two equals V to the power of N divide h to the power of three N

Thus Z equals A to the power of three N divide V to the power of N

where A equals h open parenthesis eight divide two pi m close parenthesis to the power of one half is the thermal wavelength.

Suppose we have a system of N distinguishable classical free particles in a three-dimensional box B of volume V. The state of this system is described by N positions q one, dot dot dot, q N in B and N momenta p one, dot dot dot, p N in R three. If each particle has mass m, the energy of the i th particle is equal to

E i equals pi dot pi divide two m and the energy of the system is

E equals sum from i equals one to N E i. Let's call the partition function of this system Z. To compute this, we integrate exp negative B E over the space of states, obtaining

Z equals integral V to the power of N integral R to the power of three N exponential negative B E differential three p one dot dot dot differential three p N differential three q one dot dot dot differential three q N divide h to the power of three N.

Above, I proceeded to compute Z directly by doing the Gaussian integral over momenta and integrating each position over the box. Here's a slightly different way. Because exp negative open parenthesis E close parenthesis equals exp negative B E one dot dot dot exp negative B E N,

the partition function Z is a product of integrals which are all equal:

B integral R cubed exponential negative B p dot p divide two m differential three p differential three q divide h cubed.

Z equals

The integral in the parentheses is the partition function of a single particle in a box. We have already seen that this equals

B integral R cubed exponential negative B p dot p divide two m differential three p differential three q equals V divide h cubed

A cubed where A is the thermal wavelength. Thus we have

Z equals

We can also do this calculation with a lot less work using Puzzle thirty-six. This implies that when we build a new system from N identical noninteracting copies of some old system, the partition function of the new system is the N th power of the partition function of the old system. What I just did is show this in a special case.


## GAS OF DISTINGUISHABLE PARTICLES: ENTROPY

In thermal equilibrium, an ideal gas of N distinguishable classical particles of mass m in a three-dimensional box of volume V has expected energy

E equals kNT divide by two times three and free energy

A to the power of three N divide by V to the power of N

F equals negative kT ln where A equals h divide V to the power of two m kT is the thermal wavelength. Its entropy S is E divided minus F divide T, so

S equals kN ln N open parenthesis ln V divide N plus three close parenthesis

We use the subscript d for a gas of N distinguishable particles. Since the energy is a quadratic function of three N variables, the equipartition theorem says the expected energy is E d equals k N T.

The free energy F is minus Boltzmann's constant times the logarithm of the partition function, which we just computed:

F a equals negative k ln Za equals negative k ln

Thus the entropy of the gas is

S a equals E a minus F a over T V three plus two . h equals

A equals square root of two Tk m kT over three two Tm h squared plus two

If we expand this out using we get the formula I promised earlier:

S a equals k N ln V plus ln kT plus ln.

The only advantage of this messier formula is that it separates out the temperature dependence and the volume dependence.


## THE GIBBS "PARADOX"

For the ideal gas of N distinguishable classical particles in a box of volume V, the entropy

S a equals k N ln V plus ln kT plus ln three.

two three two Tm plus three h squared two.

more than doubles if we double both N and V while keeping everything else the same. This confused people for a while, so it's called the Gibbs paradox.

Start with a box B containing an ideal gas of distinguishable classical particles. Then double the volume of the box to get a new box B', and double the number of particles in the box too, while keeping the temperature and everything else the same.

We might expect the entropy to double. After all, we could take the doubled box and slip a thin wall down the middle to get two identical copies of the original box. So the entropy should be twice as big now. Right?

Apparently not! Instead of just doubling the k N ln V term in the original entropy, we are replacing it with two k N ln two V, which is more than twice as big. The reason is that in the doubled box B' each individual particle has twice as much room to roam than if you put a wall down the middle. Thus, it takes more information to say where all the particles are.

While there's no real paradox here, people found this result deeply counterintuitive, so they called it the Gibbs paradox. And in fact they had a good reason for being suspicious of this result. It would be correct if gas molecules were distinguishable. But in fact molecules of the same kind are not distinguishable they don't have little labels on them that let you recognize which is which. And if we take this fact into account, our formula for the entropy changes. Let's see how!


## GAS OF INDISTINGUISHABLE PARTICLES: PARTITION FUNCTION

The partition function of an ideal gas of N indistinguishable classical particles of mass m in a three d box B of volume V is

Z i B equals Za B over N factorial.

beta three N over two equals one V to the N over N factorial h to the three N.

Thus

Z i three equals N factorial A to the three N over one V to the N.

where A equals h square root of beta over two T m is the thermal wavelength.

The partition function Z i for a gas of N indistinguishable particles is one over N factorial times that for a gas of distinguishable particles. Why? We got Za by integrating exp negative beta E over the space of ordered N tuples of position-momentum pairs. The energy E here does not change if we permute our N tuple, so we can also think of it as a function of unordered N-tuples. Then we get Z i by integrating exp negative beta E over the space of such unordered tuples. Notice that there are N factorial ordered N tuples for each unordered N tuple, except for N tuple with repeated entries, which form a set of measure zero and thus contribute nothing to the integral. Thus, we should not be surprised that

Z i B equals Za B over N factorial.

But we've seen

Za B equals A to the three N over V to the N

where A is the thermal wavelength, so

Z i eight equals N factorial A to the three N over one V to the N.

Making this sketchy argument precise requires more notation. I think carefully doing the case N equals two is the best way for you to see what's going on.


## GAS OF INDISTINGUISHABLE PARTICLES: ENTROPY

In thermal equilibrium, an ideal gas of N indistinguishable classical particles of mass m in a three-dimensional box of volume V has expected energy

E sub i equals three over two k N T and free energy

F sub i equals negative k T ln one over N factorial V to the N over Lambda to the three N where Lambda equals h over square root of two pi m k T is the thermal wavelength.

Its entropy S sub i is E sub i minus F sub i over T, so

S sub i equals k N ln V over Lambda cubed plus three over two minus k ln N factorial. We use the subscript i for a gas of N distinguishable particles. Since the energy is a quadratic function of the three N momentum variables, the equipartition theorem says the expected energy of this gas is

E sub i equals three over two k N T . The free energy F is minus Boltzmann's constant times the logarithm of the partition function, which we just computed.

F sub I equals negative K ln Z sub I equals negative K ln open parenthesis one divided by N factorial multiplied by V to the power of N divided by Lambda to the power of three N close parenthesis. Thus the entropy of the gas is

S sub I equals open parenthesis average E sub I close parenthesis minus F sub I close parenthesis divided by T equals K N open parenthesis ln open parenthesis V divided by Lambda cubed close parenthesis plus three halves close parenthesis minus K ln N factorial. In short, it is K ln N less than for the gas of distinguishable particles. This makes beautiful intuitive sense: there are N factorial permutations of the particles that we no longer care about in the indistinguishable case.


## STIRLING'S FORMULA

Stirling's formula says

Approximates to square root two pi N open parenthesis N divided by E close parenthesis to the power of N

N factorial and it gives ln N factorial approximately equals open parenthesis ln N minus one close parenthesis N plus one half ln two pi N where the error goes to zero as

N approaches positive infinity. Now we need a bit of math: Stirling's formula for the factorial function. In one form this says

The limit as N approaches positive infinity of the quantity square root of two pi N times open parenthesis N divided by E close parenthesis raised to the power of N divided by N factorial equals one. We abbreviate this fact, that the ratio of two quantities approaches one as N approaches positive infinity, by saying N factorial is asymptotic to square root of two pi N times open parenthesis N divided by E close parenthesis to the power of N. We also write

N factorial is asymptotic to square root of two pi N open parenthesis N divided by E close parenthesis to the power of N. where the symbol approximates means 'asymptotic to'.

If we take the logarithm of both sides we get ln N factorial approximately equals open parenthesis ln N minus one close parenthesis N plus one half ln two pi N. The symbol approximates has a vaguer meaning: 'approximately equal to'. But it turns out that in this instance the approximation is extremely good: the difference between the left and right sides goes to zero as N approaches positive infinity. In fact we will content ourselves with a cruder approximation:

ln N factorial approximately equals open parenthesis ln N minus one close parenthesis N because in the entropy entropy of an ideal gas N is typically huge, so the term we have discarded here is dwarfed by the others.

Puzzle forty-seven. Suppose N is Avogadro's number, close to the number of atoms in four grams of helium:

N approximately equals six times ten to the power of twenty-three. What is the ratio of one half ln two pi N to

N? While deriving Stirling's formula is fascinating and not at all trivial, doing so would take us rather far afield. So I will resist, and refer you instead to this:


## THE SACKUR-TETRODE EQUATION

In thermal equilibrium, an ideal gas of N indistinguishable classical particles in a three-dimensional box of volume V has entropy

S sub I equals K N open parenthesis ln open parenthesis V divided by Lambda cubed close parenthesis plus three halves close parenthesis minus K ln N factorial where Lambda equals h divided by square root of two pi m K T is the thermal wavelength.

Using Stirling's formula ln N factorial approximately equals open parenthesis ln N minus one close parenthesis N we get the Sackur-Tetrode equation:

S sub I approximately equals K N open parenthesis ln open parenthesis V divided by N Lambda cubed close parenthesis plus five halves close parenthesis Taking our formula

S sub I equals K N open parenthesis ln open parenthesis V divided by Lambda cubed close parenthesis plus three halves close parenthesis minus K ln N factorial and using a simple version of Stirling's formula, ln N factorial is asymptotic to open parenthesis ln N minus one close parenthesis N, we get the famous Sackur-Tetrode equation:

S sub I is asymptotic to K N open parenthesis ln open parenthesis V divided by Lambda cubed close parenthesis plus three halves close parenthesis minus K open parenthesis ln N minus one close parenthesis N is asymptotic to K N open parenthesis ln open parenthesis V divided by N Lambda cubed close parenthesis plus five halves close parenthesis. Note that with this formula, if we multiply both V and N by the same constant, the entropy also gets multiplied by that constant. In this situation we say the entropy is 'extensive'.

For a better approximation, we can use logarithm of N factorial is approximately equal to open parenthesis logarithm of N minus one close parenthesis times N plus one half times logarithm of two pi N where the error goes to zero as N approaches infinity. This gives a correction to the Sackur-Tetrode equation:

entropy sub i is approximately equal to k times N times open parenthesis logarithm of V over N lambda cubed plus five halves close parenthesis minus one half times logarithm of two pi N. Here if we multiply both V and N by a constant c, we don't just multiply the entropy by c: we also have to subtract one half times logarithm of two pi c. So the entropy is not quite extensive but this effect is tiny when you've got a mole of gas.


## THE ENTROPY OF AN IDEAL MONATOMIC GAS

In thermal equilibrium, an ideal gas of N indistinguishable classical particles in a three-dimensional box of volume V has entropy given approximately by the Sackur-Tetrode equation:

EN (In MAS + NA3 h

But the thermal wavelength lambda is lambda equals square root of two pi times m times k times T

so we can rewrite this as three halves k T plus three over two m plus five

S is approximately equal to k N times logarithm of V over N

We've done it: we've figured out the entropy of a gas of N indistinguishable classical free particles in a three-dimensional box of volume V. Above I've written it in two different ways. Let's mull over the meaning of each term in each formula.

The first formula says

S is approximately equal to N times k times logarithm of V over NA cubed plus five.

Like the entropy of the classical harmonic oscillator and the classical free particle in a box, this breaks up into two parts, thanks to the formula

S equals open parenthesis E close parenthesis minus F T.

But it does so a bit subtly. The two parts are not what you might naively think! They are:

One. The free energy part:

T F is approximately equal to k N times logarithm of one over NA cubed times V plus one.


## Two. The expected energy part:

open parenthesis E close parenthesis

T equals k N.

As usual, the free energy part of the entropy is k times the logarithm of the number of accessible states. The expected energy part of the entropy is approximately equal to N times k by the equipartition theorem, since there are N particles each of whose energy depends on three momentum degrees of freedom.

The expected energy part of the entropy is small compared to the free energy part when V over N is greater than A cubed: that is, when the volume available per particle greatly exceeds the cube of its thermal wavelength. This happens for a gas that is sufficiently warm and dilute, made of sufficiently massive particles. We will see that this is true for helium at standard temperature and pressure. It's even more true for the heavier monatomic gases: the noble gases like neon, argon, and krypton.

The surprise is the extra plus one in the first part of the entropy-the free energy part. It's telling us that the logarithm of the number of accessible states, divided by the number of particles, is logarithm of NA cubed plus one divided by V.

What's the physical origin of this mysterious extra nat?

Mathematically it comes from Stirling's formula, which showed up when we switched from a gas of distinguishable particles to a gas of indistinguishable particles. It may seem odd that indistinguishability would increase the entropy by one nat per particle, but don't be confused: as we've seen, it greatly reduces it. For a gas of distinguishable particles the log of the number of accessible states, divided by the number of particles, is logarithm of V over A cubed. When we switch to indistinguishable particles this drops to logarithm of V over NA cubed plus one.

Here is a rough heuristic explanation of what's going on. For a single particle in a box of volume V, the number of accessible states is V over A cubed. In a gas of distinguishable free particles, each roams independently around the whole volume V. Thus, the log of the number of accessible states is logarithm of V over A cubed per particle.

For a gas of indistinguishable particles, the story changes. For starters, we can crudely pretend each particle is trapped in its own tiny box of volume V over N. After all, if it leaves this tiny box by trading places with another particle in another tiny box, nothing really changes. In this approximation, the log of the number of accessible states is logarithm of V over NA cubed per particle.

But it's not really true that each particle can only leave its tiny box by trading places with another. We can have more than one particle in the same tiny box-or none. That is, our gas can have density fluctuations. An exact treatment of the problem gives, not logarithm of V over NA cubed nats per particle, but logarithm of V over A cubed minus logarithm of N factorial.

Stirling's formula says this is approximately logarithm of V over A cubed minus open parenthesis logarithm of N minus one close parenthesis equals logarithm of V over NA cubed plus one.

This explains the mysterious extra nat. The extra nat of entropy per particle is due to density fluctuations!

As we've seen, even this is an oversimplification. A still better approximation, again coming from Stirling's formula, says logarithm of V over A cubed minus logarithm of N factorial is approximately equal to logarithm of V over NA cubed plus one minus two times logarithm of two pi N over N.

But as we saw in Puzzle forty-seven, this further correction is negligible for a mole of gas. It only becomes interesting for microscopic systems.

Now let's look at our second formula for the entropy of a gas of N indistinguishable classical free particles:

S is approximately equal to k N times open parenthesis logarithm of plus plus logarithm of k T plus logarithm of two pi m h squared plus three close parenthesis.

Not only is this harder to remember, it's generally less friendly to physical intuition. First of all, three of the terms involve the logarithm of dimensionful quantities. Thus, when we change units they change, not by rescaling in the usual way, but by addition or subtraction. Secondly, the important role of the thermal wavelength is concealed in this formula.

The main advantage of this formula is that it separates out three contributors to the entropy per particle:

The volume available per particle, V over N. The bigger this is, the more entropy the gas has per particle.

The temperature, T. The bigger this is, the more entropy per particle.

The particle mass, m. The bigger this is, the more entropy per particle.

The first two should be rather intuitive. But what about the third? We need to combine V over N and T with the particle mass m and some constants of nature to get a dimensionless quantity, which we can then take the logarithm of. This leads us straight to the thermal wavelength:

logarithm of V plus logarithm of k T plus minus logarithm of three times two pi m h squared.

equals logarithm of N A cubed V.

Thus, my best explanation of why a gas of heavier particles has more entropy per particle is that they have a shorter thermal wavelength, so we can specify their position more accurately, and it takes more information to do so.


## WHERE ARE WE NOW?

The mystery: why does each molecule of hydrogen have approximately twenty-three bits of entropy at standard temperature and pressure?

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

N times open parenthesis logarithm of plus comma logarithm of k T plus gamma over two three including the mysterious constant gamma:

two pi times m times the square root gamma equals two over one over two plus two


## The subgoal: compute the entropy of a single classical particle in a one-dimensional box:

S equals k times logarithm of L plus minus logarithm of k T plus one over twelve plus two times the square root


## The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator:

: k ( In Ka kT +1

how

Okay, now we know the entropy of a classical ideal monatomic gas! We even know what it means. Unfortunately we're trying to figure out the entropy of hydrogen, which is diatomic. But we can do helium, which is monatomic ... and then we'll do hydrogen.


## ENTROPY PER MOLE VERSUS BITS PER MOLECULE

A nat of unknown information is one point three eight zero six four nine times ten to the negative twenty-three joules per kelvin of entropy: this is Boltzmann's constant.

There are six point zero two two one four zero seven six times ten to the twenty-three molecules per mole: this is Avogadro's number.

Thus, one nat of unknown information per molecule corresponds to one point three eight zero six four nine times ten to the negative twenty-three multiplied by six point zero two two one four zero seven six times ten to the twenty-three approximately eight point three one four four six three joules per kelvin of entropy per mole.

A bit is natural log of two approximately zero point six nine three one five nats, so one bit of unknown information per molecule corresponds to about zero point six nine three one five multiplied by eight point three one four four six three approximately five point seven six three one four six joules per kelvin of entropy per mole.

Here is a little fact we need now: one bit of Shannon entropy per molecule equals about five point seven six joules per kelvin of Gibbs entropy per mole. I apologize for the oppressively large number of decimal places above, but I want to compare our theoretical predictions of the entropy of helium and hydrogen to experimental results, and it's not clear yet how closely our answers will match experiment, so it's good to be prepared.

By the way, the values of Boltzmann's constant and Avogadro's number here are exact, fixed by the definition of SI units. So there is no experimental uncertainty in any of the numbers on this page.

THE ENTROPY OF HELIUM: THEORY

The Sackur-Tetrode equation says that assuming helium is a classical ideal monatomic gas, its entropy is

S sub i approximately k N left parenthesis natural log fraction V over N Lambda cubed plus fraction five over two right parenthesis which corresponds to natural log fraction V over N Lambda cubed plus fraction five over two nats of unknown information per atom. At standard temperature and pressure, this gives about fifteen point zero four one nats or fraction fifteen point zero four one over natural log two approximately twenty-one point seven zero zero bits of unknown information per atom.

Now let's calculate the entropy of helium in its gaseous state. NIST has tabulated its entropy at standard temperature and pressure, specifically temperature T equals two nine eight point one five Kelvin and pressure P equals one bar, so that's what we'll try to calculate. An atom of helium has a mass of m equals six point six four six four seven seven times ten to the negative twenty-seven kilograms, so at standard temperature its thermal wavelength is

Lambda equals fraction h over square root two pi m k T approximately fraction h over square root left parenthesis two pi multiplied by six point six four six four seven seven times ten to the negative twenty-seven kilograms multiplied by one point three eight zero six four nine times ten to the negative twenty-three joules per Kelvin multiplied by two nine eight point one five Kelvins right parenthesis approximately five point zero five three seven two one times ten to the negative eleven meters.

For a mole of an ideal gas we have N equals six point zero two two one four zero seven six times ten to the twenty-three (this is Avogadro's number), and at standard temperature and pressure a mole of ideal gas has V approximately zero point zero two four seven eight nine six cubic meters: this is called its 'molar volume'. The molar volume of helium is actually slightly different from this, because helium is not an ideal gas: the atoms interact. But since we're doing a calculation assuming helium is a classical ideal gas, let's ignore that for now. We then get fraction V over N Lambda cubed approximately fraction zero point zero two four seven eight nine six cubic meters over six point zero two two one four zero seven six times ten to the twenty-three multiplied by left parenthesis five point zero five three seven two one times ten to the negative eleven meters right parenthesis cubed approximately two seven nine six six three. We thus have natural log fraction V over N Lambda cubed approximately natural log two seven nine six six three approximately twelve point five four one. As explained earlier, this means that the logarithm of the number of accessible states of each helium atom would be twelve point five four one if it were trapped in its own small box of volume V over N. But density fluctuations contribute one extra nat of entropy per atom. Thus, the free energy part of the entropy per atom is thirteen point five four one nats. On the other hand, the expected energy part of the entropy per atom is two, coming from the atom's three momentum degrees of freedom. The total entropy per atom is thus

In A three plus one plus equals one NA three fifteen point zero four one nats.

To impress our friends we can convert this to bits: we divide by ln two and get about fifteen point zero four one zero point six nine three one five equals twenty-one point seven zero zero bits of unknown information per atom of helium.

I've kept only five significant figures in the later stages of these calculations, since that's how precise the experimental data is. Next let's compare the final result to experiment!


## THE ENTROPY OF HELIUM: EXPERIMENT

The entropy of helium at standard temperature and pressure has been measured to be one hundred twenty-six point one five joules per kelvin per mole.

One bit of unknown information per atom corresponds to about five point seven six three one joules per kelvin of entropy per mole.

Thus, each atom of helium at standard temperature and pressure carries about one hundred twenty-six point one five equals twenty-one point eight eight nine five point seven six three one bits of unknown information.

Experimentally, the entropy of helium at standard temperature and pressure is one hundred twenty-six point one five joules per kelvin per mole. Converting this to bits per atom we get twenty-one point eight eight nine, very close to our theoretical result of twenty-one point seven zero zero, but about zero point nine percent higher.

There are a couple of possible reasons for this slight discrepancy. First, while our theoretical calculation assumed that helium is an ideal gas of noninteracting point particles, this is not true. The helium atoms interact!

Second, our computation ignored quantum effects except for using Planck's constant to determine the thermal wavelength. Even for an ideal gas, quantum effects become important when V over NA three ceases to be large. This happens at high densities V over N, low temperatures T, or for particles of small mass m. Helium has a low mass as molecules of gas go and our ultimate goal, hydrogen, is even worse.

Now let's tackle the final summit: hydrogen. This is a diatomic gas, so it works differently.


## THE IDEAL DIATOMIC GAS

In thermal equilibrium, a classical ideal diatomic gas of N indistinguishable molecules of mass m in a three-dimensional box of volume V has expected energy five E equals kNT

and free energy

F equals negative kT In N! A three N one V N

where A equals h over square root two pi m k T is the thermal wavelength.

Its entropy S is E minus F over T, so E N over I M A three plus two minus negative k ln N!

and using Stirling's formula In N! approximately equal to (In N minus one) N we get S approximately equal to k N (In M A three plus three) N A three

It's easy to repeat our computation of entropy for a diatomic gas if we recall that the tumbling of the molecules adds two degrees of freedom to the three for position, giving E equals two kNT. Tracking the effects of this change we see the entropy is higher than for a monatomic gas. To be precise, the entropy of a classical ideal diatomic gas is approximately equal to E N (In M A S plus two) N A three

So, it has one more nat of Shannon entropy per molecule than an ideal monatomic gas! Let's see how this plays out for hydrogen.


## THE ENTROPY OF HYDROGEN: THEORY

Assuming hydrogen is a classical ideal diatomic gas, its entropy is

E N (In N A S plus two) N A three which corresponds to ln N A three V plus seven nats of unknown information per molecule. At standard temperature and pressure, this gives fifteen point one four four nats or ln two fifteen point one four four approximately equal to twenty-one point eight four eight bits of unknown information per molecule.

A hydrogen molecule has m equals three point three four seven zero six times ten to the negative twenty-seven kilograms, so at a temperature T equals two hundred ninety-eight point one five kelvin its thermal wavelength is six point six two six zero seven times ten to the negative thirty-four joule seconds approximately equal to two pi times three point three four seven zero six times ten to the negative twenty-seven kilograms times one point three eight zero six four nine times ten to the negative twenty-three joules per kelvin times two hundred ninety-eight point one five kelvin approximately equal to seven point one two one five six times ten to the negative eleven meters.

For a mole of an ideal gas at standard temperature and pressure, N equals six point zero two two one four zero seven six times ten to the twenty-third and V approximately equal to zero point zero two four seven eight nine six cubic meters, so approximately equal to one hundred thirteen thousand nine hundred seventy-one N A three V approximately equal to six point zero two two one four zero seven six times ten to the twenty-third times (seven point one two one five six times ten to the negative eleven meters) cubed zero point zero two four seven eight nine six cubic meters

We thus have ln N A three V approximately equal to In one hundred thirteen thousand nine hundred seventy-one approximately equal to eleven point six four four

Thanks to our previous work we know this means that that the logarithm of the number of accessible states of each molecule would be eleven point six four four if it were trapped in its own small box of volume V over N. There is also a correction to this simplified picture due to density fluctuations, which gives one extra nat of entropy. These add up to give the free energy contribution to the entropy per molecule: twelve point six four four nats. This is less than we got for helium. But the expected energy contribution to the entropy per molecule is larger: we again get two nats from the molecule's three momentum degrees of freedom,

but now we get one extra nat due to its two extra tumbling degrees of freedom. The total number of nats of unknown information per hydrogen molecule is thus ln V over N A cubed plus one plus three over two plus one approximately equal to fifteen point one four four. Finally, the number of bits of unknown information per hydrogen molecule is fifteen point one four four divided by zero point six nine three one five approximately equal to twenty-one point eight four eight. This is slightly more than for helium, where the number was twenty-one point seven zero zero.

As a sanity check, let's do this calculation a different way. A hydrogen molecule is close to half the mass of a helium atom, so its thermal wavelength should be square root two times as large. In our calculation we're treating V over N as the same for both gases, so hydrogen's V over N A cubed should be two to the negative three halves times as large as that for helium. Since ultimately we compute bits by taking a logarithm in base two, this reduces its entropy per molecule by three halves bits. However, hydrogen's two tumbling degrees of freedom increase its entropy per molecule by one nat, or one over ln two bits. We have negative three halves plus one over ln two approximately equal to negative one point five plus one point four four three approximately equal to negative zero point zero five seven. This suggests that each hydrogen molecule should carry zero point zero five seven fewer bits of unknown information than each helium atom. Why did our more careful calculation say hydrogen should have about twenty-one point eight four eight minus twenty-one point seven zero zero approximately equal to zero point one four eight more bits of unknown information per molecule? What's the mistake?

The slight discrepancy arises solely from the fact that a hydrogen molecule is not exactly half the mass of a helium atom! It's a bit heavier. It's actually more like zero point five zero three five-eight times the mass of a helium. This makes its thermal wavelength a bit smaller than our estimate in the last paragraph, which boosts its entropy. It's nice that such subtleties, ultimately due to nuclear physics, are showing up here.

By the way, all our calculations have been for the most common isotopes of hydrogen and helium: hydrogen whose nucleus consists of a single proton, and helium whose nucleus consists of two protons and two neutrons. Other isotopes have significantly different mass, and this changes the entropy values significantly.

Puzzle forty-eight. Helium has a lighter isotope called helium three, whose nucleus is made of two protons and just one neutron. The mass of helium three is five point zero zero eight two three times ten to the negative twenty-seven kilograms. If we repeat our calculation of the entropy of helium at standard temperature and pressure, changing only this mass, what value do we get for the bits of entropy per atom of helium three?

Puzzle forty-nine. Hydrogen has a heavier isotope called deuterium, whose nucleus is made of one proton and one neutron. The mass of a hydrogen molecule made of two deuterium atoms is three point three four four four nine times ten to the negative twenty-seven kilograms. If we repeat our calculation of the entropy of hydrogen at standard temperature and pressure, changing only this mass, what do we get for the bits of entropy per molecule of this sort?


## THE ENTROPY OF HYDROGEN: EXPERIMENT

The entropy of hydrogen at standard temperature and pressure has been measured to be one hundred thirty point six eight joules per kelvin per mole.

One bit of unknown information per molecule corresponds to about five point seven six three one joules per kelvin of entropy per mole.

Thus, each molecule of hydrogen at standard temperature and pressure has about one hundred thirty point six eight divided by twenty-two point six seven five equals five point seven six three one bits of unknown information.

Okay, let's compare our theoretical prediction to experiment.

The experimental figure for the entropy of hydrogen at standard temperature and pressure is one hundred thirty point six eight joules per kelvin per mole, which translates into twenty-two point six seven five bits per molecule. This is larger than our theoretical prediction of twenty-one point eight four eight bits per molecule by about three point eight percent.

That's not bad. We can say we solved our original problem fairly well. But the percentage error here is about four times worse than it was for calculation for helium. Why is it worse?

I haven't studied this, but I can imagine two reasons. First, remember that quantum effects kick in when V over NA cubed ceases to be large. This quantity is a bit smaller for hydrogen than for helium. Remember, for helium it was two hundred seventy-nine thousand six hundred sixty-three at standard temperature and pressure, while for hydrogen it's one hundred thirteen thousand nine hundred seventy-one. But that's still very large, so I imagine quantum effects are still quite tiny.

Second, hydrogen molecules are not chemically inert like helium atoms, and they're larger, and diatomic rather than monatomic. So I'd expect them to interact more, making the ideal gas approximation worse. This feels like a more plausible explanation for the three point eight percent discrepancy.

Puzzle fifty. Do research to find more accurate calculations of the entropy of hydrogen gas. What are the main sources of error in the calculation we have done here?


## WHERE DID WE GO?

The mystery: why does each molecule of hydrogen have roughly twenty-three bits of entropy at standard temperature and pressure?

The goal: derive and understand the formula for the entropy of a classical ideal monatomic gas:

minus Wand M plus three times In M plus minus In KT plus Y.

Including the mysterious constant Y:

two m m square root.

Y equals two plus one-half plus two.


## The subgoal: compute the entropy of a single classical particle in a one-dimensional box:

S equals k times In L plus minus In KT plus minus In one-half.

plus two times In two times one.


## The sub-subgoal: explain entropy from the ground up, and compute the entropy of a classical harmonic oscillator:

S equals k times In one plus one times h times K T square root.

We're done! Or at least we reached our stated goal. But there is a lot more to say about entropy. In a way we've scarcely scratched the surface. For more on the mathematics of entropy, I recommend these books:


## For classical and quantum statistical mechanics, I recommend these:

The second one has an intense focus on our friend the box of gas. And for the principle of maximum entropy, I again recommend this insightful and opinionated text:


## THE FIRST LAW OF THERMODYNAMICS

Suppose a system has some measure space X of states with functions called energy E : X goes to R and volume V : X goes to R.

Consider probability distributions on X maximizing the Gibbs entropy S subject to constraints on the expected values of E and V.

Then as we vary the expected values of E and V we have the derivative of the expected value of E equals T times the derivative of the entropy minus P times the derivative of the expected value of V.

where T is called temperature and P is called pressure.

I said we were done. But what kind of course on entropy doesn't cover the three laws of thermodynamics? I talked a bit about the Third Law, but I haven't even mentioned the other two yet.

Here's why: this wasn't a course on thermodynamics. In 'classical thermodynamics' there's a tradition of taking concepts such as energy, work and heat as primitive, and treating the laws of thermodynamics as axioms. I've instead been explaining a bit of 'classical statistical mechanics', where we start with probability theory and attempt to derive classical thermodynamics. In this approach the laws of thermodynamics are not fundamental. They actually look a bit odd: they become results that hold under various conditions, so each one becomes a collection of theorems and conjectures.

I'll state versions of the three laws of thermodynamics in the language we've developed here. But please be aware that my versions are idiosyncratic and will make some people raise their eyebrows. I'm afraid you'll have to go elsewhere, like Reif's book, to learn these laws in their traditional form!

We've been maximizing entropy subject to a constraint on the expected value of one quantity. What if we do two or more? Everything works the same way, but the fundamental relation between temperature, energy and entropy, the derivative of the expected value of E equals T times the derivative of the entropy, gets one extra term for each constraint. The resulting equation is a version of the 'First Law of Thermodynamics'.

I'll explain the case with one extra constraint. Suppose we've got a measure space X whose points are states of some system. Choose two functions on it. They could be anything, but let's call them energy and volume and write them as E: X goes to R and V : X goes to R. These terms are favored because thermodynamics arose in part from the study of steam engines, where you've got a cylinder of steam with some energy and some volume. For any probability distribution P: X goes to the interval from zero to one, we can write down a formula for its Shannon entropy

H equals the integral over X of negative P of x times In P of x with respect to x and also the expected values

E equals integral E of x dx, V equals integral V of x dx.

Let's not worry now about whether these integrals converge.

Suppose we only know E and V, and we are trying to choose the 'best' probability distribution p with these expected values. What should we do? Following the principle of maximum entropy, we seek the probability distribution p that maximizes H subject to our constraints on E and V. If we do this, we are led to a Lagrange multipliers problem, much as in the the simpler case of one constraint. But now we need two Lagrange multipliers: let's call them Beta and Gamma. We get this equation:

dH equals Beta dE plus Gamma dV.

This is the First Law!

But this isn't the way physicists usually write it. To get the First Law in its usual form, first let's switch to using Gibbs entropy S equals k H, and emphasize the role of energy by solving for dE:

dE equals TdS minus PdV.

Then, to simplify the look of this equation, let's introduce variables called temperature and pressure:

T equals k Beta inverse, P equals Beta.

Now the First Law of Thermodynamics looks like this:

dE equals TdS minus PdV.

It says that as we move around among probability distributions that maximize entropy subject to constraints on expected energy and volume, the change in expected energy is the sum of two terms:

heat, meaning TdS

work, meaning -PdV.

For example, if we have a cylinder of steam with pressure P and we increase its expected volume by a little bit delta V, its expected energy goes down by about P delta V: that's how we understand the minus sign. In this situation the external world has done an amount of work -P delta V on the cylinder of steam, but most people say the cylinder of steam has done an amount of work P delta V on the external world.

Here are a few puzzles if you want to dig deeper. In the first two, I ask you to generalize ideas from our earlier work on maximizing entropy subject to a single constraint.

Puzzle fifty-one. Let X equal one, to n and let E, V: X maps to R be two functions whose values at i element of X we call E sub i and V sub i. Suppose p is a probability distribution maximizing the Shannon entropy H on the surface where

E equals e, V equals v,

and also suppose p sub one, to p sub n greater than zero. Show that at p we have dH equals Beta dE plus Gamma dV

for some Beta, Gamma element of R. Hint: first do the case where not all the E sub i are equal and not all the V sub i are equal. This guarantees that dE and dV are nonzero. You can handle the other cases separately.

Puzzle fifty-two. Under the conditions of Puzzle fifty-one show that n exp of negative Beta E sub i minus Gamma V sub i p sub i sum of exp of negative Beta E sub i minus Gamma V sub i


## Puzzle fifty-three. Generalize the results of Puzzles fifty-one and fifty-two to the case of any finite number of constraints.

Puzzle fifty-four. Generalize the results of Puzzle fifty-three to the case of a system with a countable infinity of states, or an arbitrary measure space of states. You will need to add assumptions to ensure that the sums or integrals converge.


## THE SECOND LAW OF THERMODYNAMICS

Suppose a system has some measure space X of states and at any time t there is a probability distribution p of t on X.

We say the second law of thermodynamics holds if t sub one less than or equal to t sub two implies S of p of t one less than or equal to S of p of t two.

This seems to be widely true, yet the conditions under which it holds are subtle and much-argued.

The Second Law of Thermodynamics, as commonly stated, says that the entropy of a closed system never decreases. This appears to be a profound fact about our universe. A huge challenge to physics is to understand where this law comes from. Can it be derived from some realistic assumptions? One problem is that the laws of classical mechanics are invariant under time-reversal. Thus, if we evolve probability distributions on some space of states according to these laws, for any probability distribution whose entropy is nondecreasing, there is a time-reversed one whose entropy is nonincreasing.

This is called the problem of the arrow of time: briefly, why does the future look so different from the past? Quantum mechanics makes the problem subtler, but does not provide an easy resolution. The solution may be that we happen to live in a universe a particular solution of the laws of physics-where entropy was very low at the Big Bang, making it easy for entropy to increase after that. But if you get ten physicists in a room and ask them to explain the arrow of time, you are likely to hear ten different opinions. Thus, I will not attempt to resolve it here. For more on that, I recommend this book:

Instead, let's see how the Second Law sheds light on the meaning of temperature. You'll notice that in our course I never talked about systems evolving in time, and I never talked about two systems interacting: always just a single system. Now let's imagine two systems, each in thermal equilibrium, but at possibly different temperatures. Say the first has entropy S one, expected energy E one and temperature T one. As usual, these are related by dS one equals dE one divided by T one.

Say the second system works similarly, with dS two equals dE two divided by T two.

We can define the total entropy of the two systems by

S equals S one plus S two and the total expected energy by

E equals E one plus E two.

Suppose now that the two systems can exchange energy with each other, but in a slow and gentle way, so we can approximately treat each one as in thermal equilibrium at any moment. If no energy flows in or out of the combined system, the total expected energy is conserved, so dE dt equals zero and thus dE one dt

What does the Second Law give us in this situation? It implies dS dt greater than or equal to zero or dS one dt plus dS two dt dS two dt

It follows that one divided by T one dE one dt plus one divided by T two dE two dt greater than zero or one divided by T one dE one dt one divided by T two dE one dt greater than or equal to zero.

We can rewrite this as negative T one inverse

Now suppose both T one and T two are positive. Then we get a remarkable consequence: as two systems exchange energy, with each staying in thermal equilibrium at every moment, expected energy can only flow from the system with higher temperature to the system with lower temperature!


## Puzzle fifty-five. Suppose one or both of the temperatures T one, T two are negative. How does this conclusion change?

THE THIRD LAW OF THERMODYNAMICS: REVISITED

If a system has countably many states, with just one of lowest energy, and thermal equilibrium is possible for this system for some temperature T greater than zero, then its entropy in thermal equilibrium approaches zero exponentially fast as a function of one over T as T approaches zero from above.

In our earlier work on the Third Law, we only studied systems with finitely many states. Later we saw how to compute entropy from the free energy and expected energy. This makes it a bit easier to handle systems with a countable infinity of states. In the following puzzles, which are only for the most devoted readers, let's use these ideas to prove and improve the Third Law for systems with countably many states.

Earlier we worked with temperature, but it's cooler to use coolness. For all the following puzzles, let's suppose we have a system with a countable infinity of states n equals one, two, three, ... with energies E sub n. Also suppose thermal equilibrium is possible for some Bo greater than zero, i.e., the sum

Z of Bo equals the summation L exp negative Bo E sub n, n equals one to infinity converges. (Our arguments also apply to systems with finitely many states, where this convergence condition is automatic.)

Puzzle fifty-six. Show that the system's partition function, expected energy, free energy and entropy are well-defined for all B greater than Bo.

Puzzle fifty-seven. Show that if we add some constant to the energy of each state

Èn equals E sub n plus c we get a new 'shifted' system whose partition function, expected energy, free energy and entropy are related to those of our original system by

Z equals exp negative beta c times Z, expected value E equals expected value E plus c, F equals F plus c, S equals S

for all B greater than Bo.

Now further suppose that our original system has just one state of least energy. Earlier we saw that we could reindex the states so that E one is less than E two, less than or equal to E three, less than or equal to ... and E sub n approaches positive infinity. The same is true of our new shifted system, and let's choose c equals negative E one so that the lowest energy of the shifted system is zero. With this shift we have zero equals E one is less than E two is less than E three is less than...

and E sub n approaches positive infinity.

Puzzle fifty-eight. Show that for any coolness <LATEX>\beta \geq \beta _ { 0 }</LATEX> we have

<LATEX>\widetilde { Z } \left( \beta \right) - 1 = \sum _ { n = 2 } ^ { \infty } e ^ { - \beta \widetilde { E } _ { n } } .</LATEX> Using this equation show

<LATEX>| \widetilde { Z } \left( \beta \right) - 1 | \leq e ^ { - \left( \beta - \beta _ { 0 } \right) \widetilde { E } _ { 2 } } | \widetilde { Z } \left( \beta _ { 0 } \right) - 1 |</LATEX> and thus

<LATEX>| \widetilde { Z } \left( \beta \right) - 1 | < \mathrm { c o n s t } e ^ { - \left( \beta - \beta _ { 0 } \right) \widetilde { E } _ { 2 } }</LATEX> for some constant independent of <LATEX>\beta .</LATEX> Use the fact that <LATEX>\widetilde { F } \left( \beta \right) = - \frac { 1 } { \beta } \ln \widetilde { Z } \left( \beta \right)</LATEX> to show that for large enough

<LATEX>\beta ,</LATEX> <LATEX>| \widetilde { F } \left( \beta \right) | < \mathrm { c o n s t } e ^ { - \left( \beta - \beta _ { 0 } \right) \widetilde { E } _ { 2 } }</LATEX> possibly for a different constant independent of <LATEX>\beta .</LATEX> Using Puzzle fifty-seven, conclude that

<LATEX>| F \left( \beta \right) - E _ { 1 } | < \mathrm { c o n s t } e ^ { - \left( \beta - \beta _ { 0 } \right) \left( E _ { 2 } - E _ { 1 } \right) } .</LATEX> Voilà! This shows that for a system with countably many states and just one state of lowest energy, if thermal equilibrium is possible at some positive temperature, then the free energy must approach this lowest energy exponentially fast as <LATEX>\beta \rightarrow + \infty .</LATEX> Now let's show something similar for the expected energy. Again we use the shifted system to simplify the calculations. I'll leave more work to you this time.


## Puzzle fifty-nine. Show that at any coolness <LATEX>\beta > \beta _ { 0 }</LATEX> we have

<LATEX>\frac { d } { d \beta } \widetilde { Z } \left( \beta \right) = - \sum _ { n = 2 } \widetilde { E } _ { n } e ^ { - \beta \widetilde { E } _ { n } } .</LATEX> Use this to show that <LATEX>\frac { d } { d \beta } \widetilde { Z } \left( \beta \right)</LATEX> goes to zero exponentially fast as <LATEX>\beta \rightarrow + \infty .</LATEX> Using

LaTeX formula: the expected value of E with a tilde with respect to beta equals negative the derivative with respect to beta of the natural logarithm of Z with respect to beta equals negative one divided by Z with respect to beta times the derivative with respect to beta of Z with respect to beta and Puzzle fifty-eight, show that LaTeX formula: the expected value of E with a tilde with respect to beta goes to zero exponentially fast as LaTeX formula: beta approaches positive infinity. Using Puzzle fifty-seven, conclude that LaTeX formula: the expected value of E with respect to beta approaches E sub one exponentially fast as LaTeX formula: beta approaches positive infinity. Finally, since

LaTeX formula: S equals k beta times the quantity F minus the expected value of E and both LaTeX formula: F and LaTeX formula: the expected value of E approach LaTeX formula: E sub one exponentially fast as LaTeX formula: beta approaches positive infinity, conclude that LaTeX formula: S approaches zero exponentially fast as

LaTeX formula: beta approaches positive infinity. Let's summarize! Suppose we have a system with a countable infinity of states and just one state of lowest energy. If thermal equilibrium is possible for this system for some LaTeX formula: T greater than zero, the Third Law of Thermodynamics says its entropy in thermal equilibrium goes to zero as LaTeX formula: T approaches zero from above. But in fact we can say more: for some LaTeX formula: a, LaTeX formula: b greater than zero we have

LaTeX formula: the absolute value of S with respect to beta is less than a times the exponential of negative b beta for all large enough

LaTeX formula: beta. One hundred twenty-one