# Erstellen eines Einfügebereichs, das in den Koordinaten der Figur zentriert ist

Wir können einen Einfügebereich erstellen, der in den Koordinaten der Figur horizontal zentriert ist und vertikal so ausgerichtet ist, dass er mit den Achsen übereinstimmt, indem wir die Methode `blended_transform_factory()` verwenden, um eine gemischte Transformation zu erstellen und diese als Parameter `bbox_transform` zu verwenden.

```python
# Erstellen Sie einen Einfügebereich, der in den Koordinaten der Figur horizontal zentriert ist und vertikal
# so ausgerichtet ist, dass er mit den Achsen übereinstimmt.
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
