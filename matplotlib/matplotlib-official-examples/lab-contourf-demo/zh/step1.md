# 导入库并创建数据

首先，我们需要导入必要的库并创建一些要绘制的数据。

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
origin = 'lower'
delta = 0.025
x = y = np.arange(-3.0, 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
