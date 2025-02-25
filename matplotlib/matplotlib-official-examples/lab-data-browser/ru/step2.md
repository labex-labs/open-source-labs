# Генерация данных

Мы сгенерируем случайные данные с использованием NumPy.

```python
np.random.seed(19680801)
X = np.random.rand(100, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
