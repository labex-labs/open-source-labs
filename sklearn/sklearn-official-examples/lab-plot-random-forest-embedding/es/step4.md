# Visualizar el resultado después de la reducción de dimensionalidad con Truncated SVD

En este paso, visualizaremos el resultado después de la reducción de dimensionalidad con Truncated SVD.

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```
