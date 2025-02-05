# 绘制基本的功率谱密度图

首先，我们将使用随机数据绘制一个基本的功率谱密度图。我们将创建一个时间序列，添加噪声，然后使用 `matplotlib.mlab` 库中的 `psd` 函数绘制功率谱密度图。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

np.random.seed(19680801)
dt = 0.01
t = np.arange(0, 10, dt)
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]
s = 0.1 * np.sin(2 * np.pi * t) + cnse

fig, (ax0, ax1) = plt.subplots(2, 1)
ax0.plot(t, s)
ax1.psd(s, 512, 1 / dt)

plt.show()
```
