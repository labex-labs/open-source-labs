# Implementar un estilo de caja personalizado como una función

Los estilos de caja personalizados se pueden implementar como funciones que tomen argumentos que especifiquen una caja rectangular y la cantidad de "mutación", y devuelvan la ruta "mutada". Aquí, implementaremos un estilo de caja personalizado que devuelva una nueva ruta que agrega una forma de "flecha" a la izquierda de la caja.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    Dada la ubicación y el tamaño de la caja, devuelve la ruta de la caja alrededor
    de ella.

    La rotación se maneja automáticamente.

    Parámetros
    ----------
    x0, y0, width, height : float
        Ubicación y tamaño de la caja.
    mutation_size : float
        Escala de referencia de mutación, generalmente el tamaño de fuente del texto.
    """
    # padding
    mypad = 0.3
    pad = mutation_size * mypad
    # width and height with padding added.
    width = width + 2 * pad
    height = height + 2 * pad
    # boundary of the padded box
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # return the new path
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```
