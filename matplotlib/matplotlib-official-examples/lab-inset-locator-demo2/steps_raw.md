# Creating Zoomed Inset with Matplotlib

## Introduction

Matplotlib is a popular data visualization library in Python. It provides many tools to create different types of plots and graphs. One of the useful features of Matplotlib is the ability to zoom in on a particular region of a plot, which can help to analyze data more closely. In this lab, we will learn how to create a zoomed inset using Matplotlib.

## Steps

### Step 1: Import necessary libraries

Before we start creating the zoomed inset, we need to import the necessary libraries. We will be using `matplotlib.pyplot` and `numpy` for this lab.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a figure and subplots

Next, we will create a figure and subplots to display our data. We will create two subplots side-by-side to show two different examples of zoomed insets.

```python
fig, (ax, ax2) = plt.subplots(ncols=2, figsize=[6, 3])
```

### Step 3: Create a zoomed inset with a size bar

In the first subplot, we will create a zoomed inset with a size bar. This will show how to use the `.zoomed_inset_axes` method to create a zoomed inset.

```python
# Set the aspect ratio of the plot to 1
ax.set_aspect(1)

# Create a zoomed inset in the upper right corner of the plot
axins = zoomed_inset_axes(ax, zoom=0.5, loc='upper right')

# Set the number of ticks on the inset axes
axins.yaxis.get_major_locator().set_params(nbins=7)
axins.xaxis.get_major_locator().set_params(nbins=7)

# Hide the tick labels on the inset axes
axins.tick_params(labelleft=False, labelbottom=False)

# Define a function to add a size bar to the plot
def add_sizebar(ax, size):
    asb = AnchoredSizeBar(ax.transData,
                          size,
                          str(size),
                          loc=8,
                          pad=0.1, borderpad=0.5, sep=5,
                          frameon=False)
    ax.add_artist(asb)

# Add a size bar to the main plot and the inset plot
add_sizebar(ax, 0.5)
add_sizebar(axins, 0.5)
```

### Step 4: Create an image with an inset zoom and a marked inset

In the second subplot, we will create an image with an inset zoom and a marked inset. This will show how to use the `.mark_inset` method to mark the region of interest and connect it to the inset axes.

```python
# Load sample data for the image
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
extent = (-3, 4, -4, 3)
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z

# Display the image in the subplot
ax2.imshow(Z2, extent=extent, origin="lower")

# Create a zoomed inset in the upper left corner of the plot
axins2 = zoomed_inset_axes(ax2, zoom=6, loc=1)

# Display the image in the inset plot
axins2.imshow(Z2, extent=extent, origin="lower")

# Set the x and y limits of the inset plot to show the region of interest
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
axins2.set_xlim(x1, x2)
axins2.set_ylim(y1, y2)

# Set the number of ticks on the inset axes
axins2.yaxis.get_major_locator().set_params(nbins=7)
axins2.xaxis.get_major_locator().set_params(nbins=7)

# Hide the tick labels on the inset axes
axins2.tick_params(labelleft=False, labelbottom=False)

# Mark the region of interest and connect it to the inset axes
mark_inset(ax2, axins2, loc1=2, loc2=4, fc="none", ec="0.5")
```

### Step 5: Display the plot

Finally, we will display the plot using the `plt.show()` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a zoomed inset using Matplotlib. We used the `.zoomed_inset_axes` and `.mark_inset` methods to create two different examples of zoomed insets. By using these methods, we can analyze data more closely and gain insights that may not be visible in the original plot.
