# Importar bibliotecas y crear una figura

El primer paso es importar las bibliotecas necesarias y crear una figura. Usamos el módulo `matplotlib.pyplot` para crear una figura y el módulo `mpl_toolkits.axes_grid1` para hacer espacio para la etiqueta y.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```
