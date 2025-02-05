# Create Data for the Bar Graph

In this step, we need to create data for the bar graph. We will use the numpy library to create an array of values that we will use for the bar graph.

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
