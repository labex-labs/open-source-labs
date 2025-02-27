# Определение количества кластеров и алгоритмов

В этом шаге мы определим количество центров кластеров для KMeans и BisectingKMeans. Также мы определим алгоритмы, которые будут сравниваться.

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
