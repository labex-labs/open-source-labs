# Python Matplotlib Lab

## Ellipse Comparison

### Introduction

In this lab, you will learn how to compare the ellipse generated with arcs versus a polygonal approximation using Python Matplotlib.

### Steps

#### Step 1: Import Libraries

To begin, we will import the necessary libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
```

#### Step 2: Set Ellipse Parameters

In this step, we will set the parameters for the ellipse.

```python
xcenter, ycenter = 0.38, 0.52
width, height = 0.1, 0.3
angle = -30
```

#### Step 3: Generate Ellipse using Arcs

In this step, we will generate the ellipse using arcs.

```python
theta = np.deg2rad(np.arange(0.0, 360.0, 1.0))
x = 0.5 * width * np.cos(theta)
y = 0.5 * height * np.sin(theta)

rtheta = np.radians(angle)
R = np.array([
    [np.cos(rtheta), -np.sin(rtheta)],
    [np.sin(rtheta),  np.cos(rtheta)],
    ])

x, y = np.dot(R, [x, y])
x += xcenter
y += ycenter
```

#### Step 4: Generate Ellipse using Polygonal Approximation

In this step, we will generate the ellipse using a polygonal approximation.

```python
theta = np.deg2rad(np.arange(0.0, 360.0, 1.0))
x = 0.5 * width * np.cos(theta)
y = 0.5 * height * np.sin(theta)

rtheta = np.radians(angle)
R = np.array([
    [np.cos(rtheta), -np.sin(rtheta)],
    [np.sin(rtheta),  np.cos(rtheta)],
    ])

x, y = np.dot(R, [x, y])
x += xcenter
y += ycenter
```

#### Step 5: Plot Ellipse using Arcs

In this step, we will plot the ellipse using arcs.

```python
fig = plt.figure()
ax = fig.add_subplot(211, aspect='auto')
ax.fill(x, y, alpha=0.2, facecolor='yellow',
        edgecolor='yellow', linewidth=1, zorder=1)

e1 = patches.Arc((xcenter, ycenter), width, height,
                 angle=angle, linewidth=2, fill=False, zorder=2)

ax.add_patch(e1)
```

#### Step 6: Plot Ellipse using Polygonal Approximation

In this step, we will plot the ellipse using a polygonal approximation.

```python
ax = fig.add_subplot(212, aspect='equal')
ax.fill(x, y, alpha=0.2, facecolor='green', edgecolor='green', zorder=1)
e2 = patches.Arc((xcenter, ycenter), width, height,
                 angle=angle, linewidth=2, fill=False, zorder=2)

ax.add_patch(e2)
fig.savefig('arc_compare')

plt.show()
```

### Summary

In this lab, you learned how to compare the ellipse generated with arcs versus a polygonal approximation using Python Matplotlib. You learned how to set ellipse parameters, generate ellipses using arcs and a polygonal approximation, and plot them using Matplotlib.
