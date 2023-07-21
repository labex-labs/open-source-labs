# Mask Off Unwanted Triangles

We mask off unwanted triangles by calculating the midpoint of each triangle and checking if it falls within a given radius.

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```
