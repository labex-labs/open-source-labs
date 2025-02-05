# 使用 DBSCAN 对数据进行聚类

我们将使用不同的 epsilon 值，通过 DBSCAN 对数据进行聚类。在这个例子中，我们将 epsilon 设置为 0.5 和 2。

```python
labels_050 = cluster_optics_dbscan(
    reachability=clust.reachability_,
    core_distances=clust.core_distances_,
    ordering=clust.ordering_,
    eps=0.5,
)
labels_200 = cluster_optics_dbscan(
    reachability=clust.reachability_,
    core_distances=clust.core_distances_,
    ordering=clust.ordering_,
    eps=2,
)
```
