# Definir la función del evento de selección

Definiremos la función del evento de selección que cambiará la visibilidad de la línea original correspondiente a la línea proxy de la leyenda.

```python
def on_pick(event):
    # En el evento de selección, encontrar la línea original correspondiente a la
    # línea proxy de la leyenda y cambiar su visibilidad.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Cambiar la transparencia de la línea en la leyenda, para que podamos ver
    # qué líneas se han alternado.
    legline.set_alpha(1.0 si visible else 0.2)
    fig.canvas.draw()
```
