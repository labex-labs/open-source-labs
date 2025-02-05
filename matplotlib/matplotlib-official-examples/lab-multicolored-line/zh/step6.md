# 使用边界规范

我们将改为使用边界规范来为线段着色。我们将创建一个包含三种颜色（红色、绿色和蓝色）的 `ListedColormap`。然后，我们将创建一个边界为 -1、-0.5、0.5 和 1 的 `BoundaryNorm`，以及上述 `ListedColormap`。我们将使用 `set_array` 函数来设置用于颜色映射的值。

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
