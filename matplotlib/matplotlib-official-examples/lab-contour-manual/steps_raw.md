# Matplotlib Tutorial Lab

## Manual Contour

### Introduction

This lab will guide you on how to display your own contour lines and polygons using ContourSet in Matplotlib. Contour lines for each level are a list/tuple of polygons. Filled contours between two levels are also a list/tuple of polygons. Points can be ordered clockwise or anticlockwise.

### Steps

### Step 1: Import the necessary libraries

The first step is to import the necessary libraries. In this lab, we will be using Matplotlib.

```python
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.contour import ContourSet
from matplotlib.path import Path
```

### Step 2: Define the contour lines and polygons

The next step is to define the contour lines and polygons. In this example, we have lines and filled contours between two levels.

```python
# Contour lines for each level are a list/tuple of polygons.
lines0 = [[[0, 0], [0, 4]]]
lines1 = [[[2, 0], [1, 2], [1, 3]]]
lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]  # Note two lines.

# Filled contours between two levels are also a list/tuple of polygons.
# Points can be ordered clockwise or anticlockwise.
filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]],   # Note two polygons.
            [[1, 4], [3, 4], [3, 3]]]
```

### Step 3: Create the plot

The next step is to create the plot. This can be done using the ContourSet function.

```python
fig, ax = plt.subplots()

# Filled contours using filled=True.
cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
cbar = fig.colorbar(cs)

# Contour lines (non-filled).
lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='User-specified contours')
```

### Step 4: Create filled contours with holes

Multiple filled contour lines can be specified in a single list of polygon vertices along with a list of vertex kinds (code types) as described in the Path class. This is particularly useful for polygons with holes.

```python
fig, ax = plt.subplots()
filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
M = Path.MOVETO
L = Path.LINETO
kinds01 = [[M, L, L, L, M, L, L, L]]
cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
cbar = fig.colorbar(cs)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 3.5),
       title='User specified filled contours with holes')
```

### Summary

In this lab, we learned how to display our own contour lines and polygons using ContourSet in Matplotlib. We defined the contour lines and polygons, created the plot, and created filled contours with holes.
