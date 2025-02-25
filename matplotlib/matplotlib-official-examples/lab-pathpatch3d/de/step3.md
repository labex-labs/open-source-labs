# Zeichnen eines Kreises auf der Wand

Wir werden einen Kreis auf der x=0-'Wand' des 3D-Diagramms mit den `Circle`- und `pathpatch_2d_to_3d`-Funktionen von Matplotlib zeichnen.

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```
