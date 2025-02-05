# 定义一个更新第二个轴的函数

我们将定义一个闭包函数，注册为回调函数，以便根据第一个轴更新第二个轴。

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Update second axis according to first axis.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```
