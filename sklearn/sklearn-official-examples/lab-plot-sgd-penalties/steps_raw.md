# SGD Penalties

## Introduction

In this lab, we will learn about the SGDClassifier and SGDRegressor in scikit-learn and how to use them to apply L1, L2, and elastic-net penalties on data.

## Steps

### Step 1: Importing Libraries

The first step is to import the necessary libraries. We will be using numpy, matplotlib, and scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier, SGDRegressor
```

### Step 2: Generating Data

We will generate some sample data to apply our penalties on. For this example, we will generate two classes of data with 100 samples each.

```python
np.random.seed(42)

# Generate two classes of data
X = np.random.randn(200, 2)
y = np.repeat([1, -1], 100)
```

### Step 3: Applying L1 Penalty

We will now apply the L1 penalty on our data using the SGDClassifier.

```python
# Create a classifier with L1 penalty
clf = SGDClassifier(loss='hinge', penalty='l1', alpha=0.05, max_iter=1000, tol=1e-3)

# Fit the model
clf.fit(X, y)

# Plot the decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 201), np.linspace(ylim[0], ylim[1], 201))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.title('L1 Penalty')
plt.show()
```

### Step 4: Applying L2 Penalty

We will now apply the L2 penalty on our data using the SGDClassifier.

```python
# Create a classifier with L2 penalty
clf = SGDClassifier(loss='hinge', penalty='l2', alpha=0.05, max_iter=1000, tol=1e-3)

# Fit the model
clf.fit(X, y)

# Plot the decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 201), np.linspace(ylim[0], ylim[1], 201))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.title('L2 Penalty')
plt.show()
```

### Step 5: Applying Elastic-Net Penalty

We will now apply the elastic-net penalty on our data using the SGDClassifier.

```python
# Create a classifier with elastic-net penalty
clf = SGDClassifier(loss='hinge', penalty='elasticnet', alpha=0.05, l1_ratio=0.15, max_iter=1000, tol=1e-3)

# Fit the model
clf.fit(X, y)

# Plot the decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 201), np.linspace(ylim[0], ylim[1], 201))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.title('Elastic-Net Penalty')
plt.show()
```

## Summary

In this lab, we learned how to apply L1, L2, and elastic-net penalties on data using the SGDClassifier in scikit-learn. We generated sample data, applied the penalties, and plotted the decision boundaries. This is a useful tool for regularization in machine learning models, especially for preventing overfitting.
