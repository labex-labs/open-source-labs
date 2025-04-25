# 生成随机数据

我们使用 NumPy 的 `np.random.uniform` 方法生成随机数据。我们生成 `npts = 200` 个数据点，其 x 和 y 值在 -2 到 2 之间。我们还使用函数 `z = x * np.exp(-x**2 - y**2)` 计算 z 值。

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```
