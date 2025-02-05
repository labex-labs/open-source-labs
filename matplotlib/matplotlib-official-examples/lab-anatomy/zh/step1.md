# 导入库并设置数据

首先，我们需要导入必要的库并设置一些要绘制的数据。在这个例子中，我们将绘制三个添加了一些随机噪声的正弦波。

```python
import matplotlib.pyplot as plt
import numpy as np

# 设置数据
np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))
```
