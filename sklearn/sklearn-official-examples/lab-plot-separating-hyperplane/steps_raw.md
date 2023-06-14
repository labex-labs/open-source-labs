# SVM: Maximum Margin Separating Hyperplane

## Introduction

In this lab, we will use scikit-learn to create a two-class separable dataset and plot the maximum margin separating hyperplane using a Support Vector Machine (SVM) classifier with a linear kernel. SVM is a powerful classification algorithm that finds the best boundary or hyperplane that separates the data into different classes while maximizing the margin between the classes.

## Steps

### Step 1: Create a Two-Class Separable Dataset

To create a two-class separable dataset, we will use the `make_blobs()` function from scikit-learn. This function generates isotropic Gaussian blobs for clustering and classification. We will create 40 samples with two centers and a random seed of 6. We will also plot the data points using `matplotlib`.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# create a two-class separable dataset
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```

### Step 2: Fit the SVM Model

Next, we will fit the SVM model to our dataset using a linear kernel and a regularization parameter of 1000. We will use the `svm.SVC()` function from scikit-learn to create the SVM classifier.

```python
from sklearn import svm

# fit the SVM model
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```

### Step 3: Plot the Maximum Margin Separating Hyperplane

To plot the maximum margin separating hyperplane, we will use the `DecisionBoundaryDisplay.from_estimator()` function from scikit-learn. This function plots the decision function and the support vectors of the SVM classifier. We will also plot the support vectors as circles with no fill and a black edge.

```python
from sklearn.inspection import DecisionBoundaryDisplay

# plot the decision function and support vectors
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
```

## Summary

In this lab, we learned how to create a two-class separable dataset, fit an SVM model using a linear kernel, and plot the maximum margin separating hyperplane using scikit-learn. SVM is a powerful classification algorithm that can be used for a variety of applications, including image classification, text classification, and bioinformatics.
