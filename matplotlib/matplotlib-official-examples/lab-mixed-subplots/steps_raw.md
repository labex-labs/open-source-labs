# Matplotlib 2D and 3D Plotting Lab

## Introduction

This lab will guide you through creating a figure that contains both a 2D and a 3D plot using Matplotlib. The 2D plot will display a damped oscillation, while the 3D plot will display a sinusoidal wave.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries for this lab. We will use Matplotlib for plotting, NumPy for creating arrays, and mpl_toolkits for 3D plotting.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
```

### Step 2: Define Functions

In this step, we will define a function that generates a damped oscillation.

```python
def f(t):
    return np.cos(2*np.pi*t) * np.exp(-t)
```

### Step 3: Create Figure

In this step, we will create a figure with two subplots. The first subplot will be a 2D plot, and the second subplot will be a 3D plot.

```python
fig = plt.figure(figsize=plt.figaspect(2.))
fig.suptitle('A Tale of 2 Subplots')
```

### Step 4: Create 2D Plot

In this step, we will create a 2D plot of a damped oscillation.

```python
ax1 = fig.add_subplot(2, 1, 1)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.0, 2.0, 0.01)

ax1.plot(t1, f(t1), 'bo',
         t2, f(t2), 'k--', markerfacecolor='green')
ax1.grid(True)
ax1.set_ylabel('Damped oscillation')
```

### Step 5: Create 3D Plot

In this step, we will create a 3D plot of a sinusoidal wave.

```python
ax2 = fig.add_subplot(2, 1, 2, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        linewidth=0, antialiased=False)
ax2.set_zlim(-1, 1)
```

### Step 6: Show Plot

In this step, we will display the figure.

```python
plt.show()
```

## Summary

In this lab, we created a figure with both a 2D and a 3D plot using Matplotlib. The 2D plot displayed a damped oscillation, while the 3D plot displayed a sinusoidal wave. We used NumPy to create arrays and mpl_toolkits for 3D plotting.
