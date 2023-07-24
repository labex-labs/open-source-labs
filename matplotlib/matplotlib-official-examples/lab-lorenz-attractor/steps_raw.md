# Python Matplotlib Tutorial

## Introduction

This lab is a step-by-step tutorial for plotting Edward Lorenz's 1963 "Deterministic Nonperiodic Flow" in a 3-dimensional space using mplot3d. We will use Python and Matplotlib, which is a plotting library for the Python programming language.

## Steps

### Step 1: Import Libraries

We start by importing the necessary libraries: Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the Lorenz Function

We define the Lorenz function, which takes in three parameters and returns an array of three values. We use the default values `s=10`, `r=28`, and `b=2.667` for the Lorenz parameters.

```python
def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three-dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
```

### Step 3: Set Up the Initial Parameters

We set up the initial parameters for the simulation, including the time step `dt`, the number of steps `num_steps`, and the initial values for `x`, `y`, and `z`.

```python
dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values
```

### Step 4: Calculate the Lorenz Attractor

We calculate the Lorenz Attractor by stepping through time and estimating the next point using the previous point and the Lorenz function.

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```

### Step 5: Plot the Lorenz Attractor

We plot the Lorenz Attractor using Matplotlib's mplot3d module.

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
```

## Summary

In this tutorial, we learned how to plot the Lorenz Attractor using Python and Matplotlib. We defined the Lorenz function, set up the initial parameters, calculated the Lorenz Attractor, and plotted it using Matplotlib's mplot3d module.
