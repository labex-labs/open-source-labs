# Validation Curves: Plotting Scores to Evaluate Models

## Introduction

In machine learning, every estimator has its advantages and drawbacks. The generalization error of an estimator can be decomposed into bias, variance, and noise. The bias of an estimator is the average error for different training sets, while the variance indicates its sensitivity to varying training sets. Noise is a property of the data.

In this lab, we will explore how to use validation curves to evaluate the performance of machine learning models. Validation curves allow us to plot the influence of a single hyperparameter on the training score and the validation score, helping us determine if the model is overfitting or underfitting for different hyperparameter values.

## Steps

### Step 1: Import the Required Libraries and Load the Data

Let's start by importing the necessary libraries and loading a dataset. In this example, we will use the Iris dataset.

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```

### Step 2: Shuffle the Data

To ensure randomness in our analysis, let's shuffle the order of the samples in our dataset.

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```

### Step 3: Plot the Validation Curve

Now, let's plot the validation curve using the `validation_curve` function. We will use the `Ridge` estimator and vary the `alpha` hyperparameter over a range of values.

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```

## Summary

In this lab, we explored the concept of validation curves and how they can be used to evaluate machine learning models. By plotting the training score and the validation score for different hyperparameter values, we can determine if a model is overfitting or underfitting. This information helps us select the best hyperparameters for our models and improve their performance.
