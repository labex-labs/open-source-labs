# Zeichnen einer einfachen Pfeilrichtung

Nun zeichnen wir eine einfache Pfeilrichtung zwischen zwei Punkten in den Koordinaten einer einzelnen Achse.

```python
xyA = (0.2, 0.2)
xyB = (0.8, 0.8)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
                      arrowstyle="-|>", shrinkA=5, shrinkB=5,
                      mutation_scale=20, fc="w")
ax1.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], "o")
ax1.add_artist(con)
```
