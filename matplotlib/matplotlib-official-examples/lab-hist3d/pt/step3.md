# Criar o Histograma

Agora que temos nossos dados, podemos criar o histograma 3D. Usaremos a função `histogram2d()` do NumPy para criar um histograma 2D de nossos dados e, em seguida, usaremos a função `bar3d()` do Matplotlib para criar um gráfico de barras 3D do histograma.

```python
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
```
