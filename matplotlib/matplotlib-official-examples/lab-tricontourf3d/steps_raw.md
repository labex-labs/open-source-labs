# Triangular 3D Contour Plot Lab

## Introduction

In this lab, you will learn how to create a triangular 3D filled contour plot using the Matplotlib library in Python. The plot will be created using unstructured triangular grids and customized triangulation. You will be able to control the view angle and color map of the plot.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries. In this case, we will need Matplotlib, Numpy, and Matplotlib Tri.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri
```

### Step 2: Create the Coordinates

Next, we will create the x, y, z coordinates of the points. We will create the mesh in polar coordinates and compute x, y, z.

```python
n_angles = 48
n_radii = 8
min_radius = 0.25

radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles

x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```

### Step 3: Create a Custom Triangulation

In this step, we will create a custom triangulation and mask off unwanted triangles.

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

### Step 4: Create the Plot

Now, we will create the plot using the `tricontourf()` function and customize the view angle.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```

## Summary

In this lab, you learned how to create a triangular 3D filled contour plot using Matplotlib in Python. You learned how to create the coordinates, create a custom triangulation, and customize the view angle and color map of the plot.
