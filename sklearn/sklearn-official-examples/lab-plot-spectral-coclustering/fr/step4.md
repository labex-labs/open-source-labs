# Mélanger l'ensemble de données

Nous mélangeons l'ensemble de données à l'aide de la fonction `permutation()` de numpy.

```python
rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[1])
data = data[row_idx][:, col_idx]
```
