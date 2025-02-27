# Realizar PCA

Realizaremos el PCA en el conjunto de datos Iris inicializando una instancia de la clase PCA y ajustándola a los datos.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
