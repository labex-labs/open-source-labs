# SkewXAxisクラスを定義する

SkewXAxisクラスは、目盛りに2つの別々の区間セットを提供し、カスタム目盛りのインスタンスを作成するために使用されます。

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
