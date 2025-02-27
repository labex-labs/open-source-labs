# Evaluar el modelo

Evaluaremos el modelo entrenado con los datos de prueba y los datos de valores atípicos. Usaremos el método `predict` para predecir las etiquetas de los datos de prueba y los datos de valores atípicos. Luego contaremos el número de errores en los datos de prueba y los datos de valores atípicos.

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
