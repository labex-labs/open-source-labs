# Ejemplos de mapas de calor más complejos

A continuación, demostramos la versatilidad de las funciones creadas anteriormente al aplicarlas en diferentes casos y utilizar diferentes argumentos.

```python
np.random.seed(19680801)

fig, ((ax, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))

# Repite el ejemplo anterior con un tamaño de fuente y una paleta de colores diferentes.

im, _ = heatmap(harvest, vegetables, farmers, ax=ax, cmap="Wistia", cbarlabel="cosecha [t/anio]")
annotate_heatmap(im, valfmt="{x:.1f}", size=7)

# A veces, incluso los datos mismos son categóricos. Aquí usamos un `matplotlib.colors.BoundaryNorm` para clasificar los datos y usarlos para colorear la gráfica, pero también para obtener las etiquetas de clase a partir de una matriz de clases.

data = np.random.randn(6, 6)
y = [f"Prod. {i}" for i in range(10, 70, 10)]
x = [f"Cycle {i}" for i in range(1, 7)]

qrates = list("ABCDEFG")
norm = matplotlib.colors.BoundaryNorm(np.linspace(-3.5, 3.5, 8), 7)
fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: qrates[::-1][norm(x)])

im, _ = heatmap(data, y, x, ax=ax3, cmap=mpl.colormaps["PiYG"].resampled(7), norm=norm, cbar_kw=dict(ticks=np.arange(-3, 4), format=fmt), cbarlabel="Calificación de calidad")
annotate_heatmap(im, valfmt=fmt, size=9, fontweight="bold", threshold=-1, textcolors=("rojo", "negro"))

# Podemos trazar una matriz de correlación de manera agradable. Dado que está limitada por -1 y 1, los usamos como vmin y vmax.

corr_matrix = np.corrcoef(harvest)
im, _ = heatmap(corr_matrix, vegetables, vegetables, ax=ax4, cmap="PuOr", vmin=-1, vmax=1, cbarlabel="coeficiente de correlación")
annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)

plt.tight_layout()
plt.show()
```
