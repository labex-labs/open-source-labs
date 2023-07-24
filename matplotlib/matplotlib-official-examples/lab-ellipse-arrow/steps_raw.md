# Matplotlib Ellipse with Orientation Arrow Lab

## Introduction

In this lab, you will learn how to draw an ellipse with an orientation arrow using Matplotlib. Ellipses are a type of shape that are commonly used in data visualization to represent data. By adding an orientation arrow to an ellipse, you can provide additional information about the direction of the data.

## Steps

### Step 1: Import Matplotlib and Create a Figure and Axis

First, you need to import Matplotlib and create a figure and axis. The figure and axis are the containers for your plot.

```python
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```

### Step 2: Create an Ellipse

Next, you need to create an ellipse using the `Ellipse` class. You can specify the center of the ellipse, the width and height of the ellipse, and the angle of rotation.

```python
from matplotlib.patches import Ellipse

ellipse = Ellipse(
    xy=(2, 4),
    width=30,
    height=20,
    angle=35,
    facecolor="none",
    edgecolor="b"
)
ax.add_patch(ellipse)
```

### Step 3: Add an Orientation Arrow

You can add an orientation arrow to the ellipse by plotting a marker at the end point of the minor axis. You can use the `get_co_vertices()` method to get the coordinates of the vertices of the ellipse. Then, you can use the `Affine2D()` class to rotate the marker to match the angle of the ellipse.

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# Plot an arrow marker at the end point of minor axis
vertices = ellipse.get_co_vertices()
t = Affine2D().rotate_deg(ellipse.angle)
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle(">", "full", t),
    markersize=10
)
```

### Step 4: Reverse the Orientation Arrow

If you want to reverse the orientation arrow, you can switch the marker type from `>` to `<`.

```python
# To reverse the orientation arrow, switch the marker type from > to <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```

### Step 5: Display the Plot

Finally, you can display the plot using the `show()` method.

```python
plt.show()
```

## Summary

Congratulations! You have learned how to draw an ellipse with an orientation arrow using Matplotlib. This technique can be useful for visualizing data that has a direction.
