# Разделяем набор данных на обучающий и тестовый наборы

Для оценки производительности нашей модели нам нужно разделить набор данных на обучающий и тестовый наборы. Мы будем использовать функцию `train_test_split` из библиотеки scikit-learn для этого.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
