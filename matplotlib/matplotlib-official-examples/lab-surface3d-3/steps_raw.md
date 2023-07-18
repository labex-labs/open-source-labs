# Matplotlib 3D Surface Plotting Lab

## Introduction

In this lab, we will learn how to create a 3D surface plot with a checkerboard pattern using Python Matplotlib library. We will create a 3D surface plot, customize the colors of the surface, and adjust the limits of the z-axis.

## Steps

### Step 1: Import required libraries

In this step, we will import the required libraries, which include `matplotlib.pyplot`, `numpy`, and `LinearLocator` from `matplotlib.ticker`.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator
```

### Step 2: Create data for the surface plot

In this step, we will create data for the surface plot. We will create a meshgrid of X and Y values, calculate the radial distance R, and calculate the Z value based on the R value using `np.sin()`.

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

### Step 3: Create colors for the surface plot

In this step, we will create colors for the surface plot. We will create an empty array of strings with the same shape as the meshgrid, and populate it with two colors in a checkerboard pattern.

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```

### Step 4: Create the surface plot

In this step, we will create the surface plot with face colors taken from the array we made. We will also customize the z-axis.

```python
# Create the surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)

# Customize the z axis
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(6))

# Show the plot
plt.show()
```

## Summary

In this lab, we have learned how to create a 3D surface plot with a checkerboard pattern using Python Matplotlib library. We have learned how to create data for the surface plot, create colors for the surface plot, create the surface plot, and customize the z-axis. This knowledge can be applied to create various types of 3D surface plots for different applications.
