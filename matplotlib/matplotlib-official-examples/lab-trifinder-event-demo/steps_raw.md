# Matplotlib Triangulation Lab

## Introduction

This lab will guide you through creating a triangulation plot using Matplotlib. You will learn how to create a Triangulation object, use a TriFinder object, and set up interactivity to highlight the triangle under the cursor.

## Steps

### Step 1: Create Triangulation Object

First, we need to create a Triangulation object. We will use the `Triangulation` class from `matplotlib.tri`. In this example, we will create a Triangulation object with random data.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Generate random data
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```

### Step 2: Create TriFinder Object

To find the triangle under the cursor, we need to create a TriFinder object. We can get the default TriFinder object from the Triangulation object using the `get_trifinder()` method.

```python
trifinder = triang.get_trifinder()
```

### Step 3: Set up Plot

Now, we can set up the plot. We will use `plt.subplots()` to create a figure and axis object. Then, we will use `ax.triplot()` to plot the triangulation.

```python
fig, ax = plt.subplots()
ax.triplot(triang)
```

### Step 4: Highlight Triangle Under Cursor

We want to highlight the triangle under the cursor as the mouse is moved over the plot. To do this, we will create a `Polygon` object that will be updated with the vertices of the triangle under the cursor. We will use `ax.add_patch()` to add the polygon to the plot.

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

We will also create a function `update_polygon()` that will update the vertices of the polygon with the vertices of the triangle under the cursor.

```python
def update_polygon(tri):
    if tri == -1:
        points = [0, 0, 0]
    else:
        points = triang.triangles[tri]
    xs = triang.x[points]
    ys = triang.y[points]
    polygon.set_xy(np.column_stack([xs, ys]))
```

### Step 5: Set up Interactivity

We need to set up interactivity to update the triangle under the cursor. We will use the `motion_notify_event` to detect when the mouse is moved over the plot. We will create a function `on_mouse_move()` that will get the triangle under the cursor using the TriFinder object, update the polygon with the vertices of the triangle, and update the plot title with the index of the triangle.

```python
def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'Triangle {tri}')
    event.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
```

### Step 6: Show Plot

Finally, we can show the plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a triangulation plot using Matplotlib. We used the `Triangulation` and `TriFinder` classes to create a triangulation and find the triangle under the cursor. We also set up interactivity to highlight the triangle under the cursor.
