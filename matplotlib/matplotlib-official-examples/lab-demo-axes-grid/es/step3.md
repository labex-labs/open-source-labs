# Crear una cuadrícula de imágenes 2x2 con cada imagen teniendo su propia barra de color

Nuestra siguiente cuadrícula será una cuadrícula de imágenes 2x2 con cada imagen teniendo su propia barra de color. Usaremos nuevamente la función `ImageGrid`, pero esta vez estableceremos `cbar_mode` en `"each"` para especificar que cada imagen debe tener su propia barra de color.

```python
# Crear una cuadrícula de imágenes 2x2 con cada imagen teniendo su propia barra de color
grid = ImageGrid(
    fig,  # Objeto Figure
    142,  # Ubicación del subplot
    nrows_ncols=(2, 2),  # Número de filas y columnas
    axes_pad=0.1,  # Espaciado entre los ejes
    label_mode="1",  # Modo de etiquetado
    share_all=True,  # Compartir barra de color entre todas las imágenes
    cbar_location="top",  # Ubicación de la barra de color
    cbar_mode="each",  # Modo de barra de color
    cbar_size="7%",  # Tamaño de la barra de color
    cbar_pad="2%"  # Espaciado entre la barra de color y las imágenes
)

# Graficar imágenes en la cuadrícula y agregar barras de color
for ax, cax in zip(grid, grid.cbar_axes):
    im = ax.imshow(Z, extent=extent)
    cax.colorbar(im)
    cax.tick_params(labeltop=False)
```
