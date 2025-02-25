# Configurar la interactividad

Necesitamos configurar la interactividad para actualizar el triángulo debajo del cursor. Utilizaremos el evento `motion_notify_event` para detectar cuando el mouse se mueve sobre la gráfica. Crearemos una función `on_mouse_move()` que obtendrá el triángulo debajo del cursor utilizando el objeto TriFinder, actualizará el polígono con los vértices del triángulo y actualizará el título de la gráfica con el índice del triángulo.

```python
def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'Triángulo {tri}')
    event.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
```
