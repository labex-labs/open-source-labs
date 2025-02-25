# Importar las bibliotecas y datos necesarios

En primer lugar, necesitamos importar las bibliotecas y datos necesarios para crear nuestra cuadrícula. Usaremos `matplotlib.pyplot` para la representación gráfica, `cbook` para obtener un conjunto de datos de muestra y `ImageGrid` para crear nuestra cuadrícula.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Obtener datos de muestra
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # Matriz 15x15
extent = (-3, 4, -4, 3)
```
