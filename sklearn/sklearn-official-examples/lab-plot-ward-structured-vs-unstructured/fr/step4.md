# Regroupement hiérarchique structuré

Nous définissons les k plus proches voisins avec 10 voisins à l'aide de la fonction `kneighbors_graph` de Scikit-learn.

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

Nous effectuons à nouveau un AgglomerativeClustering avec des contraintes de connectivité.

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```
