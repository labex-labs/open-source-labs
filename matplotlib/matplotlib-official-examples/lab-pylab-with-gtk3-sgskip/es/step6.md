# Actualizar el texto de la etiqueta en el movimiento del mouse

Actualizaremos el texto de la etiqueta para mostrar las coordenadas x,y del mouse cuando se arrastra sobre el eje. Creamos una función para actualizar el texto de la etiqueta y la conectamos al evento `motion_notify_event` utilizando el método `mpl_connect()`.

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
