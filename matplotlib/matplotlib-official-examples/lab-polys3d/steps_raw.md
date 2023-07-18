# Python Matplotlib Tutorial: Creating Polygons to Fill Under 3D Line Graph

## Introduction

In this tutorial, we will learn how to create polygons which fill the space under a line graph in a 3D plot using Python's Matplotlib library. The polygons will be semi-transparent, creating a sort of 'jagged stained glass' effect.

## Steps

### Step 1: Import the Required Libraries

We will begin by importing the necessary libraries.

```python
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection
```

### Step 2: Define the Polygon Under Graph Function

Next, we define a function `polygon_under_graph(x, y)` which constructs the vertex list that defines the polygon filling the space under the (x, y) line graph. This function assumes that x is in ascending order.

```python
def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```

### Step 3: Create the 3D Plot

We will now create a 3D plot using Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')
```

### Step 4: Define the x and lambda Arrays

We define the x and lambda arrays using the `linspace` and `range` functions respectively.

```python
x = np.linspace(0., 10., 31)
lambdas = range(1, 9)
```

### Step 5: Compute the Vertices and Facecolors

We compute the vertices and facecolors using the `vectorize` and `colormaps` functions from Matplotlib.

```python
# verts[i] is a list of (x, y) pairs defining polygon i.
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```

### Step 6: Create the Polygons and Add to the Plot

We create the polygons using the `PolyCollection` function from Matplotlib and add them to the plot.

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```

### Step 7: Set the Plot Limits and Labels

Finally, we set the plot limits and labels using the `set` function.

```python
ax.set(xlim=(0, 10), ylim=(1, 9), zlim=(0, 0.35),
       xlabel='x', ylabel=r'$\lambda$', zlabel='probability')
```

### Step 8: Show the Plot

We display the plot using the `show` function.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create polygons which fill the space under a line graph in a 3D plot using Python's Matplotlib library. We used the `PolyCollection` function to create the polygons and set the plot limits and labels using the `set` function.
