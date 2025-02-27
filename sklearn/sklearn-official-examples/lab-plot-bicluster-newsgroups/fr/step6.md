# Biclustering à l'aide de l'algorithme de co-clustering spectral

Nous allons effectuer un biclustering à l'aide de l'algorithme de co-clustering spectral en définissant le co-cluster et en l'ajustant aux données.

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```
