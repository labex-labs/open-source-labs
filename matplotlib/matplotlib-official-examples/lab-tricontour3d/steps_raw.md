# Triangular 3D Contour Plot Lab

## Introduction

In this lab, we will create a triangular 3D contour plot using Matplotlib. This plot is useful for visualizing unstructured triangular grids. We will be using the same data as in the second plot of trisurf3d_2.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries for this lab, which include Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri
```

### Step 2: Define variables

We will define the variables that we will use to create our plot. These variables include the number of angles, number of radii, and the minimum radius.

```python
n_angles = 48
n_radii = 8
min_radius = 0.25
```

### Step 3: Create mesh and compute x, y, z

We will create the mesh in polar coordinates and compute x, y, z using the defined variables.

```python
radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles

x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```

### Step 4: Create custom triangulation

We will create a custom triangulation using the x and y coordinates.

```python
triang = tri.Triangulation(x, y)
```

### Step 5: Mask off unwanted triangles

We will mask off the unwanted triangles using the mean of the x and y coordinates.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

### Step 6: Create 3D contour plot

We will create a 3D contour plot using the created triangulation and the z coordinates. We will also customize the view angle so it's easier to understand the plot.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```

## Summary

In this lab, we created a triangular 3D contour plot using Matplotlib. We went through the steps of importing the necessary libraries, defining variables, creating a mesh, creating a custom triangulation, masking off unwanted triangles, and creating the 3D contour plot.
