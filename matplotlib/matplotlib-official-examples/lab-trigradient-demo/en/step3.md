# Create the Triangulation

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

Explanation:

- `Triangulation` is a class that creates a Delaunay triangulation from a set of points.
- `triang` is an instance of the `Triangulation` class.
- `triang.set_mask` masks off unwanted triangles.
