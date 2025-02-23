# Conectar el evento de dibujo a la función de devolución de llamada

Necesitamos conectar el `draw_event` a nuestra función `on_draw`.

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```
