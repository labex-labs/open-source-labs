# 设置图表

首先，我们需要设置一个包含两个子图的图表。我们将使用 `subplots` 函数创建一个 2x2 的子图网格，然后定义两个点的 x 和 y 坐标。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
