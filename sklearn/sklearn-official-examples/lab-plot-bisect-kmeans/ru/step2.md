# Генерация выборочных данных

В этом шаге мы сгенерируем выборочные данные с использованием функции `make_blobs()` из scikit - learn. Мы сгенерируем 10000 выборок с 2 центрами.

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
