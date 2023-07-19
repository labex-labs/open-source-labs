# Python Matplotlib 3D Surface Plotting Lab

## Introduction

This lab demonstrates how to create a 3D surface plot using Matplotlib in Python. The surface is plotted using a solid color. The lab will guide you through each step of the process, including creating the data, plotting the surface, and setting the aspect ratio.

## Steps

### Step 1: Importing Required Libraries

The first step is to import the required libraries. In this lab, we are using Matplotlib and NumPy libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating Data

The next step is to create the data for the 3D surface. We need to define `u`, `v`, `x`, `y`, and `z`. These variables will represent the angles and coordinates required to plot the surface. The `linspace()` function from NumPy is used to create the angles, and the `outer()` function is used to create the coordinates.

```python
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```

### Step 3: Creating the 3D Surface Plot

Now we can create the 3D surface plot. We start by creating a figure and adding a subplot with the `projection='3d'` argument. Then, we use the `plot_surface()` function to plot the surface using the data we created in the previous step.

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```

### Step 4: Setting the Aspect Ratio

To ensure that the plot has an equal aspect ratio, we can use the `set_aspect()` function. We pass in the string value `'equal'` to set the aspect ratio to 1:1.

```python
# Set an equal aspect ratio
ax.set_aspect('equal')
```

## Summary

This lab demonstrated how to create a 3D surface plot using Matplotlib in Python. We created the data, plotted the surface, and set the aspect ratio. The resulting plot is a basic 3D surface plot with a solid color.
