# Matplotlib Tutorial: Text Alignment

## Introduction

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. This tutorial will focus on text alignment in Matplotlib.

## Steps

### Step 1: Creating a Rectangle

We will begin by creating a rectangle in the plot using `Rectangle()` function of `matplotlib.patches` module. After creating the rectangle, we will set its horizontal and vertical limits using `set_xlim()` and `set_ylim()` functions. Finally, we will add the rectangle to the plot.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Build a rectangle in axes coords
left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Set the horizontal and vertical limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```

### Step 2: Adding Text to the Rectangle

In this step, we will add text to the rectangle using the `text()` function. The horizontal and vertical alignment of the text will be set using the `horizontalalignment` and `verticalalignment` parameters respectively.

```python
# Add text to the rectangle
ax.text(left, bottom, 'left top',
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes)

ax.text(left, bottom, 'left bottom',
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=ax.transAxes)

ax.text(right, top, 'right bottom',
        horizontalalignment='right',
        verticalalignment='bottom',
        transform=ax.transAxes)

ax.text(right, top, 'right top',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)

ax.text(right, bottom, 'center top',
        horizontalalignment='center',
        verticalalignment='top',
        transform=ax.transAxes)

ax.text(left, 0.5 * (bottom + top), 'right center',
        horizontalalignment='right',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes)

ax.text(left, 0.5 * (bottom + top), 'left center',
        horizontalalignment='left',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes)

ax.text(0.5 * (left + right), 0.5 * (bottom + top), 'middle',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)

ax.text(right, 0.5 * (bottom + top), 'centered',
        horizontalalignment='center',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes)

ax.text(left, top, 'rotated\nwith newlines',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=45,
        transform=ax.transAxes)

plt.show()
```

### Step 3: Customizing the Plot

In this step, we will customize the plot by adding axis labels and removing the axis lines.

```python
# Customize the plot
ax.set_axis_off()
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Text Alignment in Matplotlib')
plt.show()
```

## Summary

In this tutorial, we learned how to align text in Matplotlib. We used the `text()` function to add text to a rectangle and set the horizontal and vertical alignment using the `horizontalalignment` and `verticalalignment` parameters respectively. We also customized the plot by adding axis labels and removing the axis lines.
