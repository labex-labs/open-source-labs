# Importar las bibliotecas necesarias

En primer lugar, necesitamos importar las bibliotecas necesarias para generar la animación. Usaremos `numpy` para generar números aleatorios, `matplotlib` para trazar gráficos y `FFMpegWriter` para escribir los marcos en un archivo.

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```
