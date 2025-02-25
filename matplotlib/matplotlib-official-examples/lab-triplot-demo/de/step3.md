# Ungewollte Dreiecke maskieren

Wir werden ungewollte Dreiecke maskieren, indem wir den Mittelwert der x- und y-Koordinaten der Eckpunkte jedes Dreiecks berechnen und ihn mit dem Mindestradius vergleichen.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
