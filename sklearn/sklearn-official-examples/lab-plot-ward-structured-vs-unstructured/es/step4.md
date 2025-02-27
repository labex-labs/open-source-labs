# Agrupamiento jerárquico estructurado

Definimos los k-vecinos más cercanos con 10 vecinos utilizando la función `kneighbors_graph` de Scikit-learn.

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

Volvemos a realizar AgglomerativeClustering con restricciones de conectividad.

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```
