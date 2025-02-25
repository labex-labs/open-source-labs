# Definir la función del gráfico de Sombrero

En este paso, definiremos una función que crea el gráfico de Sombrero. La función toma los siguientes parámetros:

- ax: Los ejes en los que se dibujará.
- xlabels: Los nombres de las categorías que se mostrarán en el eje x.
- values: Los valores de los datos. Las filas son los grupos y las columnas son las categorías.
- group_labels: Las etiquetas de los grupos que se mostrarán en la leyenda.

```python
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
```
