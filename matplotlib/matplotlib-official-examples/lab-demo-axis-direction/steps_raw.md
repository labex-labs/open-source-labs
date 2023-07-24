# Matplotlib Axis Direction

## Introduction

In this lab, you will learn how to change the axis direction in a Matplotlib plot using the `set_axis_direction()` method. This method allows you to change the direction of an axis to any of the four cardinal directions: top, bottom, left, or right.

## Steps

### Step 1: Importing Libraries

First, we need to import the necessary libraries for this lab. We will be using `numpy` and `matplotlib`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Setting up the Plot

Next, we will define a function `setup_axes()` that will set up the polar projection in a rectangular box. This function uses `GridHelperCurveLinear` to create a polar projection with a rectangular box.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist as axisartist
import mpl_toolkits.axisartist.angle_helper as angle_helper
import mpl_toolkits.axisartist.grid_finder as grid_finder
from mpl_toolkits.axisartist.grid_helper_curvelinear import \
    GridHelperCurveLinear

def setup_axes(fig, rect):
    """Polar projection, but in a rectangular box."""
    grid_helper = GridHelperCurveLinear(
        Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform(),
        extreme_finder=angle_helper.ExtremeFinderCycle(
            20, 20,
            lon_cycle=360, lat_cycle=None,
            lon_minmax=None, lat_minmax=(0, np.inf),
        ),
        grid_locator1=angle_helper.LocatorDMS(12),
        grid_locator2=grid_finder.MaxNLocator(5),
        tick_formatter1=angle_helper.FormatterDMS(),
    )
    ax = fig.add_subplot(
        rect, axes_class=axisartist.Axes, grid_helper=grid_helper,
        aspect=1, xlim=(-5, 12), ylim=(-5, 10))
    ax.axis[:].toggle(ticklabels=False)
    ax.grid(color=".9")
    return ax
```

### Step 3: Adding Floating Axis

We will define two functions that will add floating axes to our plot. The first function `add_floating_axis1()` adds a floating axis to the plot with a label of `theta = 30`. The second function `add_floating_axis2()` adds a floating axis to the plot with a label of `r = 6`.

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```

### Step 4: Changing the Axis Direction

Now, we will create a loop to set up four different plots with the floating axis in each of the four cardinal directions. In the loop, we will use `add_floating_axis1()` and `add_floating_axis2()` to add the floating axes, and `set_axis_direction()` to set the axis direction.

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```

### Step 5: Viewing the Plot

Finally, we will view the plot. We can see the same plot with the floating axis in each of the four cardinal directions.

## Summary

In this lab, you learned how to change the axis direction in a Matplotlib plot using the `set_axis_direction()` method. By using this method, you can easily change the direction of an axis to any of the four cardinal directions: top, bottom, left, or right.
