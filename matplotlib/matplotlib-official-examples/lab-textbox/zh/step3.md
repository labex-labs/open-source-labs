# 定义提交函数

我们定义`submit`函数，当用户提交文本输入时将调用此函数。该函数会根据用户输入更新绘制的函数。

```python
def submit(expression):
    """
    将绘制的函数更新为新的数学 *表达式*。

    *表达式* 是一个以 "t" 作为自变量的字符串，例如
    "t ** 3"。
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```
