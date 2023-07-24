# Adding a Colorbar to Inset Axes

## Introduction

In this lab, you will learn how to add a colorbar to inset axes using Matplotlib in Python. A colorbar is a visual representation of the mapping of a range of colors to a range of numerical values. An inset axis is a smaller axis that is placed within the larger axis of a plot.

## Steps

### Step 1: Import Libraries and Data

First, import the necessary libraries and data that will be used in the plot.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes

fig, ax = plt.subplots(figsize=[5, 4])

Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
```

### Step 2: Set the Main Plot

Set the main plot by adjusting the aspect ratio and the limits of the x and y axes.

```python
ax.set(aspect=1, xlim=(-15, 15), ylim=(-20, 5))
```

### Step 3: Create an Inset Axis

Create an inset axis using the `zoomed_inset_axes` function. Set the zoom level and the location of the inset axis within the main plot.

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```

### Step 4: Add an Image to the Inset Axis

Add an image to the inset axis using the `imshow` function. Set the extent and the origin of the image.

```python
im = axins.imshow(Z, extent=extent, origin="lower")
```

### Step 5: Add a Colorbar

Add a colorbar to the inset axis using the `inset_axes` function. Set the width, height, location, and bounding box of the colorbar.

```python
cax = inset_axes(axins,
                 width="5%",  # width = 10% of parent_bbox width
                 height="100%",  # height : 50%
                 loc='lower left',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```

### Step 6: Display the Plot

Display the plot using the `show` function.

```python
plt.show()
```

## Summary

Congratulations! You have successfully learned how to add a colorbar to inset axes using Matplotlib in Python. This is a useful technique for visualizing data in a more detailed and informative way. Remember to adjust the parameters according to your specific needs and preferences.
