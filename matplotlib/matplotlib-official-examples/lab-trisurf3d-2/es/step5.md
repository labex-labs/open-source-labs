# Graficar la superficie

Finalmente, graficamos la superficie utilizando la función `plot_trisurf()`. Los triángulos en el espacio de parámetros determinan qué puntos `x`, `y`, `z` están conectados por un borde.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
