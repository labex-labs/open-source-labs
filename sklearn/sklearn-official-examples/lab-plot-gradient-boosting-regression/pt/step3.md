# Ajustar o Modelo de Regressão

Agora, iniciaremos os regressores de aumento de gradiente e o ajustaremos com nossos dados de treinamento. Vamos também analisar o erro quadrático médio nos dados de teste.

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("O erro quadrático médio (MSE) no conjunto de teste: {:.4f}".format(mse))
```
