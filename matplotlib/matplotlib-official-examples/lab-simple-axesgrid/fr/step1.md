# Importez les bibliothèques nécessaires et créez des tableaux d'images

Nous commençons par importer les bibliothèques nécessaires et en créant quatre tableaux d'images de 10x10 à l'aide des fonctions `arange` et `reshape` de la bibliothèque NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
