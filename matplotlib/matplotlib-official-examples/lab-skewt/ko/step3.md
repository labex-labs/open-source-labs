# SkewXAxis 클래스 정의

SkewXAxis 클래스는 눈금에 두 개의 개별 간격을 제공하고 사용자 정의 눈금의 인스턴스를 생성하는 데 사용됩니다.

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
