# Create Data

We will create two clusters of random points using the `make_blobs` function. We will create one cluster with 1000 points and another with 100 points. The centers of the clusters will be `[0.0, 0.0]` and `[2.0, 2.0]`, respectively. The `clusters_std` parameter controls the standard deviation of the clusters.

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```
