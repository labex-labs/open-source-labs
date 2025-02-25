# Agregar leyenda y colores de los ejes

Agregamos una leyenda al eje principal utilizando el método `host.legend()`. También establecemos el color de la etiqueta del eje y izquierdo del eje principal, la etiqueta del eje y derecho del primer eje parasito y la etiqueta del eje y derecho del segundo eje parasito para que coincidan con sus respectivas líneas utilizando los métodos `host.axis["left"].label.set_color(p1.get_color())`, `par1.axis["right"].label.set_color(p2.get_color())` y `par2.axis["right2"].label.set_color(p3.get_color())`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
