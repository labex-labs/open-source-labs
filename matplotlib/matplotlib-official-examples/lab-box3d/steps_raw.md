# 3D Box Surface Plot Lab

## Introduction

This lab will guide you through creating a 3D box surface plot using Python and Matplotlib. We will define dimensions, create fake data, and plot contour surfaces. We will set limits of the plot, plot edges, set labels and zticks, set zoom and angle view, and add a colorbar.

## Steps

### Step 1: Define Dimensions

Define the dimensions of the box by creating three variables for the length of each side: Nx, Ny, and Nz. Then create three meshgrids for X, Y, and Z using numpy's arange method. Finally, set the negative value for Z to create a box instead of a plane.

```python
import matplotlib.pyplot as plt
import numpy as np

# Define dimensions
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```

### Step 2: Create Fake Data

Create fake data to plot by using a formula to calculate data based on the values of X, Y, and Z. We will add one to the result to ensure that the minimum value is greater than zero.

```python
# Create fake data
data = (((X+100)**2 + (Y-20)**2 + 2*Z)/1000+1)
```

### Step 3: Plot Contour Surfaces

Plot contour surfaces for the box using the `contourf` method for each surface. Use appropriate parameters for `zdir` and `offset`.

```python
kw = {
    'vmin': data.min(),
    'vmax': data.max(),
    'levels': np.linspace(data.min(), data.max(), 10),
}

# Create a figure with 3D ax
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')

# Plot contour surfaces
_ = ax.contourf(
    X[:, :, 0], Y[:, :, 0], data[:, :, 0],
    zdir='z', offset=0, **kw
)
_ = ax.contourf(
    X[0, :, :], data[0, :, :], Z[0, :, :],
    zdir='y', offset=0, **kw
)
C = ax.contourf(
    data[:, -1, :], Y[:, -1, :], Z[:, -1, :],
    zdir='x', offset=X.max(), **kw
)
```

### Step 4: Set Limits of the Plot

Set limits of the plot using the `set` method and passing in the limits of the X, Y, and Z coordinates.

```python
# Set limits of the plot from coord limits
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])
```

### Step 5: Plot Edges

Plot edges using the `plot` method. We will plot three lines along the X and Y coordinates, and one line along the X and Z coordinates.

```python
# Plot edges
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```

### Step 6: Set Labels and Zticks

Set labels and zticks using the `set` method. We will set the labels for X, Y, and Z coordinates, and set the zticks to show the depth of the box.

```python
# Set labels and zticks
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```

### Step 7: Set Zoom and Angle View

Set zoom and angle view using the `view_init` and `set_box_aspect` methods. We will set the angle view to 40 degrees in the X direction and -30 degrees in the Y direction, and the zoom to 0.9.

```python
# Set zoom and angle view
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```

### Step 8: Add a Colorbar

Add a colorbar using the `colorbar` method. We will set the fraction and pad parameters to adjust the location of the colorbar, and set the label to show the name and units of the data.

```python
# Colorbar
fig.colorbar(C, ax=ax, fraction=0.02, pad=0.1, label='Name [units]')
```

## Summary

In this lab, we created a 3D box surface plot using Python and Matplotlib. We defined dimensions, created fake data, and plotted contour surfaces. We set limits of the plot, plotted edges, set labels and zticks, set zoom and angle view, and added a colorbar. This plot can be used to visualize 3D data and explore relationships between variables.
