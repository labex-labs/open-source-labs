# Ajuster le modèle de régression

Dans cette étape, nous allons ajuster des modèles de régression. Nous utiliserons `DecisionTreeRegressor` de sklearn.tree pour ajuster trois modèles différents avec des profondeurs maximales différentes.

```python
# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=8)
regr_1.fit(X, y)
regr_2.fit(X, y)
regr_3.fit(X, y)
```
