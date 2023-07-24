# Matplotlib Interactive Functions Lab

## Introduction

In this lab, we will learn how to use the interactive functions in Matplotlib. These interactive functions include ginput, waitforbuttonpress, and manual clabel placement. The purpose of this lab is to help you understand how to use these functions to create interactive plots in Matplotlib. By the end of this lab, you will be able to create and modify plots using interactive functions in Matplotlib.

## Steps

### Step 1: Define a Triangle by Clicking Three Points

In this step, we will define a triangle by clicking three points. We will use the `ginput` and `waitforbuttonpress` functions to achieve this. The `ginput` function allows us to select points on the plot with the mouse, and the `waitforbuttonpress` function waits for a button press event.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)

tellme('You will define a triangle, click to begin')

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme('Select 3 corners with mouse')
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme('Too few points, starting over')
            time.sleep(1)  # Wait a second

    ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=2)

    tellme('Happy? Key click for yes, mouse click for no')

    if plt.waitforbuttonpress():
        break

    # Get rid of fill
    for p in ph:
        p.remove()
```

### Step 2: Contour According to Distance from Triangle Corners

In this step, we will contour according to the distance from triangle corners. We will define a function of distance from individual points and contour according to this function.

```python
# Define a nice function of distance from individual pts
def f(x, y, pts):
    z = np.zeros_like(x)
    for p in pts:
        z = z + 1/(np.sqrt((x - p[0])**2 + (y - p[1])**2))
    return 1/z

X, Y = np.meshgrid(np.linspace(-1, 1, 51), np.linspace(-1, 1, 51))
Z = f(X, Y, pts)

CS = plt.contour(X, Y, Z, 20)

tellme('Use mouse to select contour label locations, middle button to finish')
CL = plt.clabel(CS, manual=True)
```

### Step 3: Zoom

In this step, we will zoom in on the plot. We will use the `ginput` function to select two corners of the zoom box and the `waitforbuttonpress` function to finish the zoom.

```python
tellme('Now do a nested zoom, click to begin')
plt.waitforbuttonpress()

while True:
    tellme('Select two corners of zoom, middle mouse button to finish')
    pts = plt.ginput(2, timeout=-1)
    if len(pts) < 2:
        break
    (x0, y0), (x1, y1) = pts
    xmin, xmax = sorted([x0, x1])
    ymin, ymax = sorted([y0, y1])
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

tellme('All Done!')
plt.show()
```

## Summary

In this lab, we learned how to use interactive functions in Matplotlib to create and modify plots. We used `ginput`, `waitforbuttonpress`, and manual `clabel` placement to define a triangle, contour according to the distance from triangle corners, and zoom in on the plot. By using these functions, we can create interactive plots that allow the user to interact with the data and explore it in more detail.
