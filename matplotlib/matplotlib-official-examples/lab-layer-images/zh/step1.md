# 导入必要的库并定义一个函数

导入必要的库，并定义一个函数来创建第一张图像。

```python
import matplotlib.pyplot as plt
import numpy as np

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))
```
