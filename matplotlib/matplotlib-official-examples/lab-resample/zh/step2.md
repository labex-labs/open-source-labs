# 定义类

我们将定义一个名为 `DataDisplayDownsampler` 的类，该类将对数据进行下采样，并在缩放时重新计算。该类的构造函数将把 xdata 和 ydata 作为输入参数。我们将把最大点数设置为 50，并计算 xdata 的差值。

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
