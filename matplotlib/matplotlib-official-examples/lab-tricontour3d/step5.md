# Mask off unwanted triangles

We will mask off the unwanted triangles using the mean of the x and y coordinates.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
