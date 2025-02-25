# Importando Matplotlib y configurando la gráfica

Primero, necesitamos importar la biblioteca Matplotlib y configurar la gráfica. Crearemos una gráfica vacía con un eje y y un eje x. También configuraremos el eje para que solo muestre la espina inferior, estableceremos las posiciones de las marcas y definiremos la longitud de las marcas.

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

def setup(ax, title):
    """Configura los parámetros comunes para los Ejes en el ejemplo."""
    # solo muestra la espina inferior
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    # define las posiciones de las marcas
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, ax = plt.subplots(figsize=(8, 2))
setup(ax, "Tick Formatters")
```
