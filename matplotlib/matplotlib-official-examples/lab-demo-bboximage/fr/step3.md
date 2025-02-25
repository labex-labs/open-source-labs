# Créez une BboxImage pour chaque carte de couleurs

Ensuite, nous créons une BboxImage pour chaque carte de couleurs. Nous commençons par créer une liste de toutes les cartes de couleurs en utilisant la méthode `plt.colormaps`. Nous créons ensuite une boucle `for` qui itère à travers la liste des cartes de couleurs. Pour chaque carte de couleurs, nous calculons la position `ix` et `iy` en utilisant la méthode `divmod()`. Nous créons ensuite un objet `Bbox` en utilisant la méthode `Bbox.from_bounds()`. Nous passons les valeurs `ix`, `iy`, `dx` et `dy` à la méthode `Bbox.from_bounds()` pour créer la boîte englobante. Nous créons ensuite un objet `TransformedBbox` en utilisant l'objet `Bbox` et l'objet `ax2.transAxes`. Enfin, nous créons un objet `BboxImage` en utilisant la méthode `add_artist()`. Nous passons l'objet `TransformedBbox` au constructeur `BboxImage` pour créer une image avec la carte de couleurs.

```python
cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

ncol = 2
nrow = len(cmap_names) // ncol + 1

xpad_fraction = 0.3
dx = 1 / (ncol + xpad_fraction * (ncol - 1))

ypad_fraction = 0.3
dy = 1 / (nrow + ypad_fraction * (nrow - 1))

for i, cmap_name in enumerate(cmap_names):
    ix, iy = divmod(i, nrow)
    bbox0 = Bbox.from_bounds(ix*dx*(1+xpad_fraction),
                             1 - iy*dy*(1+ypad_fraction) - dy,
                             dx, dy)
    bbox = TransformedBbox(bbox0, ax2.transAxes)
    ax2.add_artist(
        BboxImage(bbox, cmap=cmap_name, data=np.arange(256).reshape((1, -1))))
```
