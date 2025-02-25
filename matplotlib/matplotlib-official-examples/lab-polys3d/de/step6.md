# Erstellen der Polygone und Hinzufügen zum Diagramm

Wir erstellen die Polygone mit der Funktion `PolyCollection` aus Matplotlib und fügen sie zum Diagramm hinzu.

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```
