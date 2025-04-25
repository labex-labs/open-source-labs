# 创建图形并设置坐标轴

接下来，我们将创建一个图形并设置坐标轴。我们将使用`add_axes()`方法在图形中创建一组新的坐标轴。我们还将设置 x 轴和 y 轴的范围，并添加网格线。

```python
# 创建图形和坐标轴
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# 设置范围和网格线
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```
