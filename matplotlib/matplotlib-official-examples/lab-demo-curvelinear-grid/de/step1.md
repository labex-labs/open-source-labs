# Gitter für benutzerdefinierte Transformation

Zunächst erstellen wir ein benutzerdefiniertes Gitter und Strichelinien mit `GridHelperCurveLinear`. Die benutzerdefinierte Transformation wird auf das Gitter und die Strichelinien angewendet. Der folgende Code demonstriert diesen Prozess:

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
from mpl_toolkits.axisartist import Axes, HostAxes, angle_helper
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear

def curvelinear_test1(fig):
    # Definiere benutzerdefinierte Transformation
    def tr(x, y):
        return x, y - x
    def inv_tr(x, y):
        return x, y + x

    # Erstelle GridHelperCurveLinear-Objekt
    grid_helper = GridHelperCurveLinear((tr, inv_tr))

    # Erstelle ein Subplot mit dem benutzerdefinierten Gitter und den Strichelinien
    ax1 = fig.add_subplot(1, 2, 1, axes_class=Axes, grid_helper=grid_helper)

    # Plotte einige Punkte auf dem Subplot
    xx, yy = tr(np.array([3, 6]), np.array([5, 10]))
    ax1.plot(xx, yy)

    # Setze das Seitenverhältnis und die Grenzen des Subplots
    ax1.set_aspect(1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    # Füge fließende Achsen und Gitterlinien hinzu
    ax1.axis["t"] = ax1.new_floating_axis(0, 3)
    ax1.axis["t2"] = ax1.new_floating_axis(1, 7)
    ax1.grid(True, zorder=0)

fig = plt.figure(figsize=(7, 4))
curvelinear_test1(fig)
plt.show()
```
