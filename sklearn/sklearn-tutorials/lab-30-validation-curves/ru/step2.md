# Перемешиваем данные

Чтобы обеспечить случайность в нашем анализе, давайте перемешаем порядок образцов в наборе данных.

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
