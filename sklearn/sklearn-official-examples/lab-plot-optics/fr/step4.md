# Regrouper les données à l'aide de DBSCAN

Nous allons regrouper les données à l'aide de DBSCAN pour différentes valeurs d'epsilon. Dans cet exemple, nous définissons epsilon sur 0,5 et 2.

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
