# Calcular el número de errores

Calcularemos el número de errores que hace el modelo en los datos de entrenamiento, las observaciones novedosas regulares y las observaciones novedosas anormales.

```python
# Contar el número de errores
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
