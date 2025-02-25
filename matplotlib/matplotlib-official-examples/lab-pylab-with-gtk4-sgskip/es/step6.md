# Actualizar la etiqueta con las coordenadas del cursor

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

Creamos una función que actualiza la etiqueta con las coordenadas x e y del cursor cuando se mueve sobre los gráficos. Conectamos la función al evento `motion_notify_event` del lienzo.
