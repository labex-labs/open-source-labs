# Unstructured Hierarchical Clustering

We perform AgglomerativeClustering which comes under Hierarchical Clustering without any connectivity constraints.

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```


