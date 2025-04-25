# 基本的な pcolormesh

通常、四角形の辺と四角形の値を定義することで pcolormesh を指定します。ここでは、それぞれの次元において、*x*と*y*は Z よりも 1 要素多いことに注意してください。

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
```
