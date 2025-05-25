# Treinamento e previsão com Regressores DecisionTree e AdaBoost

Agora definimos os classificadores e ajustamo-los aos dados. Definimos o primeiro regressor como um `DecisionTreeRegressor` com `max_depth=4`. Definimos o segundo regressor como um `AdaBoostRegressor` com um `DecisionTreeRegressor` de `max_depth=4` como aprendiz base. Construímos o Regressor AdaBoost com `n_estimators=300` desses aprendizes base. Em seguida, ajustamos ambos os regressores aos dados e fazemos previsões nos mesmos dados para ver quão bem se ajustam.

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
