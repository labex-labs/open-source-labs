# Matplotlib Contourf Tutorial

## Introduction

In this tutorial, we will learn how to create filled contour plots using the `contourf` method in the Matplotlib library. We will cover how to create filled contours with automatic and explicit levels, and how to set the colormap and extend settings.

## Steps

### Step 1: Import Libraries and Create Data

First, we need to import the necessary libraries and create some data to plot.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
origin = 'lower'
delta = 0.025
x = y = np.arange(-3.0, 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```

### Step 2: Create Filled Contour with Automatic Levels

Next, we will create a filled contour plot with automatic levels. We will use the `contourf` method with the `cmap` parameter set to `plt.cm.bone` to specify the colormap. We will also add contour lines with the `contour` method and pass in a subset of the contour levels used for the filled contours.

```python
# Create filled contour with automatic levels
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Automatic Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')
cbar.add_lines(CS2)

# Show plot
plt.show()
```

### Step 3: Create Filled Contour with Explicit Levels

Now, we will create a filled contour plot with explicit levels. We will use the `contourf` method with the `levels` parameter set to a list of values to specify the contour levels. We will also set the colormap to a list of colors and set the `extend` parameter to `'both'` to show values outside the range of levels.

```python
# Create filled contour with explicit levels
fig, ax = plt.subplots()
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, levels, colors=('k',),
                 linewidths=(3,), origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Explicit Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')

# Show plot
plt.show()
```

### Step 4: Set Colormap and Extend Settings

Finally, we will set the colormap and extend settings. We will use the `with_extremes` method to set the colors for values below and above the range of levels. We will also create four subplots to show the four possible `extend` settings: `'neither'`, `'both'`, `'min'`, and `'max'`.

```python
# Set colormap and extend settings
extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

# Create subplots with different extend settings
fig, axs = plt.subplots(2, 2, layout="constrained")
for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

# Show plot
plt.show()
```

## Summary

In this tutorial, we learned how to create filled contour plots using the `contourf` method in the Matplotlib library. We covered how to create filled contours with automatic and explicit levels, and how to set the colormap and extend settings. With these skills, you can create beautiful and informative contour plots for your data.
