# Matplotlib Spine Placement Lab

## Introduction

In Matplotlib, the position of axis spines can be adjusted to customize the appearance of a plot. This lab will guide you through the process of adjusting spine positions in Matplotlib.

## Steps

### Step 1: Import necessary libraries

In this step, we will import the necessary libraries for creating our plots.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a basic plot

In this step, we will create a basic plot to demonstrate the different spine placement options in Matplotlib.

```python
x = np.linspace(0, 2*np.pi, 100)
y = 2 * np.sin(x)

fig, ax_dict = plt.subplot_mosaic(
    [['center', 'zero'],
     ['axes', 'data']]
)
fig.suptitle('Spine positions')

ax = ax_dict['center']
ax.set_title("'center'")
ax.plot(x, y)
ax.spines[['left', 'bottom']].set_position('center')
ax.spines[['top', 'right']].set_visible(False)

ax = ax_dict['zero']
ax.set_title("'zero'")
ax.plot(x, y)
ax.spines[['left', 'bottom']].set_position('zero')
ax.spines[['top', 'right']].set_visible(False)

ax = ax_dict['axes']
ax.set_title("'axes' (0.2, 0.2)")
ax.plot(x, y)
ax.spines.left.set_position(('axes', 0.2))
ax.spines.bottom.set_position(('axes', 0.2))
ax.spines[['top', 'right']].set_visible(False)

ax = ax_dict['data']
ax.set_title("'data' (1, 2)")
ax.plot(x, y)
ax.spines.left.set_position(('data', 1))
ax.spines.bottom.set_position(('data', 2))
ax.spines[['top', 'right']].set_visible(False)
```

### Step 3: Define a method to adjust spine locations

In this step, we will define a method that adjusts the location of the axis spines based on the specified spine locations.

```python
def adjust_spines(ax, spines):
    """
    Adjusts the location of the axis spines based on the specified spine locations.

    Parameters:
        ax (Axes): The Matplotlib Axes object to adjust the spines for.
        spines (list of str): The desired spine locations. Valid options are 'left', 'right', 'top', 'bottom'.

    Returns:
        None
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # move the spine outward by 10 points
        else:
            spine.set_color('none')  # don't draw the spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])
```

### Step 4: Create a plot using the `adjust_spines` method

In this step, we will create a plot using the `adjust_spines` method to demonstrate how to adjust spine locations.

```python
fig = plt.figure()

x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)

ax = fig.add_subplot(2, 2, 1)
ax.plot(x, y, clip_on=False)
adjust_spines(ax, ['left'])

ax = fig.add_subplot(2, 2, 2)
ax.plot(x, y, clip_on=False)
adjust_spines(ax, [])

ax = fig.add_subplot(2, 2, 3)
ax.plot(x, y, clip_on=False)
adjust_spines(ax, ['left', 'bottom'])

ax = fig.add_subplot(2, 2, 4)
ax.plot(x, y, clip_on=False)
adjust_spines(ax, ['bottom'])

plt.show()
```

## Summary

In this lab, we learned how to adjust spine positions in Matplotlib by setting the position of the axis spines using the `set_position` method, and how to define a method to adjust spine locations based on the desired spine locations. This can be useful for customizing the appearance of plots and highlighting specific features.
