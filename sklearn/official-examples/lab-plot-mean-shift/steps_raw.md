# Mean-Shift Clustering Algorithm

## Introduction

This lab will guide you through the process of implementing the Mean-Shift Clustering Algorithm using the Scikit-learn library in Python. You will learn how to generate sample data, compute clustering with MeanShift, and plot the results.

## Steps

### Step 1: Import Required Libraries

First, we need to import the required libraries: `numpy`, `sklearn.cluster`, `sklearn.datasets`, and `matplotlib.pyplot`.

```python
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
```

### Step 2: Generate Sample Data

Next, we will generate sample data using the `make_blobs` function from the `sklearn.datasets` module. We will create a dataset with 10,000 samples and three clusters with centers at `[[1, 1], [-1, -1], [1, -1]]` and a standard deviation of 0.6.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```

### Step 3: Compute Clustering with MeanShift

Now we will compute clustering using the Mean-Shift algorithm with the `MeanShift` class from the `sklearn.cluster` module. We will use the `estimate_bandwidth` function to automatically detect the bandwidth parameter, which represents the size of the region of influence for each point.

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```

### Step 4: Plot Results

Finally, we will plot the results using the `matplotlib.pyplot` library. We will use different colors and markers for each cluster, and we will also plot the cluster centers.

```python
plt.figure(1)
plt.clf()

colors = ["#dede00", "#377eb8", "#f781bf"]
markers = ["x", "o", "^"]

for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(X[my_members, 0], X[my_members, 1], markers[k], color=col)
    plt.plot(
        cluster_center[0],
        cluster_center[1],
        markers[k],
        markerfacecolor=col,
        markeredgecolor="k",
        markersize=14,
    )
plt.title("Estimated number of clusters: %d" % n_clusters_)
plt.show()
```

## Summary

In this lab, we learned how to implement the Mean-Shift Clustering Algorithm using the Scikit-learn library in Python. We generated sample data, computed clustering with MeanShift, and plotted the results. By the end of this lab, you should have a better understanding of how to use the Mean-Shift algorithm to cluster data.
