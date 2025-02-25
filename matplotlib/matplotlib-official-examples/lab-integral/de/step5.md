# Erzeuge die eingefärbte Region

Erzeuge die eingefärbte Region mit einem `Polygon`-Patch. Erzeuge x- und y-Werte für die Region mit `linspace` und der in Schritt 1 definierten Funktion. Definiere dann die Eckpunkte der Region als Liste von Tupeln. Schließlich erstelle das `Polygon`-Objekt und füge es zur Achse hinzu mit `add_patch`.

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
