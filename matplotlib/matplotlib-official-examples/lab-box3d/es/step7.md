# Establece el zoom y la vista del ángulo

Establece el zoom y la vista del ángulo utilizando los métodos `view_init` y `set_box_aspect`. Estableceremos la vista del ángulo a 40 grados en la dirección X y -30 grados en la dirección Y, y el zoom a 0.9.

```python
# Establece el zoom y la vista del ángulo
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```
