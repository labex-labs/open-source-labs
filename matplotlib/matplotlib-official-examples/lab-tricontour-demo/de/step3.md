# Entferne unerwünschte Dreiecke

Wir werden die `set_mask`-Methode verwenden, um unerwünschte Dreiecke auszublenden.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
