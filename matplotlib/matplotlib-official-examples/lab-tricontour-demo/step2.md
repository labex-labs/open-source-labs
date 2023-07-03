# Create the Triangulation

We will create the triangulation using `matplotlib.tri.Triangulation`. We do not need to specify the triangles, so the Delaunay triangulation of the points will be created automatically.

```python
triang = tri.Triangulation(x, y)
```
