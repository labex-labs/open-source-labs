# Agrupamento Hierárquico Estruturado

Definimos vizinhos mais próximos (k-Nearest Neighbors) com 10 vizinhos usando a função `kneighbors_graph` do Scikit-learn.

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

Realizamos novamente o `AgglomerativeClustering` com restrições de conectividade.

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```
