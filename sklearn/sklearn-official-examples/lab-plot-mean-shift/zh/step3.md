# 使用均值漂移算法进行聚类计算

现在我们将使用 `sklearn.cluster` 模块中的 `MeanShift` 类，通过均值漂移算法进行聚类计算。我们将使用 `estimate_bandwidth` 函数自动检测带宽参数，该参数表示每个点的影响区域大小。

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```
