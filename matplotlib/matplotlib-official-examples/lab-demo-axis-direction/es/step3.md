# Agregando ejes flotantes

Definiremos dos funciones que agregarán ejes flotantes a nuestra gráfica. La primera función `add_floating_axis1()` agrega un eje flotante a la gráfica con una etiqueta de `theta = 30`. La segunda función `add_floating_axis2()` agrega un eje flotante a la gráfica con una etiqueta de `r = 6`.

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```
