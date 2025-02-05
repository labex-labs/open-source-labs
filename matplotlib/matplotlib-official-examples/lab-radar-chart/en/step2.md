# Define the Radar Chart Function

Next, we will define a function to create a radar chart. This function will take two arguments: `num_vars` and `frame`. `num_vars` is the number of variables for the radar chart, and `frame` specifies the shape of the frame surrounding the axes.

```python
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    # code for the function goes here
```
