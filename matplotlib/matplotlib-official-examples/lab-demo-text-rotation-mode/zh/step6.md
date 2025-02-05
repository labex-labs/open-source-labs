# 突出显示文本的边界框

如果 `rotation_mode` 设置为 `'default'`，我们将使用一个矩形来突出显示文本的边界框。我们将使用 `get_window_extent` 函数获取边界框，并使用 `transData` 属性将其转换为数据坐标。

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
