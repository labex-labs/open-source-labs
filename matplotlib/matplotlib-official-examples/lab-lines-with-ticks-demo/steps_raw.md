# Matplotlib Ticked Patheffect Lab

## Introduction

In this lab, we will learn how to add ticks along a line in Matplotlib using Ticked Patheffect. Ticks can be added to mark one side as a barrier and you can control the angle, spacing, and length of the ticks. Ticks will also appear appropriately in the legend.

## Steps

### Step 1: Import Libraries and Generate Data

We will first import the necessary libraries and generate some data for plotting.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

# Generate data
nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
```

### Step 2: Plot a Straight Line with Ticked Patheffect

We will now plot a straight diagonal line with ticked patheffect.

```python
# Plot a straight diagonal line with ticked style path
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])
```

### Step 3: Plot a Curved Line with Ticked Patheffect

We will now plot a curved line with ticked patheffect.

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```

## Summary

In this lab, we have learned how to add ticks along a line in Matplotlib using Ticked Patheffect. We have also learned how to control the angle, spacing, and length of the ticks. Ticks will also appear appropriately in the legend.
