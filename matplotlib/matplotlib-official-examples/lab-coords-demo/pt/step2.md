# Evento de Movimento do Mouse

Podemos nos conectar aos eventos de movimento do mouse usando o método `motion_notify_event`. Neste exemplo, estamos imprimindo as coordenadas de dados x e y e as coordenadas de pixel x e y quando o mouse se move sobre o gráfico.

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
