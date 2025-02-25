# Crear una función de devolución de llamada para el deslizador

Crearemos una función de devolución de llamada que se llamará cada vez que el usuario cambie los valores del umbral utilizando el deslizador. La función actualizará la paleta de colores de la imagen y las posiciones de las líneas verticales en el histograma.

```python
def update(val):
    # El val pasado a una devolución de llamada por el RangeSlider será
    # una tupla de (min, max)

    # Actualizar la paleta de colores de la imagen
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Actualizar la posición de las líneas verticales
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Volver a dibujar la figura para asegurarse de que se actualice
    fig.canvas.draw_idle()


slider.on_changed(update)
```
