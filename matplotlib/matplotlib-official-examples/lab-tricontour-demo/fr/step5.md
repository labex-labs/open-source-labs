# Créer un graphique en ligne de niveau hachuré

Nous pouvons créer un graphique en ligne de niveau hachuré en spécifiant le paramètre `hatches` dans `ax.tricontourf`. Nous pouvons également utiliser une autre carte de couleurs en spécifiant le paramètre `cmap`.

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
