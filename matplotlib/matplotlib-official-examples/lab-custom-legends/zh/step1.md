# 绘制线条

在这一步中，我们将使用 Matplotlib 库绘制一组线条。首先，我们使用 NumPy 创建一些随机数据。接下来，我们使用 `cycler` 函数设置颜色循环以指定颜色映射。最后，我们使用 `plot` 函数绘制数据，并调用 `legend()` 生成图例。

```python
import matplotlib.pyplot as plt
import numpy as np

# 设置随机种子以确保可重复性
np.random.seed(19680801)

# 创建随机数据
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# 设置颜色循环
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# 绘制数据并生成图例
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```
