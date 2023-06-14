# t-SNE Tutorial

## Introduction

t-SNE (t-Distributed Stochastic Neighbor Embedding) is a dimensionality reduction technique used for visualizing high-dimensional datasets. This tutorial will guide you through the process of using t-SNE to visualize datasets using Python's scikit-learn library.

## Steps

### Step 1: Import Libraries

We begin by importing the necessary libraries for this tutorial.

```python
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import NullFormatter
from sklearn import manifold, datasets
from time import time
```

### Step 2: Create Data

We will create three different datasets to illustrate the use of t-SNE. The first dataset will be two concentric circles.

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```

### Step 3: Visualize Data

We can visualize the concentric circles dataset using a scatter plot.

```python
ax = plt.subplot(1, 1, 1)
ax.scatter(X[red, 0], X[red, 1], c="r")
ax.scatter(X[green, 0], X[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```

### Step 4: Apply t-SNE to Data

Next, we will apply t-SNE to the concentric circles dataset.

```python
t0 = time()
tsne = manifold.TSNE(
    n_components=n_components,
    init="random",
    random_state=0,
    perplexity=perplexity,
    n_iter=300,
)
Y = tsne.fit_transform(X)
t1 = time()
```

### Step 5: Visualize t-SNE Results

Finally, we can visualize the t-SNE results using a scatter plot.

```python
ax = plt.subplot(1, 1, 1)
ax.scatter(Y[red, 0], Y[red, 1], c="r")
ax.scatter(Y[green, 0], Y[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```

### Step 6: Repeat for Other Datasets

We can repeat steps 2-5 for other datasets, such as an S-curve and a 2D uniform grid.

## Summary

This tutorial provided a step-by-step guide to using t-SNE for visualizing high-dimensional datasets using Python's scikit-learn library. We learned how to create data, visualize data, apply t-SNE to data, and visualize the t-SNE results.
