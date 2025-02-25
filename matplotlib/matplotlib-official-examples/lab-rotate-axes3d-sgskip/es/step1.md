# Importar bibliotecas y conjunto de datos

En primer lugar, necesitamos importar las bibliotecas y el conjunto de datos necesarios. En este ejemplo, usaremos las bibliotecas `matplotlib` y `mpl_toolkits.mplot3d` para crear la trama 3D, y la función `axes3d.get_test_data()` para generar un conjunto de datos de muestra.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```
