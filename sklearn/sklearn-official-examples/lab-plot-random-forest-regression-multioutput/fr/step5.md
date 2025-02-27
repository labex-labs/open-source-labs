# Création d'un MultiOutputRegressor

Nous allons créer un `MultiOutputRegressor` en utilisant un arbre de décision aléatoire pour la régression comme estimateur de base. Nous utiliserons les mêmes paramètres que dans l'Étape 4.

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
