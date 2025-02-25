# Daten laden und formatieren

In diesem Schritt laden und formatieren wir die Daten für den 3D-Oberflächenplot. Wir verwenden einen Beispiel-Datensatz namens "jacksboro_fault_dem.npz".

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

# Daten laden und formatieren
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
nrows, ncols = z.shape
x = np.linspace(dem['xmin'], dem['xmax'], ncols)
y = np.linspace(dem['ymin'], dem['ymax'], nrows)
x, y = np.meshgrid(x, y)

Region = np.s_[5:50, 5:50]
x, y, z = x[region], y[region], z[region]
```
