# Dibujar un círculo en la pared

Dibujaremos un círculo en la pared 'x = 0' del gráfico tridimensional utilizando las funciones `Circle` y `pathpatch_2d_to_3d` de Matplotlib.

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```
