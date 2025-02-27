# Ajustar los estimadores

El segundo paso es ajustar los estimadores con múltiples salidas a los datos de entrenamiento. Utilizaremos cuatro algoritmos diferentes: árboles aleatorizados extremos, k-vecinos más cercanos, regresión lineal y regresión con cresta. Los estimadores predecirán la mitad inferior de los rostros a partir de la mitad superior.

```python
# Ajustar los estimadores
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(
        n_estimators=10, max_features=32, random_state=0
    ),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)
```
