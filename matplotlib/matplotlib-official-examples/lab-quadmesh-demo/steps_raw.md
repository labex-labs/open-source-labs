# Matplotlib QuadMesh Tutorial

## Introduction

This tutorial will guide you through the usage of the Matplotlib library to create a QuadMesh plot. QuadMesh is a faster generalization of the pcolor function, but with some restrictions. The demo in this tutorial will illustrate a bug in QuadMesh with masked data.

## Steps

### Step 1: Importing the necessary libraries

```python
import numpy as np
from matplotlib import pyplot as plt
```

### Step 2: Defining the data

```python
n = 12
x = np.linspace(-1.5, 1.5, n)
y = np.linspace(-1.5, 1.5, n * 2)
X, Y = np.meshgrid(x, y)
Qx = np.cos(Y) - np.cos(X)
Qz = np.sin(Y) + np.sin(X)
Z = np.sqrt(X**2 + Y**2) / 5
Z = (Z - Z.min()) / (Z.max() - Z.min())
Zm = np.ma.masked_where(np.abs(Qz) < 0.5 * np.max(Qz), Z)
```

### Step 3: Creating the plot

```python
fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].pcolormesh(Qx, Qz, Z, shading='gouraud')
axs[0].set_title('Without masked values')
cmap = plt.colormaps[plt.rcParams['image.cmap']].with_extremes(bad='y')
axs[1].pcolormesh(Qx, Qz, Zm, shading='gouraud', cmap=cmap)
axs[1].set_title('With masked values')
axs[2].pcolormesh(Qx, Qz, Zm, shading='gouraud')
axs[2].set_title('With masked values')
fig.tight_layout()
plt.show()
```

### Step 4: Explanation

- Step 2: The data is defined using numpy arrays. The X and Y arrays are used to create a meshgrid, which is used to calculate the Qx and Qz values. The Z values are then calculated based on the Qx and Qz values. The Zm array is created by masking values where the absolute value of Qz is less than 0.5 times the maximum value of Qz.
- Step 3: A figure with three subplots is created using the subplots method. The pcolormesh function is used to create a QuadMesh plot for each subplot. The first subplot shows the plot without masked values. The second subplot shows the plot with masked values and a custom colormap where the masked region is yellow. The third subplot shows the plot with masked values and the default colormap where the masked region is transparent.
- Step 4: The QuadMesh plot is a useful tool for visualizing 2D data. In this tutorial, we learned how to use the pcolormesh function to create a QuadMesh plot and how to handle masked data in the plot.

## Summary

This tutorial provided a step-by-step guide to creating a QuadMesh plot using the Matplotlib library. We learned how to handle masked data in the plot and how to customize the colormap for the masked region. The QuadMesh plot is a powerful tool for visualizing 2D data and is particularly useful for scientific applications.
