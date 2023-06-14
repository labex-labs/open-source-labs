# Principal Component Analysis on Iris Dataset

## Introduction

In this lab, we will perform Principal Component Analysis (PCA) on the Iris dataset using Python scikit-learn. PCA is a technique used to reduce the dimensionality of a dataset while retaining as much variance as possible. In simpler terms, it helps to identify the most important features in a dataset and discard the less important ones. The Iris dataset is a famous dataset in the field of machine learning and contains information about the physical attributes of three different types of Iris flowers.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries - numpy, matplotlib.pyplot, scikit-learn's decomposition and datasets modules.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn import datasets
```

### Step 2: Load the dataset

Next, we will load the Iris dataset using scikit-learn's `load_iris()` function. We will then separate the features (X) and target (y) variables.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

### Step 3: Visualize the dataset

Before performing PCA, let's first visualize the dataset in 3D using matplotlib. This will give us an idea of how the different types of Iris flowers are distributed in the dataset.

```python
fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
ax.set_position([0, 0, 0.95, 1])
plt.cla()
for name, label in [("Setosa", 0), ("Versicolour", 1), ("Virginica", 2)]:
    ax.text3D(
        X[y == label, 0].mean(),
        X[y == label, 1].mean() + 1.5,
        X[y == label, 2].mean(),
        name,
        horizontalalignment="center",
        bbox=dict(alpha=0.5, edgecolor="w", facecolor="w"),
    )
y = np.choose(y, [1, 2, 0]).astype(float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.nipy_spectral, edgecolor="k")
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])
plt.show()
```

### Step 4: Perform PCA

Now that we have visualized the dataset, let's perform PCA on it. We will use scikit-learn's `PCA()` function for this. We will set the number of components to 3, as we want to reduce the dataset from 4 dimensions (4 features) to 3 dimensions.

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```

### Step 5: Visualize the reduced dataset

Finally, let's visualize the reduced dataset in 3D using matplotlib. We will use the same code as in Step 3, but this time we will plot the reduced dataset (X) instead of the original dataset.

```python
fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
ax.set_position([0, 0, 0.95, 1])
plt.cla()
for name, label in [("Setosa", 0), ("Versicolour", 1), ("Virginica", 2)]:
    ax.text3D(
        X[y == label, 0].mean(),
        X[y == label, 1].mean() + 1.5,
        X[y == label, 2].mean(),
        name,
        horizontalalignment="center",
        bbox=dict(alpha=0.5, edgecolor="w", facecolor="w"),
    )
y = np.choose(y, [1, 2, 0]).astype(float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.nipy_spectral, edgecolor="k")
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])
plt.show()
```

## Summary

In this lab, we learned how to perform Principal Component Analysis (PCA) on the Iris dataset using Python scikit-learn. We loaded the dataset, visualized it in 3D, performed PCA on it to reduce its dimensionality, and finally visualized the reduced dataset in 3D again. PCA is a powerful technique that can be used in many applications to reduce the dimensionality of a dataset and identify the most important features.
