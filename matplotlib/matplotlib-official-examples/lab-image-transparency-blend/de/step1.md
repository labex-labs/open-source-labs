# Daten generieren

Wir beginnen mit der Erzeugung von zwei 2D-Blob's in einem 2D-Gitter. Ein Blob wird positiv und das andere negativ sein.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

def normal_pdf(x, mean, var):
    return np.exp(-(x - mean)**2 / (2*var))

# Generiere den Raum, in dem die Blob's leben werden
xmin, xmax, ymin, ymax = (0, 100, 0, 100)
n_bins = 100
xx = np.linspace(xmin, xmax, n_bins)
yy = np.linspace(ymin, ymax, n_bins)

# Generiere die Blob's. Der Wertebereich liegt grob zwischen -.0002 und.0002
means_high = [20, 50]
means_low = [50, 60]
var = [150, 200]

gauss_x_high = normal_pdf(xx, means_high[0], var[0])
gauss_y_high = normal_pdf(yy, means_high[1], var[0])

gauss_x_low = normal_pdf(xx, means_low[0], var[1])
gauss_y_low = normal_pdf(yy, means_low[1], var[1])

weights = (np.outer(gauss_y_high, gauss_x_high)
           - np.outer(gauss_y_low, gauss_x_low))

# Wir werden auch einen grauen Hintergrund erstellen, in den die Pixel abblenden
greys = np.full((*weights.shape, 3), 70, dtype=np.uint8)
```
