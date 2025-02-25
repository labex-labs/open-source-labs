# Definir los puntos de datos

Primero, definimos los puntos de datos que usaremos para nuestros gráficos. En este ejemplo, usamos `numpy` para generar un conjunto de valores de x e y para una onda senoidal.

```python
import matplotlib.pyplot as plt
import numpy as np

# define a list of markevery cases to plot
cases = [
    None,
    8,
    (30, 8),
    [16, 24, 32],
    [0, -1],
    slice(100, 200, 3),
    0.1,
    0.4,
    (0.2, 0.4)
]

# data points
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
```
