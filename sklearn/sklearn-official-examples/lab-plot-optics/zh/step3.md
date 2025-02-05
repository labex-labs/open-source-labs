# 运行 OPTICS 聚类算法

现在我们将对生成的数据运行 OPTICS 聚类算法。在这个例子中，我们设置 `min_samples=50`、`xi=0.05` 和 `min_cluster_size=0.05`。

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
