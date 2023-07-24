# Contour Plotting Lab

## Introduction

This lab will guide you through the process of creating a contour plot using Matplotlib in Python. You will learn how to generate curves with larger values and how to use `~matplotlib.patheffects.TickedStroke` to distinguish between the valid and invalid sides of the constraint boundaries.

## Steps

### Step 1: Import the Required Libraries

To get started, you need to import the necessary libraries. Matplotlib and NumPy are required to create the contour plot.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects
```

### Step 2: Set Up the Survey Vectors and Matrices

Next, set up the survey vectors and matrices. Design disk loading and gear ratio.

```python
nx = 101
ny = 105

# Set up survey vectors
xvec = np.linspace(0.001, 4.0, nx)
yvec = np.linspace(0.001, 4.0, ny)

# Set up survey matrices.  Design disk loading and gear ratio.
x1, x2 = np.meshgrid(xvec, yvec)
```

### Step 3: Evaluate the Data to Plot

Now, evaluate some data to plot. In this example, we will plot an objective function, `g1`, `g2`, and `g3`.

```python
# Evaluate some stuff to plot
obj = x1**2 + x2**2 - 2*x1 - 2*x2 + 2
g1 = -(3*x1 + x2 - 5.5)
g2 = -(x1 + 2*x2 - 4.5)
g3 = 0.8 + x1**-3 - x2
```

### Step 4: Create the Contour Plot

Now, create the contour plot using the `ax.contour()` method. This method is used to represent the topography of the objective function and generate boundary curves of the constraint functions.

```python
fig, ax = plt.subplots(figsize=(6, 6))

cntr = ax.contour(x1, x2, obj, [0.01, 0.1, 0.5, 1, 2, 4, 8, 16], colors='black')
ax.clabel(cntr, fmt="%2.1f", use_clabeltext=True)

cg1 = ax.contour(x1, x2, g1, [0], colors='sandybrown')
plt.setp(cg1.collections, path_effects=[patheffects.withTickedStroke(angle=135)])

cg2 = ax.contour(x1, x2, g2, [0], colors='orangered')
plt.setp(cg2.collections, path_effects=[patheffects.withTickedStroke(angle=60, length=2)])

cg3 = ax.contour(x1, x2, g3, [0], colors='mediumblue')
plt.setp(cg3.collections, path_effects=[patheffects.withTickedStroke(spacing=7)])

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

plt.show()
```

### Step 5: Interpret the Results

The resulting plot shows the topography of the objective function and the boundary curves of the constraint functions. The `~matplotlib.patheffects.TickedStroke` is used to distinguish between the valid and invalid sides of the constraint boundaries.

## Summary

In this lab, you learned how to create a contour plot using Matplotlib in Python. You also learned how to generate curves with larger values and how to use `~matplotlib.patheffects.TickedStroke` to distinguish between the valid and invalid sides of the constraint boundaries.
