# Alles zusammenbringen

Schauen wir uns ein vollständiges Beispiel an, das sowohl das programmgesteuerte als auch das interaktive Erstellen eines Polygons umfasst.

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# Erstellen Sie eine Figur und Achsen
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# Erstellen Sie ein PolygonSelector-Objekt und fügen Sie Eckpunkte hinzu
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plotten Sie das Polygon
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# Erstellen Sie ein weiteres PolygonSelector-Objekt für die interaktive Erstellung
selector2 = PolygonSelector(ax2, lambda *args: None)

print("Klicken Sie auf die Figur, um ein Polygon zu erstellen.")
print("Drücken Sie die 'Esc'-Taste, um ein neues Polygon zu starten.")
print("Versuchen Sie, die 'Shift'-Taste gedrückt zu halten, um alle Eckpunkte zu bewegen.")
print("Versuchen Sie, die 'Ctrl'-Taste gedrückt zu halten, um einen einzelnen Eckpunkt zu bewegen.")

plt.show()
```
