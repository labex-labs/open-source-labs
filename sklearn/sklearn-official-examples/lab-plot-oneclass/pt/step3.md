# Calcular o número de erros

Calcularemos o número de erros cometidos pelo modelo nos dados de treino, observações regulares e novas, e observações novas anormais.

```python
# Contar o número de erros
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
