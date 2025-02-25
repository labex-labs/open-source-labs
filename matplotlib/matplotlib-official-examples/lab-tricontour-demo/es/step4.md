# Crear un gráfico de pcolor

Crearemos un gráfico de pcolor utilizando `ax.tricontourf` y `fig.colorbar`.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tcf = ax1.tricontourf(triang, z)
fig1.colorbar(tcf)
ax1.tricontour(triang, z, colors='k')
ax1.set_title('Contour plot of Delaunay triangulation')
```
