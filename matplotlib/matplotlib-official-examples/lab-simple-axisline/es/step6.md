# Crear el eje y2

Finalmente, crearemos un nuevo eje y2 en el lado derecho de la gráfica con un desplazamiento de (20, 0) y lo etiquetaremos.

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
