# Matplotlib Ellipse Collection Lab

## Introduction

Matplotlib is a powerful data visualization library in Python. In this lab, we will explore the use of `EllipseCollection` to draw a collection of ellipses.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import EllipseCollection
```

### Step 2: Create data for ellipses

We create data for our ellipses in the form of arrays of x-coordinates, y-coordinates, width, height and angle.

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```

### Step 3: Create Ellipse Collection

We create an `EllipseCollection` with the above data and specify the units to be 'x' and the offsets to be `XY`.

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```

### Step 4: Set the color of ellipses

We set the color of each ellipse in the `EllipseCollection` based on the sum of its x and y coordinate.

```python
ec.set_array((X + Y).ravel())
```

### Step 5: Add collection to the plot

We add the `EllipseCollection` to the plot.

```python
ax.add_collection(ec)
ax.autoscale_view()
ax.set_xlabel('X')
ax.set_ylabel('y')
cbar = plt.colorbar(ec)
cbar.set_label('X+Y')
plt.show()
```

## Summary

In this lab, we learned how to use `EllipseCollection` to draw a collection of ellipses in Matplotlib. We also learned how to set the color of each ellipse based on its x and y coordinate.
