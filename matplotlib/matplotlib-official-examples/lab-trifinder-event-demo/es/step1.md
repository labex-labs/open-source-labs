# Crear un objeto Triangulación

En primer lugar, necesitamos crear un objeto Triangulación. Utilizaremos la clase `Triangulation` de `matplotlib.tri`. En este ejemplo, crearemos un objeto Triangulación con datos aleatorios.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Generar datos aleatorios
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
