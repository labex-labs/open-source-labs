# Specifying text points and annotation points

You must specify an annotation point `xy=(x, y)` to annotate this point. Additionally, you may specify a text point `xytext=(x, y)` for the location of the text for this annotation. Optionally, you can specify the coordinate system of `xy` and `xytext` with one of the following strings for `xycoords` and `textcoords` (default is 'data'):

- 'figure points' : points from the lower left corner of the figure
- 'figure pixels' : pixels from the lower left corner of the figure
- 'figure fraction' : (0, 0) is lower left of figure and (1, 1) is upper right
- 'axes points' : points from lower left corner of axes
- 'axes pixels' : pixels from lower left corner of axes
- 'axes fraction' : (0, 0) is lower left of axes and (1, 1) is upper right
- 'offset points' : Specify an offset (in points) from the xy value
- 'offset pixels' : Specify an offset (in pixels) from the xy value
- 'data' : use the axes data coordinate system

Note: for physical coordinate systems (points or pixels) the origin is the (bottom, left) of the figure or axes.

Optionally, you can specify arrow properties which draws and arrow from the text to the annotated point by giving a dictionary of arrow properties. Valid keys are:

- `width`: the width of the arrow in points
- `frac`: the fraction of the arrow length occupied by the head
- `headwidth`: the width of the base of the arrow head in points
- `shrink`: move the tip and base some percent away from the annotated point and text
- `any key for matplotlib.patches.polygon` (e.g., facecolor)

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# Create our figure and data we'll use for plotting
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Plot a line and add some simple annotations
line, = ax.plot(t, s)
ax.annotate('figure pixels',
            xy=(10, 10), xycoords='figure pixels')
ax.annotate('figure points',
            xy=(107, 110), xycoords='figure points',
            fontsize=12)
ax.annotate('figure fraction',
            xy=(.025, .975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# The following examples show off how these arrows are drawn.

ax.annotate('point offset from data',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('axes fraction',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# You may also use negative points or pixels to specify from (right, top).
# E.g., (-10, 10) is 10 points to the left of the right side of the axes and 10
# points above the bottom

ax.annotate('pixel offset from axes fraction',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 20), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```
