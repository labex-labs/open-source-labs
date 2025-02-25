# Definir una función para configurar los ejes

Para simplificar el código, podemos definir una función que tome un objeto de figura y una posición como entrada, y devuelva un objeto de eje con etiquetas de marcas personalizadas.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8], labels=["short", "loooong"])
    ax.set_xticks([0.2, 0.8], labels=[r"$\frac{1}{2}\pi$", r"$\pi$"])
    return ax
```
