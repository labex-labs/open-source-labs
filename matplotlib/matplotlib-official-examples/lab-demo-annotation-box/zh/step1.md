# 绘制点

首先，让我们绘制两个稍后要添加注释的点。

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# 定义第一个要注释的位置（用标记显示它）
xy1 = (0.5, 0.7)
ax.plot(xy1[0], xy1[1], ".r")

# 定义第二个要注释的位置（这次不显示标记）
xy2 = [0.3, 0.55]

# 固定显示范围以查看所有内容
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
```
