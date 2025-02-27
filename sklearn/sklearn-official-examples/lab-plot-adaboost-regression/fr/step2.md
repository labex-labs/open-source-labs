# Entraînement et prédiction avec les régresseurs DecisionTree et AdaBoost

Nous définissons maintenant les classifieurs et les ajustons aux données. Nous définissons le premier régresseur comme un `DecisionTreeRegressor` avec `max_depth=4`. Nous définissons le second régresseur comme un `AdaBoostRegressor` avec un `DecisionTreeRegressor` de `max_depth=4` en tant qu'apprenant de base. Nous construisons le régresseur AdaBoost avec `n_estimators=300` de ces apprentants de base. Nous ajustons ensuite les deux régresseurs aux données et effectuons des prédictions sur les mêmes données pour voir à quel point ils s'ajustent.

```python
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

regr_1 = DecisionTreeRegressor(max_depth=4)

regr_2 = AdaBoostRegressor(
    DecisionTreeRegressor(max_depth=4), n_estimators=300, random_state=rng
)

regr_1.fit(X, y)
regr_2.fit(X, y)

y_1 = regr_1.predict(X)
y_2 = regr_2.predict(X)
```
