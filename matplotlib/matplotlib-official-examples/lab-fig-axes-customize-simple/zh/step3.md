# 向图形中添加坐标轴

我们将使用 `fig.add_axes()` 方法向图形中添加坐标轴。我们还将使用 `rect.set_facecolor()` 方法设置坐标轴的背景颜色。

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
