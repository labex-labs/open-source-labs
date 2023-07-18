# Matplotlib 3D Voxel Plot Lab

## Introduction

In this lab, you will learn how to create a 3D voxel plot using cylindrical coordinates in Matplotlib. The plot will demonstrate how to use the _x_, _y_, and _z_ parameters of `.Axes3D.voxels` to create a 3D voxel plot.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries for this lab. We will be using `matplotlib.pyplot`, `numpy`, and `matplotlib.colors`.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors
```

### Step 2: Define Midpoints Function

Next, we define a `midpoints` function to calculate the midpoints of an array of coordinates. This function will be used later to calculate the midpoints of `r`, `theta`, and `z`.

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```

### Step 3: Define Coordinates and RGB Values

In this step, we define the coordinates `r`, `theta`, and `z`, and attach RGB values to each.

```python
r, theta, z = np.mgrid[0:1:11j, 0:np.pi*2:25j, -0.5:0.5:11j]
x = r*np.cos(theta)
y = r*np.sin(theta)

rc, thetac, zc = midpoints(r), midpoints(theta), midpoints(z)

# define a wobbly torus about [0.7, *, 0]
sphere = (rc - 0.7)**2 + (zc + 0.2*np.cos(thetac*2))**2 < 0.2**2

# combine the color components
hsv = np.zeros(sphere.shape + (3,))
hsv[..., 0] = thetac / (np.pi*2)
hsv[..., 1] = rc
hsv[..., 2] = zc + 0.5
colors = matplotlib.colors.hsv_to_rgb(hsv)
```

### Step 4: Create the 3D Voxel Plot

Now we create the 3D voxel plot using the `ax.voxels` function. We pass in `x`, `y`, `z`, and `sphere` as the parameters. We also add `facecolors` and `edgecolors` using the `colors` array we defined earlier.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
```

### Step 5: Display the Plot

Finally, we display the plot using the `plt.show()` function.

```python
plt.show()
```

## Summary

In this lab, you learned how to create a 3D voxel plot using cylindrical coordinates in Matplotlib. You also learned how to define coordinates and RGB values and how to create a 3D voxel plot using the `ax.voxels` function.
