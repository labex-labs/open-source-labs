# Вычисляем количество ошибок

Мы вычислим количество ошибок, которые делает модель на обучающих данных, обычных новаторских наблюдениях и аномальных новаторских наблюдениях.

```python
# Считаем количество ошибок
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
