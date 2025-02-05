# 为每个颜色映射创建一个BboxImage

接下来，我们为每个颜色映射创建一个BboxImage。我们首先使用`plt.colormaps`方法创建一个所有颜色映射的列表。然后，我们创建一个`for`循环，遍历颜色映射列表。对于每个颜色映射，我们使用`divmod()`方法计算`ix`和`iy`位置。然后，我们使用`Bbox.from_bounds()`方法创建一个`Bbox`对象。我们将`ix`、`iy`、`dx`和`dy`值传递给`Bbox.from_bounds()`方法以创建边界框。然后，我们使用`Bbox`对象和`ax2.transAxes`对象创建一个`TransformedBbox`对象。最后，我们使用`add_artist()`方法创建一个`BboxImage`对象。我们将`TransformedBbox`对象传递给`BboxImage`构造函数，以创建一个带有颜色映射的图像。

```python
cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

ncol = 2
nrow = len(cmap_names) // ncol + 1

xpad_fraction = 0.3
dx = 1 / (ncol + xpad_fraction * (ncol - 1))

ypad_fraction = 0.3
dy = 1 / (nrow + ypad_fraction * (nrow - 1))

for i, cmap_name in enumerate(cmap_names):
    ix, iy = divmod(i, nrow)
    bbox0 = Bbox.from_bounds(ix*dx*(1+xpad_fraction),
                             1 - iy*dy*(1+ypad_fraction) - dy,
                             dx, dy)
    bbox = TransformedBbox(bbox0, ax2.transAxes)
    ax2.add_artist(
        BboxImage(bbox, cmap=cmap_name, data=np.arange(256).reshape((1, -1))))
```
