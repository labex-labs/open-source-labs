# Grid for Custom Transform

First, we will create a custom grid and tick lines using `GridHelperCurveLinear`. The custom transform will be applied to the grid and tick lines. The following code demonstrates this process:

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
from mpl_toolkits.axisartist import Axes, HostAxes, angle_helper
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear

def curvelinear_test1(fig):
    # Define custom transform
    def tr(x, y):
        return x, y - x
    def inv_tr(x, y):
        return x, y + x

    # Create GridHelperCurveLinear object
    grid_helper = GridHelperCurveLinear((tr, inv_tr))

    # Create a subplot with the custom grid and tick lines
    ax1 = fig.add_subplot(1, 2, 1, axes_class=Axes, grid_helper=grid_helper)

    # Plot some points on the subplot
    xx, yy = tr(np.array([3, 6]), np.array([5, 10]))
    ax1.plot(xx, yy)

    # Set the aspect ratio and limits of the subplot
    ax1.set_aspect(1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    # Add floating axes and grid lines
    ax1.axis["t"] = ax1.new_floating_axis(0, 3)
    ax1.axis["t2"] = ax1.new_floating_axis(1, 7)
    ax1.grid(True, zorder=0)

fig = plt.figure(figsize=(7, 4))
curvelinear_test1(fig)
plt.show()
```
