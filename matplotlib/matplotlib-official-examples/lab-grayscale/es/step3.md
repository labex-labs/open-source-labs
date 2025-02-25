# Definiendo la función de ejemplo del ciclo de colores

Definimos la función `color_cycle_example` que toma un objeto de eje como entrada y traza una onda sinusoidal para cada color en el ciclo de colores. El ciclo de colores está definido por los rcParams.

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
