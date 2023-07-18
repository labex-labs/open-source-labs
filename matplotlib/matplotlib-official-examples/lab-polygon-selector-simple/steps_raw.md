# Creating a Polygon in Matplotlib

## Introduction

Matplotlib is a Python library used for data visualization. In this lab, we will be using Matplotlib to create a polygon programmatically or interactively. The polygon can be used to highlight a region of interest or to mask out a certain area of a plot.

## Steps

### Step 1: Import Required Libraries

Before we start working with Matplotlib, we need to import the necessary libraries. We will be using `matplotlib.pyplot` and `matplotlib.widgets` in this lab.

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector
```

### Step 2: Create a Polygon Programmatically

To create a polygon programmatically, we need to create a `Figure` object and an `Axes` object. Then, we can create a `PolygonSelector` object and add vertices to it. Finally, we can plot the polygon on the `Axes`.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# Add three vertices
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```

### Step 3: Create a Polygon Interactively

To create a polygon interactively, we need to create a `Figure` object and an `Axes` object. Then, we can create a `PolygonSelector` object and add vertices to it by clicking on the plot. We can also use the `shift` and `ctrl` keys to move the vertices.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")

plt.show()
```

### Step 4: Putting It All Together

Let's create a complete example that includes both creating a polygon programmatically and interactively.

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# Create a figure and axes
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# Create a PolygonSelector object and add vertices
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# Create another PolygonSelector object for interactive creation
selector2 = PolygonSelector(ax2, lambda *args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")

plt.show()
```

## Summary

In this lab, we learned how to create a polygon programmatically and interactively using Matplotlib. We also learned how to add vertices to a `PolygonSelector` object and plot the resulting polygon on an `Axes`. This knowledge can be useful for highlighting regions of interest or masking out certain areas in a plot.
