# Ajustar Estimadores

O segundo passo é ajustar os estimadores de saída múltipla aos dados de treino. Usaremos quatro algoritmos diferentes: árvores aleatórias extremas, vizinhos mais próximos, regressão linear e regressão de ridge. Os estimadores preverão a metade inferior dos rostos com base na metade superior.

```python
# Ajustar estimadores
ESTIMATORS = {
    "Árvores aleatórias extremas": ExtraTreesRegressor(
        n_estimators=10, max_features=32, random_state=0
    ),
    "K-vizinhos mais próximos": KNeighborsRegressor(),
    "Regressão linear": LinearRegression(),
    "Ridge": RidgeCV(),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)
```
