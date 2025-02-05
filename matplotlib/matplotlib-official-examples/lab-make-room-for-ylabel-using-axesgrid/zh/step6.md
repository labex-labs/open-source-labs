# 创建一个具有两个可调整坐标轴的图形

在这一步中，我们创建一个具有两个可调整坐标轴的图形。我们使用 `make_axes_locatable` 方法创建一个分隔器，该分隔器允许对坐标轴进行调整。我们使用 `append_axes` 方法在第一个坐标轴的右侧添加一个新的坐标轴。

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
