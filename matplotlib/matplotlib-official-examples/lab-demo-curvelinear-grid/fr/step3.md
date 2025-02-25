# Code final

Le code final combine le code des étapes 1 et 2 :

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
from mpl_toolkits.axisartist import Axes, HostAxes, angle_helper
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear

def curvelinear_test1(fig):
    # Définir la transformation personnalisée
    def tr(x, y):
        return x, y - x
    def inv_tr(x, y):
        return x, y + x

    # Créer un objet GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear((tr, inv_tr))

    # Créer un sous-graphique avec la grille et les lignes d'échelles personnalisées
    ax1 = fig.add_subplot(1, 2, 1, axes_class=Axes, grid_helper=grid_helper)

    # Tracer quelques points sur le sous-graphique
    xx, yy = tr(np.array([3, 6]), np.array([5, 10]))
    ax1.plot(xx, yy)

    # Définir le rapport d'aspect et les limites du sous-graphique
    ax1.set_aspect(1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    # Ajouter des axes flottants et des lignes de grille
    ax1.axis["t"] = ax1.new_floating_axis(0, 3)
    ax1.axis["t2"] = ax1.new_floating_axis(1, 7)
    ax1.grid(True, zorder=0)

def curvelinear_test2(fig):
    # Définir la transformation personnalisée
    tr = Affine2D().scale(np.pi/180, 1) + PolarAxes.PolarTransform()

    # Définir le chercheur d'extrêmes, le localisateur de grille et le formateur d'étiquettes d'échelle
    extreme_finder = angle_helper.ExtremeFinderCycle(
        nx=20, ny=20,
        lon_cycle=360, lat_cycle=None,
        lon_minmax=None, lat_minmax=(0, np.inf),
    )
    grid_locator1 = angle_helper.LocatorDMS(12)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Créer un objet GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(
        tr, extreme_finder=extreme_finder,
        grid_locator1=grid_locator1, tick_formatter1=tick_formatter1)
    ax1 = fig.add_subplot(
        1, 2, 2, axes_class=HostAxes, grid_helper=grid_helper)

    # Rendre les étiquettes d'échelle de l'axe droit et supérieur visibles
    ax1.axis["right"].major_ticklabels.set_visible(True)
    ax1.axis["top"].major_ticklabels.set_visible(True)

    # Faire en sorte que l'axe droit affiche les étiquettes d'échelle pour la première coordonnée (angle)
    ax1.axis["right"].get_helper().nth_coord_ticks = 0

    # Faire en sorte que l'axe inférieur affiche les étiquettes d'échelle pour la deuxième coordonnée (rayon)
    ax1.axis["bottom"].get_helper().nth_coord_ticks = 1

    # Définir le rapport d'aspect et les limites du sous-graphique
    ax1.set_aspect(1)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    # Ajouter des lignes de grille au sous-graphique
    ax1.grid(True, zorder=0)

    # Créer un axe parasite avec la transformation donnée
    ax2 = ax1.get_aux_axes(tr)

    # Tout ce que vous tracez dans ax2 correspondra aux échelles et aux grilles d'ax1.
    ax2.plot(np.linspace(0, 30, 51), np.linspace(10, 10, 51), linewidth=2)

    ax2.pcolor(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
               np.arange(9).reshape((3, 3)))
    ax2.contour(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
                np.arange(16).reshape((4, 4)), colors="k")

fig = plt.figure(figsize=(7, 4))
curvelinear_test1(fig)
curvelinear_test2(fig)
plt.show()
```
