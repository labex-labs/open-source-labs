# DBSCAN を使ってデータをクラスタリングする

異なる epsilon 値で DBSCAN を使ってデータをクラスタリングします。この例では、epsilon を 0.5 と 2 に設定します。

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
