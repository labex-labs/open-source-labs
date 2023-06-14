# Logistic Regression Model

## Introduction

This lab will provide a step-by-step guide on how to create a Logistic Regression Model using Python's scikit-learn library.

## Steps

### Step 1: Import necessary libraries

The first step is to import the necessary libraries that will be used in this lab. We will be using `numpy`, `matplotlib`, `scipy`, and `sklearn`.

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import expit
from sklearn.linear_model import LinearRegression, LogisticRegression
```

### Step 2: Generate a toy dataset

The next step is to generate a toy dataset, which is a straight line with some Gaussian noise. We will be using `numpy` to generate this dataset.

```python
# Generate a toy dataset, it's just a straight line with some Gaussian noise:
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(float)
X[X > 0] *= 4
X += 0.3 * np.random.normal(size=n_samples)

X = X[:, np.newaxis]
```

### Step 3: Fit the classifier

After generating the dataset, we will fit the classifier using `LogisticRegression` from scikit-learn.

```python
# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```

### Step 4: Plot the result

The final step is to plot the result. We will use `matplotlib` to create a scatter plot of the example data, and plot the logistic regression model and linear regression model.

```python
# and plot the result
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.scatter(X.ravel(), y, label="example data", color="black", zorder=20)
X_test = np.linspace(-5, 10, 300)

loss = expit(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, loss, label="Logistic Regression Model", color="red", linewidth=3)

ols = LinearRegression()
ols.fit(X, y)
plt.plot(
    X_test,
    ols.coef_ * X_test + ols.intercept_,
    label="Linear Regression Model",
    linewidth=1,
)
plt.axhline(0.5, color=".5")

plt.ylabel("y")
plt.xlabel("X")
plt.xticks(range(-5, 10))
plt.yticks([0, 0.5, 1])
plt.ylim(-0.25, 1.25)
plt.xlim(-4, 10)
plt.legend(
    loc="lower right",
    fontsize="small",
)
plt.tight_layout()
plt.show()
```

## Summary

This lab provided a step-by-step guide on how to create a Logistic Regression Model using Python's scikit-learn library. We began by importing necessary libraries, generating a toy dataset, fitting the classifier, and finally plotting the result.
