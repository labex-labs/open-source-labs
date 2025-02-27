# Загружаем датасет

Мы будем загружать датасет цифр с использованием `datasets.load_digits(return_X_y=True)`. Также мы стандартизируем данные с использованием `StandardScaler().fit_transform(X)`. Целевая переменная будет бинарной, где 0-4 будут классифицированы как 0, а 5-9 будут классифицированы как 1.

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```
