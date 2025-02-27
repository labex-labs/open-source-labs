# Effectuer une ACP

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

Nous effectuons une Analyse en Composantes Principales (ACP) pour extraire des caractéristiques des données d'entrée. Nous fixons le nombre de composantes à 150 et ajustons le modèle ACP aux données d'entraînement. Nous obtenons ensuite les eigenfaces et transformons les données d'entrée en composantes principales.
