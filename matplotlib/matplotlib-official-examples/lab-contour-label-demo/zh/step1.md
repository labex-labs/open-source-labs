# 定义我们的曲面

我们将首先使用 numpy 和 matplotlib 来定义我们的曲面。这将为我们提供一个可处理的数据集。

```python
import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
