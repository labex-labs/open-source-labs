# Scikit-Learn Tutorial: Understanding Model Complexity

## Introduction

In this lab, we will explore how model complexity influences both prediction accuracy and computational performance. We will be using two datasets - Diabetes Dataset for regression and 20newsgroups Dataset for classification. We will model the complexity influence on three different estimators:

- SGDClassifier (for classification data) which implements stochastic gradient descent learning
- NuSVR (for regression data) which implements Nu support vector regression
- GradientBoostingRegressor builds an additive model in a forward stage-wise fashion

We will vary the model complexity through the choice of relevant model parameters in each of our selected models. Next, we will measure the influence on both computational performance (latency) and predictive power (MSE or Hamming Loss).

## Steps

### Step 1: Load the data

We load both datasets - diabetes dataset for regression and 20newsgroups dataset for classification.

### Step 2: Choose parameters

We choose the parameters for each of our estimators by making a dictionary with all the necessary values. We define the varying parameter, complexity label, complexity computer, data and other configuration values for each estimator.

### Step 3: Benchmark influence

We calculate the influence of the parameters on the given estimator. In each round, we set the estimator with the new value of the varying parameter and collect the prediction times, prediction performance, and complexities to see how those changes affect the estimator. We calculate the complexity using the complexity computer passed as a parameter.

### Step 4: Plot the results

We plot the influence of model complexity on both accuracy and latency. We use the prediction error on the y-axis and the model complexity on the x-axis. We plot both prediction error and prediction latency on the same graph.

## Summary

In this lab, we explored how model complexity influences both prediction accuracy and computational performance. We varied the model complexity through the choice of relevant model parameters in each of our selected models. We then measured the influence on both computational performance (latency) and predictive power (MSE or Hamming Loss). We concluded that a more complex model requires larger training time and does not guarantee to reduce the prediction error.
