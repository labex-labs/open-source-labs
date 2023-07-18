# Matplotlib ConnectionPatch Lab

## Introduction

Matplotlib is a powerful data visualization library in Python. It provides a variety of visualization tools to create stunning graphics and charts. In this lab, we will learn about ConnectionPatch, which is used to draw a line between points defined in different coordinate systems and/or axes.

## Steps

### Step 1: Import the necessary libraries

Before we start, let's import the necessary libraries.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
```

### Step 2: Create the plot

Next, let's create the plot with two subplots.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))
```

### Step 3: Draw a simple arrow

Now, let's draw a simple arrow between two points in axes coordinates within a single axes.

```python
xyA = (0.2, 0.2)
xyB = (0.8, 0.8)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
                      arrowstyle="-|>", shrinkA=5, shrinkB=5,
                      mutation_scale=20, fc="w")
ax1.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], "o")
ax1.add_artist(con)
```

### Step 4: Draw an arrow between different axes

Let's draw an arrow between the same point in data coordinates, but in different axes.

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```

### Step 5: Draw a line between the different points

Finally, let's draw a line between the different points, defined in different coordinate systems.

```python
con = ConnectionPatch(
    # in axes coordinates
    xyA=(0.6, 1.0), coordsA=ax2.transAxes,
    # x in axes coordinates, y in data coordinates
    xyB=(0.0, 0.2), coordsB=ax2.get_yaxis_transform(),
    arrowstyle="-")
ax2.add_artist(con)
```

### Summary

In this lab, we learned about ConnectionPatch, which is used to draw a line between points defined in different coordinate systems and/or axes. We also learned how to draw a simple arrow and a line between different points in a plot.
