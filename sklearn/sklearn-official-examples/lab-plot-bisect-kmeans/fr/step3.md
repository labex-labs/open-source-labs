# Définir le nombre de clusters et les algorithmes

Dans cette étape, nous allons définir le nombre de centres de cluster pour KMeans et BisectingKMeans. Nous allons également définir les algorithmes à comparer.

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
