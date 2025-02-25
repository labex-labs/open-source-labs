# Conectar manejadores de eventos

Conectaremos los manejadores de eventos al lienzo de la figura.

```python
browser = PointBrowser()

fig.canvas.mpl_connect('pick_event', browser.on_pick)
fig.canvas.mpl_connect('key_press_event', browser.on_press)
```
