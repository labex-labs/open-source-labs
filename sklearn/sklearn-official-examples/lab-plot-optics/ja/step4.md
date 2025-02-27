# DBSCANを使ってデータをクラスタリングする

異なるepsilon値でDBSCANを使ってデータをクラスタリングします。この例では、epsilonを0.5と2に設定します。

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
