# Step-by-Step Lab: Creating a Polar Curve in a Rectangular Box using Matplotlib

## Introduction

Matplotlib is a Python library used for creating static, animated, and interactive visualizations in Python. One of the key features of Matplotlib is its ability to create 2D and 3D plots of all types and styles, including scatter plots, line plots, and bar charts. In this lab, you will learn how to create a polar curve in a rectangular box using Matplotlib.

## Steps

### Step 1: Import Required Libraries

In this step, we will import the required libraries for creating the polar curve. We will use `numpy` for numerical computing and `matplotlib` for creating the plot.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the Polar Axes

In this step, we will define the polar axes and set the scaling factor. We will use `PolarAxes.PolarTransform()` to define the polar axes.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Define the polar axes
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```

### Step 3: Define the Grid Helper

In this step, we will define the grid helper that will be used to create the polar curve. We will use `GridHelperCurveLinear` to define the grid helper.

```python
from mpl_toolkits.axisartist import GridHelperCurveLinear, HostAxes
import mpl_toolkits.axisartist.angle_helper as angle_helper

# Define the grid helper
extreme_finder = angle_helper.ExtremeFinderCycle(20,
                                                 20,
                                                 lon_cycle=360,
                                                 lat_cycle=None,
                                                 lon_minmax=None,
                                                 lat_minmax=(0, np.inf),
                                                 )
grid_locator1 = angle_helper.LocatorDMS(12)
tick_formatter1 = angle_helper.FormatterDMS()

grid_helper = GridHelperCurveLinear(tr,
                                    extreme_finder=extreme_finder,
                                    grid_locator1=grid_locator1,
                                    tick_formatter1=tick_formatter1
                                    )
```

### Step 4: Create the Host Axes

In this step, we will create the host axes and set the grid helper. We will use `fig.add_subplot()` to create the host axes.

```python
# Create the host axes
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```

### Step 5: Create Floating Axes

In this step, we will create two floating axes that will be used to display the polar curve in a rectangular box. We will use `new_floating_axis()` to create the floating axes.

```python
# Create the floating axes
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```

### Step 6: Set the Limits and Display the Grid

In this step, we will set the limits for the axes and display the grid. We will use `set_aspect()` to set the aspect ratio of the axes and `grid()` to display the grid.

```python
# Set the limits and display the grid
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```

### Step 7: Display the Polar Curve

In this step, we will display the polar curve in the rectangular box. We will use `plt.show()` to display the plot.

```python
# Display the polar curve
plt.show()
```

## Summary

In this lab, you learned how to create a polar curve in a rectangular box using Matplotlib. You learned how to define the polar axes and the grid helper, create the host axes, create the floating axes, set the limits, display the grid, and display the polar curve. With this knowledge, you can create a wide variety of polar curves in rectangular boxes using Matplotlib.
