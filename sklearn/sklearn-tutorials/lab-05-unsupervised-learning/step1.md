# Clustering using K-means

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
