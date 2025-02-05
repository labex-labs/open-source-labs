# 创建宿主坐标轴

在这一步中，我们将创建宿主坐标轴并设置网格辅助器。我们将使用 `fig.add_subplot()` 来创建宿主坐标轴。

```python
# 创建宿主坐标轴
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```
