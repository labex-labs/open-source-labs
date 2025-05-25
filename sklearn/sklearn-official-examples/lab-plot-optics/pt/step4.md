# Agrupar Dados usando DBSCAN

Vamos agrupar os dados usando DBSCAN em diferentes valores de epsilon. Neste exemplo, definimos epsilon como 0.5 e 2.

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
