# Defining the class

We will define a class `DataDisplayDownsampler` that will downsample the data and recompute when zoomed. The constructor of the class will take the xdata and ydata as input parameters. We will set the maximum number of points to 50 and calculate the delta of xdata.

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
