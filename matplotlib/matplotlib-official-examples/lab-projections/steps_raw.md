# **3D Plot Projection Types Lab**

## Introduction

This lab demonstrates the different camera projections for 3D plots, and the effects of changing the focal length for a perspective projection using Python Matplotlib.

## Steps

### Step 1: Import Libraries

First, import the necessary libraries, including Matplotlib and Axes3D from mpl_toolkits.mplot3d.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
```

### Step 2: Get Data

Get the test data for the 3D plot.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```

### Step 3: Create a Figure with Subplots

Create a figure with three subplots using `plt.subplots`.

```python
fig, axs = plt.subplots(1, 3, subplot_kw={'projection': '3d'})
```

### Step 4: Plot the Data

Plot the data on each of the three subplots using `plot_wireframe`.

```python
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```

### Step 5: Set the Orthographic Projection

Set the first subplot to use an orthographic projection with a `FOV` of 0 degrees and a `focal_length` of infinity.

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```

### Step 6: Set the Perspective Projections

Set the second subplot to use a perspective projection with the default `FOV` of 90 degrees and a `focal_length` of 1.

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

Set the third subplot to use a perspective projection with a `FOV` of 157.4 degrees and a `focal_length` of 0.2.

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```

### Step 7: Show the Plot

Display the plot using `plt.show()`.

```python
plt.show()
```

## Summary

This lab demonstrated how to create a 3D plot using Python Matplotlib and how to change the projection type and focal length of the plot. The orthographic projection flattens the image while the perspective projection exaggerates the perspective and gives the image more apparent depth. The default focal length of 1 corresponds to a Field of View (FOV) of 90 deg.
