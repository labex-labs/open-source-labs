# Crear una cuadrícula de imágenes 2x2 con una sola barra de color

Nuestra primera cuadrícula será una cuadrícula de imágenes 2x2 con una sola barra de color. Usaremos la función `ImageGrid` para crear la cuadrícula y especificar el número de filas y columnas que queremos. También especificaremos la ubicación de la barra de color y estableceremos `share_all` en `True` para compartir la barra de color entre todas las imágenes.

```python
# Crear una cuadrícula de imágenes 2x2 con una sola barra de color
grid = ImageGrid(
    fig,  # Objeto Figure
    141,  # Ubicación del subplot
    nrows_ncols=(2, 2),  # Número de filas y columnas
    axes_pad=0.0,  # Espaciado entre los ejes
    label_mode="L",  # Modo de etiquetado
    share_all=True,  # Compartir barra de color entre todas las imágenes
    cbar_location="top",  # Ubicación de la barra de color
    cbar_mode="single"  # Modo de barra de color
)

# Graficar imágenes en la cuadrícula
for ax in grid:
    im = ax.imshow(Z, extent=extent)

# Agregar barra de color a la cuadrícula
grid.cbar_axes[0].colorbar(im)
for cax in grid.cbar_axes:
    cax.tick_params(labeltop=False)
```
