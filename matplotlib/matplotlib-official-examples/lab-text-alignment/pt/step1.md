# Criando um Retângulo

Começaremos criando um retângulo no gráfico usando a função `Rectangle()` do módulo `matplotlib.patches`. Após criar o retângulo, definiremos seus limites horizontal e vertical usando as funções `set_xlim()` e `set_ylim()`. Finalmente, adicionaremos o retângulo ao gráfico.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Build a rectangle in axes coords
left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Set the horizontal and vertical limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
