# Mask off unwanted triangles

We will use the `set_mask` method to mask off unwanted triangles.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

#
