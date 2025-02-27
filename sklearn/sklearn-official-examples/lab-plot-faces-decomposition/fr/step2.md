# Eigenfaces - PCA utilisant la SVD aléatoire

La première méthode que nous appliquons est la PCA, qui est une technique de réduction de dimension linéaire qui utilise la Décoposition en Valeurs Singulières (SVD) des données pour les projeter dans un espace de dimension plus faible. Nous utilisons la SVD aléatoire, qui est une approximation plus rapide de l'algorithme de SVD standard. Nous traçons les six premiers composants principaux, qui sont appelés eigenfaces.

```python
# Eigenfaces - PCA utilisant la SVD aléatoire
pca_estimator = decomposition.PCA(
    n_components=n_components, svd_solver="randomized", whiten=True
)
pca_estimator.fit(faces_centered)
plot_gallery(
    "Eigenfaces - PCA utilisant la SVD aléatoire", pca_estimator.components_[:n_components]
)
```
