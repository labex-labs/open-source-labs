# Generate Sample Data

Next, let's generate some sample data to work with. We will use the `make_blobs` function from the `sklearn.datasets` module to create a synthetic dataset with clusters.

```python
# Generate sample data
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
