# Generate Sample Data

Next, we will generate sample data using the `make_blobs` function from the `sklearn.datasets` module. We will create a dataset with 10,000 samples and three clusters with centers at `[[1, 1], [-1, -1], [1, -1]]` and a standard deviation of 0.6.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```


