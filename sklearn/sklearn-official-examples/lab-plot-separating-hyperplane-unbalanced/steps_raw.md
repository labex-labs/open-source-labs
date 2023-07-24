# SVM for Unbalanced Classes

## Introduction

In this lab, we will learn how to use Support Vector Machines (SVM) for classes that are unbalanced. We will first find the separating plane with a plain SVM and then plot (dashed) the separating hyperplane with automatic correction for unbalanced classes. We will use the `make_blobs` function to create two clusters of random points.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries for the lab: `matplotlib.pyplot`, `svm`, `make_blobs`, and `DecisionBoundaryDisplay`.

```python
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs
from sklearn.inspection import DecisionBoundaryDisplay
```

### Step 2: Create Data

We will create two clusters of random points using the `make_blobs` function. We will create one cluster with 1000 points and another with 100 points. The centers of the clusters will be `[0.0, 0.0]` and `[2.0, 2.0]`, respectively. The `clusters_std` parameter controls the standard deviation of the clusters.

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```

### Step 3: Fit the Model

We will fit the model and get the separating hyperplane using the `SVC` function from the `svm` library. We will use a linear kernel and set `C` to 1.0.

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```

### Step 4: Fit the Model with Weighted Classes

We will fit the model and get the separating hyperplane using the `SVC` function from the `svm` library. We will use a linear kernel and set `class_weight` to `{1: 10}`. This will give more weight to the smaller class.

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```

### Step 5: Plot the Samples

We will plot the samples using the `scatter` function from `matplotlib.pyplot`.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
```

### Step 6: Plot the Decision Functions for Both Classifiers

We will plot the decision functions for both classifiers using the `DecisionBoundaryDisplay` function from the `sklearn.inspection` library. We will set `plot_method` to `"contour"`, `colors` to `"k"` for the plain SVM and `"r"` for the weighted SVM, `levels` to `[0]`, `alpha` to `0.5`, and `linestyles` to `["-"]`. We will also set `ax` to `plt.gca()`.

```python
ax = plt.gca()
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)

wdisp = DecisionBoundaryDisplay.from_estimator(
    wclf,
    X,
    plot_method="contour",
    colors="r",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)
```

### Step 7: Add Legend

We will add a legend to the plot using the `legend` function from `matplotlib.pyplot`. We will set the labels to `"non weighted"` and `"weighted"`, respectively.

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```

### Step 8: Show the Plot

Finally, we will show the plot using the `show` function from `matplotlib.pyplot`.

```python
plt.show()
```

## Summary

In this lab, we learned how to use Support Vector Machines (SVM) for classes that are unbalanced. We used the `make_blobs` function to create two clusters of random points and created two SVM models, one with plain SVM and another with automatic correction for unbalanced classes. We plotted the samples and the decision functions for both classifiers and added a legend to the plot.
