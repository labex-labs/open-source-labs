# Define the `fill` and `plot` Methods

Within the `RadarAxes` class, we will define the `fill` and `plot` methods. These methods will be used to fill the area inside the chart and plot the data points, respectively.

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
