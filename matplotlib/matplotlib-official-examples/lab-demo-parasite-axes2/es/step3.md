# Ajustar el eje parasito

Necesitamos ajustar la posición de los ejes parasitos. La función `new_fixed_axis()` se utiliza para crear un nuevo eje y en el lado derecho de la gráfica. La función `toggle()` se utiliza para activar todas las marcas de graduación y etiquetas del eje y derecho.

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```
