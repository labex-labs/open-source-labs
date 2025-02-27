# Entraîner un régresseur Ridge sur les données brutes

Dans cette section, nous allons entraîner un régresseur Ridge sur l'ensemble de données avec et sans codage et explorer l'influence du codage cible avec et sans validation croisée par intervalle. Tout d'abord, nous allons entraîner un modèle Ridge sur les caractéristiques brutes. Exécutez le code suivant pour entraîner le modèle Ridge :

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```
