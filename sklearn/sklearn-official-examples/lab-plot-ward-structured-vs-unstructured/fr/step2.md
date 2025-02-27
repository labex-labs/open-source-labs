# Regroupement hiérarchique non structuré

Nous effectuons un AgglomerativeClustering qui relève du regroupement hiérarchique sans aucune contrainte de connectivité.

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```
