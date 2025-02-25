# Créer un graphique en couleur de surface

Nous allons créer un graphique en couleur de surface à l'aide de `ax.tricontourf` et `fig.colorbar`.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tcf = ax1.tricontourf(triang, z)
fig1.colorbar(tcf)
ax1.tricontour(triang, z, colors='k')
ax1.set_title('Contour plot of Delaunay triangulation')
```
