# Definir a Função do Gráfico de Chapéu

Nesta etapa, definiremos uma função que cria o Gráfico de Chapéu. A função recebe os seguintes parâmetros:

- ax: Os Axes (eixos) para plotar.
- xlabels: Os nomes das categorias a serem exibidos no eixo x.
- values: Os valores dos dados. As linhas são os grupos e as colunas são as categorias.
- group_labels: Os rótulos dos grupos exibidos na legenda.

```python
def hat_graph(ax, xlabels, values, group_labels):
    """
    Cria um gráfico de chapéu.

    Parâmetros
    ----------
    ax : matplotlib.axes.Axes
        Os Axes para plotar.
    xlabels : list de str
        Os nomes das categorias a serem exibidos no eixo x.
    values : (M, N) array-like
        Os valores dos dados.
        As linhas são os grupos (len(group_labels) == M).
        As colunas são as categorias (len(xlabels) == N).
    group_labels : list de str
        Os rótulos dos grupos exibidos na legenda.
    """

    def label_bars(heights, rects):
        """Anexa um rótulo de texto no topo de cada barra."""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 4 pontos de deslocamento vertical.
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # espaçamento entre os grupos de chapéus
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)
```
