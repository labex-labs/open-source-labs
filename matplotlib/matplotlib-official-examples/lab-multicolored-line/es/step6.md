# Usar una norma de frontera

En lugar de eso, usaremos una norma de frontera para colorear los segmentos de línea. Crearemos un `ListedColormap` que contenga tres colores: rojo, verde y azul. Luego, crearemos una `BoundaryNorm` con los límites -1, -0.5, 0.5 y 1, y el `ListedColormap`. Usaremos la función `set_array` para establecer los valores utilizados para la asignación de colores.

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
