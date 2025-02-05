# 为特定线条创建图例

在这一步中，我们将为特定线条创建一个图例。

```python
# 导入必要的库
import matplotlib.pyplot as plt
import numpy as np

# 定义图表数据
t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)

# 创建一个包含多条线的绘图
fig, ax = plt.subplots()
l1, = ax.plot(t2, np.exp(-t2))
l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2),'s-.')

# 为其中两条线创建一个图例
ax.legend((l2, l4), ('oscillatory', 'damped'), loc='upper right', shadow=True)

# 为图表添加标签和标题
ax.set_xlabel('time')
ax.set_ylabel('volts')
ax.set_title('Damped oscillation')

# 显示图表
plt.show()
```
