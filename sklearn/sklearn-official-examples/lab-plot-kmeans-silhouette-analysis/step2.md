# Generate Data

We will generate sample data using the `make_blobs` function from the `sklearn.datasets` library. This function generates isotropic Gaussian blobs for clustering.

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # For reproducibility
```
