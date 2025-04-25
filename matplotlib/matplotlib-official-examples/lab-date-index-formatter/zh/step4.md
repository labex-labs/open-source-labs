# 使用可调用对象作为格式化器

除了将函数传递给`.Axis.set_major_formatter`，我们还可以使用任何其他可调用对象，例如实现了`__call__`的类的实例。在这一步中，我们将创建一个`MyFormatter`类，它将刻度标记格式化为时间。

```python
# 使用可调用对象作为格式化器
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """返回位置 pos 处时间 x 的标签。"""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```
