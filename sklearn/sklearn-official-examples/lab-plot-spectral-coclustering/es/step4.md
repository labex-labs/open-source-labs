# Mezclar el conjunto de datos

Mezclamos el conjunto de datos utilizando la función `permutación()` de numpy.

```python
rng = np.random.RandomState(0)
row_idx = rng.permutación(data.shape[0])
col_idx = rng.permutación(data.shape[1])
data = data[row_idx][:, col_idx]
```
