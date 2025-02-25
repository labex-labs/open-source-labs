# Importar bibliotecas y obtener estilos de caja

En este paso, importaremos las bibliotecas necesarias y obtendremos los estilos de caja que usaremos para la representación gráfica.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```
