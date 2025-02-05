# 向散点图添加文本

现在我们将使用 `offset_copy` 向散点图添加文本。我们首先创建一个变换，该变换将文本相对于以任何坐标给出的位置，在屏幕坐标中的指定偏移量处定位。然后，我们将使用 `matplotlib.pyplot` 中的 `text` 函数将文本添加到图中。

```python
# 创建变换
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# 向图中添加文本
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
