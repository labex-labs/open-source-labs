# Matplotlib Anchored Objects Lab

## Introduction

In this lab, you will learn how to use Anchored Objects in Matplotlib. Anchored Objects are used to add auxiliary objects to a plot. These objects can be used to add annotations, scale bars, and legends to a plot.

## Steps

### Step 1: Import Libraries

The first step is to import the required libraries. We will be using Matplotlib for this lab.

```python
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.offsetbox import (AnchoredOffsetbox, AuxTransformBox,
                                  DrawingArea, TextArea, VPacker)
from matplotlib.patches import Circle, Ellipse
```

### Step 2: Create a Figure

The next step is to create a figure. We will create a simple figure with a single subplot.

```python
fig, ax = plt.subplots()
ax.set_aspect(1)
```

### Step 3: Add Anchored Text

In this step, we will add a text box anchored to the upper-left corner of the figure.

```python
def draw_text(ax):
    """Draw a text-box anchored to the upper-left corner of the figure."""
    box = AnchoredOffsetbox(child=TextArea("Figure 1a"),
                            loc="upper left", frameon=True)
    box.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(box)

draw_text(ax)
```

### Step 4: Add Anchored Circles

In this step, we will add two circles to the plot using Anchored Objects.

```python
def draw_circles(ax):
    """Draw circles in axes coordinates."""
    area = DrawingArea(width=40, height=20)
    area.add_artist(Circle((10, 10), 10, fc="tab:blue"))
    area.add_artist(Circle((30, 10), 5, fc="tab:red"))
    box = AnchoredOffsetbox(
        child=area, loc="upper right", pad=0, frameon=False)
    ax.add_artist(box)

draw_circles(ax)
```

### Step 5: Add Anchored Ellipse

In this step, we will add an ellipse to the plot using Anchored Objects.

```python
def draw_ellipse(ax):
    """Draw an ellipse of width=0.1, height=0.15 in data coordinates."""
    aux_tr_box = AuxTransformBox(ax.transData)
    aux_tr_box.add_artist(Ellipse((0, 0), width=0.1, height=0.15))
    box = AnchoredOffsetbox(child=aux_tr_box, loc="lower left", frameon=True)
    ax.add_artist(box)

draw_ellipse(ax)
```

### Step 6: Add Size Bar

In this step, we will add a size bar to the plot using Anchored Objects.

```python
def draw_sizebar(ax):
    """
    Draw a horizontal bar with length of 0.1 in data coordinates,
    with a fixed label center-aligned underneath.
    """
    size = 0.1
    text = r"1$^{\prime}$"
    sizebar = AuxTransformBox(ax.transData)
    sizebar.add_artist(Line2D([0, size], [0, 0], color="black"))
    text = TextArea(text)
    packer = VPacker(
        children=[sizebar, text], align="center", sep=5)  # separation in points.
    ax.add_artist(AnchoredOffsetbox(
        child=packer, loc="lower center", frameon=False,
        pad=0.1, borderpad=0.5))  # paddings relative to the legend fontsize.

draw_sizebar(ax)
```

### Step 7: Display the Plot

The final step is to display the plot.

```python
plt.show()
```

## Summary

In this lab, you learned how to use Anchored Objects in Matplotlib. You learned how to add text, circles, ellipses, and size bars to a plot using Anchored Objects. Anchored Objects are a powerful tool that can be used to add annotations and legends to a plot.
