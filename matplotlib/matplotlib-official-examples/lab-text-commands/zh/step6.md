# 向图表中添加文本

我们可以使用 `ax.text()` 函数向图表中添加文本。此函数接受三个参数：x 坐标、y 坐标和文本字符串。我们可以使用 `style`、`bbox` 和 `fontsize` 参数来自定义文本样式。

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```
