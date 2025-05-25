# Código Completo

Aqui está o código completo para criar o Gráfico de Chapéu em Python.

```python
import matplotlib.pyplot as plt
import numpy as np


def hat_graph(ax, xlabels, values, group_labels):
    """
    Cria um gráfico de chapéu.

    Parâmetros
    ----------
    ax : matplotlib.axes.Axes
        Os Axes para plotar.
    xlabels : lista de str
        Os nomes das categorias a serem exibidos no eixo x.
    values : (M, N) array-like
        Os valores dos dados.
        As linhas são os grupos (len(group_labels) == M).
        As colunas são as categorias (len(xlabels) == N).
    group_labels : lista de str
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
    spacing = 0.3  # espaçamento entre os grupos de chapéu
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)


# inicializar rótulos e um array numpy, certifique-se de ter
# N rótulos com N números de valores no array
xlabels = ['I', 'II', 'III', 'IV', 'V']
playerA = np.array([5, 15, 22, 20, 25])
playerB = np.array([25, 32, 34, 30, 27])

fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# Adicionar algum texto para rótulos, título e rótulos personalizados do eixo x, etc.
ax.set_xlabel('Jogos')
ax.set_ylabel('Pontuação')
ax.set_ylim(0, 60)
ax.set_title('Pontuações por número de jogo e jogadores')
ax.legend()

fig.tight_layout()
plt.show()
```
