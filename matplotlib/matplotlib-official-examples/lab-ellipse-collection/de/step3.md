# Ellipsen-Sammlung erstellen

Wir erstellen eine `EllipseCollection` mit den oben genannten Daten und legen die Maßeinheiten auf 'x' und die Verschiebungen auf `XY` fest.

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
