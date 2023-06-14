# Biclustering using Spectral Co-clustering Algorithm

We will perform biclustering using Spectral Co-clustering algorithm by defining the cocluster and fitting it to the data.

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```


