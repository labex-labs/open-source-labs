# 中心坐标

通常，用户希望将与*Z*大小相同的*X*和*Y*传递给`.axes.Axes.pcolormesh`。如果传递了`shading='auto'`（由:rc:`pcolor.shading`设置的默认值），这也是允许的。在 Matplotlib 3.3 之前，`shading='flat'`会丢弃*Z*的最后一列和最后一行，但现在会报错。如果这确实是你想要的，那么只需手动丢弃*Z*的最后一行和最后一列：

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(10)  # 长度 = 10
y = np.arange(6)  # 长度 = 6
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z),
                  shading='flat')
axs[1].set_title("shading='flat'")
```
