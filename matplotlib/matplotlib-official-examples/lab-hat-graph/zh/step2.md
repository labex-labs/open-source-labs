# 定义帽形图函数

在这一步中，我们将定义一个创建帽形图的函数。该函数接受以下参数：

- ax：要绘制图形的坐标轴。
- xlabels：要在 x 轴上显示的类别名称。
- values：数据值。行是组，列是类别。
- group_labels：图例中显示的组标签。

```python
def hat_graph(ax, xlabels, values, group_labels):
    """
    创建一个帽形图。

    参数
    ----------
    ax : matplotlib.axes.Axes
        要绘制图形的坐标轴。
    xlabels : list of str
        要在 x 轴上显示的类别名称。
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
                        xytext=(0, 4),  # 4 个点的垂直偏移。
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
```
