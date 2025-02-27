# Entrenamiento y predicción con regresores DecisionTree y AdaBoost

Ahora definimos los clasificadores y los ajustamos a los datos. Definimos el primer regresor como un `DecisionTreeRegressor` con `max_depth = 4`. Definimos el segundo regresor como un `AdaBoostRegressor` con un `DecisionTreeRegressor` de `max_depth = 4` como aprendiz base. Construimos el regresor AdaBoost con `n_estimators = 300` de esos aprendices base. Luego ajustamos ambos regresores a los datos y hacemos predicciones en los mismos datos para ver qué tan bien se ajustan a ellos.

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
