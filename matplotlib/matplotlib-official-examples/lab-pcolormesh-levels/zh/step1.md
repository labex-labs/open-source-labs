# 基本的 pcolormesh

我们通常通过定义四边形的边缘和四边形的值来指定一个 pcolormesh。请注意，这里的*x*和*y*在各自的维度上比*Z*都多一个元素。

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # 长度 = 11
y = np.arange(4.5, 11, 1)  # 长度 = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
```
