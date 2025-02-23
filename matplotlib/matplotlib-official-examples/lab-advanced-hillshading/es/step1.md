# Mostrar una barra de colores para un gráfico sombreado

En este paso, aprenderás a mostrar una barra de colores numérica correcta para un gráfico sombreado.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import LightSource, Normalize

def display_colorbar():
    """Mostrar una barra de colores numérica correcta para un gráfico sombreado."""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z = 10 * np.cos(x**2 + y**2)

    cmap = plt.cm.copper
    ls = LightSource(315, 45)
    rgb = ls.shade(z, cmap)

    fig, ax = plt.subplots()
    ax.imshow(rgb, interpolation='bilinear')

    # Usar un artista proxy para la barra de colores...
    im = ax.imshow(z, cmap=cmap)
    im.remove()
    fig.colorbar(im, ax=ax)

    ax.set_title('Using a colorbar with a shaded plot', size='x-large')
```
