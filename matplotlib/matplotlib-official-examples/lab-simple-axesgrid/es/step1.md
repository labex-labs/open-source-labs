# Importar las bibliotecas necesarias y crear matrices de imágenes

Comenzamos importando las bibliotecas necesarias y creando cuatro matrices de imágenes de 10x10 usando las funciones `arange` y `reshape` de la biblioteca NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
