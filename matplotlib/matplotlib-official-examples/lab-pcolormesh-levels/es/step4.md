# Creación de niveles usando normas

Muestra cómo combinar instancias de Normalización y Colormap para dibujar "niveles" en gráficos de tipo `.axes.Axes.pcolor`, `.axes.Axes.pcolormesh` y `.axes.Axes.imshow` de manera similar al argumento de palabras clave levels para contour/contourf.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# haz estos más pequeños para aumentar la resolución
dx, dy = 0.05, 0.05

# genera 2 mallas 2d para los límites de x & y
y, x = np.mgrid[slice(1, 5 + dy, dy),
                slice(1, 5 + dx, dx)]

z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# x e y son límites, entonces z debe ser el valor *dentro* de esos límites.
# Por lo tanto, elimina el último valor del array z.
z = z[:-1, :-1]
niveles = MaxNLocator(nbins=15).tick_values(z.min(), z.max())


# elige la colormap deseada, niveles sensatos y define una instancia de normalización
# que toma valores de datos y los traduce en niveles.
cmap = plt.colormaps['PiYG']
norm = BoundaryNorm(niveles, ncolors=cmap.N, clip=True)

fig, (ax0, ax1) = plt.subplots(nrows=2)

im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh con niveles')


# los contornos son gráficos *basados en puntos*, entonces convierte nuestro límite en
# centros de puntos
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, niveles=niveles,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf con niveles')

# ajusta el espaciado entre subgráficos para que el título de `ax1` y las etiquetas de
# marcas de `ax0` no se solapen
fig.tight_layout()

plt.show()
```
