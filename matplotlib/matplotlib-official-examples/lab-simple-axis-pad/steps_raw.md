# Simple Axis Pad Lab

## Introduction

This lab will teach you how to use the `add_floating_axis` function in Matplotlib to add floating axes to a plot, which can be used to display additional information about the plot. Specifically, you will learn how to adjust the padding of tick labels and axis labels, as well as how to adjust the position of ticks on the floating axes.

## Steps

### Step 1: Import Libraries

First, import the necessary libraries, including `matplotlib.pyplot`, `numpy`, and `mpl_toolkits.axisartist`.

```python
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
```

### Step 2: Define Setup Axes Function

Next, define the `setup_axes()` function, which sets up the polar projection of the plot. This function uses a `GridHelperCurveLinear` to create a polar projection in a rectangular box. It also sets the limits of the plot and returns the `ax1` object.

```python
def setup_axes(fig, rect):
    # Define the PolarAxes transform and the extreme finder
    tr = Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform()
    extreme_finder = angle_helper.ExtremeFinderCycle(20, 20, lon_cycle=360, lat_cycle=None, lon_minmax=None, lat_minmax=(0, np.inf))

    # Define the grid locators and formatters
    grid_locator1 = angle_helper.LocatorDMS(12)
    grid_locator2 = grid_finder.MaxNLocator(5)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Define the GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(tr, extreme_finder=extreme_finder, grid_locator1=grid_locator1, grid_locator2=grid_locator2, tick_formatter1=tick_formatter1)

    # Create the axis object and set its limits
    ax1 = fig.add_subplot(rect, axes_class=axisartist.Axes, grid_helper=grid_helper)
    ax1.axis[:].set_visible(False)
    ax1.set_aspect(1.)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    return ax1
```

### Step 3: Define Add Floating Axis Function

Define the `add_floating_axis` function, which adds a floating axis to the plot. This function takes in the `ax1` object as an argument and returns the `axis` object.

```python
def add_floating_axis(ax1):
    # Define the floating axis
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```

### Step 4: Add Padding to Tick Labels

In this step, add padding to the tick labels on the floating axis. This can be done by setting the `pad` attribute of the `major_ticklabels` object to the desired padding value.

```python
# Add Padding to Tick Labels
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticklabels.set_pad(10)

plt.show()
```

### Step 5: Adjust Axis Label Padding

In this step, adjust the padding of the axis label on the floating axis. This can be done by setting the `pad` attribute of the `label` object to the desired padding value.

```python
# Adjust Axis Label Padding
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.label.set_pad(20)

plt.show()
```

### Step 6: Adjust Tick Position

In this step, adjust the position of the ticks on the floating axis. This can be done by setting the `tick_out` attribute of the `major_ticks` object to `True`.

```python
# Adjust Tick Position
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticks.set_tick_out(True)

plt.show()
```

## Summary

In this lab, you learned how to use the `add_floating_axis` function in Matplotlib to add floating axes to a plot. You also learned how to adjust the padding of tick labels and axis labels, as well as how to adjust the position of ticks on the floating axes. By the end of this lab, you should be able to create customized plots with floating axes that display additional information about the plot.
