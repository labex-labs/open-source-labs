# 为图形添加注释

最后，我们将使用`text()`和`Circle()`方法为图形添加注释，以展示各种 Matplotlib 元素的名称。我们还将使用`withStroke()`方法为文本和标记添加白色轮廓，以提高可见性。

```python
# 为图形添加注释
from matplotlib.patches import Circle
from matplotlib.patheffects import withStroke

royal_blue = [0, 20/256, 82/256]

def annotate(x, y, text, code):
    # 圆形标记
    c = Circle((x, y), radius=0.15, clip_on=False, zorder=10, linewidth=2.5,
               edgecolor=royal_blue + [0.6], facecolor='none',
               path_effects=[withStroke(linewidth=7, foreground='white')])
    ax.add_artist(c)

    # 将 path_effects 用作文本的背景
    # 分别绘制 path_effects 和彩色文本，以便 path_effects 不会裁剪其他文本
    for path_effects in [[withStroke(linewidth=7, foreground='white')], []]:
        color = 'white' if path_effects else royal_blue
        ax.text(x, y-0.2, text, zorder=100,
                ha='center', va='top', weight='bold', color=color,
                style='italic', fontfamily='Courier New',
                path_effects=path_effects)

        color = 'white' if path_effects else 'black'
        ax.text(x, y-0.33, code, zorder=100,
                ha='center', va='top', weight='normal', color=color,
                fontfamily='monospace', fontsize='medium',
                path_effects=path_effects)

annotate(3.5, -0.13, "次要刻度标签", "ax.xaxis.set_minor_formatter")
annotate(-0.03, 1.0, "主要刻度", "ax.yaxis.set_major_locator")
annotate(0.00, 3.75, "次要刻度", "ax.yaxis.set_minor_locator")
annotate(-0.15, 3.00, "主要刻度标签", "ax.yaxis.set_major_formatter")
annotate(1.68, -0.39, "x 轴标签", "ax.set_xlabel")
annotate(-0.38, 1.67, "y 轴标签", "ax.set_ylabel")
annotate(1.52, 4.15, "标题", "ax.set_title")
annotate(1.75, 2.80, "线条", "ax.plot")
annotate(2.25, 1.54, "标记", "ax.scatter")
annotate(3.00, 3.00, "网格", "ax.grid")
annotate(3.60, 3.58, "图例", "ax.legend")
annotate(2.5, 0.55, "坐标轴", "fig.subplots")
annotate(4, 4.5, "图形", "plt.figure")
annotate(0.65, 0.01, "x 轴", "ax.xaxis")
annotate(0, 0.36, "y 轴", "ax.yaxis")
annotate(4.0, 0.7, "脊柱", "ax.spines")
```
