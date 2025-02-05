# 定义一个调整轴脊位置的方法

在这一步中，我们将定义一个方法，该方法根据指定的轴脊位置来调整轴脊的位置。

```python
def adjust_spines(ax, spines):
    """
    根据指定的轴脊位置调整轴脊的位置。

    参数：
        ax (Axes)：要调整轴脊的Matplotlib Axes对象。
        spines (字符串列表)：所需的轴脊位置。有效选项为'left'（左）、'right'（右）、'top'（上）、'bottom'（下）。

    返回：
        无
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # 将轴脊向外移动10个点
        else:
            spine.set_color('none')  # 不绘制轴脊

    # 在没有轴脊的地方关闭刻度
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])
```
