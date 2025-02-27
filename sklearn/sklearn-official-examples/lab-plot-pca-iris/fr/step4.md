# Effectuer une PCA

Maintenant que nous avons visualisé l'ensemble de données, effectuons une PCA dessus. Nous utiliserons la fonction `PCA()` de scikit-learn à cet effet. Nous définirons le nombre de composantes sur 3, car nous souhaitons réduire l'ensemble de données de 4 dimensions (4 caractéristiques) à 3 dimensions.

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```