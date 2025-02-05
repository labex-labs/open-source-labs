# 创建阻尼和无阻尼振荡图

首先，我们将创建一个包含两个子图的图形，一个用于绘制阻尼振荡，另一个用于绘制无阻尼振荡。我们将使用 `np.linspace()` 函数创建一个时间值数组，然后使用 `np.cos()` 和 `np.exp()` 函数绘制每种振荡类型对应的振幅值。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('damped')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('time (s)')
ax2.set_title('undamped')

fig.suptitle('Different types of oscillations', fontsize=16)

plt.show()
```
