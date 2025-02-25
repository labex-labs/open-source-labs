# Zeichnen einer Pfeilrichtung zwischen verschiedenen Achsen

Zeichnen wir eine Pfeilrichtung zwischen demselben Punkt in den Datenkoordinaten, aber in verschiedenen Achsen.

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
