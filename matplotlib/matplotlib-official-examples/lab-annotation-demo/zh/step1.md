# 指定文本点和注释点

你必须指定一个注释点 `xy=(x, y)` 来注释该点。此外，你可以为该注释的文本位置指定一个文本点 `xytext=(x, y)`。或者，你可以使用以下字符串之一为 `xycoords` 和 `textcoords` 指定 `xy` 和 `xytext` 的坐标系（默认为 'data'）：

- 'figure points'：从图形左下角开始的点
- 'figure pixels'：从图形左下角开始的像素
- 'figure fraction'：(0, 0) 是图形的左下角，(1, 1) 是右上角
- 'axes points'：从坐标轴左下角开始的点
- 'axes pixels'：从坐标轴左下角开始的像素
- 'axes fraction'：(0, 0) 是坐标轴的左下角，(1, 1) 是右上角
- 'offset points'：指定相对于 `xy` 值的偏移量（以点为单位）
- 'offset pixels'：指定相对于 `xy` 值的偏移量（以像素为单位）
- 'data'：使用坐标轴数据坐标系

注意：对于物理坐标系（点或像素），原点是图形或坐标轴的（底部，左侧）。

或者，你可以通过提供一个箭头属性字典来指定从文本到注释点绘制箭头的箭头属性。有效的键包括：

- `width`：箭头的宽度（以点为单位）
- `frac`：箭头头部占箭头长度的比例
- `headwidth`：箭头头部底部的宽度（以点为单位）
- `shrink`：将箭头的尖端和底部从注释点和文本处移开一定百分比
- `matplotlib.patches.polygon` 的任何键（例如，facecolor）

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# 创建我们的图形和用于绘图的数据
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# 绘制一条线并添加一些简单的注释
line, = ax.plot(t, s)
ax.annotate('figure pixels',
            xy=(10, 10), xycoords='figure pixels')
ax.annotate('figure points',
            xy=(107, 110), xycoords='figure points',
            fontsize=12)
ax.annotate('figure fraction',
            xy=(.025,.975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# 以下示例展示了这些箭头的绘制方式。

ax.annotate('point offset from data',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('axes fraction',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# 你也可以使用负的点或像素来从（右侧，顶部）指定。
# 例如，(-10, 10) 是坐标轴右侧向左 10 个点且底部向上 10 个点的位置

ax.annotate('pixel offset from axes fraction',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 20), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```
