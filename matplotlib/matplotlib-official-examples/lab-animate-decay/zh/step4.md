# 定义初始化函数

我们需要定义一个初始化函数，用于设置绘图的初始状态。在这个函数中，我们将设置 y 轴的范围，并清除线条对象中的数据。

```python
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
```
