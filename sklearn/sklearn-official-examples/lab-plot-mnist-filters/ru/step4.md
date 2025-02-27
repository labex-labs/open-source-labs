# Разделение данных

Мы разделим набор данных на обучающую и тестовую выборки с помощью функции `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
