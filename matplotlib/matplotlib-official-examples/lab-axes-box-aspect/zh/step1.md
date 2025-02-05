# 与数据无关的正方形坐标轴

无论数据范围如何，我们都将创建一个正方形的坐标轴。

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```
