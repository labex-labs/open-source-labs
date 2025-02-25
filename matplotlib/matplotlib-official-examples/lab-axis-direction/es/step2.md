# Crear una función para configurar los ejes

Crearemos una función llamada `setup_axes` para configurar los ejes de nuestros gráficos. Esta función toma dos parámetros, un objeto `fig` y un objeto `pos`. El objeto `fig` es el objeto de figura sobre el que graficaremos, y el objeto `pos` es la posición del subgráfico dentro de la figura.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```
