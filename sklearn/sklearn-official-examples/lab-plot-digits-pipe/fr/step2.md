# Définir les composants du pipeline

Nous allons définir les composants du pipeline, y compris la PCA, l'Échelleur Standard et la Régression Logistique. Nous allons définir la tolérance à une valeur élevée pour que l'exemple soit plus rapide.

```python
# Définir un pipeline pour rechercher la meilleure combinaison de la troncature de la PCA
# et de la régularisation du classifieur.
pca = PCA()
# Définir un Échelleur Standard pour normaliser les entrées
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```
