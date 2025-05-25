# Implementar um estilo de caixa personalizado como uma função

Estilos de caixa personalizados podem ser implementados como funções que recebem argumentos especificando tanto uma caixa retangular quanto a quantidade de "mutação" (mutation), e retornam o caminho "mutado" (mutated). Aqui, implementaremos um estilo de caixa personalizado que retorna um novo caminho que adiciona uma forma de "seta" (arrow) no lado esquerdo da caixa.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    Dada a localização e o tamanho da caixa, retorna o caminho da caixa ao redor
    dela.

    A rotação é automaticamente tratada.

    Parâmetros
    ----------
    x0, y0, width, height : float
        Localização e tamanho da caixa.
    mutation_size : float
        Escala de referência da mutação, tipicamente o tamanho da fonte do texto.
    """
    # padding
    mypad = 0.3
    pad = mutation_size * mypad
    # largura e altura com padding adicionado.
    width = width + 2 * pad
    height = height + 2 * pad
    # limite da caixa com padding
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # retorna o novo caminho
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```
