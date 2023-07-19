# Clustering

## Introduction

In this lab, we will explore clustering, a popular unsupervised machine learning technique. Clustering is used to group similar data points together based on their features or attributes, without the need for labeled training data. There are various clustering algorithms available, each with its own strengths and weaknesses. In this lab, we will focus on the k-means clustering algorithm.

## Steps

### Step 1: Import the Required Libraries

Before we begin, let's import the libraries we will need for this lab.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
```

### Step 2: Generate Sample Data

Next, let's generate some sample data to work with. We will use the `make_blobs` function from the `sklearn.datasets` module to create a synthetic dataset with clusters.

```python
# Generate sample data
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```

### Step 3: Visualize the Data

Let's visualize the generated data using a scatter plot.

```python
# Plot the data points
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

### Step 4: Perform K-Means Clustering

Now, let's apply the k-means clustering algorithm to the data.

```python
# Perform K-Means clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
```

### Step 5: Visualize the Clusters

Let's visualize the clusters that were formed by the k-means algorithm.

```python
# Get the cluster labels for each data point
labels = kmeans.labels_

# Plot the data points with color-coded clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

### Step 6: Evaluate the Clustering

To evaluate the clustering results, we can calculate the inertia of the clusters, which represents the sum of squared distances of samples to their closest cluster center.

```python
# Calculate the inertia of the clusters
inertia = kmeans.inertia_
print("Inertia:", inertia)
```

## Summary

In this lab, we explored the k-means clustering algorithm. We generated a synthetic dataset, performed k-means clustering on the data, and visualized the resulting clusters. We also calculated the inertia of the clusters as a measure of clustering performance. Clustering is a powerful technique for finding structure in unlabeled data and can be applied to various domains and types of data.
