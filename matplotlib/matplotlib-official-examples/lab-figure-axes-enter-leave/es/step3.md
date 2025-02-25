# Definiendo los Manejadores de Eventos

Ahora definiremos cuatro funciones de manejador de eventos: `on_enter_axes`, `on_leave_axes`, `on_enter_figure` y `on_leave_figure`. Estas funciones se llamarán cuando el mouse entre o salga de un eje o de la figura.

```python
def on_enter_axes(event):
    print('enter_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()

def on_leave_axes(event):
    print('leave_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()

def on_enter_figure(event):
    print('enter_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('red')
    event.canvas.draw()

def on_leave_figure(event):
    print('leave_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()
```
