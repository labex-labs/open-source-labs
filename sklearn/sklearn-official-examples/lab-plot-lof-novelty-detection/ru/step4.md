# Оценка модели

Мы оценим обученную модель на тестовых данных и данных с выбросами. Мы будем использовать метод predict для предсказания меток тестовых данных и данных с выбросами. Затем мы подсчитаем количество ошибок в тестовых данных и данных с выбросами.

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
