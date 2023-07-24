# Failure of Machine Learning to Infer Causal Effects

## Introduction

This lab demonstrates that Machine Learning models are great for measuring statistical associations but are unable to infer causal effects without making strong assumptions about the data. We will simulate a situation in which we try to answer one of the most important questions in economics of education: what is the causal effect of earning a college degree on hourly wages? Although the answer to this question is crucial to policy makers, Omitted-Variable Biases prevent us from identifying that causal effect.

## Steps

### Step 1: Generate the dataset

We generate a simulated dataset of hourly wages, work experience, ability, parental hourly wages, and college degrees. Work experience in years and a measure of ability are drawn from Normal distributions. The hourly wage of one of the parents is drawn from Beta distribution. We create an indicator of college degree which is positively impacted by ability and parental hourly wage. Finally, we model hourly wages as a linear function of all the previous variables and a random component.

### Step 2: Train predictive models with fully observed variables

We train a predictive model, a Linear Regression model, assuming that all variables used by the true generative model are available. We predict the hourly wages using features like experience, parent hourly wage, college degree, and ability. We also plot the model coefficients to show that we exactly recover the values of the true generative model.

### Step 3: Train predictive models with partial observations

We train a predictive model again, but this time we omit the ability feature, which is not observed or is only estimated from proxies that inadvertently measure education as well (e.g. by IQ tests). We predict the hourly wages again using features like experience, parent hourly wage, and college degree. We then check if the coefficient of the model are different from the true generative model. To compensate for the omitted variable, the model inflates the coefficient of the college degree feature. Therefore, interpreting this coefficient value as a causal effect of the true generative model is incorrect.

### Step 4: Lessons learned

Machine learning models are not designed for the estimation of causal effects. While we showed this with a linear model, OVB can affect any type of model. Whenever interpreting a coefficient or a change in predictions brought about by a change in one of the features, it is important to keep in mind potentially unobserved variables that could be correlated with both the feature in question and the target variable. Such variables are called Confounding Variables. In order to still estimate causal effect in the presence of confounding, researchers usually conduct experiments in which the treatment variable (e.g. college degree) is randomized. When an experiment is prohibitively expensive or unethical, researchers can sometimes use other causal inference techniques such as Instrumental Variables (IV) estimations.

## Summary

This lab demonstrates that Machine Learning models are not designed for the estimation of causal effects. Omitted-Variable Biases prevent us from identifying the true causal effect of a feature on the target variable. Whenever interpreting a coefficient or a change in predictions, it is important to keep in mind potentially unobserved variables that could be correlated with both the feature in question and the target variable.
