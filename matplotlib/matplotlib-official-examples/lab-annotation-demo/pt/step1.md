# Especificando pontos de texto e pontos de anotação

Você deve especificar um ponto de anotação `xy=(x, y)` para anotar este ponto. Adicionalmente, você pode especificar um ponto de texto `xytext=(x, y)` para a localização do texto para esta anotação. Opcionalmente, você pode especificar o sistema de coordenadas de `xy` e `xytext` com uma das seguintes strings para `xycoords` e `textcoords` (o padrão é 'data'):

- 'figure points' (pontos da figura): pontos a partir do canto inferior esquerdo da figura
- 'figure pixels' (pixels da figura): pixels a partir do canto inferior esquerdo da figura
- 'figure fraction' (fração da figura): (0, 0) é o canto inferior esquerdo da figura e (1, 1) é o canto superior direito
- 'axes points' (pontos dos eixos): pontos a partir do canto inferior esquerdo dos eixos
- 'axes pixels' (pixels dos eixos): pixels a partir do canto inferior esquerdo dos eixos
- 'axes fraction' (fração dos eixos): (0, 0) é o canto inferior esquerdo dos eixos e (1, 1) é o canto superior direito
- 'offset points' (pontos de deslocamento): especifica um deslocamento (em pontos) do valor xy
- 'offset pixels' (pixels de deslocamento): especifica um deslocamento (em pixels) do valor xy
- 'data' (dados): usa o sistema de coordenadas de dados dos eixos

Observação: para sistemas de coordenadas físicas (pontos ou pixels), a origem é a (inferior, esquerda) da figura ou dos eixos.

Opcionalmente, você pode especificar propriedades da seta, que desenha uma seta do texto para o ponto anotado, fornecendo um dicionário de propriedades da seta. As chaves válidas são:

- `width` (largura): a largura da seta em pontos
- `frac`: a fração do comprimento da seta ocupada pela cabeça
- `headwidth` (largura da cabeça): a largura da base da cabeça da seta em pontos
- `shrink` (encolher): move a ponta e a base alguns por cento para longe do ponto anotado e do texto
- `any key for matplotlib.patches.polygon` (qualquer chave para matplotlib.patches.polygon) (por exemplo, facecolor)

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# Create our figure and data we'll use for plotting
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Plot a line and add some simple annotations
line, = ax.plot(t, s)
ax.annotate('figure pixels',
            xy=(10, 10), xycoords='figure pixels')
ax.annotate('figure points',
            xy=(107, 110), xycoords='figure points',
            fontsize=12)
ax.annotate('figure fraction',
            xy=(.025, .975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# The following examples show off how these arrows are drawn.

ax.annotate('point offset from data',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('axes fraction',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# You may also use negative points or pixels to specify from (right, top).
# E.g., (-10, 10) is 10 points to the left of the right side of the axes and 10
# points above the bottom

ax.annotate('pixel offset from axes fraction',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 20), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```
