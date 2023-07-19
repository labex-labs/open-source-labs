# Matplotlib Floating Axes Tutorial

## Introduction

In this lab, we will learn how to use the `floating_axes` module of Matplotlib to create custom plots with non-rectangular shapes. This module is useful when we need to plot data on non-Cartesian coordinate systems, such as polar or logarithmic plots. We will demonstrate how to create a scatter plot, a bar plot, and a sector plot using different coordinate systems.

## Steps

### Step 1: Importing necessary libraries

First, we need to import the necessary libraries. We will use Matplotlib, NumPy, and some modules from `mpl_toolkits.axisartist` and `mpl_toolkits.axisartist.grid_finder`.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.angle_helper as angle_helper
import mpl_toolkits.axisartist.floating_axes as floating_axes
from mpl_toolkits.axisartist.grid_finder import (DictFormatter, FixedLocator,
                                                 MaxNLocator)
```

### Step 2: Creating a simple floating axes plot

In this step, we will create a simple floating axes plot using `GridHelperCurveLinear`. We will create a scatter plot and a bar plot with a non-rectangular shape.

```python
def setup_axes1(fig, rect):
    tr = Affine2D().scale(2, 1).rotate_deg(30)

    grid_helper = floating_axes.GridHelperCurveLinear(
        tr, extremes=(-0.5, 3.5, 0, 4),
        grid_locator1=MaxNLocator(nbins=4),
        grid_locator2=MaxNLocator(nbins=4))

    ax1 = fig.add_subplot(
        rect, axes_class=floating_axes.FloatingAxes, grid_helper=grid_helper)
    ax1.grid()

    aux_ax = ax1.get_aux_axes(tr)

    return ax1, aux_ax

fig = plt.figure(figsize=(8, 4))
fig.subplots_adjust(wspace=0.3, left=0.05, right=0.95)

ax1, aux_ax1 = setup_axes1(fig, 131)
aux_ax1.bar([0, 1, 2, 3], [3, 2, 1, 3])
```

### Step 3: Creating a polar plot

In this step, we will create a polar plot using `GridHelperCurveLinear`. We will create a scatter plot with a non-rectangular shape.

```python
def setup_axes2(fig, rect):
    tr = PolarAxes.PolarTransform()

    pi = np.pi
    angle_ticks = [(0, r"$0$"),
                   (.25*pi, r"$\frac{1}{4}\pi$"),
                   (.5*pi, r"$\frac{1}{2}\pi$")]
    grid_locator1 = FixedLocator([v for v, s in angle_ticks])
    tick_formatter1 = DictFormatter(dict(angle_ticks))

    grid_locator2 = MaxNLocator(2)

    grid_helper = floating_axes.GridHelperCurveLinear(
        tr, extremes=(.5*pi, 0, 2, 1),
        grid_locator1=grid_locator1,
        grid_locator2=grid_locator2,
        tick_formatter1=tick_formatter1,
        tick_formatter2=None)

    ax1 = fig.add_subplot(
        rect, axes_class=floating_axes.FloatingAxes, grid_helper=grid_helper)
    ax1.grid()

    aux_ax = ax1.get_aux_axes(tr)

    aux_ax.patch = ax1.patch
    ax1.patch.zorder = 0.9

    return ax1, aux_ax

ax2, aux_ax2 = setup_axes2(fig, 132)
theta = np.random.rand(10)*.5*np.pi
radius = np.random.rand(10) + 1.
aux_ax2.scatter(theta, radius)
```

### Step 4: Creating a sector plot

In this step, we will create a sector plot using `GridHelperCurveLinear`. We will create a scatter plot with a non-rectangular shape.

```python
def setup_axes3(fig, rect):
    tr_rotate = Affine2D().translate(-95, 0)
    tr_scale = Affine2D().scale(np.pi/180., 1.)
    tr = tr_rotate + tr_scale + PolarAxes.PolarTransform()

    grid_locator1 = angle_helper.LocatorHMS(4)
    tick_formatter1 = angle_helper.FormatterHMS()

    grid_locator2 = MaxNLocator(3)

    ra0, ra1 = 8.*15, 14.*15
    cz0, cz1 = 0, 14000
    grid_helper = floating_axes.GridHelperCurveLinear(
        tr, extremes=(ra0, ra1, cz0, cz1),
        grid_locator1=grid_locator1,
        grid_locator2=grid_locator2,
        tick_formatter1=tick_formatter1,
        tick_formatter2=None)

    ax1 = fig.add_subplot(
        rect, axes_class=floating_axes.FloatingAxes, grid_helper=grid_helper)

    ax1.axis["left"].set_axis_direction("bottom")
    ax1.axis["right"].set_axis_direction("top")

    ax1.axis["bottom"].set_visible(False)
    ax1.axis["top"].set_axis_direction("bottom")
    ax1.axis["top"].toggle(ticklabels=True, label=True)
    ax1.axis["top"].major_ticklabels.set_axis_direction("top")
    ax1.axis["top"].label.set_axis_direction("top")

    ax1.axis["left"].label.set_text(r"cz [km$^{-1}$]")
    ax1.axis["top"].label.set_text(r"$\alpha_{1950}$")
    ax1.grid()

    aux_ax = ax1.get_aux_axes(tr)

    aux_ax.patch = ax1.patch
    ax1.patch.zorder = 0.9

    return ax1, aux_ax

ax3, aux_ax3 = setup_axes3(fig, 133)
theta = (8 + np.random.rand(10)*(14 - 8))*15.
radius = np.random.rand(10)*14000.
aux_ax3.scatter(theta, radius)
```

### Step 5: Displaying the plot

Finally, we need to display the plot using the `show()` function of Matplotlib.

```python
plt.show()
```

## Summary

In this lab, we learned how to use the `floating_axes` module of Matplotlib to create custom plots with non-rectangular shapes. We created a scatter plot, a bar plot, and a sector plot using different coordinate systems. We used `GridHelperCurveLinear` to create the necessary transformations, `FixedLocator` and `MaxNLocator` to set the grid lines, and `DictFormatter` and `FormatterHMS` to format the tick labels.
