# Diagrama de dispersión sin el modo de autolimitación round_numbers

En este paso, crearemos un diagrama de dispersión sin el modo de autolimitación round_numbers y observaremos el comportamiento de la colocación automática de las marcas de graduación.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```
