# 3D Plots as Subplots Lab

## Introduction

In data analysis, it's often necessary to create 3D plots to visualize data. In Matplotlib, we can create 3D plots as subplots to compare different 3D data. This lab will demonstrate how to create 3D plots as subplots using Matplotlib.

## Steps

### Step 1: Import Libraries

Before we start, we need to import the libraries that we will use in this lab. We will use Matplotlib, NumPy, and Axes3D from mpl_toolkits.mplot3d.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
```

### Step 2: Create the Figure and Subplots

We will create a figure with two subplots. The first subplot will be a 3D surface plot, and the second subplot will be a 3D wireframe plot.

```python
# Create a figure with two subplots
fig = plt.figure(figsize=plt.figaspect(0.5))

# Add the first subplot with 3D projection
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Add the second subplot with 3D projection
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```

### Step 3: Create the 3D Surface Plot

We will create a 3D surface plot for the first subplot. We will use NumPy to create the data for the plot.

```python
# Create data for the 3D surface plot
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the 3D surface plot
surf = ax1.plot_surface(X, Y, Z, cmap='coolwarm', linewidth=0, antialiased=False)

# Add a color bar to the plot
fig.colorbar(surf, shrink=0.5, aspect=10)

# Set the limits for the z-axis
ax1.set_zlim(-1.01, 1.01)
```

### Step 4: Create the 3D Wireframe Plot

We will create a 3D wireframe plot for the second subplot. We will use the `get_test_data` function from mpl_toolkits.mplot3d.axes3d to create the data for the plot.

```python
# Create data for the 3D wireframe plot
X, Y, Z = Axes3D.get_test_data(0.05)

# Plot the 3D wireframe plot
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```

### Step 5: Show the Plot

We will use the `plt.show()` function to display the plot.

```python
plt.show()
```

## Summary

In this lab, we learned how to create 3D plots as subplots using Matplotlib. We created a figure with two subplots, a 3D surface plot, and a 3D wireframe plot. We used NumPy to create the data for the 3D surface plot and the `get_test_data` function from mpl_toolkits.mplot3d.axes3d to create the data for the 3D wireframe plot. We also added a color bar to the 3D surface plot and set the limits for the z-axis.
