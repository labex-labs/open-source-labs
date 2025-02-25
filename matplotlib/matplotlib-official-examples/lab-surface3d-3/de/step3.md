# Farben für den Oberflächenplot erstellen

In diesem Schritt werden wir Farben für den Oberflächenplot erstellen. Wir werden ein leeres Array von Zeichenketten mit der gleichen Form wie das Gitternetz erstellen und es mit zwei Farben in einem Schachbrettmuster befüllen.

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
