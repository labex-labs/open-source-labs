# 完整代码

以下是用Python创建帽形图的完整代码。

```python
import matplotlib.pyplot as plt
import numpy as np


def hat_graph(ax, xlabels, values, group_labels):
    """
    创建一个帽形图。

    参数
    ----------
    ax : matplotlib.axes.Axes
        要绘制图形的坐标轴。
    xlabels : list of str
        要在x轴上显示的类别名称。
    values : (M, N) 类似数组
        数据值。
        行是组 (len(group_labels) == M)。
        列是类别 (len(xlabels) == N)。
    group_labels : list of str
        图例中显示的组标签。
    """

    def label_bars(heights, rects):
        """在每个柱子顶部附加一个文本标签。"""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 4个点的垂直偏移。
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # 帽形组之间的间距
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)


# 初始化标签和一个NumPy数组，确保数组中有
# N个值对应的N个标签
xlabels = ['I', 'II', 'III', 'IV', 'V']
playerA = np.array([5, 15, 22, 20, 25])
playerB = np.array([25, 32, 34, 30, 27])

fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# 添加一些文本用于标签、标题和自定义x轴刻度标签等
ax.set_xlabel('Games')
ax.set_ylabel('Score')
ax.set_ylim(0, 60)
ax.set_title('Scores by number of game and players')
ax.legend()

fig.tight_layout()
plt.show()
```
