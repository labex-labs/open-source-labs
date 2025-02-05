# 将脊柱（坐标轴框架）边界限制在数据范围内进行自定义

在第三个子图中，我们将显示边界被限制在数据范围内的脊柱（坐标轴框架）。我们可以使用`set_bounds`方法将每个脊柱（坐标轴框架）的范围限制在数据范围内。

```python
ax2.plot(x, y)
ax2.set_title('Spines with Bounds Limited to Data Range')

# Only draw spines for the data range, not in the margins
ax2.spines.bottom.set_bounds(x.min(), x.max())
ax2.spines.left.set_bounds(y.min(), y.max())
# Hide the right and top spines
ax2.spines.right.set_visible(False)
ax2.spines.top.set_visible(False)
```
