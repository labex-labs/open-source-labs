# Define the Polar Axes

In this step, we will define the polar axes and set the scaling factor. We will use `PolarAxes.PolarTransform()` to define the polar axes.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Define the polar axes
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
