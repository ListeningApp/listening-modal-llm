## Thirteen GLM two: Comparing means adjusted for other predictors (analysis of covariance)

Thirteen point one. What will this chapter tell me?

My road to rock stardom had taken a bit of a knock with my unexpected entry to an all-boys' grammar school (rock bands and grammar schools really didn't go together). I needed to be inspired and I turned to the masters: Iron Maiden. I first heard Iron Maiden at the age of eleven when a friend lent me Piece of Mind on a cassette and told me to listen to 'The Trooper'. It was, to put it mildly, an epiphany. I became their smallest (I was eleven) biggest fan and obsessed about them in the unhealthiest of ways. I bombarded the man who ran their fan club (a guy called Keith) with letters, and, bless him, he replied to them all. Eventually my stalking paid off and Keith arranged for me to go backstage when they played what was then (and to me always will be) the Hammersmith Odeon in London on fifth November nineteen eighty-six. Not only was it the first time I had seen them live, but I got to meet them too. It is difficult to convey how exciting and anxiety-provoking that night was. It was all quite overwhelming. I was so utterly awe-struck that I managed to say precisely nothing to any of the band (but I do have some good photos where my speechlessness is tangible; see Figure thirteen point one). Soon to become a theme in my life, a social situation had provoked me to make an utter fool of myself. When it was over I was in no doubt that this was the best day of my life. In fact, I thought, I should just kill myself there and then because nothing would ever be as good. This may be true, but I have subsequently had other very nice experiences, so who is to say that they were not better? I could compare experiences to see which one is the best, but there is an important confound: my age. At the age of thirteen, meeting Iron Maiden was bowel-weakeningly exciting, but adulthood (sadly) dulls your capacity for this kind of unqualified excitement. To really see which experience was best, I would have to take account of the variance in enjoyment that is attributable to my age at the time. Doing so will give me a purer measure of how much variance in my enjoyment is attributable to the event itself.

This chapter extends the previous one to look at situations in which you want to compare groups' means, but also adjust those means for another variable (or variables) that you expect to affect the outcome. This involves a linear model in which an outcome is predicted from dummy variables representing group membership but one or more other predictors (usually continuous variables) are included. These additional predictors are sometimes labelled covariates, and this configuration of the linear model is sometimes known as analysis of covariance.


## Thirteen point two. What is ANCOVA?

In the previous chapter we saw how we can compare multiple group means with the linear model by using dummy variables to code group membership. In addition, in Chapter nine we saw how the linear model can incorporate several continuous predictor variables. It should, therefore, be no surprise that the linear model to compare means can be extended to include one or more continuous variables that predict the outcome (or dependent variable). When the main focus of the model is to compare means (perhaps from different experimental groups) then these additional predictors in the model are sometimes referred to as covariates. Also, this form of the linear model is sometimes referred to as analysis of covariance (or ANCOVA for short).

As we've discussed before, these labels for special cases of the linear model (such as one-way independent ANOVA in the previous chapter, and ANCOVA here) reflect historical divisions in methods. They are unhelpful because they create the impression that we're using distinct statistical models when we're not. I want you to focus on the general linear model that underpins these special cases, but I can't really avoid using the ANOVA/ANCOVA labels now and again so that when your supervisor tells you to do ANOVA/ANCOVA you can find the relevant part of the book!

In the previous chapter, we used an example about the effects of puppy therapy on happiness. Let's think about things other than puppy therapy that might influence happiness. Well, the obvious one is how much you like dogs (a dog phobic is going to be about as happy after puppy therapy as I would be after tarantula therapy), but there are other things too such as individual differences in temperament. If these variables (the covariates) are measured, then it is possible to adjust for the influence they have on the outcome variable by including them in the linear model. From what we know of hierarchical regression it should be clear that if we enter the covariate into the model first, and then enter the dummy variables representing the group means (e.g., the experimental manipulation), we can see what effect a predictor variable has, adjusting for the effect of the covariate. In essence, rather than predicting the outcome from group means, we predict it from group means that have been adjusted for the effect of covariate(s). There are two main reasons to include covariates in ANOVA:

To reduce within-group error variance: When we predict an outcome from group means (e.g., when these represent the effect of an experiment), we compute an F-statistic by comparing the amount of variability in the outcome that the experiment can explain against the variability that it cannot explain. If we can attribute some of this 'unexplained' variance to other measured variables (covariates), then we reduce the error variance, allowing us to assess more sensitively the difference between group means.

Elimination of confounds: In any experiment, there may be unmeasured variables that confound the results (i.e., variables other than the experimental manipulation that affect the outcome variable). If any variables are known to influence the outcome variable being measured, then including them as covariates can remove these variables as potential explanations for the effect of interest.


## Thirteen point three. ANCOVA and the general linear model

The researchers who conducted the puppy therapy study in the previous chapter suddenly realized that a participant's love of dogs would affect whether puppy therapy would affect happiness. Therefore, they repeated the study on different participants, but included a self-report measure of love of puppies from zero (I am a weird person who hates puppies, please be deeply suspicious of me) to seven (puppies are the best thing ever, one day I might marry one). The data are in Table thirteen point one and in the file Puppy Love dot sav, which contains the variables Dose (one equals control, two equals fifteen minutes, three equals thirty minutes), Happiness (the person's happiness

The summary of the model resulting from the self-test (Output thirteen point one) shows us the goodness of fit of the model first when only the covariate is used in the model, and second when both the covariate and the dummy variables are used. The difference between the values of R squared zero point two eight eight minus zero point zero six one equals zero point two two seven represents the individual contribution of puppy therapy to predicting happiness. Puppy therapy accounted for twenty-two point seven percent of the variation in happiness, whereas love of puppies accounted for only six point one percent. This additional information provides some insight into the substantive importance of puppy therapy. The next table is the ANOVA table, which is also divided into two sections. The top half represents the effect of the covariate alone, whereas the bottom half represents the whole model (i.e., covariate and puppy therapy included). Notice at the bottom of the ANOVA table (the bit for model two) that the entire model (love of puppies and the dummy variables) accounts for thirty-one point nine two units of variance S S sub M, there are one hundred ten point nine seven units in total S S sub T and the unexplained variance S S sub R is seventy-nine point zero five.

The interesting bit is the table of model coefficients (Output thirteen point two). The top half shows the effect when only the covariate is in the model, and the bottom half contains the whole model. The B values for the dummy variables represent the difference between the means of the fifteen-minute group and the control group (Dummy one) and the thirty-minute group and the control group (Dummy two - see Section twelve point two for an explanation of why). The means of the fifteen-and thirty-minute groups were four point eight eight and four point eight five respectively, and the mean of the control group was three point two two. Therefore, the B values for the two dummy variables should be roughly the same four point eight eight minus three point two two equals one point six six for Dummy one and four point eight five minus three point two two equals one point six three for Dummy two). The astute among you might notice that the B values in Output thirteen point two are not only very different from each other (which shouldn't be the case because the fifteen-and thirty-minute groups means are virtually the same), but also different from the values I've just calculated. Does this mean I've been lying to you for the past fifty pages about what the beta values represent? I'm evil, but I'm not that evil. The reason for this apparent anomaly is that with a covariate present, the B values represent the differences between the means of each group and the control adjusted for the covariate(s). In this case, they represent the difference in the means of the puppy therapy groups adjusted for the love of puppies. Output thirteen point one

These adjusted means come directly from the model. If we replace the B values in equation thirteen point one with the values in Output thirteen point two, our model becomes: Happiness equals one point seven eight nine plus two point two two five Long plus one point seven eight six Short plus zero point four one six Puppy love (thirteen point two) Remember that Long and Short are dummy variables such that Long takes the value of one only for the thirty-minute group, and Short takes a value of one only for the fifteen-minute group; in all other situations they have a value of zero. To get the adjusted means, we use this equation, but rather than replacing the covariate with an individual's score, we replace it with the mean value of the covariate from Table thirteen point two (two point seven three) because we're interested in the predicted value for each group at the mean level of the covariate. For the control group, the dummy variables are both coded as zero, so we replace Long and Short in the model with zero. The adjusted mean will, therefore, be two point nine two five: Happiness Control equals one point seven eight nine plus (two point two two five times zero) plus (one point seven eight six times zero) plus (zero point four one six times X Puppy love) equals one point seven eight nine plus (zero point four one six times two point seven three) (thirteen point three) equals two point nine two five

For the fifteen-minute group, the dummy variable Short is one and Long is zero, so the adjusted mean is four point seven one:

Happiness bar fifteen minutes equals one point seven eight nine plus (two point two two five times zero) plus (one point seven eight six times one) plus (zero point four one six times X bar Puppy love) equals one point seven eight nine plus one point seven eight six plus (zero point four one six times two point seven three) (thirteen point four)

equals four point seven one For the thirty-minute group, the dummy variable Short is zero and Long is one, so the adjusted mean is five point one five:

Happiness tilde thirty minutes equals one point seven eight nine plus (two point two two five times one) plus (one point seven eight six times zero) plus (zero point four one six times X bar Puppy love) equals one point seven eight nine plus two point two two five plus (zero point four one six times two point seven three) equals five point one five (thirteen point five)

We can now see that the B-values for the two dummy variables represent the differences between these adjusted means four point seven one minus two point nine three equals one point seven eight for Dummy one and five point one five minus two point nine three equals two point two two for Dummy two). These adjusted means are the average amount of happiness for each group at the mean level of love of puppies. Some people think of this kind of model (i.e., ANCOVA) as 'controlling' for the covariate, because it compares the predicted group means at the average value of the covariate, so the groups are being compared at a level of the covariate that is the same for each group. However, as we shall see, the 'controlling for the covariate' analogy is not a good one.

Output thirteen point two


## Thirteen point four Assumptions and issues in ANCOVA

Including covariates doesn't change the fact we're using the general linear model, so all the sources of potential bias (and counteractive measures) discussed in Chapter six apply. There are two additional considerations: (one) independence of the covariate and treatment effect; and (two) homogeneity of regression slopes.


## Thirteen point four point one Independence of the covariate and treatment

IIII

effect

I said in the previous section that covariates can be used to reduce within-group error variance if the covariate explains some of this error variance, which will be the case if the covariate is independent of the experimental effect (group means). Figure thirteen point two shows three different scenarios. Part A shows a basic model that compares group means (it is like Figure twelve point five). The variance in the outcome (in our example happiness) can be partitioned into two parts that represent the experimental or treatment effect (in this case the administration of puppy therapy) and the error or unexplained variance (i.e., factors that affect happiness that we haven't measured). Part B shows the ideal scenario when including a covariate, which is that the covariate shares its variance only with the bit of happiness that is currently unexplained. In other words, it is completely independent of the treatment effect (it does not overlap with the effect of puppy therapy at all). Some argue that this scenario is the only one in which ANCOVA is appropriate. Part C shows a situation in which the effect of the covariate overlaps with the experimental effect. In other words, the experimental effect is confounded with the effect of the covariate. In this situation, the covariate will reduce (statistically speaking) the experimental effect because it explains some of the variance that would otherwise be attributable to the experiment. When the covariate and the experimental effect (independent variable) are not independent, the treatment effect is obscured, spurious treatment effects can arise, and at the very least the interpretation of the ANCOVA is seriously compromised.

The problem of the covariate and treatment sharing variance is common and is ignored or misunderstood by many people. Miller and Chapman are not the only people to point this out, but their paper is very readable and they cite many examples of people misapplying ANCOVA. Their main point is that when treatment groups differ on the covariate, putting the covariate into the analysis will not 'control for' or 'balance out' those differences. This situation arises mostly when participants are not randomly assigned to experimental treatment conditions. For example, anxiety and depression are closely correlated (anxious people tend to be depressed), so if you wanted to compare an anxious group of people against a non-anxious group on some task, the chances are that the anxious group would also be more depressed than the non-anxious group. You might think that by adding depression as a covariate into the analysis you can look at the 'pure' effect of anxiety, but you can't. This situation matches part C of Figure thirteen point two because the effect of the covariate (depression) would contain some of the variance from the effect of anxiety. Statistically speaking, all that we know is that anxiety and depression share variance; we cannot separate this shared variance into 'anxiety variance' and 'depression variance', it will always be shared. Another common example is if you happen to find that your experimental groups differ in their ages. Placing age into the analysis as a covariate will not solve this problem - it is still confounded with the experimental manipulation. The use of covariates cannot solve this problem.

This problem can be avoided by randomizing participants to experimental groups, or by matching experimental groups on the covariate (in our anxiety example, you could try to find participants for the low-anxiety group who score high on depression). We can see whether this problem is likely to be an issue by checking whether experimental groups differ on the covariate before fitting the model. To use our anxiety example again, we could test whether our high-and low-anxiety groups differ on levels of depression. If the groups do not significantly differ then we might consider it reasonable to use depression as a covariate.

The treatment effect and covariate are simply predictor variables in a general linear model, yet despite several hundred pages discussing linear models, I haven't before mentioned that predictors should be completely independent. I've said that they shouldn't overlap too much (e.g., collinearity) but that's quite different from saying that they shouldn't overlap at all. If, in general, we don't care about predictors being independent in linear models, why should we care now? The short answer is we don't - there is no statistical requirement for the treatment variable and covariate to be independent.

However, there are situations in which ANCOVA can be biased when the covariate is not independent of the treatment variable. One situation, common in medical research, has been discussed a lot: an outcome (e.g., hypertension) is measured at baseline, and after a treatment intervention (with participants assigned to a treatment or control group). This design can be analyzed using an ANCOVA in which treatment effects on post-intervention hypertension are analyzed while covarying baseline levels of hypertension. In this scenario the independence of treatment and covariate variables means that baseline levels of hypertension are equal in the different treatment groups. According to Senn, the idea that ANCOVA is biased unless treatment groups are equal on the covariate applies only when there is temporal additivity. To use our hypertension example, temporal additivity is the assumption that both treatment groups would experience the same change in hypertension over time if the treatment had no effect. In other words, had we left the two groups alone, their hypertension would change by exactly the same amount. Given that the groups have different overall levels of hypertension to begin with, this assumption might not be reasonable, which undermines the argument for requiring group equality in baseline measures.

To sum up, the independence of the covariate and treatment makes interpretation more straightforward but is not a statistical requirement. ANCOVA can be unbiased when groups differ on levels of the covariate, but as Miller and Chapman point out, it creates an interpretational problem that ANCOVA cannot magic away.


## Thirteen point four point two Homogeneity of regression slopes

When a covariate is used we look at its overall relationship with the outcome variable: we ignore the group to which a person belongs. We assume that this relationship between covariate and outcome variable holds true for all groups of participants, which is known as the assumption of homogeneity of regression slopes. Think of the assumption like this: imagine a scatterplot for each group of participants with the covariate on one axis, the outcome on the other, and a regression line summarizing their relationship. If the assumption is met then the regression lines should look similar (i.e., the values of B in each group should be equal).

Let's make this concept a bit more concrete. Remember that the main example in this chapter looks at whether different doses of puppy therapy affect happiness when including love of puppies as a covariate. The homogeneity of regression slopes assumption means that the relationship between the outcome (dependent variable) and the covariate is the same in each of our treatment groups. Figure thirteen point three shows a scatterplot with regression line that summarizes this relationship (i.e., the relationship between love of puppies, the covariate, and the outcome, participant's happiness) for the three experimental conditions (shown in different panels). There is a positive relationship (the regression line slopes upwards from left to right) between love of puppies and participant's happiness in both the control (left panel) and fifteen-minute conditions (middle panel). In fact, the slopes of the lines for these two groups are very similar, showing that the relationship between happiness and love of puppies is very similar in these two groups. This situation is an example of homogeneity of regression slopes. However, in the thirty-minute condition (right panel) there is a slightly negative relationship between happiness and love of puppies. The slope of this line differs from the slopes in the other two groups, suggesting heterogeneity of regression slopes (because the relationship between happiness and love of puppies is different in the thirty-minute group compared to the other two groups).

Although in a traditional ANCOVA heterogeneity of regression slopes is a bad thing, there are situations where you might expect regression slopes to differ across groups and that variability may be interesting.

For example, when research is conducted across different locations, you might expect the effects to vary across those locations. Imagine you had a new treatment for backache, and you recruit several physiotherapists to try it out in different hospitals. The effect of the treatment is likely to differ across these hospitals (because therapists will differ in expertise, the patients they see will have different problems and so on). As such, heterogeneity of regression slopes is not a bad thing per se. If you have violated the assumption of homogeneity of regression slopes, or if the variability in regression slopes is an interesting hypothesis in itself, then you can explicitly model this variation using multilevel linear models (see Chapter twenty-one).


## Thirteen point four point three What to do when assumptions are violated

A bootstrap for the model parameters and post hoc tests can be used so that these, at least, are robust. The bootstrap won't help for the F-tests though. There is a robust variant of ANCOVA that can be implemented using R, and we'll discuss this in Section thirteen point eight.


## Thirteen point five Conducting ANCOVA using SPSS Statistics

Thirteen point five point one General procedure

The general procedure is much the same as for any linear model, so remind yourself of the steps for fitting a linear model. Figure thirteen point four shows a simpler overview of the process that highlights some of the specific issues for ANCOVA-style models. As with any analysis, begin by graphing the data and looking for and correcting sources of bias.

Figure thirteen point four General procedure for analysis of covariance

We have already looked at the data and the data file. To remind you, the data file is set out like Table thirteen point one and contains three columns: a coding variable called Dose (one equals control, two equals fifteen minutes, three equals thirty minutes), a variable called Happiness containing the scores for the person's happiness, and a variable called Puppy_love containing the scores for love of puppies from zero to seven. The thirty rows correspond to each person's scores on these three variables.


## Thirteen point five point three Testing the independence of the treatment

variable and covariate


## variable and covariate

In Section thirteen point four point one, I mentioned that if the covariate and group means (independent variable) are independent then the interpretation of ANCOVA models is a lot more straightforward. In this case, the covariate is love of puppies, so we'd want to check that the mean level of love of puppies is roughly equal across the three puppy therapy groups by fitting a linear model with Puppy_love as the outcome and Dose as the predictor.

Output thirteen point three shows that the main effect of dose is not significant, F two comma twenty-seven equals one point nine eight, P equals zero point one six, which shows that the average level of love of puppies was roughly the same in the three puppy therapy groups. In other words, the means for love of puppies in Table thirteen point two are not significantly different across the control, fifteen-and thirty-minute groups. This result is good news for using love of puppies as a covariate in the model.


## Thirteen point five point four The main analysis

Most of the General Linear Model (GLM) procedures in SPSS Statistics contain the facility to include one or more covariates. For designs that don't involve repeated measures it is easiest to include covariates by selecting Analyze General Linear Model GLM GEN Univariate to activate the dialog box in Figure thirteen point five. Drag the variable Happiness into the box labelled Dependent Variable (or click

), drag Dose into the box labelled Fixed Factor(s) and drag Puppy_love into the box labelled Covariate(s).


## Thirteen point five point five Contrasts

There are various dialog boxes that can be accessed from the main dialog box. If a covariate is selected, the post hoc tests are disabled because the tests that we used in the previous chapter are not designed for models that include covariates.

However, comparisons can be done by clicking Contrasts to access the

Contrasts dialog box in Figure thirteen point six. You cannot enter codes to specify user-defined contrasts (but see SPSS Tip thirteen point one); instead you can select one of the standard contrasts that we met in Table twelve point six. In this example, there was a control condition (coded as the first group), so a sensible set of contrasts would be simple contrasts comparing each experimental group to the control (this results in the same contrasts as dummy coding). Click the drop-down list and select a type of contrast (in this case Simple) from this list. For simple contrasts you need to specify the reference category (i.e., the category against which all other groups are compared). By default the last category is used, which for our data is the thirty-minute group. We need to change the reference category to be the control group, which is the first category (assuming that you coded control as one). We make this change by selecting

First. Having selected a contrast, click Change to register the selection. Figure thirteen point six shows the completed dialog box. Click Continue to return to the main dialog box.


## Thirteen point five point six Other options

You can get a limited range of post hoc tests by clicking EM Means ... to access the Estimated Marginal Means dialog box (see Figure Thirteen point seven). To specify post hoc tests, drag the independent variable (in this case Dose) from the box labelled Estimated Marginal Means: Factor(s) and Factor Interactions to the box labelled Display Means for (or click Save ... ). Once a variable has been transferred, you'll be able to select Compare main effects to activate the drop-down list ( LSD(none) ) of post hoc tests. The default is to perform a Tukey LSD post hoc test which makes no adjustment for multiple tests (and which I don't recommend). The other options are a Bonferroni post hoc test (recommended) and a Šidák correction, which is like the Bonferroni correction but is less conservative and so should be selected if you are concerned about the loss of power associated with Bonferroni. For this example we'll use the Šidák correction just for variety (we have used Bonferroni in previous examples). As well as producing post hoc tests for the Dose variable, the options we've selected will create a table of estimated marginal means for this variable: these are the

Continue group means adjusted for the effect of the covariate. Click

Clicking Options ... opens a dialog box containing the options described in Jane Superbrain Box Thirteen point three. The most useful are (in my opinion) descriptive statistics, parameter estimates, residual plot and HC-four robust standard errors (see Figure Thirteen point seven).

There is no option for specifying planned contrasts like we used in the previous chapter (see Section Twelve point six point two). However, these contrasts can be done if we fit the model using the regression menu. Imagine you chose some planned contrasts as in Chapter Twelve, in which the first contrast compared the control group to all doses of puppy therapy, and the second contrast then compared the thirty-and fifteen-minute groups (see Section Twelve point four). We saw in Sections Twelve point four and Twelve point six point two that we specify these contrasts with codes. For the first contrast we discovered that an appropriate set of codes was negative two for the control group and then one for both the thirty-and fifteen-minute groups. For the second contrast the codes were zero for the control group, negative one for the fifteen-minute group and one for the thirty-minute group (see Table Twelve point four). To do these contrasts when a covariate is included in the model, enter these values as two dummy variables. In other words, add a column called Dummy one in which every person in the control group has a value of negative two and all other participants have a value of one. Add a second column called Dummy two, in which everyone in the control group has the value zero, everyone in the fifteen-minute group has the value negative one and those in the thirty-minute group have a value of one. The file Puppy Love Contrast.sav includes these dummy variables. Output Thirteen point four

Run the analysis as described in Section Thirteen point three. The model summary and ANOVA table for the model will be identical to Output Thirteen point one (because we've done the same thing as before; the only difference is how the model variance is subsequently broken down with the contrasts). The B b-values for the dummy variables will be different than before because we've specified different contrasts. Output Thirteen point four shows the model parameters. The first dummy variable compares the control group with the fifteen-and thirty-minute groups. As such, it compares the adjusted mean of the control group (two point nine three) with the average of the adjusted means for the fifteen-and thirty-minute groups: the average of four point seven one plus five point one five over two equals four point nine three. The B b-value for the first dummy variable should reflect the difference between these values: four point nine three minus two point nine three equals two. We discovered in a rather complex and boring bit of Section Twelve point four point two that this value gets divided by the number of groups within the contrast (i.e., three) and so will be two over three equals zero point six seven (as in Output Thirteen point four). The associated T t-statistic is significant: P equals zero point zero one zero, indicating that the control group was significantly different from the combined adjusted mean of the puppy therapy groups.

The second dummy variable compares the fifteen-and thirty-minute groups, and so the B b-value should reflect the difference between the adjusted means of these groups: five point one five minus four point seven one equals zero point four four. In Section Twelve point four point two we discovered that this value gets divided by the number of groups within the contrast (i.e., two) and so will be zero point four four over two equals zero point two two (as in Output Thirteen point four). The associated T t-statistic is not significant: P equals zero point five nine three, indicating that the thirty-minute group did not produce significantly higher happiness than the fifteen-minute group after adjusting for love of puppies.


## The remaining options in this dialog box are as follows:

· Descriptive statistics: This option produces a table of means and standard deviations for each group.

· Estimates of effect size: This option produces the value of partial eta squared (partial eta squared) - see Section Thirteen point ten.

Observed power: This option provides an estimate of the probability that the statistical test could detect the difference between the observed group means (see Section two point nine point seven). This measure is pointless because if the F-test is significant then the probability that the effect was detected will, of course, be high. Likewise, if group differences were small, the observed power would be low. Do power calculations before the experiment is conducted, not after (see Section two point nine point eight).

Parameter estimates: This option produces a table of model parameters (b-values) and their tests of significance for the variables in the model (see Section thirteen point six point two).

Contrast coefficient matrix: This option produces matrices of the coding values used for any contrasts in the analysis, which is useful for checking which groups are being compared in which contrast.

Homogeneity tests: This option produces Levene's test of the homogeneity of variance assumption (see Section nine point three). You'll have seen by now that I think this test needs to be taken with a pinch of salt.

Spread versus level plot: This option produces a chart that plots the mean of each group of a factor (x-axis) against the standard deviation of that group (y-axis). This plot is useful to check that there is no relationship between the mean and standard deviation. If a relationship exists then the data may need to be stabilized using a logarithmic transformation (see Chapter six).

Residual plot: This option produces a matrix scatterplot of all combinations of pairs of the following variables: observed values of the outcome, predicted values from the model, standardized residuals from the model. These plots can be used to assess the assumption of homoscedasticity. In particular, the plot of the standardized residuals against the predicted values from the model can be interpreted in a similar way to the zpred versus zresid plot that we have discussed before.

Heteroskedasticity tests: There are four tests for heteroscedasticity that you can select (two variants of the Breusch-Pagan test, White's test and an F-test). For the same reasons that I don't recommend Levene's test, I also don't recommend these (that is, because they are significance tests your decisions based on them will be confounded by your sample size).

Parameter estimates with robust standard errors: This produces one of five methods (HC0 to HC4) to estimate standard errors (and, therefore, confidence intervals) for the model parameters that are robust to heteroscedasticity. These methods are described clearly in Hayes and Cai in twenty zero seven. In short, HC3 has been shown to outperform HC0 to HC2 (Long and Ervin in two thousand) but HC4 outperforms HC3 in some circumstances (Cribari-Neto in two thousand four). Basically choose HC3 or HC4.


## Oditi's Lantern ANCOVA Thirteen point five point seven Bootstrapping and plots

There are other options available from the main dialog box. For example, if you have several independent variables you can plot them against each other (which is useful for interpreting interaction effects, see Section fourteen point seven). There's also the

Bootstrap button, which you can use to activate bootstrapping. Selecting this option will bootstrap confidence intervals around the estimated marginal means, parameter estimates (b-values) and post hoc tests, but not the main F-statistic.

O K

Select the options described in Section six point twelve point three and click in the main dialog box to run the analysis.


## Thirteen point six Interpreting ANCOVA Thirteen point six point one What happens when the covariate is excluded?

Output thirteen point five shows (for illustrative purposes) the ANOVA table for these data when the covariate is not included. It is clear from the significance value, which is greater than zero point zero five, that puppy therapy seems to have no significant effect on happiness. Note that the total amount of variation in happiness (SST) was one hundred ten point ninety-seven (Corrected Total), of which the therapy condition accounted for sixteen point eighty-four units while ninety-four point twelve were unexplained differ in their levels of happiness.


## Thirteen point six point two The main analysis

The format of the ANOVA table in Output thirteen point six is largely the same as without the covariate, except that there is an additional row of information about the covariate (Puppy_love). Looking first at the significance values, the covariate significantly predicts the dependent variable which is less than zero point zero five. Therefore, the person's happiness is significantly influenced by their love of puppies. What's more interesting is that when the effect of love of puppies is removed, the effect of puppy therapy is significant which is less than zero point zero five. The amount of variation accounted for by puppy therapy has increased to twenty-five point nineteen units and the unexplained variance has been reduced to seventy-nine point zero five units. Notice that SST has not changed; all that has changed is how that total variation is partitioned.

This example illustrates how covariates can help us to exert stricter experimental control by taking account of confounding variables to give us a 'purer' measure of effect of the experimental manipulation. Looking back at the group means from Table thirteen point one, you might think that the significant F-statistic reflects a difference between the control group and the two experimental groups - because the fifteen and thirty-minute groups have very similar means (four point eighty-eight and four point eighty-five) whereas the control group mean is much lower at three point twenty-two. However, we can't use these group means to interpret the effect because they have not been adjusted for the effect of the covariate. These original means tell us nothing about the group differences reflected by the significant F. Output thirteen point seven gives the adjusted values of the group means (which we calculated in Section thirteen point three), and we use these values for interpretation (this is why we selected Display Means for in Section thirteen point five point six). From these adjusted means you can see that happiness increased across the three doses. Output thirteen point seven

Output thirteen point eight shows the parameter estimates selected in the Options dialog box and their bootstrapped confidence intervals and P-values (bottom table). These estimates result from Dose being coded using two dummy coding variables. The dummy variables are coded with the last category (the category coded with the highest value in the data editor, in this case the thirty-minute group) as the reference category. This reference category (labelled Dose equals three in the output) is coded with a zero for both dummy variables (see Section twelve point two for a reminder of how dummy coding works). Dose equals two, therefore, represents the difference between the group coded as two (fifteen minutes) and the reference category (thirty minutes), and Dose equals one represents the difference between the group coded as one (control) and the reference category (thirty minutes). The B-values represent the differences between the adjusted means in Output thirteen point seven and the significances of the T-tests tell us whether these adjusted group means differ significantly. The B for Dose equals one in Output thirteen point eight is the difference between the adjusted means for the control group and the thirty-minute group, two point nine two six minus five point one five one equals negative two point two two five, and the B for Dose equals two is the difference between the adjusted means for the fifteen-minute group and the thirty-minute group,

four point seven one two minus five point one five one equals negative zero point four three nine. The degrees of freedom for the T-test of the B-values are N minus K minus one (see Section nine point two point five), in which N is the total sample size (in this case thirty) and K is the number of predictors (in this case three, the two dummy variables and the covariate). For these data, D F equals thirty minus three minus one equals twenty-six. Based on the bootstrapped significance and confidence intervals (remember you'll get different values than me because of how bootstrapping works), we could conclude that the thirty-minute group differs significantly from the control group, P equals zero point zero two one (Dose equals one in the table), but not from the fifteen-minute group, P equals zero point five five eight, Dose equals two in the table.

The final thing to note is the value of B for the covariate (zero point four one six), which is the same as in Output thirteen point two (when we ran the analysis through the regression menu). This value tells us that if love of puppies increases by one unit, then the person's happiness should increase by just under half a unit (although there is nothing to suggest a causal link between the two); because the coefficient is positive we know that as love of puppies increases so does happiness. A negative coefficient would mean the opposite: as one increases, the other decreases.

Output thirteen point nine repeats the parameter estimates from Output thirteen point eight but with standard errors, P-values and confidence intervals robust to heteroscedasticity (the HC four estimates that we asked for). We can interpret the effects for Dose in the same way as for the regular and Bootstrap P-values and confidence intervals. For the effect of puppy love, the HC four robust confidence interval and P-value supports the conclusion from the non-robust model: the P-value is zero point zero three eight, which is less than zero point zero five, and the confidence interval does not contain zero (zero point zero two five, zero point eight zero seven). However, the bootstrap confidence interval (Output thirteen point eight) contradicts this conclusion because it contains zero (negative zero point zero two three, zero point six nine eight) and has a P equals zero point zero five two (again, we're reminded of how daft it is to have a threshold that yields such opposing conclusions from such small differences in a value).

Output thirteen point eight

Parameter Estimates

Parameter Estimates with Robust Standard Errors

Output thirteen point ten Contrast Results (K Matrix)


## Thirteen point six point three Contrasts

Output thirteen point ten shows the result of the contrast analysis specified in Figure thirteen point six and compares level two (fifteen minutes) against level one (control) as a first comparison, and level three (thirty minutes) against level one (control) as a second comparison. The group differences are displayed: a difference value, standard error, significance value and ninety-five percent confidence interval. These results show that both the fifteen-minute group (contrast one, P equals zero point zero four five) and thirty-minute group (contrast two, P equals zero point zero one zero) had significantly different happiness compared to the control group. Output thirteen point eleven shows the results of the Sidak corrected post hoc comparisons that were requested in Section thirteen point five point six. The bottom table shows the bootstrapped significance and confidence intervals for these tests and because these will be robust we'll interpret this table. There is a significant difference between the control group and both the fifteen- P equals zero point zero zero three and thirty-minute P equals zero point zero two one groups. The thirty-and fifteen-minute groups did not significantly differ P equals zero point five five eight. It is interesting that the significant difference between the fifteen-minute and control groups when bootstrapped P equals zero point zero zero three is not present for the normal post hoc tests P equals zero point one three zero. This anomaly could reflect properties of the data that have biased the non-robust version of the post hoc test.


## Thirteen point six point four Interpreting the covariate

I've already mentioned that the parameter estimates (Output thirteen point eight) tell us how to interpret the covariate: the sign of the B-value tells us the direction of the relationship between the covariate and outcome variable. For these data the B-value was positive, indicating that as the love of puppies increases, so does the participant's happiness. Another way to discover the same thing is to draw a scatterplot of the covariate against the outcome.

Anxious people tend to interpret ambiguous information in a negative way. For example, being highly anxious myself, if I overheard a student saying 'Andy Field's lectures are really different,' I would assume that 'different' meant rubbish, but it could also mean 'refreshing' or 'innovative'. Muris, Huijding, Mayer, and Hameetman addressed how these interpretational biases develop in children. Children imagined that they were astronauts who had discovered a new planet. They were given scenarios about their time on the planet (e.g., 'On the street, you encounter a spaceman. He has a toy handgun and he fires at you...') and the child had to decide whether a positive ('You laugh: it is a water pistol and the weather is fine anyway') or negative ('Oops, this hurts! The pistol produces a red beam which burns your skin!') outcome occurred. After each response the child was told whether their choice was correct. Half of the children were always told that the negative interpretation was correct, and the remainder were told that the positive interpretation was correct.

Over thirty scenarios children were trained to interpret their experiences on the planet as negative or positive. Muris et al. then measured interpretational biases in everyday life to see whether the training had created a bias to interpret things negatively. In doing so, they could ascertain whether children might learn interpretational biases through feedback.

The data from this study are in the file Muris et al two thousand and eight. The independent variable is Training (positive or negative) and the outcome is the child's interpretational bias score

(Interpretational_Bias) - a high score reflects a tendency to interpret situations negatively. It is important to adjust for the Age and Gender of the child and also their natural anxiety level (which they measured with a standard questionnaire of child anxiety called the SCARED) because these things affect interpretational biases also. Labcoat Leni wants you to fit a model to see whether Training significantly affected children's Interpretational_Bias using Age, Gender and SCARED as covariates. What can you conclude? Answers are on the companion website (or look at pages four hundred seventy-five to four hundred seventy-six in the original article).


## Thirteen point seven Testing the assumption of homogeneity of

regression slopes

Remember that the assumption of homogeneity of regression slopes means that the relationship between the covariate and outcome variable (in this case Puppy_love and Happiness) should be similar at different levels of the predictor variable (in this case in the three Dose groups). Figure thirteen point three shows that the relationship between Puppy_love and Happiness looks comparable in the fifteen-minute and control groups, but seems different in the thirty-minute group. To test the assumption of homogeneity of regression slopes we need to refit the model but customize it to include the interaction between the covariate and categorical predictor. Access the main dialog box as before and place the variables in the same boxes as before (the finished dialog box should look like

Figure thirteen point five). To customize the model, click Model to access the dialog box in Figure thirteen point nine and select Custom. The variables specified in the main dialog box are listed on the left-hand side. We need a model that includes the interaction between the covariate and grouping variable. To test this interaction term it's important to also include the main effects otherwise variance in the outcome (happiness) may be attributed to the interaction term that would otherwise be attributed to the main effects. To begin with, then, select Dose and

Puppy_love (you can select both simultaneously by holding down Control, or Command on a Mac), change the drop-down menu to Main effects, and click to transfer the main effects of Dose and Puppy_love to the box labelled Model. Next specify the interaction term by selecting Dose and

Puppy_love simultaneously (as just described), change the drop-down menu to

Interaction and click to transfer the interaction of Dose and Puppy_love to the box labelled Model. The finished dialog box should look like

Continue

Figure thirteen point nine. Click to return to the main dialog box and

OK

to run the analysis.

Output thirteen point eleven shows the main summary table for the model including the interaction term. The effects of the dose of puppy therapy and love of puppies are still significant, but so is the covariate by outcome interaction (Dose by

Puppy_love), implying that the assumption of homogeneity of regression slopes is not realistic (p equals zero point zero two eight). Although this finding is not surprising given the pattern of relationships shown in Figure thirteen point three, it raises concerns about the main analysis.

· When the linear model is used to compare several means adjusted for the effect of one or more other variables (called covariates) it can be referred to as analysis of covariance (ANCOVA).

· Before the analysis check that the covariate(s) are independent of any independent variables by seeing whether those independent variables predict the covariate (i.e., the covariate should not differ across groups).

· In the table labelled Tests of Between-Subjects Effects, assuming you're using an alpha of zero point zero five, look to see if the value in the column labelled Sig. is below zero point zero five for both the covariate and the independent variable. If it is for the covariate then this variable has a significant relationship to the outcome variable; if it is for the independent variable then the means (adjusted for the effect of the covariate) are significantly different across categories of this variable.

· If you have generated specific hypotheses before the experiment use planned contrasts; if not, use post hoc tests.

· For parameters and post hoc tests, look at the columns labelled Sig. to discover if your comparisons are significant (they will be if the significance value is less than zero point zero five). Use bootstrapping to get robust versions of these tests.

· In addition to the assumptions in Chapter six, test for homogeneity of regression slopes by customizing the model to look at the independent variable × covariate interaction.

We have already looked at robust confidence intervals and p-values for the model parameters that were computed using bootstrapping and heteroscedasticity robust standard errors. In addition, the companion website contains a syntax file for running a robust variant of ANCOVA that works on trimmed means and is described by Wilcox. We need the Essentials for R plugin and W R S two package installed. This test is limited to the situation where the independent variable (the categorical predictor) has two categories and there is one covariate. But it does enable you to ignore assumptions and get on with your life. Because this syntax only works when you have two groups, I have provided a data file called Puppies Two Group, which contains the example data for this chapter but excluding the fifteen-minute condition, so it compares the control (no puppies) with the thirty-minute group (Dose), and has the scores for the love of puppies covariate too (Puppy_love). The syntax to run the robust test is as follows: BEGIN PROGRAM R.

library(WRS2)

mySPSSdata = spssdata.GetDataFromSPSS(factorMode = "labels") ancboot(Happiness ~ Dose + Puppy_love, data = mySPSSdata, tr = zero point two, nboot = one thousand) END PROGRAM.

Select and run these five lines of syntax. As Output shows, the test works by identifying values of the covariate for which the relationship between the covariate and outcome are comparable in the two groups. In this example it identifies five values of Puppy_love (two, three, five, six, and eight) for which the relationship between love of puppies and happiness is comparable. At each of these design points, we're told the number of cases for the two groups (n one and n two) that have a value of the covariate (Puppy_love) close to these design points (not exactly x, but close to it). Based on these two samples, trimmed means (twenty percent by default) are computed and the difference between them tested. This difference is stored in the column Diff along with the boundaries of the associated ninety-five percent bootstrap confidence interval (corrected to control for doing five tests) in the next two columns. The test statistic comparing the difference is in the column statistic, with its p-value in the final column. Output shows no significant differences between trimmed means for any of the design points (all p-values are greater than zero point zero five).


## Thirteen point nine Bayesian analysis with covariates

Because the model we have fitted is a linear model with a categorical predictor and a continuous predictor, you can use what you learned to run a Bayesian regression. You would need to manually create dummy variables (as in the file Puppy Love Dummy) and drag these to the box labelled Factor(s) and drag Puppy_Love to the box labelled Covariate(s). You would interpret in the same way as the model we fitted.


## Thirteen point ten Calculating the effect size

In the previous chapter we used eta squared as an effect size measure when comparing means. When we include a covariate too we have more than one effect and we could calculate eta squared for each effect. We can also use an effect size measure called partial eta squared. This differs from eta squared in that it looks not at the proportion of total variance that a variable explains, but at the proportion of variance that a variable explains that is not explained by other variables in the analysis. Let's look at this with our example. Suppose we want to know the effect size of the dose of puppy therapy. Partial eta squared is the proportion of variance in happiness that the dose of puppy therapy shares that is not attributed to love of puppies (the covariate). If you think about the variance that the covariate cannot explain, there are two sources: it cannot explain the variance attributable to the dose of puppy therapy, sum of squares puppy therapy, and it cannot explain the error variability, sum of squares residual. Therefore, we use these two sources of variance instead of the total variability, sum of squares total, in the calculation. The difference between eta squared and partial eta squared is illustrated by comparing the following two equations:

Two sum of squares Effect eta squared equals sum of squares Total

(Equation thirteen point six)

Partial eta squared equals sum of squares Effect plus sum of squares Residual sum of squares Effect

(Equation thirteen point seven)

SPSS Statistics will produce partial eta squared for us, but to illustrate its calculation look at equation thirteen point eight, where we use the sums of squares in Output for the effect of dose (twenty-five point one nine), the covariate (fifteen point zero eight) and the error (seventy-nine point zero five):

13.3), but to illustrate its calculation look at equation (13.8), where we use the sums of squares in Output 13.6 for the effect of dose (25.19), the covariate (15.08) and the error (79.05):

Partial eta dose equals sum of squares dose plus sum of squares residual sum of squares dose equals twenty-five point one nine over twenty-five point one nine plus seventy-nine point zero five equals twenty-five point one nine over one hundred four point two four equals zero point two four

(Equation thirteen point eight)

Partial eta Puppy_love equals sum of squares Puppy_love plus sum of squares residual sum of squares Puppy_love equals fifteen point zero eight over fifteen point zero eight plus seventy-nine point zero five equals fifteen point zero eight over ninety-four point one three equals zero point one six

You can also use omega squared. However, this measure can be calculated only when we have equal numbers of participants in each group (which is not the case in this example). So, we're a bit stumped! Not all is lost, though, because, as I've said many times already, the overall effect size is not nearly as interesting as the effect size for more focused comparisons. These are easy to calculate because we selected to see the model parameters and so we have t-statistics for the covariate and comparisons between the fifteen-and thirty-minute groups and the control and thirty-minute group. These t-statistics have twenty-six degrees of freedom. We can use the same equation as in Section ten point nine point five.

Six. Strictly speaking, we should use a slightly more elaborate procedure when groups are unequal. It's a bit beyond the scope of this book, but Rosnow, Rosenthal, and Rubin give a very clear account.

"Contrast equals Vt two plus degrees of freedom t two

(thirteen point nine)

Therefore, we get (using t from Output thirteen point eight) values of zero point four zero for the covariate, and zero point four eight and zero point one one respectively for the comparison of the thirty-minute group and control, and the fifteen and thirty-minute groups:

R sub covariate equals the square root of two point two three squared divided by two point two three squared plus twenty-six equals the square root of four point nine seven divided by thirty point nine seven equals zero point four zero. R sub thirty mins vs. control equals the square root of negative two point seven seven squared divided by negative two point seven seven squared plus twenty six equals the square root of seven point six seven divided by thirty-three point six seven equals zero point four eight. R sub thirty vs fifteen mins equals the square root of negative zero point five four squared divided by negative zero point five four squared plus twenty six equals the square root of zero point two nine divided by twenty-six point two nine equals zero point one one. (thirteen point ten)

For the effect of the covariate and the difference between the thirty-minute and control groups the effects are not only statistically significant but also substantive in size. The difference between the thirty and fifteen-minute groups was a fairly small effect.


## Thirteen point eleven. Reporting results

When using covariates you can report the model in much the same way as any other. For the covariate and the experimental effect give details of the F-statistic and the degrees of freedom from which it was calculated. In both cases, the F-statistic was derived from dividing the mean squares for the effect by the mean squares for the residual. Therefore, the degrees of freedom used to assess the F-statistic are the degrees of freedom for the effect of the model (degrees of freedom sub M equals one for the covariate and two for the experimental effect) and the degrees of freedom for the residuals of the model (degrees of freedom sub R equals twenty-six for both the covariate and the experimental effect) - see Output thirteen point six. The correct way to report the main findings would be:

The covariate, love of puppies, was significantly related to the participant's happiness, F left parenthesis one, twenty-six right parenthesis equals four point nine six, P equals zero point zero three five, R equals zero point four zero. There was also a significant effect of puppy therapy on levels of happiness after controlling for the effect of love of puppies, F left parenthesis two, twenty-six right parenthesis equals four point one four, P equals zero point zero two seven, partial eta squared equals zero point two four.

We can also report some contrasts (see Output thirteen point eight):

Planned contrasts revealed that having thirty minutes of puppy therapy significantly increased happiness compared to having a control, t left parenthesis twenty-six right parenthesis equals negative two point seven seven, P equals zero point zero one, R equals zero point four eight, but not compared to having fifteen minutes, t left parenthesis twenty-six right parenthesis equals negative zero point five four,

P equals zero point five nine, R equals zero point one one. Thirteen point twelve. Brian's attempt to woo Jane

The encounter in Blow Your Speakers had been beyond weird. Jane felt terrible. This Brian guy was so nice to her, and she'd just told him where to go - again! It had been easy to dismiss Brian at first, he'd seemed like a loser, a waste of her time. But there was more to him than that: he'd been working hard to learn statistics, and he'd made impressive progress. She liked how awkward he was around her, and how he always defaulted to talking stats. It was endearing. It could derail her research, though, and he could never know about that. She was a monster, and if he found out the truth it would be another let-down. Best to keep her distance.

The phone rang. It was her brother, Jake. She loved and admired Jake like no one else. Until he left home, he'd been her sanity in the madhouse that they grew up in. Their parents, both highly successful academics, were at home only long enough to pile the pressure on them both to succeed. Jane reacted by spending her youth in books, in a futile pursuit of their attention. Every set of straight A's was met with 'these are just a step towards the exams that really matter, you'll need to up your game'. She was tired of trying to impress them. Jake was her opposite - he'd realized early on that he could never win. He let the pressure roll off him, and left home as soon as he could. But he always looked out for Jane.

'Mum is in hospital,' he said as the blood drained from Jane's legs.

'I don't care,' she replied, but she did. She also wanted to see Brian, because he was the closest thing she had to a friend in this town.


## Thirteen point thirteen. What next?

At the age of thirteen I met my heroes, Iron Maiden, and very nice they were too. I've met them a couple of times since (not because they're my best buddies or anything exciting like that, but over the years the fan club put on various events where you were allowed to stand next to them and gibber like a fool while they humoured you politely). You'll notice that the photo at the start of this chapter is signed by Dave Murray. This wasn't possible because I had my own darkroom installed backstage at the Hammersmith Odeon in which I could quickly process photographs, or because I had access to time travel (sadly), but because I took the photo with me when I met him in two thousand. I recounted the tale of how terrified I had been about meeting him in nineteen eighty-six. If he thought I was some strange stalker he certainly didn't let on. Uncharacteristic of most people who've sold millions of albums, they're lovely blokes.

Anyway, having seen Iron Maiden in their glory, I was inspired. They still inspire me: I still rate them as the best live band I've ever seen (and I've seen them over thirty-five times, so I ought to know). Although I had briefly been deflected from my destiny by the shock of grammar school, I was back on track. I had to form a band. There was just one issue: no one else played a musical instrument. The solution was easy: through several months of covert subliminal persuasion I convinced my two best friends (both called Mark, oddly enough) that they wanted nothing more than to start learning the drums and bass guitar. A power trio was in the making.


## Thirteen point fourteen. Key terms that I've discovered

Adjusted mean Analysis of covariance ANCOVA Covariate Homogeneity of regression slopes Partial eta squared partial N squared Šidák correction


## Smart Alex's tasks

· Task One: A few years back I was stalked. You'd think they could have found someone a bit more interesting to stalk, but apparently times were hard. It could have been a lot worse, but it wasn't particularly pleasant. I imagined a world in which a psychologist tried two different therapies on different groups of stalkers (twenty-five stalkers in each group - this variable is called Group). To the first group he gave cruel-to-be-kind therapy (every time the stalkers followed him around, or sent him a letter, the psychologist attacked them with a cattle prod). The second therapy was psychodynamic therapy, in which stalkers were hypnotized and regressed into their childhood to discuss their penis (or lack of penis), their father's penis, their dog's penis, the seventh penis of a seventh penis and any other penis that sprang to mind. The psychologist measured the number of hours stalking in one week both before (stalk one) and after (stalk two) treatment. Analyse the effect of therapy on stalking behaviour after therapy, covarying for the amount of stalking behaviour before therapy.

· Task Two: Compute effect sizes for Task One and report the results.

· Task Three: A marketing manager tested the benefit of soft drinks for curing hangovers. He took fifteen people and got them drunk. The next morning as they awoke, dehydrated and feeling as though they'd licked a camel's sandy feet clean with their tongue, he gave five of them water to drink, five of them Lucozade (a very nice glucose-based UK drink) and the remaining five a leading brand of cola (this variable is called drink). He measured how well they felt (on a scale from zero equals I feel like death to ten equals I feel really full of beans and healthy) two hours later (this variable is called well). He measured how drunk the person got the night before on a scale of zero equals as sober as a nun to ten equals flapping about like a haddock out of water on the floor in a puddle of their own vomit. Fit a model to see whether people felt better after different drinks when covarying for how drunk they were the night before.

· Task Four: Compute effect sizes for Task Three and report the results.

· Task Five: The highlight of the elephant calendar is the annual elephant soccer event in Nepal. A heated argument burns between the African and Asian elephants. In two thousand ten, the president of the Asian Elephant Football Association, an elephant named Boji, claimed that Asian elephants were more talented than their African counterparts. The head of the African Elephant Soccer Association, an elephant called Tunc, issued a press statement that read 'I make it a matter of personal pride never to take seriously any remark made by something that looks like an enormous scrotum'. I was called in to settle things. I collected data from the two types of elephants over a season and recorded how many goals each elephant scored and how many years of experience the elephant had. Analyse the effect of the type of elephant on goal scoring, covarying for the amount of football experience the elephant has.

· Task Six: In Chapter Four (Task Six) we looked at data from people who had been forced to marry goats and dogs and measured their life satisfaction and also how much they like animals. Fit a model predicting life satisfaction from the type of animal to which a person was married and their animal liking score.

· Task Seven: Compare your results for Task Six to those for the corresponding task in Chapter Eleven. What differences do you notice and why?

· Task Eight: In Chapter Ten we compared the number of mischievous acts (mischief two) in people who had invisibility cloaks to those without. Imagine we also had information about the baseline number of mischievous acts in these participants (mischief one). Fit a model to see whether people with invisibility cloaks get up to more mischief than those without when factoring in their baseline level of mischief.

Baseline.sav).