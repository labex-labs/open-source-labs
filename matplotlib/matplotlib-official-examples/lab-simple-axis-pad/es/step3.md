# Definir la función de eje flotante agregado

Define la función `add_floating_axis`, que agrega un eje flotante a la gráfica. Esta función toma el objeto `ax1` como argumento y devuelve el objeto `axis`.

```python
def add_floating_axis(ax1):
    # Define the floating axis
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```
