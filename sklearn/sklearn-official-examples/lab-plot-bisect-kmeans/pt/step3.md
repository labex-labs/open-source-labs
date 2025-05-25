# Definir o Número de Clusters e Algoritmos

Neste passo, definiremos o número de centros de clusters para KMeans e BisectingKMeans. Também definiremos os algoritmos a serem comparados.

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
