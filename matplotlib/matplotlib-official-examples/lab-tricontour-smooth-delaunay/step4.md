# Perform Delaunay Triangulation

We perform a Delaunay triangulation on the test data points using the `Triangulation` function from the `matplotlib.tri` module.

```python
# meshing with Delaunay triangulation
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
