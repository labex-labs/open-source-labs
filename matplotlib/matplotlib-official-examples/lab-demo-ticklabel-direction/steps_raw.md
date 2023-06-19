# Matplotlib Ticklabel Direction Lab

## Introduction

This lab will guide you through how to set the direction of tick labels in a Matplotlib plot. You will learn how to customize the direction of tick labels for both the x and y axes.

## Steps

### Step 1: Import necessary modules

First, we need to import the necessary modules to create our plot. We will be using Matplotlib and AxisArtist from mpl_toolkits.

```python
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist.axislines as axislines
```

### Step 2: Create a function to set up axes

We will create a function to set up our axes with the desired tick labels.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axislines.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```

### Step 3: Customize tick label direction

We will create three subplots to demonstrate different ways to customize the direction of tick labels.

#### Step 3.1: Tick labels pointing outwards

In this step, we will create a subplot with tick labels pointing outwards.

```python
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.2)

ax = setup_axes(fig, 131)
for axis in ax.axis.values():
    axis.major_ticks.set_tick_out(True)
```

#### Step 3.2: Customized tick label direction

In this step, we will create a subplot with customized tick label direction.

```python
ax = setup_axes(fig, 132)
ax.axis["left"].set_axis_direction("right")
ax.axis["bottom"].set_axis_direction("top")
ax.axis["right"].set_axis_direction("left")
ax.axis["top"].set_axis_direction("bottom")
```

#### Step 3.3: Tick labels pointing outwards on one side

In this step, we will create a subplot with tick labels pointing outwards on one side.

```python
ax = setup_axes(fig, 133)
ax.axis["left"].set_axis_direction("right")
ax.axis[:].major_ticks.set_tick_out(True)

ax.axis["left"].label.set_text("Long Label Left")
ax.axis["bottom"].label.set_text("Label Bottom")
ax.axis["right"].label.set_text("Long Label Right")
ax.axis["right"].label.set_visible(True)
ax.axis["left"].label.set_pad(0)
ax.axis["bottom"].label.set_pad(10)

plt.show()
```

## Summary

In this lab, we learned how to customize the direction of tick labels in a Matplotlib plot using AxisArtist. By using the `set_axis_direction()` and `major_ticks.set_tick_out()` methods, we can create subplots with different tick label directions.
