# Actualizar imágenes

Finalmente, actualizaremos las imágenes para responder a los cambios en la norma de otras imágenes. Esto nos permitirá cambiar el mapa de colores y la escala de color de una imagen y que todas las demás se actualicen en consecuencia.

```python
def update(changed_image):
    for im in images:
        if (changed_image.get_cmap()!= im.get_cmap()
                or changed_image.get_clim()!= im.get_clim()):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())

for im in images:
    im.callbacks.connect('changed', update)
```
