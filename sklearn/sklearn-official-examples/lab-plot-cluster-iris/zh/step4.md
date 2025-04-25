# 应用 K 均值聚类

现在，我们将对数据应用 K 均值聚类算法。我们将用 3 个簇初始化该算法，并将其应用于我们的数据。

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
