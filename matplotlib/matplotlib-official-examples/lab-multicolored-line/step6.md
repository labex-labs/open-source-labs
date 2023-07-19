# Use a Boundary Norm

We will use a boundary norm instead to color the line segments. We will create a `ListedColormap` containing three colors - red, green, and blue. We will then create a `BoundaryNorm` with boundaries -1, -0.5, 0.5, and 1, and the `ListedColormap`. We will use the `set_array` function to set the values used for colormapping.

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
