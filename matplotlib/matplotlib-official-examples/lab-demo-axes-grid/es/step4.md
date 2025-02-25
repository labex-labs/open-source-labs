# Crear una cuadrícula de imágenes 2x2 con cada imagen teniendo su propia barra de color y un rango de barra de color diferente

Nuestra última cuadrícula también será una cuadrícula de imágenes 2x2 con cada imagen teniendo su propia barra de color, pero esta vez usaremos un rango de barra de color diferente para cada imagen. Estableceremos el rango de la barra de color usando `vmin` y `vmax` al graficar cada imagen.

```python
# Crear una cuadrícula de imágenes 2x2 con cada imagen teniendo su propia barra de color y un rango de barra de color diferente
grid = ImageGrid(
    fig,  # Objeto Figure
    143,  # Ubicación del subplot
    nrows_ncols=(2, 2),  # Número de filas y columnas
    axes_pad=(0.45, 0.15),  # Espaciado entre los ejes
    label_mode="1",  # Modo de etiquetado
    share_all=True,  # Compartir barra de color entre todas las imágenes
    cbar_location="right",  # Ubicación de la barra de color
    cbar_mode="each",  # Modo de barra de color
    cbar_size="7%",  # Tamaño de la barra de color
    cbar_pad="2%"  # Espaciado entre la barra de color y las imágenes
)

# Graficar imágenes en la cuadrícula y agregar barras de color
limits = ((0, 1), (-2, 2), (-1.7, 1.4), (-1.5, 1))  # Rangos de barra de color diferentes
for ax, cax, vlim in zip(grid, grid.cbar_axes, limits):
    im = ax.imshow(Z, extent=extent, vmin=vlim[0], vmax=vlim[1])
    cb = cax.colorbar(im)
    cb.set_ticks((vlim[0], vlim[1]))
```
