# 导入库并定义图像

第一步，我们导入必要的库并定义示例中要使用的图像。该图像是两个高斯函数的组合。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms

def get_image():
    delta = 0.25
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2)
    return Z
```
