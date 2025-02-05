# 训练聚类算法

在这一步中，我们将在生成的训练数据上训练一个聚类算法，并获取聚类标签。我们将使用 scikit-learn 中的 `AgglomerativeClustering` 来训练具有 3 个聚类的算法。

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
