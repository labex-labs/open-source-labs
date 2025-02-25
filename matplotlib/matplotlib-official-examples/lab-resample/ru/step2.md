# Определение класса

Мы определим класс `DataDisplayDownsampler`, который будет уменьшать частоту дискретизации данных и пересчитывать их при приближении. Конструктор класса будет принимать xdata и ydata в качестве входных параметров. Мы установим максимальное количество точек равным 50 и вычислим разницу между начальным и конечным значением xdata.

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
