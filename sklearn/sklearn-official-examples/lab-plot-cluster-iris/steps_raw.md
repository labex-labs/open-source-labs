# K-Means Clustering

## Introduction

In this lab, we will explore the K-Means Clustering algorithm and its implementation in Python using the scikit-learn library. Clustering is a type of unsupervised learning that involves grouping data points into clusters based on their similarities. K-Means Clustering is a popular algorithm for clustering and is widely used in various fields such as image processing, bioinformatics, and marketing research.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries for this lab. We will be using NumPy, Matplotlib, and scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
```

### Step 2: Load Data

Next, we will load the iris dataset, which is a popular dataset in machine learning. This dataset contains information about the characteristics of different types of iris flowers. We will be using this dataset to demonstrate the K-Means Clustering algorithm.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

### Step 3: Visualize Data

Before applying the K-Means Clustering algorithm, let's first visualize the data to get a better understanding of it. We will be using a 3D scatter plot to visualize the data.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```

### Step 4: Apply K-Means Clustering

Now, we will apply the K-Means Clustering algorithm to our data. We will initialize the algorithm with 3 clusters and fit it to our data.

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```

### Step 5: Visualize Clusters

After applying the K-Means Clustering algorithm, let's visualize the clusters that were formed. We will be using a 3D scatter plot to visualize the data points and their respective clusters.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```

### Step 6: Evaluate Clustering

To evaluate the performance of the K-Means Clustering algorithm, we can calculate the inertia score. The inertia score measures the sum of distances between each data point and its assigned cluster center. A lower inertia score indicates better clustering.

```python
print("Inertia Score:", kmeans.inertia_)
```

## Summary

In this lab, we learned about the K-Means Clustering algorithm and its implementation in Python using the scikit-learn library. We loaded the iris dataset, visualized the data, applied the K-Means Clustering algorithm, and evaluated its performance. Clustering is a powerful technique for data analysis and can be used in a variety of applications.
