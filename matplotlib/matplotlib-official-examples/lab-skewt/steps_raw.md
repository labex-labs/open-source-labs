# SkewT-logP Diagram using Matplotlib

## Introduction

In this lab, we will learn how to create a SkewT-logP diagram using Matplotlib library in Python. A SkewT-logP diagram is commonly used in meteorology for displaying vertical profiles of temperature. It is a complex plot as it involves non-orthogonal X and Y axes. We will use the Matplotlib's transforms and custom projection API to create this plot.

## Steps

### Step 1: Import Required Libraries

We will start by importing the required libraries. We will be using Matplotlib, NumPy and StringIO for this example.

```python
from contextlib import ExitStack
from matplotlib.axes import Axes
import matplotlib.axis as maxis
from matplotlib.projections import register_projection
import matplotlib.spines as mspines
import matplotlib.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from matplotlib.ticker import (MultipleLocator, NullFormatter, ScalarFormatter)
```

### Step 2: Define SkewXTick Class

The SkewXTick class is used to draw the ticks on the SkewT-logP diagram. It checks if the tick needs to be drawn on the upper or lower X-axis and accordingly sets the visibility of the tick and gridline.

```python
class SkewXTick(maxis.XTick):
    def draw(self, renderer):
        with ExitStack() as stack:
            for artist in [self.gridline, self.tick1line, self.tick2line, self.label1, self.label2]:
                stack.callback(artist.set_visible, artist.get_visible())
            needs_lower = transforms.interval_contains(self.axes.lower_xlim, self.get_loc())
            needs_upper = transforms.interval_contains(self.axes.upper_xlim, self.get_loc())
            self.tick1line.set_visible(self.tick1line.get_visible() and needs_lower)
            self.label1.set_visible(self.label1.get_visible() and needs_lower)
            self.tick2line.set_visible(self.tick2line.get_visible() and needs_upper)
            self.label2.set_visible(self.label2.get_visible() and needs_upper)
            super().draw(renderer)

    def get_view_interval(self):
        return self.axes.xaxis.get_view_interval()
```

### Step 3: Define SkewXAxis Class

The SkewXAxis class is used to provide two separate sets of intervals to the tick and create instances of the custom tick.

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```

### Step 4: Define SkewSpine Class

The SkewSpine class calculates the separate data range of the upper X-axis and draws the spine there. It also provides this range to the X-axis artist for ticking and gridlines.

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```

### Step 5: Define SkewXAxes Class

The SkewXAxes class handles the registration of the skew-xaxes as a projection as well as setting up the appropriate transformations. It overrides standard spines and axes instances as appropriate.

```python
class SkewXAxes(Axes):
    name = 'skewx'

    def _init_axis(self):
        super()._init_axis()
        self.xaxis = SkewXAxis(self)
        self.spines.top.register_axis(self.xaxis)
        self.spines.bottom.register_axis(self.xaxis)

    def _gen_axes_spines(self):
        spines = {'top': SkewSpine.linear_spine(self, 'top'),
                  'bottom': mspines.Spine.linear_spine(self, 'bottom'),
                  'left': mspines.Spine.linear_spine(self, 'left'),
                  'right': mspines.Spine.linear_spine(self, 'right')}
        return spines

    def _set_lim_and_transforms(self):
        super()._set_lim_and_transforms()
        rot = 30
        self.transDataToAxes = (self.transScale + self.transLimits + transforms.Affine2D().skew_deg(rot, 0))
        self.transData = self.transDataToAxes + self.transAxes
        self._xaxis_transform = (transforms.blended_transform_factory(
            self.transScale + self.transLimits, transforms.IdentityTransform()) + transforms.Affine2D().skew_deg(rot, 0) + self.transAxes)

    @property
    def lower_xlim(self):
        return self.axes.viewLim.intervalx

    @property
    def upper_xlim(self):
        pts = [[0., 1.], [1., 1.]]
        return self.transDataToAxes.inverted().transform(pts)[:, 0]
```

### Step 6: Register Projection

We will register the projection with Matplotlib so that we can use it in our plot.

```python
register_projection(SkewXAxes)
```

### Step 7: Prepare Data

We will prepare the data for our SkewT-logP diagram. We will use the StringIO module to read the data from a string and NumPy to load it into arrays.

```python
data_txt = '''
        978.0    345    7.8    0.8
        971.0    404    7.2    0.2
        946.7    610    5.2   -1.8
        ...
    '''
sound_data = StringIO(data_txt)
p, h, T, Td = np.loadtxt(sound_data, unpack=True)
```

### Step 8: Create SkewT-logP Diagram

We will now create the SkewT-logP diagram using the SkewXAxes projection that we registered earlier. We will first create a figure object and add a subplot with the SkewXAxes projection. We will then plot the temperature and dew point data on the diagram using the semilogy function. Finally, we will set the limits and ticks for the X and Y axis and display the plot.

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```

## Summary

In this lab, we learned how to create a SkewT-logP diagram using Matplotlib's transforms and custom projection API. We created a SkewXTick class to draw the ticks, a SkewXAxis class to provide separate intervals for ticks and a SkewSpine class to draw the spine. We also created a SkewXAxes class to handle the transformations and registration of the SkewXAxes projection. Finally, we created a SkewT-logP diagram by preparing the data and plotting it on the SkewXAxes subplot.
