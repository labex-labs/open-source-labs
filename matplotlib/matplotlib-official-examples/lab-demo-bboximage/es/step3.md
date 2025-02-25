# Crear una BboxImage para cada mapa de colores

A continuación, creamos una BboxImage para cada mapa de colores. Comenzamos creando una lista de todos los mapas de colores utilizando el método `plt.colormaps`. Luego creamos un bucle `for` que itera a través de la lista de mapas de colores. Para cada mapa de colores, calculamos la posición `ix` e `iy` utilizando el método `divmod()`. Luego creamos un objeto `Bbox` utilizando el método `Bbox.from_bounds()`. Pasamos los valores `ix`, `iy`, `dx` y `dy` al método `Bbox.from_bounds()` para crear el cuadro delimitador. Luego creamos un objeto `TransformedBbox` utilizando el objeto `Bbox` y el objeto `ax2.transAxes`. Finalmente, creamos un objeto `BboxImage` utilizando el método `add_artist()`. Pasamos el objeto `TransformedBbox` al constructor de `BboxImage` para crear una imagen con el mapa de colores.

```python
cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

ncol = 2
nrow = len(cmap_names) // ncol + 1

xpad_fraction = 0.3
dx = 1 / (ncol + xpad_fraction * (ncol - 1))

ypad_fraction = 0.3
dy = 1 / (nrow + ypad_fraction * (nrow - 1))

for i, cmap_name in enumerate(cmap_names):
    ix, iy = divmod(i, nrow)
    bbox0 = Bbox.from_bounds(ix*dx*(1+xpad_fraction),
                             1 - iy*dy*(1+ypad_fraction) - dy,
                             dx, dy)
    bbox = TransformedBbox(bbox0, ax2.transAxes)
    ax2.add_artist(
        BboxImage(bbox, cmap=cmap_name, data=np.arange(256).reshape((1, -1))))
```
