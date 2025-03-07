# Pfad-Daten definieren

Wir definieren in diesem Schritt die Pfad-Daten. Pfad-Daten sind eine Sequenz von Tupeln, die die Eckpunkte und Codes des Pfads angeben. Wir verwenden die `mpath.Path`-Klasse, um aus diesen Daten ein Path-Objekt zu erstellen.

```python
Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
```
