# Creating a Custom Grid of Axes with Matplotlib

## Introduction

In this lab, we will learn how to create a custom grid of axes with Matplotlib using the `mpl_toolkits.axes_grid1` module. We will create two examples: one with fixed axes sizes and paddings, and another with scalable axes sizes and fixed paddings.

## Steps

### Step 1: Importing Required Libraries

We will start by importing the required libraries: `matplotlib.pyplot` for visualization and `mpl_toolkits.axes_grid1` for creating the custom grid of axes.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Divider, Size
```

### Step 2: Defining Helper Function

We will define a helper function `label_axes()` that will be used to place a label at the center of an axes and remove the axis ticks.

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5, .5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```

### Step 3: Creating a Custom Grid of Axes with Fixed Sizes and Paddings

We will create a custom grid of axes with fixed sizes and paddings. We will use the `Divider` class to divide the axes rectangle into a grid with sizes specified by `horiz * vert`. We will then add four axes to the figure using the `add_axes()` method and specify the positions of each axes using the `new_locator()` method of the `Divider` class.

```python
# Sizes are in inches.
horiz = [Size.Fixed(1.), Size.Fixed(.5), Size.Fixed(1.5), Size.Fixed(.5)]
vert = [Size.Fixed(1.5), Size.Fixed(.5), Size.Fixed(1.)]

rect = (0.1, 0.1, 0.8, 0.8)
fig = plt.figure(figsize=(6, 6))
fig.suptitle("Fixed axes sizes, fixed paddings")

div = Divider(fig, rect, horiz, vert, aspect=False)

# The rect parameter will actually be ignored and overridden by axes_locator.
ax1 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=0))
label_axes(ax1, "nx=0, ny=0")
ax2 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=2))
label_axes(ax2, "nx=0, ny=2")
ax3 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, ny=2))
label_axes(ax3, "nx=2, ny=2")
ax4 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, nx1=4, ny=0))
label_axes(ax4, "nx=2, nx1=4, ny=0")

plt.show()
```

### Step 4: Creating a Custom Grid of Axes with Scalable Sizes and Fixed Paddings

We will create another custom grid of axes with scalable sizes and fixed paddings. We will use the `Size.Scaled()` option to specify axes sizes that scale with the figure size. The remaining steps are similar to the previous example.

```python
# Sizes are in inches.
horiz = [Size.Scaled(1.5), Size.Fixed(.5), Size.Scaled(1.), Size.Scaled(.5)]
vert = [Size.Scaled(1.), Size.Fixed(.5), Size.Scaled(1.5)]

rect = (0.1, 0.1, 0.8, 0.8)
fig = plt.figure(figsize=(6, 6))
fig.suptitle("Scalable axes sizes, fixed paddings")

div = Divider(fig, rect, horiz, vert, aspect=False)

# The rect parameter will actually be ignored and overridden by axes_locator.
ax1 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=0))
label_axes(ax1, "nx=0, ny=0")
ax2 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=2))
label_axes(ax2, "nx=0, ny=2")
ax3 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, ny=2))
label_axes(ax3, "nx=2, ny=2")
ax4 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, nx1=4, ny=0))
label_axes(ax4, "nx=2, nx1=4, ny=0")

plt.show()
```

## Summary

In this lab, we learned how to create a custom grid of axes with Matplotlib using the `mpl_toolkits.axes_grid1` module. We created two examples: one with fixed axes sizes and paddings, and another with scalable axes sizes and fixed paddings. We used the `Divider` class to divide the axes rectangle into a grid with sizes specified by `horiz * vert` and added axes to the figure using the `add_axes()` method and `new_locator()` method of the `Divider` class.
