# Mettre tout ça ensemble

Créons un exemple complet qui inclut à la fois la création d'un polygone de manière programmée et interactive.

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# Créez une figure et des axes
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# Créez un objet PolygonSelector et ajoutez des sommets
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Tracez le polygone
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# Créez un autre objet PolygonSelector pour la création interactive
selector2 = PolygonSelector(ax2, lambda *args: None)

print("Cliquez sur la figure pour créer un polygone.")
print("Appuyez sur la touche 'échappement' pour commencer un nouveau polygone.")
print("Essayez de maintenir la touche 'Maj' pour déplacer tous les sommets.")
print("Essayez de maintenir la touche 'Ctrl' pour déplacer un seul sommet.")

plt.show()
```
