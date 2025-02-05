# 创建数据

```python
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

我们为绘图创建数据。我们将 `X` 和 `Y` 值创建为数组，其值从 -5 到 5 均匀分布，增量为 0.25。然后，我们使用 `np.meshgrid()` 创建 `X` 和 `Y` 值的网格。我们使用该网格来计算 `R` 值，即到原点的距离。然后，我们使用 `R` 的 `sin()` 函数计算 `Z` 值。
