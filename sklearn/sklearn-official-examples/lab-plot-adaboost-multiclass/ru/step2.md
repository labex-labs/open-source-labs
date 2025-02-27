# Загружаем датасет

Мы будем использовать функцию `make_gaussian_quantiles` из `sklearn.datasets` для генерации датасета. Эта функция генерирует изотропные Гауссовы распределения и добавляет разделение между классами, чтобы сделать задачу более сложной.

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```
