# Criar uma Função para Configurar os Eixos

Criaremos uma função chamada `setup_axes` para configurar os eixos para nossos gráficos. Esta função recebe dois parâmetros: um objeto `fig` e um objeto `pos`. O objeto `fig` é o objeto figura no qual faremos a plotagem, e o objeto `pos` é a posição do subplot dentro da figura.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```
