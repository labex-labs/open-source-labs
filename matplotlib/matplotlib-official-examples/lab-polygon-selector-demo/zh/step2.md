# 创建数据

在这一步中，我们将创建一些数据用于可视化。我们将在网格上创建一个点的散点图。

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```
