# Projecting Filled Contour onto a 3D Graph

## Introduction

This lab will guide you through the process of creating a 3D surface graph with filled contour profiles projected onto the walls of the graph. This is a useful visualization technique for understanding complex 3D data. We will be using Python's Matplotlib library to create the graph.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
```

### Step 2: Create 3D Axes

Next, we will create a 3D axis object using the `add_subplot` method.

```python
ax = plt.figure().add_subplot(projection='3d')
```

### Step 3: Create Data

We will use the `axes3d.get_test_data` method to create sample data for our graph.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```

### Step 4: Plot the 3D Surface

We will plot the 3D surface using the `plot_surface` method. We will also set some parameters such as edgecolor, linewidth, and alpha.

```python
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)
```

### Step 5: Project Contour Profiles

We will now project the contour profiles onto the walls of the graph. This is done using the `contourf` method. We will set the `zdir` parameter to 'z', 'x', and 'y' to project the contour profiles onto the z, x, and y walls respectively. We will also set the `offset` parameter to match the appropriate axes limits.

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```

### Step 6: Set Graph Limits and Labels

Finally, we will set the limits and labels for the graph axes.

```python
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```

### Summary

This lab provided a step-by-step guide to creating a 3D surface graph with filled contour profiles projected onto the walls of the graph. We used Python's Matplotlib library to create the graph.
