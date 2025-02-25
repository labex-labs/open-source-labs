# Die Triangulation erstellen

Wir werden die Triangulation mit `matplotlib.tri.Triangulation` erstellen. Wir müssen die Dreiecke nicht angeben, daher wird automatisch die Delaunay-Triangulation der Punkte erstellt.

```python
triang = tri.Triangulation(x, y)
```
