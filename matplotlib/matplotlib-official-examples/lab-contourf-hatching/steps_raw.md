# Python Matplotlib Tutorial

## Introduction

In this lab, we will learn how to create filled contour plots with hatched patterns using Python's Matplotlib library. Contour plots are used to display three-dimensional data in two dimensions. They are particularly useful for visualizing data that has peaks and valleys, such as topographical data.

## Steps

### Step 1: Import Libraries

We begin by importing the necessary libraries. In this lab, we will be using NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data

Next, we will create some sample data to plot. In this example, we will create a 2D grid of x and y values and use them to calculate z values.

```python
# invent some numbers, turning the x and y arrays into simple
# 2d arrays, which make combining them together easier.
x = np.linspace(-3, 5, 150).reshape(1, -1)
y = np.linspace(-3, 5, 120).reshape(-1, 1)
z = np.cos(x) + np.sin(y)
```

### Step 3: Simplest Hatched Plot with a Colorbar

In this step, we will create the simplest hatched plot with a colorbar. We will use the `contourf` function to create the filled contour plot and specify the hatches using the `hatches` parameter.

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```

### Step 4: Plot of Hatches without Color with a Legend

In this step, we will create a plot of hatches without color and add a legend. We will use the `contour` function to create the contour lines and the `contourf` function to specify the hatches without color.

```python
fig2, ax2 = plt.subplots()
n_levels = 6
ax2.contour(x, y, z, n_levels, colors='black', linestyles='-')
cs = ax2.contourf(x, y, z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')

# create a legend for the contour set
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax2.legend(artists, labels, handleheight=2, framealpha=1)
```

### Step 5: Display the Plots

Finally, we will display the plots using the `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create filled contour plots with hatched patterns using Matplotlib. We used the `contour` and `contourf` functions to create the plots and specified the hatches using the `hatches` parameter. We also added a colorbar and legend to our plots.
