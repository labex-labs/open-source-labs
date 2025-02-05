# 添加注释

最后一步是给图表添加注释。我们将使用 `ax.annotate` 方法在图表上添加文本和箭头。我们还将使用 `bbox` 和 `arrowprops` 参数来设置注释的样式。

```python
bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(
    arrowstyle="->",
    connectionstyle="angle,angleA=0,angleB=90,rad=10")

offset = 72
ax.annotate(
    f'data = ({xdata:.1f}, {ydata:.1f})',
    (xdata, ydata),
    xytext=(-2*offset, offset), textcoords='offset points',
    bbox=bbox, arrowprops=arrowprops)
ax.annotate(
    f'display = ({xdisplay:.1f}, {ydisplay:.1f})',
    xy=(xdisplay, ydisplay), xycoords='figure pixels',
    xytext=(0.5*offset, -offset), textcoords='offset points',
    bbox=bbox, arrowprops=arrowprops)
```
