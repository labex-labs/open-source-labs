# Ausschließen unerwünschter Dreiecke

Wir schließen unerwünschte Dreiecke aus, indem wir den Mittelpunkt jedes Dreiecks berechnen und überprüfen, ob er innerhalb eines angegebenen Radius liegt.

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```
