# Entrenar un regresor utilizando SGD

A continuación, entrenaremos un regresor utilizando la clase SGDRegressor. Utilizaremos la función de pérdida squared_error y la penalización l2.

```python
# Entrenar un regresor utilizando SGD
reg = SGDRegressor(loss="squared_error", penalty="l2", max_iter=100, random_state=42)
reg.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = reg.predict(X_test)

# Medir el error cuadrático medio del regresor
mse = mean_squared_error(y_test, y_pred)

# Imprimir el error cuadrático medio
print("Error cuadrático medio del regresor:", mse)
```
