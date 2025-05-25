# Importar as bibliotecas necessárias e configurar o gráfico

Primeiramente, precisamos importar as bibliotecas necessárias e configurar o gráfico. Usaremos `matplotlib.pyplot` e `numpy`. Também criaremos uma figura e um objeto de eixo para plotar nossos dados.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots()
ax.set(xlim=(0, 6), ylim=(-1, 5))
ax.set_title("Orientação das setas de colchete em relação a angleA e angleB")
```
