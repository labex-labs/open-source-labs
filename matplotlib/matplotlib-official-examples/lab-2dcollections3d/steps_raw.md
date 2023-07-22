# Matplotlib 2D Data on 3D Plot

## Introduction

This lab demonstrates how to plot 2D data on selective axes of a 3D plot using `ax.plot`'s `zdir` keyword. The `matplotlib` library in Python is used to create the 3D plot.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries. We need `matplotlib` and `numpy` to plot the 3D graph.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a 3D Plot

The second step is to create a 3D plot using `ax = plt.figure().add_subplot(projection='3d')`.

```python
ax = plt.figure().add_subplot(projection='3d')
```

### Step 3: Plot 2D Data on the 3D Plot

The third step is to plot 2D data on the 3D plot using `ax.plot` and `ax.scatter`. The `ax.plot` function plots a sin curve using the x and y axes. The `ax.scatter` function plots scatterplot data on the x and z axes.

```python
# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ('r', 'g', 'b', 'k')

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# By using zdir='y', the y value of these points is fixed to the zs value 0
# and the (x, y) points are plotted on the x and z axes.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')
```

### Step 4: Customize the Plot

The fourth step is to customize the plot by adding a legend, setting axes limits and labels, and changing the view angle.

```python
# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()
```

### Step 5: View the Plot

The final step is to view the 3D plot by running the code.

## Summary

In this lab, we learned how to plot 2D data on selective axes of a 3D plot using `ax.plot`'s `zdir` keyword. We also learned how to customize the plot by adding a legend, setting axes limits and labels, and changing the view angle.
