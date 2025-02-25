# Conectar la función del evento de selección a la superficie de dibujo

Conectaremos la función del evento de selección a la superficie de dibujo.

```python
fig.canvas.mpl_connect('pick_event', on_pick)
```
