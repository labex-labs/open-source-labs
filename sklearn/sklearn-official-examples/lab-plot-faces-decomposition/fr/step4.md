# Composantes indépendantes - FastICA

L'Analyse en Composantes Indépendantes (ICA) est une méthode pour séparer des signaux multivariés en sous-composantes additives qui sont maximale ment indépendantes. Nous appliquons FastICA, qui est un algorithme rapide et robuste pour l'ICA.

```python
# Composantes indépendantes - FastICA
ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
plot_gallery(
    "Composantes indépendantes - FastICA", ica_estimator.components_[:n_components]
)
```
