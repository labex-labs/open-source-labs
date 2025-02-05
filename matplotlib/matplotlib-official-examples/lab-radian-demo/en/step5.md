# Plot data in the second subplot

Plot the cosine of the x values in the second subplot using the plot function from matplotlib.pyplot. Use the xunits parameter to specify that the x-axis should be in degrees.

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
