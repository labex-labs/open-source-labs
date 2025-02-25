# Establecer escala de color y crear barra de colores

Ahora, estableceremos la escala de color para nuestras imágenes y crearemos una barra de colores para mostrar el rango de valores. Encontraremos los valores mínimo y máximo para todas las imágenes y normalizaremos la escala de color en consecuencia.

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```
