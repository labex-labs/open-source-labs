# Conectar o evento de desenho à função de retorno de chamada

Precisamos conectar o `draw_event` à nossa função `on_draw`.

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```
