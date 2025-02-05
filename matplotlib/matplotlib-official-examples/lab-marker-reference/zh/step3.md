# 标记填充样式

实心标记的边缘颜色和填充颜色可以分别指定。此外，`fillstyle` 可以配置为空心、完全填充或在各个方向上半填充。半填充样式使用 `markerfacecoloralt` 作为辅助填充颜色。以下代码演示了如何创建标记填充样式：

```python
fig, ax = plt.subplots()
fig.suptitle('Marker fillstyle', fontsize=14)
fig.subplots_adjust(left=0.4)

filled_marker_style = dict(marker='o', linestyle=':', markersize=15,
                           color='darkgrey',
                           markerfacecolor='tab:blue',
                           markerfacecoloralt='lightsteelblue',
                           markeredgecolor='brown')

for y, fill_style in enumerate(Line2D.fillStyles):
    ax.text(-0.5, y, repr(fill_style), **text_style)
    ax.plot([y] * 3, fillstyle=fill_style, **filled_marker_style)
format_axes(ax)
```
