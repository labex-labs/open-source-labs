# 修改坐标格式化器

现在我们将修改坐标格式化器，以便根据给定的 x 和 y 报告最近像素的图像 “z” 值。这可以通过自定义 `~.axes.Axes.format_coord` 函数来实现。

```python
def format_coord(x, y):
    col = round(x)
    row = round(y)
    nrows, ncols = X.shape
    if 0 <= col < ncols and 0 <= row < nrows:
        z = X[row, col]
        return f'x={x:1.4f}, y={y:1.4f}, z={z:1.4f}'
    else:
        return f'x={x:1.4f}, y={y:1.4f}'

ax.format_coord = format_coord
```
