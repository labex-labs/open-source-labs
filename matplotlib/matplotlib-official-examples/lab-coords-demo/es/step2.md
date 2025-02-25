# Evento de movimiento del mouse

Podemos conectarnos a los eventos de movimiento del mouse utilizando el método `motion_notify_event`. En este ejemplo, estamos imprimiendo las coordenadas de datos x e y y las coordenadas de píxeles x e y cuando el mouse se mueve sobre el gráfico.

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
