# Definiendo una función auxiliar

Definiremos una función auxiliar `label_axes()` que se utilizará para colocar una etiqueta en el centro de un eje y eliminar las marcas de los ejes.

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5,.5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```
