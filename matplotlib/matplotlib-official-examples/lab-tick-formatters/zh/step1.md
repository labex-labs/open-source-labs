# 导入 Matplotlib 并设置绘图

首先，我们需要导入 Matplotlib 库并设置绘图。我们将创建一个带有一个 y 轴和一个 x 轴的空绘图。我们还将配置坐标轴，使其仅显示底部的脊柱线，设置刻度位置，并定义刻度长度。

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    # only show the bottom spine
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    # define tick positions
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, ax = plt.subplots(figsize=(8, 2))
setup(ax, "Tick Formatters")
```

# 示例中的坐标轴通用参数设置

1. **仅显示底部脊柱线**：将 y 轴的主定位器设置为 NullLocator，隐藏左、右、上脊柱线。
2. **定义刻度位置**：
   - x 轴的主定位器设置为 MultipleLocator(1.00)，表示主刻度间隔为 1。
   - x 轴的次定位器设置为 MultipleLocator(0.25)，表示次刻度间隔为 0.25。
   - 将 x 轴的刻度位置设置在底部。
   - 设置主刻度的宽度为 1.00，长度为 5；次刻度的宽度为 0.75，长度为 2.5，标签大小为 10。
3. **设置坐标轴范围**：x 轴范围为 0 到 5，y 轴范围为 0 到 1。
4. **添加标题**：在坐标 (0.0, 0.2) 处添加标题，使用 ax.transAxes 进行坐标转换，字体大小为 14，字体为 'Monospace'，颜色为 'tab:blue'。

创建一个大小为 (8, 2) 的图形和坐标轴，并调用 setup 函数设置标题为 "Tick Formatters"。
