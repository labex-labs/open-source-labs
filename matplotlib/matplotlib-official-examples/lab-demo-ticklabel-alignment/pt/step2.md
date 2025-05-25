# Definir uma Função para Configurar os Eixos

Para simplificar o código, podemos definir uma função que recebe um objeto figura e uma posição como entrada, e retorna um objeto eixo com rótulos de marcação (tick labels) personalizados.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8], labels=["short", "loooong"])
    ax.set_xticks([0.2, 0.8], labels=[r"$\frac{1}{2}\pi$", r"$\pi$"])
    return ax
```
