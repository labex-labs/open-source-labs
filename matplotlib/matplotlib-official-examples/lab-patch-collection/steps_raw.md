# Python Matplotlib Tutorial

## Introduction

This tutorial is designed to guide users on how to create circles, wedges and polygons using Python Matplotlib. Users will also be able to use `.collections.PatchCollection` to visualize the created shapes.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Polygon, Wedge
```

### Step 2: Create a figure and an axis

We create a figure and an axis to plot the shapes.

```python
fig, ax = plt.subplots()
```

### Step 3: Define the number of vertices and the number of shapes

We define the number of vertices and the number of shapes to create.

```python
resolution = 50  # the number of vertices
N = 3
```

### Step 4: Create circles

We create circles using `Circle()` and append them to a list of patches.

```python
x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1*np.random.rand(N)
patches = []
for x1, y1, r in zip(x, y, radii):
    circle = Circle((x1, y1), r)
    patches.append(circle)
```

### Step 5: Create wedges

We create wedges using `Wedge()` and append them to the list of patches.

```python
x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1*np.random.rand(N)
theta1 = 360.0*np.random.rand(N)
theta2 = 360.0*np.random.rand(N)
for x1, y1, r, t1, t2 in zip(x, y, radii, theta1, theta2):
    wedge = Wedge((x1, y1), r, t1, t2)
    patches.append(wedge)
```

### Step 6: Add limiting conditions to wedges

We add limiting conditions to wedges.

```python
patches += [
    Wedge((.3, .7), .1, 0, 360),             # Full circle
    Wedge((.7, .8), .2, 0, 360, width=0.05),  # Full ring
    Wedge((.8, .3), .2, 0, 45),              # Full sector
    Wedge((.8, .3), .2, 45, 90, width=0.10),  # Ring sector
]
```

### Step 7: Create polygons

We create polygons using `Polygon()` and append them to the list of patches.

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```

### Step 8: Set colors and create PatchCollection

We set the colors of the shapes and create a `PatchCollection()`.

```python
colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)
```

### Step 9: Display the plot

We display the plot.

```python
plt.show()
```

## Summary

This tutorial has shown how to create circles, wedges, and polygons using Python Matplotlib. We have also learned how to use `.collections.PatchCollection` to visualize the created shapes.
