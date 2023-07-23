# Run OPTICS Clustering Algorithm

We will now run OPTICS clustering algorithm on the generated data. In this example, we set `min_samples=50`, `xi=0.05`, and `min_cluster_size=0.05`.

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
