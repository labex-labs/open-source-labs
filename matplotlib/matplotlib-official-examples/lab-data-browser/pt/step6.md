# Conectar Manipuladores de Eventos

Conectaremos os manipuladores de eventos (event handlers) ao canvas da figura.

```python
browser = PointBrowser()

fig.canvas.mpl_connect('pick_event', browser.on_pick)
fig.canvas.mpl_connect('key_press_event', browser.on_press)
```
