# Erstelle die Triangulation

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

Erklärung:

- `Triangulation` ist eine Klasse, die eine Delaunay-Triangulation aus einem Punktmengen erstellt.
- `triang` ist eine Instanz der `Triangulation`-Klasse.
- `triang.set_mask` maskiert unerwünschte Dreiecke.
