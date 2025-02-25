# Crear un gráfico de contorno con sombreado

Podemos crear un gráfico de contorno con sombreado especificando el parámetro `hatches` en `ax.tricontourf`. También podemos utilizar una mapa de colores diferente especificando el parámetro `cmap`.

```python
fig2, ax2 = plt.subplots()
ax2.set_aspect("equal")
tcf = ax2.tricontourf(
    triang,
    z,
    hatches=["*", "-", "/", "//", "\\", None],
    cmap="cividis"
)
fig2.colorbar(tcf)
ax2.tricontour(triang, z, linestyles="solid", colors="k", linewidths=2.0)
ax2.set_title("Hatched Contour plot of Delaunay triangulation")
```
