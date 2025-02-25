# Importar bibliotecas y generar datos

Primero, necesitamos importar las bibliotecas necesarias y generar algunos datos de ejemplo con los que trabajar. En este ejemplo, usaremos numpy para generar los datos y matplotlib para visualizarlos.

```python
import matplotlib.pyplot as plt
import numpy as np

# datos de ejemplo
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# valores de barras de error variables de ejemplo
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
