# SVM Kernel Tutorial

## Introduction

This tutorial will walk through the process of using different SVM kernels for classification. We will be using the Iris dataset, which contains measurements of flowers. This dataset has three classes, but we will be using only two of them for binary classification.

## Steps

### Step 1: Load the Data

We will start by loading the Iris dataset and selecting only the first two features for visualization purposes.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 0, :2]
y = y[y != 0]
```

### Step 2: Prepare the Data

Next, we will prepare the data for training and testing. We will split the data into 90% for training and 10% for testing.

```python
n_sample = len(X)

np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(float)

X_train = X[: int(0.9 * n_sample)]
y_train = y[: int(0.9 * n_sample)]
X_test = X[int(0.9 * n_sample) :]
y_test = y[int(0.9 * n_sample) :]
```

### Step 3: Train the Model with Different Kernels

We will now train the SVM model using three different kernels: linear, rbf, and poly. For each kernel, we will fit the model to the training data, plot the decision boundary, and show the accuracy on the test data.

```python
# fit the model
for kernel in ("linear", "rbf", "poly"):
    clf = svm.SVC(kernel=kernel, gamma=10)
    clf.fit(X_train, y_train)

    plt.figure()
    plt.clf()
    plt.scatter(
        X[:, 0], X[:, 1], c=y, zorder=10, cmap=plt.cm.Paired, edgecolor="k", s=20
    )

    # Circle out the test data
    plt.scatter(
        X_test[:, 0], X_test[:, 1], s=80, facecolors="none", zorder=10, edgecolor="k"
    )

    plt.axis("tight")
    x_min = X[:, 0].min()
    x_max = X[:, 0].max()
    y_min = X[:, 1].min()
    y_max = X[:, 1].max()

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(
        XX,
        YY,
        Z,
        colors=["k", "k", "k"],
        linestyles=["--", "-", "--"],
        levels=[-0.5, 0, 0.5],
    )

    plt.title(kernel)
    plt.show()

    print(f"Accuracy with {kernel} kernel: {clf.score(X_test, y_test)}")
```

### Step 4: Interpret the Results

We can see that the linear kernel produces a linear decision boundary, while the rbf and poly kernels produce more complex boundaries. The accuracy on the test data is highest with the rbf kernel, followed by the poly kernel and then the linear kernel.

## Summary

In this tutorial, we learned how to use different SVM kernels for classification. We trained an SVM model with three different kernels and visualized the decision boundaries for each. We also calculated the accuracy on the test data for each kernel. We found that the rbf kernel produced the best results for the Iris dataset.
