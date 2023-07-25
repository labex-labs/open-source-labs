# Prediction Intervals for Gradient Boosting Regression

## Introduction

This lab demonstrates how to use quantile regression to create prediction intervals using scikit-learn. We will generate synthetic data for a regression problem, apply the function to it, and create observations of the target using a lognormal distribution. We will then split the data into training and test datasets, fit non-linear quantile and least squares regressors, and create an evenly spaced evaluation set of input values spanning the [0, 10] range. We will compare the predicted median with the predicted mean, analyze the error metrics, and calibrate the confidence interval. Finally, we will tune the hyper-parameters of the quantile regressors.

## Steps

### Step 1: Generate Synthetic Data

We will generate synthetic data for a regression problem by applying the function to uniformly sampled random inputs. To make the problem interesting, we generate observations of the target y as the sum of a deterministic term computed by the function f and a random noise term that follows a centered log-normal distribution. The lognormal distribution is non-symmetric and long tailed: observing large outliers is likely but it is impossible to observe small outliers.

### Step 2: Split Data into Train and Test Datasets

We will split the data into train and test datasets.

### Step 3: Fit Non-Linear Quantile and Least Squares Regressors

We will fit gradient boosting models trained with the quantile loss and alpha=0.05, 0.5, 0.95. The models obtained for alpha=0.05 and alpha=0.95 produce a 90% confidence interval. The model trained with alpha=0.5 produces a regression of the median.

### Step 4: Create an Evenly Spaced Evaluation Set of Input Values

We will create an evenly spaced evaluation set of input values spanning the [0, 10] range.

### Step 5: Plot the True Conditional Mean Function f

We will plot the true conditional mean function f, the predictions of the conditional mean (loss equals squared error), the conditional median and the conditional 90% interval (from 5th to 95th conditional percentiles).

### Step 6: Analyze the Error Metrics

We will measure the models with mean_squared_error and mean_pinball_loss metrics on the training dataset. One column shows all models evaluated by the same metric.

### Step 7: Tune the Hyper-parameters of the Quantile Regressors

We will tune the hyper-parameters of a new regressor of the 5th percentile by selecting the best model parameters by cross-validation on the pinball loss with alpha=0.05. We will then tune the hyper-parameters for the 95th percentile regressor.

### Summary

This lab demonstrated how to use quantile regression to create prediction intervals using scikit-learn. We generated synthetic data for a regression problem, applied the function to it, and created observations of the target using a lognormal distribution. We split the data into training and test datasets, fit non-linear quantile and least squares regressors, and created an evenly spaced evaluation set of input values spanning the [0, 10] range. We compared the predicted median with the predicted mean, analyzed the error metrics, and calibrated the confidence interval. Finally, we tuned the hyper-parameters of the quantile regressors.
