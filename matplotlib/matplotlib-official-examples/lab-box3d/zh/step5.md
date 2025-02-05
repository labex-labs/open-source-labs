# 绘制边缘

使用 `plot` 方法绘制边缘。我们将沿着 X 和 Y 坐标绘制三条线，以及沿着 X 和 Z 坐标绘制一条线。

```python
# 绘制边缘
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```
