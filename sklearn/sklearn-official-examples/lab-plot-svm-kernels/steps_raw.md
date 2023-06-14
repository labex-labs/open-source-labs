# SVM-Kernels

## Introduction

This lab provides a step-by-step guide on how to use SVM-Kernels to classify data-points. SVM-Kernels are especially useful when the data-points are not linearly separable. We will use Python scikit-learn to carry out this task.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries to carry out the classification task.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
```

### Step 2: Create Dataset and Targets

In this step, we will create a dataset and targets for our classification task. We will use the `numpy` library to create the dataset and targets.

```python
X = np.c_[
    (0.4, -0.7),
    (-1.5, -1),
    (-1.4, -0.9),
    (-1.3, -1.2),
    (-1.1, -0.2),
    (-1.2, -0.4),
    (-0.5, 1.2),
    (-1.5, 2.1),
    (1, 1),
    # --
    (1.3, 0.8),
    (1.2, 0.5),
    (0.2, -2),
    (0.5, -2.4),
    (0.2, -2.3),
    (0, -2.7),
    (1.3, 2.1),
].T
Y = [0] * 8 + [1] * 8
```

### Step 3: Create the Model

In this step, we will create the SVM-Kernel model with three different kernels: linear, polynomial, and radial basis function (RBF). The linear kernel is used for linearly separable data-points, while the polynomial and RBF kernels are useful for nonlinearly separable data-points.

```python
# fit the model
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```

### Step 4: Visualize the Model

In this step, we will visualize the SVM-Kernel model by plotting the line, the points, and the nearest vectors to the plane.

```python
    # plot the line, the points, and the nearest vectors to the plane
    plt.figure(fignum, figsize=(4, 3))
    plt.clf()

    plt.scatter(
        clf.support_vectors_[:, 0],
        clf.support_vectors_[:, 1],
        s=80,
        facecolors="none",
        zorder=10,
        edgecolors="k",
    )
    plt.scatter(X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.cm.Paired, edgecolors="k")

    plt.axis("tight")
    x_min = -3
    x_max = 3
    y_min = -3
    y_max = 3

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(XX.shape)
    plt.figure(fignum, figsize=(4, 3))
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(
        XX,
        YY,
        Z,
        colors=["k", "k", "k"],
        linestyles=["--", "-", "--"],
        levels=[-0.5, 0, 0.5],
    )

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.xticks(())
    plt.yticks(())
    fignum = fignum + 1
plt.show()
```

## Summary

In this lab, we learned how to use SVM-Kernels to classify data-points. We created a dataset and targets, created the SVM-Kernel model with three different kernels, and visualized the model. SVM-Kernels are especially useful when the data-points are not linearly separable.
