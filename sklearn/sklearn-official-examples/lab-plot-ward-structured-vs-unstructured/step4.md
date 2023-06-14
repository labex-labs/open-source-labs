# Structured Hierarchical Clustering

We define k-Nearest Neighbors with 10 neighbors using the `kneighbors_graph` function from Scikit-learn.

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

We perform AgglomerativeClustering again with connectivity constraints.

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```


