# 定义 SkewXAxis 类

SkewXAxis 类用于为刻度提供两组独立的区间，并创建自定义刻度的实例。

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
