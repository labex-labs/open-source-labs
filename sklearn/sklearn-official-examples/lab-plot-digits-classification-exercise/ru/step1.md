# Загрузка набора данных Digits

Начнем с загрузки набора данных Digits с использованием функции `load_digits` из scikit-learn. Эта функция возвращает два массива: `X_digits`, содержащий входные данные, и `y_digits`, содержащий целевые метки.

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```
