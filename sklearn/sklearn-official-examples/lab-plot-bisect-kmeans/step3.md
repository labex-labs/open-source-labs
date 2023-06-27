# Define Number of Clusters and Algorithms

In this step, we will define the number of cluster centers for KMeans and BisectingKMeans. We will also define the algorithms to be compared.

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
