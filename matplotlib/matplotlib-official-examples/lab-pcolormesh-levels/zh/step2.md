# 非矩形的pcolormesh

请注意，我们也可以为*X*和*Y*指定矩阵，从而得到非矩形的四边形。

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # 长度 = 11
y = np.arange(4.5, 11, 1)  # 长度 = 7
X, Y = np.meshgrid(x, y)
X = X + 0.2 * Y  # 倾斜坐标。
Y = Y + 0.3 * X

fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z)
```
