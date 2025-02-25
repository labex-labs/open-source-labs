# Einen benutzerdefinierten Triangulationsvorgang erstellen

In diesem Schritt werden wir einen benutzerdefinierten Triangulationsvorgang erstellen und unerwünschte Dreiecke ausblenden.

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
