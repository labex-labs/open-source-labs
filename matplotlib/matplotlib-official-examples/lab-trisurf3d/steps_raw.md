# Triangular 3D Surfaces Lab

## Introduction

In this lab, we will learn how to create a 3D surface with a triangular mesh using Python Matplotlib library.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries:

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define Variables

We will define the variables for the radii and angles:

```python
n_radii = 8
n_angles = 36
```

### Step 3: Create Radii and Angles Spaces

We will create the radii and angles spaces using the `linspace` function:

```python
# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]
```

### Step 4: Convert Polar Coordinates to Cartesian Coordinates

We will convert the polar coordinates to Cartesian coordinates:

```python
# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage, so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())
```

### Step 5: Compute Z to Make the Pringle Surface

We will compute z to make the pringle surface:

```python
# Compute z to make the pringle surface.
z = np.sin(-x*y)
```

### Step 6: Create the 3D Surface

We will create the 3D surface using the `plot_trisurf` function:

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```

## Summary

In this lab, we have learned how to create a 3D surface with a triangular mesh using Python Matplotlib library. We have imported the necessary libraries, defined the variables for the radii and angles, created the radii and angles spaces, converted the polar coordinates to Cartesian coordinates, computed z to make the pringle surface, and created the 3D surface using the `plot_trisurf` function.
