# Creating the Vertices and Codes

We will create the vertices and codes for the two polygons that we want to combine into a compound path. We will use `Path.MOVETO` to move the cursor to the starting point of the polygon, `Path.LINETO` to create a line from the starting point to the next point, and `Path.CLOSEPOLY` to close the polygon.

```python
vertices = []
codes = []

# First Polygon - Rectangle
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# Second Polygon - Triangle
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```
