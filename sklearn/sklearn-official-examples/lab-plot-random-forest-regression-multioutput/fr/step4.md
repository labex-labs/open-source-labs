# Création d'un arbre de décision aléatoire pour la régression

Nous allons créer un arbre de décision aléatoire pour la régression avec une profondeur maximale de 30 et 100 estimateurs en utilisant `RandomForestRegressor` de scikit-learn.

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
