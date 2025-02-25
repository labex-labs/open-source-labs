# Generar patrones de sombreado etiquetados sin color

Podemos generar patrones de sombreado etiquetados sin color especificando el parámetro `colors` como `"none"` en `ax.tricontourf`. También podemos crear una leyenda para el conjunto de contornos utilizando `ContourSet.legend_elements`.

```python
fig3, ax3 = plt.subplots()
n_levels = 7
tcf = ax3.tricontourf(
    triang,
    z,
    n_levels,
    colors="none",
    hatches=[".", "/", "\\", None, "\\\\", "*"],
)
ax3.tricontour(triang, z, n_levels, colors="black", linestyles="-")

artists, labels = tcf.legend_elements(str_format="{:2.1f}".format)
ax3.legend(artists, labels, handleheight=2, framealpha=1)
```
