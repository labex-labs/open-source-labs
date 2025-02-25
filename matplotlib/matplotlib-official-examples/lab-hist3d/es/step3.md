# Crear el histograma

Ahora que tenemos nuestros datos, podemos crear el histograma tridimensional. Usaremos la función `histogram2d()` de NumPy para crear un histograma bidimensional de nuestros datos, y luego usaremos la función `bar3d()` de Matplotlib para crear un gráfico de barras tridimensional del histograma.

```python
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construir matrices para las posiciones de anclaje de las 16 barras.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construir matrices con las dimensiones para las 16 barras.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
```
