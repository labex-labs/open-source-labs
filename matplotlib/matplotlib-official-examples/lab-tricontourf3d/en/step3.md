# Create a Custom Triangulation

In this step, we will create a custom triangulation and mask off unwanted triangles.

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
