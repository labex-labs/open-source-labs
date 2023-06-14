# Ridge Regression

## Introduction

In this lab, we will learn how to use Ridge Regression for linear regression with L2 regularization to prevent overfitting. We will use scikit-learn, a popular machine learning library for Python.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries for this lab.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
```

### Step 2: Generate random data

We will generate random data with `make_regression` function from scikit-learn. We will set `n_samples` to 10, `n_features` to 10, and `random_state` to 1. This function will return our input features X, our target variable y, and the true coefficient values w.

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```

### Step 3: Initialize Ridge Regression model

We will initialize the Ridge Regression model with its default hyperparameters.

```python
clf = Ridge()
```

### Step 4: Train the model with different regularization strengths

We will train the model with different regularization strengths using a loop. We will set the regularization strength by changing the value of alpha in the `set_params` function. We will save the coefficients and errors for each value of alpha.

```python
coefs = []
errors = []

alphas = np.logspace(-6, 6, 200)

for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, w))
```

### Step 5: Plot the results

We will plot the coefficients and errors as a function of the regularization strength using Matplotlib.

```python
plt.figure(figsize=(20, 6))

plt.subplot(121)
ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale("log")
plt.xlabel("alpha")
plt.ylabel("weights")
plt.title("Ridge coefficients as a function of the regularization")
plt.axis("tight")

plt.subplot(122)
ax = plt.gca()
ax.plot(alphas, errors)
ax.set_xscale("log")
plt.xlabel("alpha")
plt.ylabel("error")
plt.title("Coefficient error as a function of the regularization")
plt.axis("tight")

plt.show()
```

## Summary

In this lab, we learned how to use Ridge Regression with L2 regularization to prevent overfitting. We generated random data, trained a Ridge Regression model with different regularization strengths, and plotted the coefficients and errors as a function of the regularization strength.
