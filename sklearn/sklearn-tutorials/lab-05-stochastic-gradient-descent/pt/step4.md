# Treinar um regressor usando SGD

Em seguida, treinaremos um regressor usando a classe SGDRegressor. Usaremos a função de perda squared_error e a penalidade l2.

```python
# Treinar um regressor usando SGD
reg = SGDRegressor(loss="squared_error", penalty="l2", max_iter=100, random_state=42)
reg.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = reg.predict(X_test)

# Medir o erro quadrático médio do regressor
mse = mean_squared_error(y_test, y_pred)

# Imprimir o erro quadrático médio
print("Erro Quadrático Médio do Regressor:", mse)
```
