# Erstellen der Eckpunkte und Codes

Wir werden die Eckpunkte und Codes für die beiden Polygone erstellen, die wir zu einem zusammengesetzten Pfad kombinieren möchten. Wir werden `Path.MOVETO` verwenden, um den Cursor an den Startpunkt des Polygons zu bewegen, `Path.LINETO` verwenden, um eine Linie vom Startpunkt zum nächsten Punkt zu erstellen und `Path.CLOSEPOLY` verwenden, um das Polygon zu schließen.

```python
vertices = []
codes = []

# Erstes Polygon - Rechteck
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# Zweites Polygon - Dreieck
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```
