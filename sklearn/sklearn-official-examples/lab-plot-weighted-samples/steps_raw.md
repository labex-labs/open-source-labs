# Support Vector Machine (SVM) Weighted Samples

## Introduction

In this lab, we will learn how to plot a decision function of a weighted dataset in SVM. We will create a model that takes into account sample weights and another model that does not take into account sample weights. We will then compare the two models by plotting their decision functions.

## Steps

### Step 1: Import Libraries

We will start by importing the required libraries.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
```

### Step 2: Create Data

We will create a dataset of 20 points, where the first 10 points belong to class 1 and the last 10 points belong to class -1.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
```

### Step 3: Create Sample Weights

We will create two sets of sample weights. The first set of sample weights will be constant for all points, and the second set of sample weights will be greater for some outliers.

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```

### Step 4: Train Models

We will create two SVM models. The first model will not take into account sample weights, and the second model will take into account the sample weights we just created.

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```

### Step 5: Plot Decision Functions

We will plot the decision functions of the two models we just created. We will plot the decision function of the first model on the left, and the decision function of the second model on the right. The size of the points will be proportional to their weight.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
Z = clf_no_weights.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[0].contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
axes[0].scatter(X[:, 0], X[:, 1], c=y, s=100 * sample_weight_constant, alpha=0.9, cmap=plt.cm.bone, edgecolors="black")
axes[0].axis("off")
axes[0].set_title("Constant Weights")

Z = clf_weights.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[1].contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
axes[1].scatter(X[:, 0], X[:, 1], c=y, s=100 * sample_weight_last_ten, alpha=0.9, cmap=plt.cm.bone, edgecolors="black")
axes[1].axis("off")
axes[1].set_title("Modified Weights")

plt.show()
```

## Summary

In this lab, we learned how to plot a decision function of a weighted dataset in SVM. We created two models, one that takes into account sample weights and another that does not take into account sample weights. We then compared the two models by plotting their decision functions.
