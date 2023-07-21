# Matplotlib Inset Locator Lab

## Introduction

Matplotlib is a data visualization library in Python. The `.inset_locator` feature allows for easy placement of insets in the corners of the axes. In this lab, we will explore how to use the `.inset_locator` feature to create insets in Matplotlib plots.

## Steps

### Step 1: Create a Figure with Two Subplots

First, we need to create a figure with two subplots. We will use the `plt.subplots()` method to create a figure with two subplots side by side.

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```

### Step 2: Create Inset Axes

Next, we will create inset axes in each of the subplots. We will use the `inset_axes()` method to create the inset axes. We will create four insets with different sizes and locations.

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Create inset of width 1.3 inches and height 0.9 inches
# at the default upper right location
axins = inset_axes(ax, width=1.3, height=0.9)

# Create inset of width 30% and height 40% of the parent axes' bounding box
# at the lower left corner (loc=3)
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# Create inset of mixed specifications in the second subplot;
# width is 30% of parent axes' bounding box and
# height is 1 inch at the upper left corner (loc=2)
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# Create an inset in the lower right corner (loc=4) with borderpad=1, i.e.
# 10 points padding (as 10pt is the default fontsize) to the parent axes
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```

### Step 3: Turn Off Tick Labels

To remove the tick labels from each of the insets, we can use the `tick_params()` method and set `labelleft` and `labelbottom` to `False`.

```python
# Turn ticklabels of insets off
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```

### Step 4: Control Inset Position and Size

We can use the `bbox_to_anchor` and `bbox_transform` parameters to control the position and size of the inset. These parameters allow for fine-grained control over the inset position and size or even to position the inset at completely arbitrary positions.

```python
# We use the axes transform as bbox_transform. Therefore, the bounding box
# needs to be specified in axes coordinates ((0, 0) is the lower left corner
# of the axes, (1, 1) is the upper right corner).
# The bounding box (.2, .4, .6, .5) starts at (.2, .4) and ranges to (.8, .9)
# in those coordinates.
# Inside this bounding box an inset of half the bounding box' width and
# three quarters of the bounding box' height is created. The lower left corner
# of the inset is aligned to the lower left corner of the bounding box (loc=3).
# The inset is then offset by the default 0.5 in units of the font size.
axins = inset_axes(ax, width="50%", height="75%",
                   bbox_to_anchor=(.2, .4, .6, .5),
                   bbox_transform=ax.transAxes, loc=3)
```

### Step 5: Create Insets with Arbitrary Positions

We can create insets with arbitrary positions by using the `bbox_to_anchor` parameter to specify a bounding box in data coordinates and using the `bbox_transform` parameter to specify the transform for the bounding box.

```python
# Create inset in data coordinates using ax.transData as transform
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```

### Step 6: Create an Inset Outside the Axes

We can create an inset outside the axes by using the `bbox_to_anchor` parameter to specify a bounding box in axes coordinates that extends outside the axes.

```python
# Create an inset outside the axes
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05, .6, .5, .4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```

### Step 7: Create an Inset with a 2-Tuple Bounding Box

We can create an inset with a 2-tuple bounding box by specifying the width and height in inches and using the `bbox_to_anchor` parameter to specify the lower left corner of the inset.

```python
# Create an inset with a 2-tuple bounding box. Note that this creates a
# bbox without extent. This hence only makes sense when specifying
# width and height in absolute units (inches).
axins2 = inset_axes(ax, width=0.5, height=0.4,
                    bbox_to_anchor=(0.33, 0.25),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
```

### Step 8: Create an Inset Centered in Figure Coordinates

We can create an inset that is horizontally centered in figure coordinates and vertically bound to line up with the axes by using the `blended_transform_factory()` method to create a blended transform and using it as the `bbox_transform` parameter.

```python
# Create an inset horizontally centered in figure coordinates and vertically
# bound to line up with the axes.
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```

## Summary

In this lab, we learned how to use the `.inset_locator` feature in Matplotlib to create insets in plots. We created insets with different sizes and locations, controlled the inset position and size, and created insets with arbitrary positions. We also created insets outside the axes, insets with 2-tuple bounding boxes, and insets centered in figure coordinates.
