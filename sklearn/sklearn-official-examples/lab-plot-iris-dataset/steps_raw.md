# Scikit-learn Tutorial: Iris Dataset

## Introduction

This is a step-by-step lab to demonstrate the usage of Scikit-learn, a popular machine learning library in Python. We will be using the Iris Dataset, which contains information about the physical attributes of different types of iris flowers. The goal of this lab is to show how to use Scikit-learn to perform basic machine learning tasks such as data loading, data preprocessing, feature selection, and visualization.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries. In this lab, we will be using Scikit-learn, NumPy, and Matplotlib.

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
```

### Step 2: Load the Iris Dataset

We will load the Iris Dataset using the Scikit-learn built-in `load_iris` function.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
```

### Step 3: Visualize the Data

We will visualize the Iris Dataset using a scatter plot. We will plot the Sepal Length against the Sepal Width, and color the points based on their class.

```python
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
```

### Step 4: Perform PCA

We will perform Principal Component Analysis (PCA) to reduce the dimensionality of the dataset. We will project the data onto the first three principal components and plot the results in 3D.

```python
fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=y,
    cmap=plt.cm.Set1,
    edgecolor="k",
    s=40,
)

ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.zaxis.set_ticklabels([])
```

## Summary

In this lab, we learned how to load the Iris Dataset using Scikit-learn, visualize the data using Matplotlib, and perform PCA using Scikit-learn. We also learned how to project the data onto the first three principal components and visualize the results in 3D.
