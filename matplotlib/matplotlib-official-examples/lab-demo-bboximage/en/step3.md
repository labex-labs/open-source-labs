# Create a BboxImage for each colormap

Next, we create a BboxImage for each colormap. We start by creating a list of all colormaps using the `plt.colormaps` method. We then create a `for` loop that iterates through the list of colormaps. For each colormap, we calculate the `ix` and `iy` position using the `divmod()` method. We then create a `Bbox` object using the `Bbox.from_bounds()` method. We pass the `ix`, `iy`, `dx`, and `dy` values to the `Bbox.from_bounds()` method to create the bounding box. We then create a `TransformedBbox` object using the `Bbox` object and the `ax2.transAxes` object. Finally, we create a `BboxImage` object using the `add_artist()` method. We pass the `TransformedBbox` object to the `BboxImage` constructor to create an image with the colormap.

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
