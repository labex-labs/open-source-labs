# 计算均值和标准差

接下来，我们将计算这 100 个数据集中每个数据集的均值和标准差。我们将使用 numpy 的 mean 和 std 函数来计算这些值。

```python
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
