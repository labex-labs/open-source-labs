# Importar Bibliotecas e Definir a Função

O primeiro passo é importar as bibliotecas necessárias e definir a função `make_arrow_graph()`. Esta função recebe vários parâmetros, como os eixos, dados, tamanho, exibição, forma, `max_arrow_width`, `arrow_sep`, alfa, `normalize_data`, `ec`, `labelcolor` e `kwargs`. Ela usa esses parâmetros para criar um gráfico de setas.

```python
# Import libraries
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def make_arrow_graph(ax, data, size=4, display='length', shape='right',
                     max_arrow_width=0.03, arrow_sep=0.02, alpha=0.5,
                     normalize_data=False, ec=None, labelcolor=None,
                     **kwargs):
    """
    Makes an arrow plot.

    Parameters
    ----------
    ax
        The axes where the graph is drawn.
    data
        Dict with probabilities for the bases and pair transitions.
    size
        Size of the plot, in inches.
    display : {'length', 'width', 'alpha'}
        The arrow property to change.
    shape : {'full', 'left', 'right'}
        For full or half arrows.
    max_arrow_width : float
        Maximum width of an arrow, in data coordinates.
    arrow_sep : float
        Separation between arrows in a pair, in data coordinates.
    alpha : float
        Maximum opacity of arrows.
    **kwargs
        `.FancyArrow` properties, e.g. *linewidth* or *edgecolor*.
    """

    # code block
```
