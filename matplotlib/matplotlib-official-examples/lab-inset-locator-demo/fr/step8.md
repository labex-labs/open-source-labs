# Créer un inset centré dans les coordonnées de la figure

Nous pouvons créer un inset qui est horizontalement centré dans les coordonnées de la figure et verticalement lié pour être aligné avec les axes en utilisant la méthode `blended_transform_factory()` pour créer une transformation mixte et en l'utilisant comme paramètre `bbox_transform`.

```python
# Crée un inset horizontalement centré dans les coordonnées de la figure et verticalement
# lié pour être aligné avec les axes.
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
