# Генерация данных

Мы сгенерируем выборочные данные с использованием функции `make_blobs` из библиотеки `sklearn.datasets`. Эта функция генерирует изотропные гауссовские "куски" для кластеризации.

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # For reproducibility
```
