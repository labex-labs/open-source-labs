# Agregar leyenda y color

Agregaremos una leyenda a la gráfica y colorearemos las etiquetas de cada eje para que coincidan con el color del conjunto de datos correspondiente utilizando las funciones `legend()` y `label.set_color()`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```
