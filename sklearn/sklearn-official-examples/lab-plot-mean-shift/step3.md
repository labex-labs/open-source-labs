# Compute Clustering with MeanShift

Now we will compute clustering using the Mean-Shift algorithm with the `MeanShift` class from the `sklearn.cluster` module. We will use the `estimate_bandwidth` function to automatically detect the bandwidth parameter, which represents the size of the region of influence for each point.

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```


