# Python Matplotlib Tutorial - Radar Chart

## Introduction

In this lab, you will learn how to create a radar chart using Python's Matplotlib library. A radar chart, also known as a spider or star chart, is a graphical method of displaying multivariate data in the form of a two-dimensional chart of three or more quantitative variables represented on axes starting from the same point. It is often used to compare different products or solutions based on several factors.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries. Matplotlib and numpy are required for this tutorial.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the Radar Chart Function

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

### Step 3: Define the Radar Transform and Radar Axes Classes

Within the `radar_factory` function, we will define the `RadarTransform` and `RadarAxes` classes. These classes will be used to create the radar chart.

```python
class RadarTransform(PolarAxes.PolarTransform):
    # code for the RadarTransform class goes here

class RadarAxes(PolarAxes):
    # code for the RadarAxes class goes here
```

### Step 4: Define the `fill` and `plot` Methods

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

### Step 5: Define the `set_varlabels`, `_gen_axes_patch`, and `_gen_axes_spines` Methods

Within the `RadarAxes` class, we will also define the `set_varlabels`, `_gen_axes_patch`, and `_gen_axes_spines` methods. These methods will set the variable labels, generate the axes patch, and generate the axes spines, respectively.

```python
class RadarAxes(PolarAxes):
    # code for the RadarAxes class goes here

    def set_varlabels(self, labels):
        self.set_thetagrids(np.degrees(theta), labels)

    def _gen_axes_patch(self):
        if frame == 'circle':
            return Circle((0.5, 0.5), 0.5)
        elif frame == 'polygon':
            return RegularPolygon((0.5, 0.5), num_vars,
                                  radius=.5, edgecolor="k")
        else:
            raise ValueError("Unknown value for 'frame': %s" % frame)

    def _gen_axes_spines(self):
        if frame == 'circle':
            return super()._gen_axes_spines()
        elif frame == 'polygon':
            spine = Spine(axes=self,
                          spine_type='circle',
                          path=Path.unit_regular_polygon(num_vars))
            spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                + self.transAxes)
            return {'polar': spine}
        else:
            raise ValueError("Unknown value for 'frame': %s" % frame)
```

### Step 6: Define the Example Data

Now, we will define the example data that we will use to create the radar chart. This data is taken from a study on pollution source profile estimates.

```python
def example_data():
    data = [
        ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO', 'O3'],
        ('Basecase', [
            [0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00],
            [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00, 0.00],
            [0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00, 0.00],
            [0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00, 0.00],
            [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00, 0.00]]),
        ('With CO', [
            [0.88, 0.02, 0.02, 0.02, 0.00, 0.05, 0.00, 0.05, 0.00],
            [0.08, 0.94, 0.04, 0.02, 0.00, 0.01, 0.12, 0.04, 0.00],
            [0.01, 0.01, 0.79, 0.10, 0.00, 0.05, 0.00, 0.31, 0.00],
            [0.00, 0.02, 0.03, 0.38, 0.31, 0.31, 0.00, 0.59, 0.00],
            [0.02, 0.02, 0.11, 0.47, 0.69, 0.58, 0.88, 0.00, 0.00]]),
        ('With O3', [
            [0.89, 0.01, 0.07, 0.00, 0.00, 0.05, 0.00, 0.00, 0.03],
            [0.07, 0.95, 0.05, 0.04, 0.00, 0.02, 0.12, 0.00, 0.00],
            [0.01, 0.02, 0.86, 0.27, 0.16, 0.19, 0.00, 0.00, 0.00],
            [0.01, 0.03, 0.00, 0.32, 0.29, 0.27, 0.00, 0.00, 0.95],
            [0.02, 0.00, 0.03, 0.37, 0.56, 0.47, 0.87, 0.00, 0.00]]),
        ('CO & O3', [
            [0.87, 0.01, 0.08, 0.00, 0.00, 0.04, 0.00, 0.00, 0.01],
            [0.09, 0.95, 0.02, 0.03, 0.00, 0.01, 0.13, 0.06, 0.00],
            [0.01, 0.02, 0.71, 0.24, 0.13, 0.16, 0.00, 0.50, 0.00],
            [0.01, 0.03, 0.00, 0.28, 0.24, 0.23, 0.00, 0.44, 0.88],
            [0.02, 0.00, 0.18, 0.45, 0.64, 0.55, 0.86, 0.00, 0.16]])
    ]
    return data
```

### Step 7: Set the Number of Variables and Calculate the Axis Angles

We will now set the number of variables and calculate the evenly-spaced axis angles using numpy.

```python
N = 9
theta = radar_factory(N, frame='polygon')
```

### Step 8: Create the Radar Chart

Finally, we can create the radar chart using the example data and the `RadarAxes` class.

```python
data = example_data()
spoke_labels = data.pop(0)

fig, axs = plt.subplots(figsize=(9, 9), nrows=2, ncols=2,
                        subplot_kw=dict(projection='radar'))
fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

colors = ['b', 'r', 'g', 'm', 'y']
for ax, (title, case_data) in zip(axs.flat, data):
    ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
    ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                 horizontalalignment='center', verticalalignment='center')
    for d, color in zip(case_data, colors):
        ax.plot(theta, d, color=color)
        ax.fill(theta, d, facecolor=color, alpha=0.25, label='_nolegend_')
    ax.set_varlabels(spoke_labels)

labels = ('Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5')
legend = axs[0, 0].legend(labels, loc=(0.9, .95),
                          labelspacing=0.1, fontsize='small')

fig.text(0.5, 0.965, '5-Factor Solution Profiles Across Four Scenarios',
         horizontalalignment='center', color='black', weight='bold',
         size='large')

plt.show()
```

## Summary

In this lab, you learned how to create a radar chart using Python's Matplotlib library. A radar chart is a graphical method of displaying multivariate data in the form of a two-dimensional chart of three or more quantitative variables represented on axes starting from the same point. It is often used to compare different products or solutions based on several factors.
