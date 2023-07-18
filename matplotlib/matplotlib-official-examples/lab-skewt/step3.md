# Define SkewXAxis Class

The SkewXAxis class is used to provide two separate sets of intervals to the tick and create instances of the custom tick.

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
