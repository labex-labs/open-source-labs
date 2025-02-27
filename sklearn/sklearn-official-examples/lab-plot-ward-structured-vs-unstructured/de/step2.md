# Unstrukturiertes hierarchisches Clustering

Wir führen AgglomerativeClustering durch, das unter hierarchischem Clustering ohne jegliche Verbindungsbedingungen steht.

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```
