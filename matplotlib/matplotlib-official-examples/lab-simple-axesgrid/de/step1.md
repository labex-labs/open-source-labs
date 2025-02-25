# Importieren von erforderlichen Bibliotheken und Erstellen von Bildarrays

Wir beginnen, indem wir die erforderlichen Bibliotheken importieren und mit den Funktionen `arange` und `reshape` aus der NumPy-Bibliothek vier 10x10-Bildarrays erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
