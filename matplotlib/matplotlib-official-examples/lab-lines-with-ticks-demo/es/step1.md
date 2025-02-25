# Importar bibliotecas y generar datos

Primero importaremos las bibliotecas necesarias y generaremos algunos datos para la representación gráfica.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

# Generate data
nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
```
