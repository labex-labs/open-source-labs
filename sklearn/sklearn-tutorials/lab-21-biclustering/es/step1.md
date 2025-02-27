# Importar las bibliotecas necesarias y el conjunto de datos

Primero, importemos las bibliotecas necesarias y carguemos un conjunto de datos de muestra que usaremos para el biclustering.

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# Cargar datos de muestra
data = np.arange(100).reshape(10, 10)
```
