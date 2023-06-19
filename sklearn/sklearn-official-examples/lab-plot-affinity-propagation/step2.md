# Generate sample data

We will generate a sample dataset using the `make_blobs` function from the `sklearn.datasets` module. The `make_blobs` function generates a dataset of points in n-dimensional space, with each point belonging to one of k clusters. We will generate a dataset with 300 points in 2-dimensional space, with 3 clusters and a standard deviation of 0.5.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)
```


