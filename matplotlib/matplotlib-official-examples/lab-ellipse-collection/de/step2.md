# Daten für Ellipsen erstellen

Wir erstellen die Daten für unsere Ellipsen in Form von Arrays von x-Koordinaten, y-Koordinaten, Breite, Höhe und Winkel.

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
