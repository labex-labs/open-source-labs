# Avaliar o Modelo

Avaliaremos o modelo treinado nos dados de teste e nos dados de outliers. Usaremos o método `predict` para prever as etiquetas dos dados de teste e dos dados de outliers. Em seguida, contaremos o número de erros nos dados de teste e nos dados de outliers.

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
