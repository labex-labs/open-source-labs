# Create the shaded region

Create the shaded region using a `Polygon` patch. Generate x and y values for the region using `linspace` and the function defined in step 1. Then, define the vertices of the region as a list of tuples. Finally, create the `Polygon` object and add it to the axis using `add_patch`.

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
