# Crear una función para configurar los ejes

Vamos a crear una función para configurar nuestros ejes con las etiquetas de los ejes deseadas.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axislines.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
