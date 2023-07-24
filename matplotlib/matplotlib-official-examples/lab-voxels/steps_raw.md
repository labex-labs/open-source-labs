# 3D Voxel Plotting with Matplotlib

## Introduction

This lab will guide you through the process of creating a 3D voxel plot using the Matplotlib library in Python. Voxel plots are useful for visualizing 3D data in a way that is both clear and aesthetically pleasing. In this lab, we will be using the `Axes3D.voxels` function to create a voxel plot of two cubes and a link between them.

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries. In this case, we will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Prepare coordinates

Next, we will prepare the coordinates for our voxel plot. We will be creating an 8x8x8 grid of points using NumPy's `indices` function.

```python
x, y, z = np.indices((8, 8, 8))
```

### Step 3: Create the cubes and link

Now, we will create the two cubes and the link between them. We will do this by defining three boolean arrays that will be combined into a single boolean array. The first two arrays define the location of the cubes, while the third array defines the location of the link.

```python
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

voxelarray = cube1 | cube2 | link
```

### Step 4: Set colors

We will now set the colors for each object in the voxel plot. We will do this by creating an empty array of the same shape as the boolean array we created in Step 3, and then setting the color of each object based on its location.

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```

### Step 5: Plot the voxel array

Finally, we can use the `Axes3D.voxels` function to plot the voxel array with the specified colors.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```

## Summary

In this lab, we learned how to create a 3D voxel plot using the Matplotlib library in Python. We prepared the coordinates for the plot, created the cubes and link, set the colors for each object, and plotted the voxel array using the `Axes3D.voxels` function. Voxel plots are a useful way to visualize 3D data, and Matplotlib makes it easy to create them.
