## The Analysis of Spatial Association by Use of Distance Statistics

Introduced in this paper is a family of statistics, G, that can be used as a measure of spatial association in a number of circumstances. The basic statistic is derived, its properties are identified, and its advantages explained. Several of the G statistics make it possible to evaluate the spatial association of a variable within a specified distance of a single point. A comparison is made between a general G statistic and Moran's I for similar hypothetical and empirical conditions. The empirical work includes studies of sudden infant death syndrome by county in North Carolina and dwelling unit prices in metropolitan San Diego by zip-code districts. Results indicate that G statistics should be used in conjunction with I in order to identify characteristics of patterns not revealed by the I statistic alone and, specifically, the G sub i and G star statistics enable us to detect local "pockets" of dependence that may not show up when using global statistics.


## INTRODUCTION

The importance of examining spatial series for spatial correlation and autocorrelation is undeniable. Both Anselin and Griffith and Arbia have shown that failure to take necessary steps to account for or avoid spatial autocorrelation can lead to serious errors in model interpretation. In spatial modeling, researchers must not only account for dependence structure and spatial heteroskedasticity, they must also assess the effects of spatial scale. In the last twenty years a number of instruments for testing for and measuring spatial autocorrelation have appeared. To geographers, the best-known statistics are Moran's I and, to a lesser extent, Geary's c. To geologists and remote sensing analysts, the semi-variance is most popular. To spatial econometricians, estimating spatial autocorrelation coefficients of regression equations is the usual approach.

A common feature of these procedures is that they are applied globally, that is, to the complete region under study. However, it is often desirable to examine pattern at a more local scale, particularly if the process is spatially nonstationary. Foster and Gorr provide an adaptive filtering method for smoothing parameter estimates, and Cressie and Read present a modeling procedure. The ideas presented in this paper are complementary to these approaches in that we also focus upon local effects, but from the viewpoint of testing rather than smoothing.

This paper introduces a family of measures of spatial association called G statistics. These statistics have a number of attributes that make them attractive for measuring association in a spatially distributed variable. When used in conjunction with a statistic such as Moran's I, they deepen the knowledge of the processes that give rise to spatial association, in that they enable us to detect local "pockets" of dependence that may not show up when using global statistics. In this paper, we first derive the statistics G sub i left parenthesis d right parenthesis and G left parenthesis d right parenthesis, then outline their attributes. Next, the G left parenthesis d right parenthesis statistic is compared with Moran's I. Finally, there is a discussion of empirical examples. The examples are taken from two different geographic scales of analysis and two different sets of data. They include sudden infant death syndrome by county in North Carolina, and house prices by zip-code district in the San Diego metropolitan area.


## THE G sub i left parenthesis d right parenthesis STATISTIC

This statistic measures the degree of association that results from the concentration of weighted points (or area represented by a weighted point) and all other weighted points included within a radius of distance d from the original weighted point. We are given an area subdivided into n regions, i equals one, two, ellipses, n, where each region is identified with a point whose Cartesian coordinates are known. Each i has associated with it a value x (a weight) taken from a variable X. The variable has a natural origin and is positive. The G sub i left parenthesis d right parenthesis statistic developed below allows for tests of hypotheses about the spatial concentration of the sum of x values associated with the j points within d of the i th point.


## The statistic is

G sub i left parenthesis d right parenthesis equals fraction numerator summation from j equals one to n w sub i j left parenthesis d right parenthesis x sub j over denominator summation from j equals one to n x sub j end fraction, comma j not equal to i, (one)

where left curly bracket w sub i j right curly bracket is a symmetric one/zero spatial weight matrix with ones for all links defined as being within distance d of a given i; all other links are zero including the link of point i to itself. The numerator is the sum of all x sub j, within d of i but not including x sub i. The denominator is the sum of all x sub i not including x sub i. Adopting standard arguments (cf. Cliff and Ord, pages thirty-two to thirty-three), we may fix the value x, for the i th point and consider the set of left parenthesis n minus one right parenthesis factorial random permutations of the remaining x values at the j points. Under the null hypothesis of spatial independence, these permutations are equally likely. That is, let X sub j be the random variable describing the value assigned to point j, then

P left parenthesis X sub j equals x sub r right parenthesis equals one over left parenthesis n minus one right parenthesis, comma r not equal to i, and

Thus


## (two)

E left parenthesis G sub i right parenthesis equals summation from j not equal to i w sub i j left parenthesis d right parenthesis E left parenthesis X sub j right parenthesis over summation from j not equal to i summation from j not equal to i, equals W sub i over left parenthesis n minus one right parenthesis, where

W sub i equals summation sub j w sub i j left parenthesis d right parenthesis. Similarly,

E left parenthesis G sub i superscript two right parenthesis equals one over left parenthesis Sigma sub j x sub j right parenthesis squared left bracket Sigma sub j w sub i j squared left parenthesis d right parenthesis E left parenthesis X sub j squared right parenthesis plus sum sub j not equal k w sub i j left parenthesis d right parenthesis w sub i k left parenthesis d right parenthesis E left parenthesis X sub j X sub k right parenthesis right bracket Since

E left parenthesis X sub j squared right parenthesis equals sum sub r not equal i x sub r squared over left parenthesis n minus one right parenthesis and

E left parenthesis X sub f X sub k right parenthesis equals sum sub r not equal s not equal i x sub r x sub s over left parenthesis n minus one right parenthesis left parenthesis n minus two right parenthesis equals left brace left parenthesis sum sub r not equal i x sub r right parenthesis squared minus sum sub r not equal i x sub r squared right brace over left parenthesis n minus one right parenthesis left parenthesis n minus two right parenthesis period Recalling that the weights are binary

Sigma Sigma sub j not equal k w sub i j w sub i k equals W sub i squared minus W sub i and so

E left parenthesis G sub i superscript two right parenthesis equals one over left parenthesis Sigma sub j x sub j right parenthesis squared left brace fraction numerator W sub i Sigma sub j x sub j squared over denominator left parenthesis n minus one right parenthesis plus fraction numerator W sub i left parenthesis W sub i minus one right parenthesis over denominator left parenthesis n minus one right parenthesis left parenthesis n minus two right parenthesis left bracket left parenthesis Sigma sub j x sub j right parenthesis squared minus Sigma sub j x sub j squared right bracket right brace period Thus

Var left parenthesis G sub i right parenthesis equals E left parenthesis G sub i superscript two right parenthesis minus E squared left parenthesis G sub i right parenthesis equals one over left parenthesis Sigma sub j x sub j right parenthesis squared left bracket fraction numerator W sub i left parenthesis n minus one minus W sub i right parenthesis Sigma sub j x sub j squared over denominator left parenthesis n minus one right parenthesis left parenthesis n minus two right parenthesis right bracket plus fraction numerator W sub i left parenthesis W sub i minus one right parenthesis over denominator left parenthesis n minus one right parenthesis left parenthesis n minus two right parenthesis minus fraction numerator W sub i squared over denominator left parenthesis n minus one right parenthesis squared period If we sec t fraction numerator Sigma sub j x sub j over denominator left parenthesis n minus one right parenthesis equals Y sub i one and fraction numerator Sigma sub j x sub j squared over denominator left parenthesis n minus one right parenthesis minus Y sub i one squared equals Y sub i two comma then

Var left parenthesis G sub i right parenthesis equals fraction numerator W sub i left parenthesis n minus one minus W sub i right parenthesis over denominator left parenthesis n minus one right parenthesis squared left parenthesis n minus two right parenthesis end fraction left parenthesis fraction numerator Y sub i two over denominator Y sub i one squared end fraction right parenthesis period As expected, Var left parenthesis G sub i right parenthesis equals zero when W sub i equals zero (no neighbors within d right parenthesis, or when W sub i equals n minus one (all n minus one observations are within d right parenthesis, or when Y sub i two equals zero (all n minus one observations are equal).

Note that W sub i, Y sub i one, and Y sub i two depend on i. Since G sub i is a weighted sum of the variable X sub i, and the denominator of G sub i is invariant under random permutations of left brace x sub i, j not equal i right brace, it follows, provided W sub i over left parenthesis n minus one right parenthesis is bounded away from zero and from one, that the permutations distribution of G sub i under H sub zero approaches normality as n approaches infinity; cf. Hoeffding and Cliff and Ord. When d, and thus W sub i, is small, normality is lost, and when d is large enough to encompass the whole study fraction numerator W sub i left parenthesis n minus one minus W sub i right parenthesis Y sub i two over denominator left parenthesis n minus one right parenthesis squared left parenthesis n minus two right parenthesis Y one one squared end fraction fraction numerator W sub t star left parenthesis n minus W sub t star right parenthesis Y sub t star over denominator n squared left parenthesis n minus one right parenthesis left parenthesis Y one star right parenthesis squared end fraction area, and thus left parenthesis n minus one minus W sub i right parenthesis is small, normality is also lost. It is important to note that the conditions must be satisfied separately for each point if its G sub i is to be assessed via the normal approximation.


## ATTRIBUTES OF G sub i STATISTICS

It is important to note that G sub i is scale-invariant left parenthesis Y sub i equals b X sub i right parenthesis yields the same scores as X sub t but not location-invariant left parenthesis Y sub i equals a plus X sub i right parenthesis gives different results than X sub i. The statistic is intended for use only for those variables that possess a natural origin. Like all other such statistics, transformations like Y sub i equals log X sub i will change the results.

G sub i left parenthesis d right parenthesis measures the concentration or lack of concentration of the sum of values associated with variable X in the region under study. G sub i left parenthesis d right parenthesis is a proportion of the sum of all x sub j values that are within d of i. If, for example, high-value x sub j s are within d of point i, then G sub i left parenthesis d right parenthesis is high. Whether the G sub i left parenthesis d right parenthesis value is statistically significant depends on the statistic's distribution.

Earlier work on a form of the G sub i left parenthesis d right parenthesis statistic is in Getis, Getis and Franklin, and Getis. Their work is based on the second-order approach to map pattern analysis developed by Ripley left parenthesis one nine seven seven right parenthesis. In typical circumstances, the null hypothesis the set of x values within d of location i is a random sample drawn without replacement from the set of all x values. The estimated G sub i left parenthesis d right parenthesis is computed from equation one using the observed x sub j values. Assuming that G sub i left parenthesis d right parenthesis is approximately normally distributed, when

Z sub i equals left brace G sub i left parenthesis d right parenthesis minus E left bracket G sub i left parenthesis d right parenthesis right bracket right brace over square root of Var G sub i left parenthesis d right parenthesis four is positively or negatively greater than some specified level of significance, then we say that positive or negative spatial association obtains. A large positive Z sub i implies that large values of x sub j (values above the mean x) are within d of point i. A large negative Z sub i, means that small values of x sub j are within d of point i.

A special feature of this statistic is that the pattern of data points is neutralized when the expectation is that all x values are the same. This is illustrated for the case when data point densities are high in the vicinity of point i, and d is just large enough to contain the area of the clustered points. Theoretical G sub i of d values are high because W sub i is high. However, only if the observed x sub j values in the vicinity of point i differ systematically from the mean is there the opportunity to identify significant spatial concentration of the sum of x sub js. That is, as data points become more clustered in the vicinity of point i, the expectation of G sub i of d rises, neutralizing the effect of the dense cluster of x sub j values.

In addition to its above meaning, the value of d can be interpreted as a distance that incorporates specified cells in a lattice. It is to be expected that neighboring G sub i will be correlated if d includes neighbors. To examine this issue, consider a regular lattice. When n is large, the denominator of each G sub i is almost constant so it follows that correlation G sub i, G sub j equals proportion of neighbors that i and j have in common.


## EXAMPLE ONE

Consider the rook's case. Cell i has no common neighbors with its four immediate neighbors, but two with its immediate diagonal neighbors. The numbers of common neighbors are as illustrated below:

All the other cells have no common neighbors with i. Thus, the G-indices for the four diagonal neighbors have correlations of about zero point five with G sub i, four others have correlations of about zero point two five and the rest are virtually uncorrelated.

For more highly connected lattices (such as the queen's case) the array of nonzero correlations stretches further, but the maximum correlation between any pair of G-indices remains about zero point five.


## EXAMPLE TWO

X bar equals m. N equals fifty. A is greater than or equal to zero.

B is greater than or equal to zero. Put

A equals m times one plus c, B equals m times one minus c, zero is less than or equal to c is less than or equal to one. Using this example, the G sub i and G sub i star statistics are compared in the following table.

cell

G sub T. Z left parenthesis G sub I right parenthesis G sub I superscript star Z left parenthesis G sub I superscript star right parenthesis A, surrounded by As eight plus eight C over four nine minus C. five point thirty star five point forty-seven nine plus nine C over five zero A, adjacent to

M S eight plus three C over four nine minus C. two point zero six star nine plus four C over five zero. two point forty-three

We note that G sub I, and G sub I superscript star are similar in this case; if the central A was replaced by a B, Z left parenthesis G sub I right parenthesis would be unchanged, whereas Z left parenthesis G sub I superscript star right parenthesis drops to four point twenty-five. Thus, G sub I and G sub I superscript star typically convey much the same information.


## EXAMPLE THREE

Consider a large regular lattice for which we seek the distribution under H sub zero for G sub I superscript star with W sub I neighbors. Let P equals proportion of As equals proportion of Bs and one minus two P equals proportion of

M S. Let angle bracket K sub one, K sub two, K sub three denote the number of As, Bs, and M S, respectively so that K sub one plus K sub two plus K sub three equals N. For large lattices, in this case, the joint distribution is approximately tri-multinomial with index W and parameters left parenthesis P, P, one minus two P right parenthesis. Since

G sub I superscript star equals W sub I plus left parenthesis K sub one minus K sub two right parenthesis C over N clearly E left parenthesis G sub I superscript star right parenthesis equals W sub I over N as expected and V left parenthesis G sub I superscript star right parenthesis equals two P W sub I over N,

reflecting the large sample approximation. The distribution is symmetric and the standardized fourth moment is three plus one minus six P over two P W sub I. This is close to three provided P W sub I is not too small.

Since we are using G sub I and G sub I superscript star primarily in a diagnostic mode, we suggest that W sub I is greater than or equal to eight at least, that is, the queen's case, although further work is clearly necessary to establish cut-off values for the statistics.


## A GENERAL G STATISTIC

Following from these arguments, a general statistic, G left parenthesis D right parenthesis, can be developed. The statistic is general in the sense that it is based on all pairs of values left parenthesis X sub I, X sub J right parenthesis such that I and J are within distance D of each other. No particular location I is fixed in this case. The statistic is

G left parenthesis D right parenthesis equals the sum from I equals one to the sum from J equals one to N W sub I J left parenthesis D right parenthesis X sub I X sub J over the sum from I equals one to the sum from J equals one to N X sub I X sub J, J not equal to I. N left parenthesis five.

The G-statistic is a member of the class of linear permutation statistics, first introduced by Pitman in nineteen thirty-seven. Such statistics were first considered in a spatial context by Mantel in nineteen sixty-seven and Cliff and Ord in nineteen seventy-three, and developed as a general cross-product statistic by Hubert in nineteen seventy-seven and nineteen seventy-nine, and Hubert, Golledge, and Costanzo in nineteen eighty-one.

For equation five,

W equals the sum from I equals one to the sum from J equals one W sub I J left parenthesis D right parenthesis, J not equal to I so that

E left bracket G left parenthesis D right parenthesis right bracket equals W over left bracket N left parenthesis N minus one right parenthesis right bracket. six.

The variance of G follows from Cliff and Ord in nineteen seventy-three, pages seventy to seventy-one:

E left parenthesis G squared right parenthesis equals one over left parenthesis M sub one squared minus M sub two right parenthesis squared N superscript four left bracket B sub zero M sub two squared plus B sub one M sub four plus B sub two M sub one squared M sub two plus B sub three M sub one M sub three plus B sub four M sub one to the fourth power. Where M sub J equals sum from I equals one X sub I to the J, J equals one, two, three, four,

and

N superscript R equals N times N minus one times N minus two dot dot dot times N minus R plus one. The coefficients, B, are

B subscript zero equals N squared minus three N plus three S subscript one minus N S subscript two plus three W squared. B subscript one equals negative quantity N squared minus N S subscript one minus two N S subscript two plus three W squared. B subscript two equals negative quantity two N S subscript one minus quantity N plus three S subscript two plus six W squared. B subscript three equals four times N minus one S subscript one minus two times N plus one S subscript two plus eight W squared.

B subscript four equals S subscript one minus S subscript two plus W squared and where S subscript one equals one half summation summation quantity w subscript I J plus w subscript J I squared, J not equal to I, I J

S subscript two equals summation subscript I quantity w subscript I dot plus w subscript dot I squared; w subscript I dot equals summation subscript J w subscript I J, and J not equal to I;

thus variance of G equals expected G squared minus quantity W divided by N times N minus one squared.


## The G of D statistic and Moran's I compared

The G of D statistic measures overall concentration or lack of concentration of all pairs of x subscript I, x subscript I such that I and J are within D of each other. Following equation five, one finds G of D by taking the sum of the multiples of each x subscript I with all x subscript J s within D of all I as a proportion of the sum of all x subscript I x subscript J. Moran's I, on the other hand, is often used to measure the correlation of each x subscript I with all x subscript J s within D of I and, therefore,

G subscript min equals one seven zero divided by two four five zero equals zero point zero six nine four. variance of G subscript min equals zero point zero zero zero zero from equation seven.

is based on the degree of covariance within D of all X sub i. Consider K sub one, K sub two as constants invariant under random permutations. Then using summation shorthand we have

G of D equals K sub one sigma sum W sub i j X sub i X sub j and

I of D equals K sub two sigma sigma W sub i j left parenthesis X sub i minus X bar right parenthesis left parenthesis X sub j minus X bar right parenthesis. Equals parentheses K sub two divided by K sub one close parentheses G of D minus K sub two X bar sigma left parenthesis W sub i plus W sub i close parenthesis X sub i plus K sub two X bar squared W W sub i equals sum sub j W sub i j text and W dot i equals sum sub j W sub j i.

Since both G of D and I of D can measure the association among the same set of weighted points or areas represented by points, they may be compared. They will differ when the weighted sums sum W sub i X sub i, and sum W sub i X sub i, differ from W X tilde, that is, when the patterns of weights are unequal. The basic hypothesis is of a random pattern in each case. We may compare the performance of the two measures by using their equivalent Z values of the approximate normal distribution.


## EXAMPLE FOUR

Let us use the lattice of Example TWO. As before,

Set A plus B equals two m, therefore

X bar equals m. n equals fifty; A greater than or equal to zero B greater than or equal to zero put

A equals m left parenthesis one plus c right parenthesis; B equals m left parenthesis one minus c right parenthesis; zero less than or equal to c less than or equal to one. In addition, put a equals A minus m; B equals two m minus A equals m minus a; B minus m equals a; m greater than or equal to a j not equal to i. For the rook's case,

W equals sigma sigma W sub i j equals one seventy. I equals left parenthesis n sigma sigma sub i j left parenthesis X sub i minus X bar right parenthesis left parenthesis X sub j minus X bar right parenthesis divided by W sigma left parenthesis X sub i minus X bar right parenthesis squared right parenthesis equals left parenthesis fifty dot two four a squared dot two right parenthesis divided by left parenthesis one seventy dot eighteen a squared right parenthesis equals zero point seven eight four for all choices of a,

m. Var left parenthesis I right parenthesis equals zero point zero one zero eight nine seven. Z left parenthesis I right parenthesis equals seven point seven zero eight eight whenever A greater than B. G equals left parenthesis sum sum W sub i j X sub i X sub j divided by sigma sigma X sub i X sub j right parenthesis equals left parenthesis twenty-four A squared plus twenty-four B squared plus twenty-four A m plus twenty-four B m plus seventy-four m squared right parenthesis divided by left parenthesis two five zero zero m squared minus nine A squared minus nine B squared minus thirty-two m squared right parenthesis. Equals left parenthesis one seventy plus forty-eight c squared right parenthesis divided by two four five zero minus eighteen c squared. When c equals zero, A equals B equals m, and G is a minimum.

When c equals one, A equals two m, B equals zero, and G is a maximum.

G max equals two eighteen divided by two four three two equals zero point zero eight nine six. Var left parenthesis G max right parenthesis equals zero point zero zero zero zero one one eight five five. Z left parenthesis G max right parenthesis equals five point eight seven for any m.

G depends on the relative absolute magnitudes of the sample values. Note that I is positive for any A and B, while G values approach a maximum when the ratio of A to B or B to A becomes large.


## EXAMPLE FIVE

I equals zero, for any possible A, B, or m.

Z of I equals zero point one nine two zero since E of I equals negative one divided by n minus one, whenever A is greater than B.

G sub min equals G sub max equals zero point zero six nine four, for any possible A, B, or M.

V a r of G sub min equals zero, but V a r of G sub max equals zero point zero zero zero zero zero zero five nine.

Z of G max equals zero point zero seven three nine. Neither statistic can differentiate between a random pattern and one with little spatial variation. Contributions to G of d are large only when the product x sub I x sub I is large, whereas contributions to I of d are large when x sub I minus M x sub J minus M is large. It should be noted that the distribution is nowhere near normal in this case. A


## EXAMPLE SIX

One equals negative zero point seven eight four three, V a r of I equals zero point zero one zero eight nine seven, Z of I equals negative seven point three one seven seven. When A equals two M and B equals zero,

The juxtaposition of high values next to lows provides the high negative covariance needed for the strong negative spatial autocorrelation Z of I, but it is the multiplicative effect of high values near lows that has the negative effect on

Z of G. Table two gives some idea of the values of Z of G and Z of I under various circumstances. The differences result from each statistic's structure. As shown in the examples above, if high values within d of other high values dominate the pattern, then the summation of the products of neighboring values is high, with resulting high positive Z of G values. If low values within d of low values dominate, then the sum of the product of the xs is low resulting in strong negative Z of G values. In the Moran's case, both when high values are within d of other high values and low values are within d of other low values, positive covariance is high, with resulting high Z of I values.

Any test for spatial association should use both types of statistics. Sums of products and covariances are two different aspects of pattern. Both reflect the dependence structure in spatial patterns. The I bar of d statistic has its peculiar weakness in not being able to discriminate between patterns that have high values dominant within d or low values dominant. Both statistics have difficulty discerning a random pattern from one in which there is little deviation from the mean.

If a study requires that I of d or G of d values be traced over time, there are advantages to using both statistics to explore the processes thought to be responsible for changes in association among regions. If data values increase or decrease at the same rate, that is, if they increase or decrease in proportion to their already existing size, Moran's I changes while G of d remains the same. On the other hand, if all x values increase or decrease by the same amount, G of d changes but I of d remains the same.

It must be remembered that G of d is based on a variable that is positive and has a natural origin. Thus, for example, it is inappropriate to use G of d to study residuals from regression. Also, for both I of d and G of d one must recognize that transformations of the variable X result in different values for the test statistic. As has

Arthur Getis and J. K. Ord / 199

been mentioned above, conditions may arise when d is so small or large that tests based on the normal approximation are inappropriate.


## EMPIRICAL EXAMPLES

The following examples of the use of G statistics were selected based on size and type of spatial units, size of the X values, and subject matter. The first is a problem concerning the rate of sudden infant death syndrome by county in North Carolina, and the second is a study of the mean price of housing units sold by zip code district in the San Diego metropolitan region. In both cases the data are explained, hypotheses made clear, and G of d and I of d values calculated for comparable circumstances.


## One. Sudden Infant Death Syndrome by County in North Carolina

SIDS is the sudden death of an infant one year old or less that is unexpected and inexplicable after a postmortem examination. The data presented by Cressie and Chan were collected from a variety of sources cited in the article. Among other data, the authors give the number of SIDs by county for the period nineteen seventy-nine to nineteen eighty-four, the number of births for the same period, and the coordinates of the counties. We use as our data the number of SIDs as a proportion of births multiplied by one thousand. Since no viral or other causes have been given for SIDS, one should not expect any spatial association in the data. To some extent, high or low rates may be dependent on the health care infants receive. The rates may correlate with variables such as income or the availability of physicians' services. In this study we shall not expect any spatial association.

Results using the G statistic verify the hypothesis that there is no discernible association among counties with regard to SIDS rates. The values of Z of G are less than one. In addition, there seems to be no smooth pattern of Z values as d increases. The Z of I results are somewhat contradictory, however. Although none are statistically significant at the point zero five level, Z of I values from thirty to fifty miles, about the distance from the center of each county to the center of its contiguous neighboring counties, are well over one. This represents a tendency toward positive spatial autocorrelation at those distances. Taking the two results together, one should be cautious before concluding that a spatial association exists for SIDS

among counties in North Carolina. Perhaps more light can be shed on the issue by using the G sub i of d and G sub i star of d statistics.

Table four and Figure two give the results of an analysis based on the G sub i of d and G sub i star of d statistics for a d of thirty-three miles. This represents the distance to the furthest first-nearest neighbor county of any county.

The G sub i star of d statistic identifies five of the one hundred counties of North Carolina as significantly positively or negatively associated with their neighboring counties at the point zero five level. Four of these, clustered in the central south portion of the state, display values greater than positive one point nine six, while one county, Washington near Albemarle Sound, has a Z value of less than negative one point nine six. Taking into account values greater than positive one point fifteen, the eighty-seven point five percentile, it is clear that several small clusters in addition to the main cluster are widely dispersed in the southern part of the state. The main cluster of values less than negative one point fifteen, the twelve point five percentile, is in the eastern part of the state. It is interesting to note that many of the counties in this cluster are in the sparsely populated swamp lands surrounding the Albemarle and Pamlico Sounds. If overall error is fixed at point zero five and a Bonferroni correction is applied, the cutoff value for each county is raised to about three point five zero. However, such a figure is unduly conservative given the small numbers of neighbors.

Arthur Getis and J. K. Ord / 201

Positive one point one five to negative one point one five Positive one point one five to positive one point nine six Greater than positive one point nine six FIG. two. Z of G star of d equals furthest nearest neighbor equals thirty-three miles for SIDS Rates of Counties of North Carolina, nineteen seventy-nine to eighty-four.

In this case it becomes clear that an overall measure of association such as G of d or I of d can be misleading because it prompts one to dismiss the possibility of significant spatial clustering. The G sub i of d statistics, however, are able to identify the tendency for positive spatial clustering and the location of pockets of high and low spatial association. It remains for the social scientist or epidemiologist to explain the subtle patterns shown in Figure two.


## Two. Dwelling Unit Prices in San Diego County by Zip Code Area, September nineteen eighty-nine

Data published in the Los Angeles Times on October twenty-nine, nineteen eighty-nine, give the adjusted average price by zip code for all new and old dwelling units sold by builders, real estate agents, and homeowners during the month of September nineteen eighty-nine in San Diego County. The data are supplied by TRW Real Estate Information Services. One outlier was identified: Rancho Santa Fe, a wealthy suburb of the city of San Diego, had prices of sold dwelling units that were nearly three times higher than the next highest district, La Jolla. Since neither statistic is robust enough to be only marginally affected by such an observation, Rancho Santa Fe was not considered in the analysis.

Although the city of San Diego has a large and active downtown, San Diego County is not a monocentric region. One would not expect housing prices to trend upward from the city center to the suburbs in a uniform way. One would expect, however, that since the data are for reasonably small sections of the metropolitan area, that there would be distinct spatial autocorrelation tendencies. High positive I values are expected. G of d values are dependent on the tendencies for high values or low values to group. If the low cost areas dominate, the G of d value is negative. In this case, G of d is a refinement of the knowledge gained from

I. Table five shows that there are strong positive values for Z of I for distances of four miles and greater. Z of G also shows highly significant values at four miles and beyond, but here the association is negative, that is, low values near low values are much more influential than are the high values near high values. Moran's I clearly indicates that there is significant spatial autocorrelation, but, without knowledge of G of d, one might conclude that at this scale of analysis, in general, high income districts are significantly associated with one another.

By looking at the results of the G sub i of d statistics analysis for d equal to five, the individual district pattern is unmistakable. The Z of G sub i star of five values shown in Table six and Figure four provide evidence that two coastal districts are positively associated at the point zero five level of significance while eight central and south central districts are negatively associated at the point zero five level. There is a strong tendency for the negative values to be higher. It is for this reason that the Z of G values given above are so decidedly negative. The districts with high values along the coast have fewer near neighbors with similar values than do the central city lower value districts. The

Arthur Getis and J. K. Ord cluster of districts with negative Z of G sub i star values dominates the pattern. The adjusted Bonferroni cutoff is about three point two seven, but again is overly conservative.


## CONCLUSIONS

The G statistics provide researchers with a straightforward way to assess the degree of spatial association at various levels of spatial refinement in an entire sample or in relation to a single observation. When used in conjunction with Moran's I or some other measure of spatial autocorrelation, they enable us to deepen our understanding of spatial series. One of the G statistics' useful features, that of neutralizing the spatial distribution of the data points, allows for the development of hypotheses where the pattern of data points will not bias results.

When G statistics are contrasted with Moran's I, it becomes clear that the two statistics measure different things. Fortunately, both statistics are evaluated using normal theory so that a set of standard normal variates taken from tests using each type of statistic are easily compared and evaluated.