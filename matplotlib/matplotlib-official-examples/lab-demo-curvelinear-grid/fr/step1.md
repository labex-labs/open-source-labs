# Grille pour une transformation personnalisée

Tout d'abord, nous allons créer une grille personnalisée et des lignes d'échelles en utilisant `GridHelperCurveLinear`. La transformation personnalisée sera appliquée à la grille et aux lignes d'échelles. Le code suivant illustre ce processus :

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

fig = plt.figure(figsize=(7, 4))
curvelinear_test1(fig)
plt.show()
```
