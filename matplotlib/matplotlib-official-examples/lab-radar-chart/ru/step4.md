# Определить методы `fill` и `plot`

Внутри класса `RadarAxes` мы определим методы `fill` и `plot`. Эти методы будут использоваться для заполнения области внутри диаграммы и построения точек данных соответственно.

```python
class RadarAxes(PolarAxes):
    # код для класса RadarAxes будет здесь

    def fill(self, *args, closed=True, **kwargs):
        # переопределение метода fill
        return super().fill(closed=closed, *args, **kwargs)

    def plot(self, *args, **kwargs):
        # переопределение метода plot
        lines = super().plot(*args, **kwargs)
        for line in lines:
            self._close_line(line)

    def _close_line(self, line):
        # вспомогательный метод для закрытия линии
        x, y = line.get_data()
        if x[0]!= x[-1]:
            x = np.append(x, x[0])
            y = np.append(y, y[0])
            line.set_data(x, y)
```
