# Simple Anchored Artists Lab

## Introduction

In this lab, you will learn how to use the anchored helper classes found in Matplotlib's offsetbox and mpl_toolkits.axes_grid1. You will create a figure that contains text boxes, a circle, and a size bar using these classes.

## Steps

### Step 1: Import Libraries

To get started, you will need to import Matplotlib and the necessary modules.

```python
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib.patches import Circle
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDrawingArea, AnchoredSizeBar
```

### Step 2: Create the Figure

Create a figure and axis object using Matplotlib's `subplots()` function.

```python
fig, ax = plt.subplots()
ax.set_aspect(1.)
```

### Step 3: Add Text Boxes

Add two text boxes to the figure, anchored by different corners to the upper-left corner of the figure.

```python
at = AnchoredText("Figure 1a",
                  loc='upper left', prop=dict(size=8), frameon=True,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)

at2 = AnchoredText("Figure 1(b)",
                   loc='lower left', prop=dict(size=8), frameon=True,
                   bbox_to_anchor=(0., 1.),
                   bbox_transform=ax.transAxes
                   )
at2.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at2)
```

### Step 4: Draw a Circle

Draw a circle in axis coordinates.

```python
ada = AnchoredDrawingArea(20, 20, 0, 0,
                          loc='upper right', pad=0., frameon=False)
p = Circle((10, 10), 10)
ada.da.add_artist(p)
ax.add_artist(ada)
```

### Step 5: Add a Size Bar

Draw a horizontal bar with a length of 0.1 in data coordinates, with a fixed label underneath.

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```

### Step 6: Display the Figure

Display the figure using Matplotlib's `show()` function.

```python
plt.show()
```

## Summary

In this lab, you learned how to use the anchored helper classes found in Matplotlib's offsetbox and mpl_toolkits.axes_grid1 to create a figure with text boxes, a circle, and a size bar. You can use these classes to add informative annotations and graphics to your figures.
