# 创建绘图数据

在这一步中，我们将创建用于在等高线图上绘制的数据。我们使用 `np.meshgrid()` 函数创建一个点网格，然后使用正弦和余弦函数计算 `z` 值。

```python
# 要绘制的数据。
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```
