# Erstellen von Ebenen mit Norms

Zeigt, wie Normalisierung und Colormap-Instanzen kombiniert werden, um "Ebenen" in `.axes.Axes.pcolor`, `.axes.Axes.pcolormesh` und `.axes.Axes.imshow`-Typen von Plots zu zeichnen, ähnlich wie das levels-Schlüsselwortargument für contour/contourf.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# Verkleinern Sie diese Werte, um die Auflösung zu erhöhen
dx, dy = 0.05, 0.05

# Generieren Sie 2 2D-Gitter für die x- und y-Grenzen
y, x = np.mgrid[slice(1, 5 + dy, dy),
                slice(1, 5 + dx, dx)]

z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# x und y sind die Grenzen, daher sollte z der Wert *innerhalb* dieser Grenzen sein.
# Entfernen Sie daher den letzten Wert aus dem z-Array.
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())


# Wählen Sie die gewünschte Farbpalette, sinnvolle Ebenen und definieren Sie eine Normalisierungsinstanz,
# die Datenwerte annimmt und diese in Ebenen umwandelt.
cmap = plt.colormaps['PiYG']
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig, (ax0, ax1) = plt.subplots(nrows=2)

im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh mit Ebenen')


# Konturlinien sind *punktbasiertes* Plots, daher konvertieren wir unsere Grenze in Punktzentren
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=levels,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf mit Ebenen')

# Anpassen Sie den Abstand zwischen den Teilplots, damit der Titel von `ax1` und die Strichmarkenbeschriftungen von `ax0`
# nicht überlappen
fig.tight_layout()

plt.show()
```
