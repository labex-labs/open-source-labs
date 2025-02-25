# Определяем класс SkewXAxis

Класс SkewXAxis используется для предоставления двух отдельных наборов интервалов делениям и создания экземпляров пользовательских делений.

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
