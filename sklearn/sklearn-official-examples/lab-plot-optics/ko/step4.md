# DBSCAN 을 이용한 데이터 군집화

다양한 epsilon 값으로 DBSCAN 을 사용하여 데이터를 군집화합니다. 이 예제에서는 epsilon 을 0.5 와 2 로 설정합니다.

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
