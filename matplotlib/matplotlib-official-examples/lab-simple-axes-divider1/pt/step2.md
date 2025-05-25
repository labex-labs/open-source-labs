# Definindo a Função Auxiliar

Definiremos uma função auxiliar `label_axes()` que será usada para colocar um rótulo no centro de um eixo e remover as marcas de eixo.

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5, .5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```
