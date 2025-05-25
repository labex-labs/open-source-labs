# Escala das Setas com a Largura do Gráfico, Não com a Visualização

A função `quiver()` pode ser usada para criar um gráfico de vetores (quiver plot). Por padrão, as setas no gráfico serão escaladas com os dados, em vez do próprio gráfico. Isso pode dificultar a visualização de setas que estão próximas da borda do gráfico.

```python
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()
```
