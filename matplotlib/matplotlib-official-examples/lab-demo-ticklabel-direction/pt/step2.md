# Criar uma função para configurar os eixos

Criaremos uma função para configurar nossos eixos com os rótulos de marcação (tick labels) desejados.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axislines.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
