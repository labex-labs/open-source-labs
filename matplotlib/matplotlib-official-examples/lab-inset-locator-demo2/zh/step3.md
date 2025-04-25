# 创建一个带有尺寸条的放大插入图

在第一个子图中，我们将创建一个带有尺寸条的放大插入图。这将展示如何使用 `.zoomed_inset_axes` 方法来创建一个放大插入图。

```python
# 将绘图的纵横比设置为 1
ax.set_aspect(1)

# 在绘图的右上角创建一个放大插入图
axins = zoomed_inset_axes(ax, zoom=0.5, loc='upper right')

# 设置插入图坐标轴上的刻度数量
axins.yaxis.get_major_locator().set_params(nbins=7)
axins.xaxis.get_major_locator().set_params(nbins=7)

# 隐藏插入图坐标轴上的刻度标签
axins.tick_params(labelleft=False, labelbottom=False)

# 定义一个函数，用于向绘图中添加尺寸条
def add_sizebar(ax, size):
    asb = AnchoredSizeBar(ax.transData,
                          size,
                          str(size),
                          loc=8,
                          pad=0.1, borderpad=0.5, sep=5,
                          frameon=False)
    ax.add_artist(asb)

# 向主图和插入图中添加尺寸条
add_sizebar(ax, 0.5)
add_sizebar(axins, 0.5)
```
