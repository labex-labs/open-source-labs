# Перемешиваем набор данных

Мы перемешиваем набор данных с использованием функции `permutation()` из библиотеки numpy.

```python
rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[1])
data = data[row_idx][:, col_idx]
```
