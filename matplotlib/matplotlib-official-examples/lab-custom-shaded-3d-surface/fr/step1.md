# Charger et formater les données

Dans cette étape, nous allons charger et formater les données pour le tracé de surface 3D. Nous utiliserons un ensemble de données d'échantillonnage appelé "jacksboro_fault_dem.npz".

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

# Charger et formater les données
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
nrows, ncols = z.shape
x = np.linspace(dem['xmin'], dem['xmax'], ncols)
y = np.linspace(dem['ymin'], dem['ymax'], nrows)
x, y = np.meshgrid(x, y)

region = np.s_[5:50, 5:50]
x, y, z = x[region], y[region], z[region]
```
