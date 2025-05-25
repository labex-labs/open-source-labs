# Plotar a Superfície

Finalmente, plotamos a superfície usando a função `plot_trisurf()`. Os triângulos no espaço paramétrico determinam quais pontos `x`, `y`, `z` são conectados por uma aresta.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
