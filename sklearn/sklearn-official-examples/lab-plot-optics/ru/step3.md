# Запуск алгоритма кластеризации OPTICS

Теперь мы запустим алгоритм кластеризации OPTICS на сгенерированных данных. В этом примере мы задаем `min_samples=50`, `xi=0.05` и `min_cluster_size=0.05`.

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
