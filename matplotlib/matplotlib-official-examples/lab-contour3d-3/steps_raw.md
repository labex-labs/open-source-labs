# Matplotlib 3D Surface and Contour Plotting Lab

## Introduction

This lab demonstrates how to create a 3D surface plot and project contour 'profiles' onto the walls of the graph using Matplotlib.

## Steps

### Step 1: Import necessary libraries

In this step, we will import the necessary libraries for creating the 3D surface plot and projecting contour profiles.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
```

### Step 2: Create 3D figure and data

In this step, we will create a 3D figure and get test data for the surface plot.

```python
# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Get test data for the surface plot
X, Y, Z = axes3d.get_test_data(0.05)
```

### Step 3: Plot the 3D surface

In this step, we will plot the 3D surface with the test data and customize the appearance of the plot.

```python
# Plot the 3D surface
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# Customize the appearance of the plot
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```

### Step 4: Project contour profiles onto the walls of the graph

In this step, we will project contour profiles onto the walls of the graph by plotting the contours for each dimension with appropriate offsets.

```python
# Plot projections of the contours for each dimension
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```

### Step 5: Display the plot

In this step, we will display the 3D surface plot with projected contour profiles.

```python
plt.show()
```

## Summary

This lab demonstrated how to create a 3D surface plot and project contour profiles onto the walls of the graph using Matplotlib. The steps included importing necessary libraries, creating a 3D figure and data, plotting the 3D surface, projecting contour profiles, and displaying the plot.
