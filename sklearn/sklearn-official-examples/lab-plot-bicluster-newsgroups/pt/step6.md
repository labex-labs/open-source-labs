# Biclustering usando o Algoritmo de Co-clustering Espectral

Realizaremos o biclustering usando o algoritmo de Co-clustering Espectral definindo o `cocluster` e ajustando-o aos dados.

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```
