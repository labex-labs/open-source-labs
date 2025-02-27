# Biclustering utilizando el algoritmo de co-agrupamiento espectral

Realizaremos el biclustering utilizando el algoritmo de co-agrupamiento espectral definiendo el co-agrupamiento y ajustándolo a los datos.

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```
