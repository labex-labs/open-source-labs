# Importar las bibliotecas necesarias y fijar el estado aleatorio

Primero, necesitamos importar las bibliotecas necesarias y fijar el estado aleatorio para la reproducibilidad. Usaremos `numpy` para generar algunos datos aleatorios, `matplotlib.pyplot` para crear visualizaciones y `cm` de `matplotlib` para definir las mapas de color.

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```
