# Python Matplotlib 3D Voxel Plot Lab

## Introduction

In this lab, you will learn how to create a 3D voxel plot with RGB colors using Matplotlib. Voxel plots are a way of representing 3D data on a 2D plot by using cubes to represent the data points. The RGB colors will be used to represent the different values of the data.

## Steps

### Step 1: Importing Libraries

Before creating the plot, we need to import the required libraries. In this case, we will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Defining the Coordinates and Colors

Next, we need to define the coordinates and colors for the plot. In this example, we will use the `np.indices` function to create a 17x17x17 grid of values for the RGB colors.

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

We will also define a function `midpoints` to find the midpoints between the values in the grid. This will be used later to create the sphere.

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```

### Step 3: Creating the Sphere

We will now create a sphere in the plot by defining a condition for the RGB values that lie within a certain distance from the center of the plot.

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```

### Step 4: Combining the Colors

We will now combine the RGB color components into a single array of shape `(17, 17, 17, 3)`.

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```

### Step 5: Plotting the Voxel Plot

Finally, we can plot the voxel plot using the `ax.voxels` function. We will pass in the RGB values, the condition for the sphere, the face colors, edge colors, and linewidth.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```

## Summary

In this lab, we learned how to create a 3D voxel plot with RGB colors using Matplotlib. We imported the required libraries, defined the coordinates and colors, created a sphere, combined the colors, and plotted the voxel plot. Voxel plots are a useful way to represent 3D data on a 2D plot, and can be customized with different colors and shapes to represent different types of data.
