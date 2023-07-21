# Matplotlib Colorbar Inset Axes Tutorial

## Introduction

This tutorial will show you how to control the position, height, and width of colorbars using `mpl_toolkits.axes_grid1.inset_locator.inset_axes`. This is useful when you want to add a colorbar to your plot but want to customize its size and position.

## Steps

### Step 1: Import Required Libraries

First, we need to import the required libraries: matplotlib and inset_axes from mpl_toolkits.axes_grid1.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
```

### Step 2: Create Plot and Image

Next, we will create a plot and an image to show how to add a colorbar using inset axes.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
im2 = ax2.imshow([[1, 2], [2, 3]])
```

### Step 3: Add Colorbar using Inset Axes

Now, we will add a colorbar to each of the images using inset_axes. The first colorbar will be added to ax1 and the second to ax2.

```python
# add colorbar to ax1
axins1 = inset_axes(
    ax1,
    width="50%",  # width: 50% of parent_bbox width
    height="5%",  # height: 5%
    loc="upper right",
)
axins1.xaxis.set_ticks_position("bottom")
fig.colorbar(im1, cax=axins1, orientation="horizontal", ticks=[1, 2, 3])

# add colorbar to ax2
axins2 = inset_axes(
    ax2,
    width="5%",  # width: 5% of parent_bbox width
    height="50%",  # height: 50%
    loc="lower left",
    bbox_to_anchor=(1.05, 0., 1, 1),
    bbox_transform=ax2.transAxes,
    borderpad=0,
)
fig.colorbar(im2, cax=axins2, ticks=[1, 2, 3])
```

### Step 4: Display the Plot

Finally, we will display the plot using plt.show().

```python
plt.show()
```

## Summary

In this tutorial, we learned how to use `mpl_toolkits.axes_grid1.inset_locator.inset_axes` to add a colorbar to a plot with customized size and position. The `inset_axes` function allows us to control the position, height, and width of the colorbar, making it easier to create professional-looking plots.
