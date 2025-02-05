# 向极坐标图添加文本

最后，我们将使用 `offset_copy` 和 `matplotlib.pyplot` 中的 `text` 函数向极坐标图添加文本。

```python
# 创建变换
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       y=6, units='dots')

# 向图中添加文本
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)),
             transform=trans_offset,
             horizontalalignment='center',
             verticalalignment='bottom')
```
