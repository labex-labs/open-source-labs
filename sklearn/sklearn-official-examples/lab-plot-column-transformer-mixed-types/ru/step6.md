# Разделение данных

В этом шаге мы разделим наши данные на обучающий и тестовый наборы с использованием `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```
