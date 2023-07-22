# Python Matplotlib Tutorial: 3D Surface (Colormap)

## Introduction

This lab is a step-by-step tutorial on how to plot a 3D surface using Matplotlib in Python. The 3D surface is colored with the coolwarm colormap and made opaque by using "antialiased=False". The tutorial also demonstrates using the `.LinearLocator` and custom formatting for the z axis tick labels.

## Steps

### Step 1: Import Libraries

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator
```

We import the necessary libraries for the tutorial. Matplotlib is a plotting library for Python that provides an interface similar to MATLAB. Numpy is a fundamental package for scientific computing in Python.

### Step 2: Create Figure and Axes

```python
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
```

We create a figure and axes with the `subplot_kw` parameter set to `"projection": "3d"`. This will create a 3D projection of the plot.

### Step 3: Create Data

```python
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

We create the data for the plot. We create the `X` and `Y` values as arrays with evenly spaced values from -5 to 5 in increments of 0.25. We then create a meshgrid of `X` and `Y` values using `np.meshgrid()`. We use the meshgrid to calculate the `R` values, which is the distance from the origin. We then calculate the `Z` values using the `sin()` function of `R`.

### Step 4: Plot the Surface

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

We plot the surface using the `plot_surface()` function. We pass in the `X`, `Y`, and `Z` values as well as the `cmap` parameter set to `cm.coolwarm` to color the surface with the coolwarm colormap. We also set `linewidth=0` to remove the wireframe and `antialiased=False` to make the surface opaque.

### Step 5: Customize the Z Axis

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

We customize the z axis using the `set_zlim()` function to set the limits of the z axis to -1.01 to 1.01. We then use the `set_major_locator()` function to set the number of ticks on the z axis to 10 using `LinearLocator(10)`. Finally, we use the `set_major_formatter()` function to format the z axis tick labels using a `StrMethodFormatter`.

### Step 6: Add a Color Bar

```python
fig.colorbar(surf, shrink=0.5, aspect=5)
```

We add a color bar to the plot using the `colorbar()` function. We pass in the `surf` object and set `shrink=0.5` and `aspect=5` to adjust the size of the color bar.

## Summary

This tutorial demonstrated how to plot a 3D surface using Matplotlib in Python. We created a figure and axes, created the data, plotted the surface, customized the z axis, and added a color bar. Matplotlib is a powerful tool for creating visualizations in Python.
