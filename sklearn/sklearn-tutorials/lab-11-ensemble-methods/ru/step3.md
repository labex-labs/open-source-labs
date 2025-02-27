# Разделение данных

Мы разделим данные на обучающую и тестовую выборки с использованием функции `train_test_split` из библиотеки scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
