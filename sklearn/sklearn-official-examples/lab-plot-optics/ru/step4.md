# Кластеризация данных с использованием DBSCAN

Мы будем кластеризовать данные с использованием DBSCAN при различных значениях эпсилон (epsilon). В этом примере мы устанавливаем эпсилон равным 0,5 и 2.

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
