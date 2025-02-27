# Calculez le nombre d'erreurs

Nous allons calculer le nombre d'erreurs commises par le modèle sur les données d'entraînement, les observations nouvelles régulières et les observations nouvelles anormales.

```python
# Comptez le nombre d'erreurs
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
