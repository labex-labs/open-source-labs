# Python Matplotlib Tutorial - Creating a Compound Path

## Introduction

In this tutorial, we will learn how to create a compound path using Matplotlib in Python. A compound path is a collection of simple paths that can be used to create complex shapes. We will create a compound path by combining two simple polygons, a rectangle, and a triangle.

## Steps

### Step 1: Importing the Required Libraries

We will start by importing the required libraries. We need `matplotlib.pyplot` for creating the plot, `matplotlib.patches` for creating patches, `matplotlib.path.Path` for creating paths, and `numpy` for creating arrays.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import numpy as np
```

### Step 2: Creating the Vertices and Codes

We will create the vertices and codes for the two polygons that we want to combine into a compound path. We will use `Path.MOVETO` to move the cursor to the starting point of the polygon, `Path.LINETO` to create a line from the starting point to the next point, and `Path.CLOSEPOLY` to close the polygon.

```python
vertices = []
codes = []

# First Polygon - Rectangle
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# Second Polygon - Triangle
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```

### Step 3: Creating the Path

We will use `Path` to create the path from the vertices and codes that we created in the previous step.

```python
path = Path(vertices, codes)
```

### Step 4: Creating the PathPatch

We will create a `PathPatch` from the path that we created in the previous step. We will set the `facecolor` to `'none'` and the `edgecolor` to `'green'`.

```python
pathpatch = PathPatch(path, facecolor='none', edgecolor='green')
```

### Step 5: Creating the Plot

We will create the plot and add the `PathPatch` to the plot. We will set the title of the plot to `'A Compound Path'`.

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```

## Summary

In this tutorial, we learned how to create a compound path using Matplotlib in Python. We created a compound path by combining two simple polygons, a rectangle, and a triangle. We used `Path` to create the path from the vertices and codes, and `PathPatch` to create a patch from the path. Finally, we added the patch to the plot to display the compound path.
