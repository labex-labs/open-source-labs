# Strukturiertes hierarchisches Clustering

Wir definieren die k-Nearest Neighbors mit 10 Nachbarn mit der Funktion `kneighbors_graph` aus Scikit-learn.

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

Wir führen erneut AgglomerativeClustering mit Verbindungsbedingungen durch.

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```
