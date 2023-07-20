# Changing Line Colors of a Rectangle

## Introduction

In this lab, we will learn how to change the colors of lines intersecting a rectangle using the `.intersects_bbox` function from Matplotlib. We will create a rectangle and generate random lines that intersect it. Then, we will change the color of the intersecting lines to red and the remaining lines to blue.

## Steps

### Step 1: Import the required libraries

We will import `matplotlib.pyplot` and `numpy` libraries to create the rectangle and generate random lines.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Set up the rectangle

We will define the position and dimensions of the rectangle using `left`, `bottom`, `width`, and `height` variables. Then, we will create the rectangle using `Rectangle` class and add it to the plot using `add_patch` method.

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```

### Step 3: Generate random lines

We will generate 12 random lines using `numpy` library and plot them using `plot` method. If a line intersects the rectangle, its color will be red, otherwise blue. We will use `Path` class to create a line and `intersects_bbox` method to check if it intersects the rectangle.

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```

### Step 4: Display the plot

We will display the plot using `show` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to change the colors of lines intersecting a rectangle using the `.intersects_bbox` function from Matplotlib. We created a rectangle and generated random lines that intersected it. Then, we changed the color of the intersecting lines to red and the remaining lines to blue.
