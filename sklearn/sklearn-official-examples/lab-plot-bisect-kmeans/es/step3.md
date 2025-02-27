# Definir el número de clusters y los algoritmos

En este paso, definiremos el número de centros de cluster para KMeans y BisectingKMeans. También definiremos los algoritmos que se van a comparar.

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
