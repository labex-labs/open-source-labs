# Importar as bibliotecas necessárias e criar arrays de imagem

Começamos importando as bibliotecas necessárias e criando quatro arrays de imagem 10x10 usando as funções `arange` e `reshape` da biblioteca NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
