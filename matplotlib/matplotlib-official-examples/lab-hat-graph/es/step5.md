# Código completo

A continuación se presenta el código completo para crear el gráfico de Sombrero en Python.

```python
import matplotlib.pyplot as plt
import numpy as np


def hat_graph(ax, xlabels, values, group_labels):
    """
    Crea un gráfico de Sombrero.

    Parámetros
    ----------
    ax : matplotlib.axes.Axes
        Los ejes en los que se dibujará.
    xlabels : lista de str
        Los nombres de las categorías que se mostrarán en el eje x.
    values : (M, N) array-like
        Los valores de los datos.
        Las filas son los grupos (len(group_labels) == M).
        Las columnas son las categorías (len(xlabels) == N).
    group_labels : lista de str
        Las etiquetas de los grupos que se mostrarán en la leyenda.
    """

    def label_bars(heights, rects):
        """Adjunta una etiqueta de texto encima de cada barra."""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 4 puntos de desplazamiento vertical.
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # Espaciado entre los grupos de Sombrero
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)


# inicialise labels and a numpy array make sure you have
# N labels of N number of values in the array
xlabels = ['I', 'II', 'III', 'IV', 'V']
playerA = np.array([5, 15, 22, 20, 25])
playerB = np.array([25, 32, 34, 30, 27])

fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Games')
ax.set_ylabel('Score')
ax.set_ylim(0, 60)
ax.set_title('Scores by number of game and players')
ax.legend()

fig.tight_layout()
plt.show()
```
