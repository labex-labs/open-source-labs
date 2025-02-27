# Agrupamiento jerárquico no estructurado

Realizamos AgglomerativeClustering, que se incluye en el agrupamiento jerárquico sin ninguna restricción de conectividad.

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```
