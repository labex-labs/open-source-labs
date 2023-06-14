# Mask Unwanted Triangles

We will mask off unwanted triangles by computing the mean of the x and y coordinates of the vertices of each triangle and comparing it to the minimum radius.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
