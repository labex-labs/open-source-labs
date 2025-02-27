# Anzahl der Cluster und Algorithmen definieren

In diesem Schritt werden wir die Anzahl der Clusterzentren für KMeans und BisectingKMeans definieren. Wir werden auch die Algorithmen definieren, die verglichen werden sollen.

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
