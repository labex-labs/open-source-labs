# Générer des données

Nous commencerons par générer deux blobs 2D dans une grille 2D. Un blob sera positif et l'autre négatif.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

def normal_pdf(x, mean, var):
    return np.exp(-(x - mean)**2 / (2*var))

# Générer l'espace dans lequel les blobs seront situés
xmin, xmax, ymin, ymax = (0, 100, 0, 100)
n_bins = 100
xx = np.linspace(xmin, xmax, n_bins)
yy = np.linspace(ymin, ymax, n_bins)

# Générer les blobs. La plage des valeurs est approximativement de -.0002 à.0002
means_high = [20, 50]
means_low = [50, 60]
var = [150, 200]

gauss_x_high = normal_pdf(xx, means_high[0], var[0])
gauss_y_high = normal_pdf(yy, means_high[1], var[0])

gauss_x_low = normal_pdf(xx, means_low[0], var[1])
gauss_y_low = normal_pdf(yy, means_low[1], var[1])

weights = (np.outer(gauss_y_high, gauss_x_high)
           - np.outer(gauss_y_low, gauss_x_low))

# Nous créerons également un fond gris dans lequel les pixels vont se fondre
greys = np.full((*weights.shape, 3), 70, dtype=np.uint8)
```
