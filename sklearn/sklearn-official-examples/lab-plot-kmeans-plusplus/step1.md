# Generate sample data

We will use the scikit-learn library's `make_blobs` function to generate sample data. This function generates isotropic Gaussian blobs for clustering. We will generate 4000 samples with 4 centers.

```python
# Generate sample data
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```


