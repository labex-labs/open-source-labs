# Matplotlib Tutorial Lab

## Drawing Ellipses with Python Matplotlib

### Introduction

This lab demonstrates how to use Python Matplotlib to draw ellipses. The lab covers two examples:

- Drawing individual ellipses
- Drawing ellipses with different angles

### Steps

#### Step 1: Importing Required Libraries

First, we need to import the required libraries. We will use `numpy` to generate random data, and `matplotlib.pyplot` and `matplotlib.patches` to draw the ellipses.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
```

#### Step 2: Drawing Individual Ellipses

In this example, we will draw many ellipses with random sizes, positions, and colors. Each ellipse will be an instance of the `Ellipse` class.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Number of ellipses to draw
NUM = 250

# Generate the ellipses
ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

# Create the plot and set the aspect ratio to 'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Add each ellipse to the plot
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

# Set the x and y limits of the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Show the plot
plt.show()
```

#### Step 3: Drawing Ellipses with Different Angles

In this example, we will draw many ellipses with different angles. We will use a loop to create an `Ellipse` instance for each angle we want to draw.

```python
# Define the angle step and the range of angles to draw
angle_step = 45  # degrees
angles = np.arange(0, 180, angle_step)

# Create the plot and set the aspect ratio to 'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Loop over the angles and draw an ellipse for each angle
for angle in angles:
    ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
    ax.add_artist(ellipse)

# Set the x and y limits of the plot
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

# Show the plot
plt.show()
```

### Summary

In this lab, we have learned how to use Python Matplotlib to draw ellipses. We have covered two examples: drawing individual ellipses and drawing ellipses with different angles. By following the steps in this lab, you should be able to draw ellipses in your own Python projects using Matplotlib.
