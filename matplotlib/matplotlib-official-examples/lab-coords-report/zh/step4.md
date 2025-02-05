# 格式化图表

为了使我们的图表更具可读性，我们可以使用 Matplotlib 的格式化函数对其进行格式化。在本示例中，我们将格式化 y 轴标签，以百万为单位显示数值。

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```
