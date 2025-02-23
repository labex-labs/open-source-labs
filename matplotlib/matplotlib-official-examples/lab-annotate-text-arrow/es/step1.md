# Importar bibliotecas y generar datos aleatorios

Primero, necesitamos importar las bibliotecas necesarias y generar algunos datos aleatorios para nuestro diagrama de dispersión.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fijar el estado aleatorio para la reproducibilidad
np.random.seed(19680801)

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_aspect(1)

x1 = -1 + np.random.randn(100)
y1 = -1 + np.random.randn(100)
x2 = 1. + np.random.randn(100)
y2 = 1. + np.random.randn(100)

ax.scatter(x1, y1, color="r")
ax.scatter(x2, y2, color="g")
```
