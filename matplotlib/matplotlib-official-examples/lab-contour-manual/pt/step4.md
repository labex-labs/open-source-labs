# Criar contornos preenchidos com buracos

Múltiplas linhas de contorno preenchidas podem ser especificadas em uma única lista de vértices de polígono, juntamente com uma lista de tipos de vértices (tipos de código), conforme descrito na classe `Path`. Isso é particularmente útil para polígonos com buracos.

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
