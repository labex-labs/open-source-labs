# Unsupervised Learning: Seeking Representations of the Data

## Introduction

In this lab, we will explore the concept of unsupervised learning, specifically clustering and decomposition. Unsupervised learning is a type of machine learning where we don't have labeled data to train on. Instead, we try to find patterns or structures in the data without any prior knowledge. Clustering is a common unsupervised learning technique used to group similar observations together. Decomposition, on the other hand, is used to find a lower-dimensional representation of the data by extracting the most important features or components.

## Steps

### Step 1: Clustering using K-means

The first technique we will explore is clustering using the K-means algorithm. K-means is a popular clustering algorithm that aims to split the observations into well-separated groups called clusters. Let's use the Iris dataset as an example to demonstrate clustering with K-means.

```python
from sklearn import cluster, datasets

# Load the Iris dataset
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# Perform K-means clustering
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# Print the cluster labels
print(k_means.labels_)
```

### Step 2: Clustering Evaluation

After performing clustering, it is important to evaluate the results. However, in unsupervised learning, we don't have access to ground truth labels. Therefore, we need to be cautious when interpreting clustering results. It is common to evaluate clustering results based on metrics such as silhouette score and within-cluster sum of squares. These metrics can provide insights into the quality of the clustering.

### Step 3: Vector Quantization

One application of clustering is vector quantization, where we use clustering to choose a small number of exemplars to compress information. For example, we can use clustering to posterize an image:

```python
import scipy as sp
from sklearn import cluster, datasets

# Load a sample image
face = sp.face(gray=True)
X = face.reshape((-1, 1))

# Perform K-means clustering
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# Compress the image using cluster centers
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = face.shape
```

## Summary

In this lab, we explored the concepts of unsupervised learning, specifically clustering and decomposition. We learned about K-means clustering, hierarchical agglomerative clustering, feature agglomeration, principal component analysis (PCA), and independent component analysis (ICA). These techniques are valuable for discovering patterns and structures in unlabeled data and finding lower-dimensional representations that capture the most important information.
