# 导入库并设置图形

第一步，我们将导入必要的库，并为图表设置图形和坐标轴。

```python
import matplotlib.pyplot as plt
import numpy as np

# set up the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
```
