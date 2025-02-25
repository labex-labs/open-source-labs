# Agregar líneas a la Figura

Podemos agregar líneas a la figura utilizando el método `fig.add_artist()`. Crearemos dos líneas: una que va de (0,0) a (1,1) y otra que va de (0,1) a (1,0).

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```
