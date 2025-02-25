# Graficando Puntos

Para comenzar, graficaremos dos puntos que anotaremos más adelante.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Define una 1ª posición para anotar (muéstrala con un marcador)
xy1 = (0.5, 0.7)
ax.plot(xy1[0], xy1[1], ".r")

# Define una 2ª posición para anotar (esta vez no la muestre con un marcador)
xy2 = [0.3, 0.55]

# Fije los límites de visualización para ver todo
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
```
