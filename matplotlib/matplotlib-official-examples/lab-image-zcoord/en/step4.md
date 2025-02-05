# Modify coordinate formatter

We will now modify the coordinate formatter to report the image "z" value of the nearest pixel given x and y. This can be achieved by customizing the `~.axes.Axes.format_coord` function.

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
