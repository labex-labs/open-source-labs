# Créer l'histogramme

Maintenant que nous avons nos données, nous pouvons créer l'histogramme 3D. Nous utiliserons la fonction `histogram2d()` de NumPy pour créer un histogramme 2D de nos données, puis la fonction `bar3d()` de Matplotlib pour créer un graphique en barres 3D de l'histogramme.

```python
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construire des tableaux pour les positions d'ancrage des 16 barres.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construire des tableaux avec les dimensions pour les 16 barres.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
```
