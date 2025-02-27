# Effectuer la PCA

Nous allons effectuer la PCA sur l'ensemble de données Iris en initialisant une instance de la classe PCA et en l'ajustant aux données.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
