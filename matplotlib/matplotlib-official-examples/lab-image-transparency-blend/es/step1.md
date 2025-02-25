# Generar datos

Comenzaremos generando dos manchas bidimensionales en una cuadrícula 2D. Una mancha será positiva y la otra negativa.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

def normal_pdf(x, mean, var):
    return np.exp(-(x - mean)**2 / (2*var))

# Generar el espacio en el que vivirán las manchas
xmin, xmax, ymin, ymax = (0, 100, 0, 100)
n_bins = 100
xx = np.linspace(xmin, xmax, n_bins)
yy = np.linspace(ymin, ymax, n_bins)

# Generar las manchas. El rango de los valores es aproximadamente de -.0002 a.0002
means_high = [20, 50]
means_low = [50, 60]
var = [150, 200]

gauss_x_high = normal_pdf(xx, means_high[0], var[0])
gauss_y_high = normal_pdf(yy, means_high[1], var[0])

gauss_x_low = normal_pdf(xx, means_low[0], var[1])
gauss_y_low = normal_pdf(yy, means_low[1], var[1])

weights = (np.outer(gauss_y_high, gauss_x_high)
           - np.outer(gauss_y_low, gauss_x_low))

# También crearemos un fondo gris en el que los píxeles se desvanecerán
greys = np.full((*weights.shape, 3), 70, dtype=np.uint8)
```
