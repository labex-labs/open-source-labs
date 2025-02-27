# Ajustar el modelo de regresión

Ahora iniciaremos los regresores de Gradient Boosting y los ajustaremos con nuestros datos de entrenamiento. Echemos también un vistazo a la error cuadrático medio en los datos de prueba.

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
```
