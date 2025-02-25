# Función para configurar los ejes

Crea una función para configurar los ejes. Esta función establecerá los valores de las marcas en el eje x y en el eje y.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
