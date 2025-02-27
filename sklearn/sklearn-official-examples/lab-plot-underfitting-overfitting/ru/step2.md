# Генерация данных

Мы сгенерируем 30 образцов на основе косинусной функции, добавив к образцам некоторый случайный шум.

```python
def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)

n_samples = 30

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1
```
