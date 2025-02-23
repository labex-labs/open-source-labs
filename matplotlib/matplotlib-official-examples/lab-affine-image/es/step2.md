# Crear una función para trazar la imagen

En este paso, definimos una función que toma la imagen, el eje de trazado y la transformación como entradas. La función muestra la imagen en el eje de trazado con la transformación especificada. La función también muestra un rectángulo amarillo alrededor de la imagen para mostrar la extensión deseada de la imagen.

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
