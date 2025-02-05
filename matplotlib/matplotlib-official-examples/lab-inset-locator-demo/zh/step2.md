# 创建内嵌轴

接下来，我们将在每个子图中创建内嵌轴。我们将使用 `inset_axes()` 方法来创建内嵌轴。我们将创建四个大小和位置不同的内嵌图。

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# 创建宽度为1.3英寸、高度为0.9英寸的内嵌图
# 位于默认的右上角位置
axins = inset_axes(ax, width=1.3, height=0.9)

# 创建宽度为父轴边界框的30%、高度为40%的内嵌图
# 位于左下角（loc=3）
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# 在第二个子图中创建混合规格的内嵌图；
# 宽度为父轴边界框的30%，
# 高度为1英寸，位于左上角（loc=2）
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# 在右下角（loc=4）创建一个内嵌图，边框填充为1，即
# 相对于父轴有10个点的填充（因为默认字体大小是10pt）
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```
