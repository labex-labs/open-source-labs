# Bisecting K-Means and Regular K-Means Performance Comparison

## Introduction

This is a step-by-step tutorial to compare the performance of Regular K-Means algorithm and Bisecting K-Means. The tutorial will demonstrate the differences between these algorithms in terms of clustering with increasing n_clusters.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries required for this tutorial.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import BisectingKMeans, KMeans
```

### Step 2: Generate Sample Data

In this step, we will generate sample data using the `make_blobs()` function from scikit-learn. We will generate 10000 samples with 2 centers.

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```

### Step 3: Define Number of Clusters and Algorithms

In this step, we will define the number of cluster centers for KMeans and BisectingKMeans. We will also define the algorithms to be compared.

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```

### Step 4: Visualize Results

In this step, we will visualize the results of the algorithms using subplots. We will use the scatter plot to represent the data points and the cluster centroids. We will iterate through each algorithm and the number of clusters to be compared and plot the results.

```python
fig, axs = plt.subplots(len(clustering_algorithms), len(n_clusters_list), figsize=(12, 5))
axs = axs.T

for i, (algorithm_name, Algorithm) in enumerate(clustering_algorithms.items()):
    for j, n_clusters in enumerate(n_clusters_list):
        algo = Algorithm(n_clusters=n_clusters, random_state=random_state, n_init=3)
        algo.fit(X)
        centers = algo.cluster_centers_

        axs[j, i].scatter(X[:, 0], X[:, 1], s=10, c=algo.labels_)
        axs[j, i].scatter(centers[:, 0], centers[:, 1], c="r", s=20)

        axs[j, i].set_title(f"{algorithm_name} : {n_clusters} clusters")

for ax in axs.flat:
    ax.label_outer()
    ax.set_xticks([])
    ax.set_yticks([])

plt.show()
```

## Summary

This tutorial compared the performance of Regular K-Means algorithm and Bisecting K-Means using sample data generated from scikit-learn. We visualized the results using subplots with scatter plots representing the data points and the cluster centroids. We found that the Bisecting K-Means algorithm tends to create clusters that have a more regular large-scale structure, whereas the Regular K-Means algorithm creates different clusterings when increasing n_clusters.
