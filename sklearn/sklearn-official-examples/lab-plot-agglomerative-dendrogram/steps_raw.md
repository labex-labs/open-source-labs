# Hierarchical Clustering Dendrogram

## Introduction

In this lab, we will learn how to plot the corresponding dendrogram of a hierarchical clustering using AgglomerativeClustering and the dendrogram method available in scipy.

## Steps

### Step 1: Import the necessary libraries

We will start by importing the necessary libraries for this lab.

```python
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
```

### Step 2: Load the dataset

We will use the `load_iris()` function from the `sklearn.datasets` module to load the iris dataset.

```python
iris = load_iris()
X = iris.data
```

### Step 3: Create the model

Next, we will create the agglomerative clustering model using the `AgglomerativeClustering()` function from the `sklearn.cluster` module.

```python
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
```

### Step 4: Fit the model

We will fit the agglomerative clustering model using the `fit()` method of the model object.

```python
model = model.fit(X)
```

### Step 5: Plot the dendrogram

We will plot the dendrogram using the `dendrogram()` function from the `scipy.cluster.hierarchy` module and the `plot_dendrogram()` function defined in the original code.

```python
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
```

## Summary

In this lab, we learned how to plot the corresponding dendrogram of a hierarchical clustering using AgglomerativeClustering and the dendrogram method available in scipy. We loaded the iris dataset, created an agglomerative clustering model, and fit the model. Finally, we plotted the dendrogram using the `dendrogram()` function from the `scipy.cluster.hierarchy` module and the `plot_dendrogram()` function defined in the original code.
