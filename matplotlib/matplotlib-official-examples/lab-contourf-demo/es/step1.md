# Importar bibliotecas y crear datos

Primero, necesitamos importar las bibliotecas necesarias y crear algunos datos para graficar.

```python
import matplotlib.pyplot as plt
import numpy as np

# Crear datos
origen = 'lower'
delta = 0.025
x = y = np.arange(-3.0, 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
