# Импортируем необходимые библиотеки и создаем массивы изображений

Начнем с импорта необходимых библиотек и создания четырех массивов изображений размером 10x10 с использованием функций `arange` и `reshape` из библиотеки NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
