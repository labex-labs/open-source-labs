# SVM Tie Breaking

## Introduction

This lab introduces SVM tie-breaking and its effect on decision boundary. In SVM, tie-breaking is the mechanism used to resolve the conflicts between the two or more classes when their distances are equal. It is not enabled by default when `decision_function_shape='ovr'` because it is costly. Therefore, this lab illustrates the effect of the `break_ties` parameter for a multiclass classification problem and `decision_function_shape='ovr'`.

## Steps

### Step 1: Import Required Libraries

In this step, we will import the required libraries for SVM and visualization.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_blobs
```

### Step 2: Create Sample Data

In this step, we will create a sample dataset using the `make_blobs` function from scikit-learn. This dataset contains 3 classes and 2 features.

```python
X, y = make_blobs(random_state=27)
```

### Step 3: Create SVM Model with and without Tie-Breaking

In this step, we will create two SVM models - one with tie-breaking disabled and another with tie-breaking enabled. We will use the `SVC` class from scikit-learn to create these models. The `break_ties` parameter is set to `False` and `True` for the two models, respectively.

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```

### Step 4: Create Decision Boundary

In this step, we will create the decision boundary for the two models. We will use the `predict` function to predict the classes for the sample data points and plot the decision boundary.

```python
    xs = np.linspace(xlim[0], xlim[1], 1000)
    ys = np.linspace(ylim[0], ylim[1], 1000)
    xx, yy = np.meshgrid(xs, ys)

    pred = svm.predict(np.c_[xx.ravel(), yy.ravel()])

    colors = [plt.cm.Accent(i) for i in [0, 4, 7]]

    points = ax.scatter(X[:, 0], X[:, 1], c=y, cmap="Accent")
    classes = [(0, 1), (0, 2), (1, 2)]
    line = np.linspace(X[:, 1].min() - 5, X[:, 1].max() + 5)
    ax.imshow(
        -pred.reshape(xx.shape),
        cmap="Accent",
        alpha=0.2,
        extent=(xlim[0], xlim[1], ylim[1], ylim[0]),
    )
```

### Step 5: Plot Decision Boundary

In this step, we will plot the decision boundary created in the previous step. We will use the `coef_` and `intercept_` attributes of the SVM model to plot the decision boundary.

```python
    for coef, intercept, col in zip(svm.coef_, svm.intercept_, classes):
        line2 = -(line * coef[1] + intercept) / coef[0]
        ax.plot(line2, line, "-", c=colors[col[0]])
        ax.plot(line2, line, "--", c=colors[col[1]])
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title)
    ax.set_aspect("equal")
```

### Step 6: Show the Plot

In this step, we will show the plot containing the decision boundary for both models.

```python
plt.show()
```

## Summary

This lab illustrated the effect of SVM tie-breaking on decision boundary. We created two SVM models - one with tie-breaking disabled and another with tie-breaking enabled. We then plotted the decision boundary for both models. The decision boundary for the model with tie-breaking enabled was non-convex in the area where the classes were tied.
