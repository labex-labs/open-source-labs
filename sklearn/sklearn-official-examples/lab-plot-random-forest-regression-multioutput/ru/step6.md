# Предсказания на новых данных

Мы будем использовать как регрессора случайного леса, так и мульти-выходной регрессор для получения предсказаний на наших тестовых данных.

```python
y_rf = regr_rf.predict(X_test)
y_multirf = regr_multirf.predict(X_test)
```
