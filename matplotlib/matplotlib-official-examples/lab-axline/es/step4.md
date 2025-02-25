# Dibujar líneas diagonales

Podemos usar `axline` con el parámetro `transform` para dibujar líneas diagonales con una pendiente fija. Vamos a dibujar líneas de cuadrícula diagonales con una pendiente fija de `0.5`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Draw diagonal lines
for pos in np.linspace(-2, 1, 10):
    plt.axline((pos, 0), slope=0.5, color='k', transform=plt.gca().transAxes)

plt.ylim([0, 1])
plt.xlim([0, 1])
plt.show()
```
