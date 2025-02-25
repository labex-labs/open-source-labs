# Crear contornos rellenos con agujeros

Se pueden especificar múltiples líneas de contorno relleno en una sola lista de vértices de polígono junto con una lista de tipos de vértices (tipos de código) tal como se describe en la clase Path. Esto es particularmente útil para polígonos con agujeros.

```python
fig, ax = plt.subplots()
filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
M = Path.MOVETO
L = Path.LINETO
kinds01 = [[M, L, L, L, M, L, L, L]]
cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
cbar = fig.colorbar(cs)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 3.5),
       title='User specified filled contours with holes')
```
