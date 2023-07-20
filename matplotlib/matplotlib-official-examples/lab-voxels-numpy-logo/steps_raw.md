# 3D Voxel Plot of the NumPy Logo

## Introduction

This lab demonstrates how to use the `Axes3D.voxels` function in Matplotlib to create a 3D voxel plot of the NumPy logo.

## Steps

### Step 1: Import libraries

First, we need to import the necessary libraries, which are Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the explode function

Next, we define a function called `explode` that will be used to upscale the voxel image of the NumPy logo. This function takes in a NumPy array as its input and returns a new NumPy array that is twice the size of the input array.

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```

### Step 3: Build the NumPy logo

Now we can begin to build the NumPy logo using a 3D NumPy array called `n_voxels`. We set certain elements in the array to True to represent the logo's shape. We also define two other NumPy arrays called `facecolors` and `edgecolors` that will be used to color the voxels.

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```

### Step 4: Upscale the voxel image

We now use the `explode` function defined earlier to upscale the voxel image, leaving gaps between each voxel.

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```

### Step 5: Shrink the gaps

We shrink the gaps between each voxel by modifying the coordinates of each voxel using NumPy's `indices` function.

```python
x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
x[0::2, :, :] += 0.05
y[:, 0::2, :] += 0.05
z[:, :, 0::2] += 0.05
x[1::2, :, :] += 0.95
y[:, 1::2, :] += 0.95
z[:, :, 1::2] += 0.95
```

### Step 6: Create the voxel plot

Finally, we create the 3D voxel plot using the `voxels` function of the `Axes3D` class in Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```

## Summary

This lab demonstrated how to create a 3D voxel plot of the NumPy logo using Matplotlib. We used NumPy to build the logo, and the `Axes3D.voxels` function to create the plot. We also used a function called `explode` to upscale the voxel image of the logo.
