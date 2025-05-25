# `fill` 및 `plot` 메서드 정의

`RadarAxes` 클래스 내에서 `fill` 및 `plot` 메서드를 정의합니다. 이 메서드는 각각 차트 내부 영역을 채우고 데이터 포인트를 플롯하는 데 사용됩니다.

```python
class RadarAxes(PolarAxes):
    # code for the RadarAxes class goes here

    def fill(self, *args, closed=True, **kwargs):
        # override the fill method
        return super().fill(closed=closed, *args, **kwargs)

    def plot(self, *args, **kwargs):
        # override the plot method
        lines = super().plot(*args, **kwargs)
        for line in lines:
            self._close_line(line)

    def _close_line(self, line):
        # helper method to close the line
        x, y = line.get_data()
        if x[0] != x[-1]:
            x = np.append(x, x[0])
            y = np.append(y, y[0])
            line.set_data(x, y)
```
