# Criar um gráfico de contorno hachurado

Podemos criar um gráfico de contorno hachurado especificando o parâmetro `hatches` em `ax.tricontourf`. Também podemos usar um mapa de cores diferente especificando o parâmetro `cmap`.

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
ax2.set_title("Gráfico de contorno hachurado da triangulação de Delaunay")
```
