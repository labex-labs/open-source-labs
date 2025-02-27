# Разделение набора данных на обучающую и тестовую выборки

Далее мы разделим набор данных на обучающую и тестовую выборки с использованием функции `train_test_split` из scikit-learn. Мы будем использовать 90% данных для обучения и 10% для тестирования.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```
