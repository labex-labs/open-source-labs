# Maskieren unerwünschter Dreiecke

Wir werden die unerwünschten Dreiecke mithilfe des Mittelwerts der x- und y-Koordinaten maskieren.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
