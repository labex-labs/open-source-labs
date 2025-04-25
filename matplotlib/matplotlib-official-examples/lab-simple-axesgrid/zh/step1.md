# 导入必要的库并创建图像数组

我们首先导入必要的库，并使用 NumPy 库中的`arange`和`reshape`函数创建四个 10x10 的图像数组。

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
