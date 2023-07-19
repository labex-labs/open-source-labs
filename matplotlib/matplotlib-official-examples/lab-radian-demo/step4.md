# Plot data in the first subplot

Plot the cosine of the x values in the first subplot using the plot function from matplotlib.pyplot. Use the xunits parameter to specify that the x-axis should be in radians.

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
