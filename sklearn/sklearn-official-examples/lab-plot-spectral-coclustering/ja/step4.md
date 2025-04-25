# データセットをシャッフルする

numpy の `permutation()` 関数を使用して、データセットをシャッフルします。

```python
rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[1])
data = data[row_idx][:, col_idx]
```
