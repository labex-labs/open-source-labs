# 带边距绘图

Matplotlib 中的 `margins()` 方法可用于设置绘图的边距，而不是使用 `set_xlim()` 和 `set_ylim()` 方法。在本步骤中，我们将学习如何使用 `margins()` 方法而不是 `set_xlim()` 和 `set_ylim()` 方法对绘图进行放大和缩小。

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

# 创建一个带边距的子图
ax1 = plt.subplot(212)
ax1.margins(0.05) # 默认边距是0.05，值为0表示拟合
ax1.plot(t1, f(t1))

# 创建一个边距放大的子图
ax2 = plt.subplot(221)
ax2.margins(2, 2) # 值>0.0会放大
ax2.plot(t1, f(t1))
ax2.set_title('放大')

# 创建一个边距缩小的子图
ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25) # 值在(-0.5, 0.0)范围内会缩小到中心
ax3.plot(t1, f(t1))
ax3.set_title('缩小')

plt.show()
```
