# Créer la région ombrée

Créez la région ombrée à l'aide d'un patch `Polygon`. Générez les valeurs de x et de y pour la région à l'aide de `linspace` et de la fonction définie dans l'étape 1. Ensuite, définissez les sommets de la région comme une liste de tuples. Enfin, créez l'objet `Polygon` et ajoutez-le à l'axe à l'aide de `add_patch`.

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
