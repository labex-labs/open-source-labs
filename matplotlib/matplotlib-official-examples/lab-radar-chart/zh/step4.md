# 定义 `fill` 和 `plot` 方法

在 `RadarAxes` 类中，我们将定义 `fill` 和 `plot` 方法。这些方法将分别用于填充图表内部的区域和绘制数据点。

```python
class RadarAxes(PolarAxes):
    # RadarAxes 类的代码写在这里

    def fill(self, *args, closed=True, **kwargs):
        # 重写 fill 方法
        return super().fill(closed=closed, *args, **kwargs)

    def plot(self, *args, **kwargs):
        # 重写 plot 方法
        lines = super().plot(*args, **kwargs)
        for line in lines:
            self._close_line(line)

    def _close_line(self, line):
        # 用于闭合线条的辅助方法
        x, y = line.get_data()
        if x[0]!= x[-1]:
            x = np.append(x, x[0])
            y = np.append(y, y[0])
            line.set_data(x, y)
```
