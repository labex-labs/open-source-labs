# Configurar Função de Eixos

Crie uma função para configurar os eixos. Esta função irá definir os valores de marcação (tick values) de x e y.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
