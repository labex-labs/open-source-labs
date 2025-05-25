# Embaralhar o conjunto de dados

Embaralhamos o conjunto de dados usando a função `permutation()` do numpy.

```python
rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[1])
data = data[row_idx][:, col_idx]
```
