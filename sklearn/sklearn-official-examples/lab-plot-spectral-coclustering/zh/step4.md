# 打乱数据集

我们使用numpy中的 `permutation()` 函数来打乱数据集。

```python
rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[1])
data = data[row_idx][:, col_idx]
```
