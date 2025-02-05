# 应用K均值聚类

现在，我们将对数据应用K均值聚类算法。我们将用3个簇初始化该算法，并将其应用于我们的数据。

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
