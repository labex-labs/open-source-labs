# Получение предсказаний

Теперь мы можем использовать обученную модель для получения предсказаний на тестовой выборке.

```python
# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)
```
