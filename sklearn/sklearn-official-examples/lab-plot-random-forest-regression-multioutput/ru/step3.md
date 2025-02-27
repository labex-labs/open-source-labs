# Разделение данных на обучающий и тестовый наборы

Мы разделим наши данные на обучающий набор из 400 элементов и тестовый набор из 200 элементов с использованием функции `train_test_split` из scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```
