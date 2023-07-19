# More Triangular 3D Surfaces Tutorial

## Introduction

This tutorial demonstrates how to create 3D surfaces using triangular mesh in Python's Matplotlib library. It shows two examples of plotting surfaces with triangular mesh.

## Steps

### Step 1: Import Required Libraries

We begin by importing the required libraries: `matplotlib.pyplot` and `numpy`. We also import `matplotlib.tri` to create the triangular meshes.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as mtri
```

### Step 2: Create a Mesh

We create a mesh in the space of parameterization variables `u` and `v`. This is done using the `np.meshgrid()` function to create a grid of `u` and `v` points.

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```

### Step 3: Define the Surface

Next, we define the surface. In this example, we use a Mobius mapping to take a `u`, `v` pair and return an `x`, `y`, `z` triple.

```python
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)
```

### Step 4: Triangulate Parameter Space

We triangulate the parameter space to determine the triangles that will connect the `x`, `y`, `z` points.

```python
tri = mtri.Triangulation(u, v)
```

### Step 5: Plot the Surface

Finally, we plot the surface using `plot_trisurf()` function. The triangles in parameter space determine which `x`, `y`, `z` points are connected by an edge.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```

### Step 6: Create a Mask

In this example, we create a mask to remove unwanted triangles. We first create parameter spaces `radii` and `angles`.

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles
```

### Step 7: Map to `x`, `y`, `z` Points

We map the `radius`, `angle` pairs to `x`, `y`, `z` points.

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```

### Step 8: Create Triangulation

We create the triangulation using the `Triangulation()` function. Since there are no triangles, the Delaunay triangulation is created.

```python
triang = mtri.Triangulation(x, y)
```

### Step 9: Mask Off Unwanted Triangles

We mask off unwanted triangles by calculating the midpoint of each triangle and checking if it falls within a given radius.

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```

### Step 10: Plot the Surface

Finally, we plot the surface using `plot_trisurf()` function.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```

## Summary

This tutorial demonstrated how to create 3D surfaces using triangular mesh in Python's Matplotlib library. We covered the steps involved in creating a mesh, defining the surface, triangulating parameter space, creating a mask, and plotting the surface.
