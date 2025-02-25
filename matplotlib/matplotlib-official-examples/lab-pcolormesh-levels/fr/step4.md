# Création de niveaux à l'aide de normes

Montre comment combiner des instances de Normalization et de Colormap pour tracer des "niveaux" dans les graphiques de type `.axes.Axes.pcolor`, `.axes.Axes.pcolormesh` et `.axes.Axes.imshow` de manière similaire à l'argument clé `levels` pour contour/contourf.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# Rendre ces valeurs plus petites pour augmenter la résolution
dx, dy = 0.05, 0.05

# Générer 2 grilles 2D pour les limites x et y
y, x = np.mgrid[slice(1, 5 + dy, dy),
                slice(1, 5 + dx, dx)]

z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# x et y sont des limites, donc z devrait être la valeur *à l'intérieur* de ces limites.
# Par conséquent, supprimer la dernière valeur du tableau z.
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())


# Sélectionner la colormap souhaitée, des niveaux sensés et définir une instance de normalisation
# qui prend les valeurs de données et les traduit en niveaux.
cmap = plt.colormaps['PiYG']
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig, (ax0, ax1) = plt.subplots(nrows=2)

im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh avec niveaux')


# Les contours sont des graphiques *basés sur des points*, donc convertir nos limites en points
# centraux
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=levels,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf avec niveaux')

# Ajuster l'espacement entre les sous-graphiques pour que le titre d'`ax1` et les étiquettes d'échelle d'`ax0`
# ne se chevauchent pas
fig.tight_layout()

plt.show()
```
