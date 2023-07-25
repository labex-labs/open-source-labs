# Matplotlib Tutorial - Drawing a Curve with Error Band

## Introduction

This tutorial will guide you on how to draw a curve with an error band using Python Matplotlib. An error band is used to indicate the uncertainty of the curve. In this example, we assume that the error can be given as a scalar _err_ that describes the uncertainty perpendicular to the curve in every point. We visualize this error as a colored band around the path using a `.PathPatch`. The patch is created from two path segments _(xp, yp)_, and _(xn, yn)_ that are shifted by +/- _err_ perpendicular to the curve _(x, y)_.

## Steps

### Step 1: Import Required Libraries

The first step is to import the required libraries. We will be using Matplotlib, NumPy, PathPatch, and Path.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path
```

### Step 2: Define the Curve

Next, we define the curve that we want to draw the error band around. In this example, we will be using a parametrized curve. A parametrized curve x(t), y(t) can directly be drawn using `~.Axes.plot`.

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```

### Step 3: Define the Error Band

We will now define the error band that we want to draw around the curve. In this example, we will be assuming that the error can be given as a scalar _err_ that describes the uncertainty perpendicular to the curve in every point.

```python
def draw_error_band(ax, x, y, err, **kwargs):
    # Calculate normals via centered finite differences (except the first point
    # which uses a forward difference and the last point which uses a backward
    # difference).
    dx = np.concatenate([[x[1] - x[0]], x[2:] - x[:-2], [x[-1] - x[-2]]])
    dy = np.concatenate([[y[1] - y[0]], y[2:] - y[:-2], [y[-1] - y[-2]]])
    l = np.hypot(dx, dy)
    nx = dy / l
    ny = -dx / l

    # end points of errors
    xp = x + nx * err
    yp = y + ny * err
    xn = x - nx * err
    yn = y - ny * err

    vertices = np.block([[xp, xn[::-1]],
                         [yp, yn[::-1]]]).T
    codes = np.full(len(vertices), Path.LINETO)
    codes[0] = codes[len(xp)] = Path.MOVETO
    path = Path(vertices, codes)
    ax.add_patch(PathPatch(path, **kwargs))
```

### Step 4: Draw the Error Band

We can now draw the error band by calling the `draw_error_band` function and passing in the appropriate parameters.

```python
fig, axs = plt.subplots(1, 2, layout='constrained', sharex=True, sharey=True)
errs = [
    (axs[0], "constant error", 0.05),
    (axs[1], "variable error", 0.05 * np.sin(2 * t) ** 2 + 0.04),
]
for i, (ax, title, err) in enumerate(errs):
    ax.set(title=title, aspect=1, xticks=[], yticks=[])
    ax.plot(x, y, "k")
    draw_error_band(ax, x, y, err=err,
                    facecolor=f"C{i}", edgecolor="none", alpha=.3)

plt.show()
```

### Step 5: View the Error Band

The error band should now be visible around the curve.

## Summary

In this tutorial, we have learned how to draw a curve with an error band using Python Matplotlib. We started by importing the required libraries, defining the curve, defining the error band, drawing the error band, and viewing the error band.
