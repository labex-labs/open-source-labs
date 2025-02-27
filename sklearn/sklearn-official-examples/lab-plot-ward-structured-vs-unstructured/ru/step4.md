# Структурная иерархическая кластеризация

Определяем k-ближайших соседей с 10 соседями с использованием функции `kneighbors_graph` из библиотеки Scikit-learn.

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

Выполняем AgglomerativeClustering снова с ограничениями связности.

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```
