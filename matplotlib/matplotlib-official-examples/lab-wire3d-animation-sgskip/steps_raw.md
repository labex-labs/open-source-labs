# Animate a 3D Wireframe Plot

## Introduction

In this lab, we will learn how to animate a 3D wireframe plot using Matplotlib, a popular data visualization library in Python.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries: Matplotlib, NumPy, and time.

```python
import time
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Set up the Figure and Subplot

The second step is to set up the figure and subplot. We will create a 3D plot using `add_subplot`.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
```

### Step 3: Create a Meshgrid

The third step is to create a meshgrid using `linspace`.

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```

### Step 4: Set Z Axis Limits

The fourth step is to set the z axis limits so they aren't recalculated each frame.

```python
ax.set_zlim(-1, 1)
```

### Step 5: Animate the Plot

The fifth step is to animate the plot. We will use a for loop to iterate through a range of values for phi. In each iteration, we will remove the previous line collection, generate new data, plot the new wireframe, and pause briefly before continuing.

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```

### Step 6: Display the Average FPS

The sixth step is to display the average frames per second (FPS) using the total time it took to run the animation.

```python
print('Average FPS: %f' % (100 / (time.time() - tstart)))
```

## Summary

In this lab, we learned how to animate a 3D wireframe plot using Matplotlib. We used a for loop to iterate through a range of values for phi, generated new data, plotted the new wireframe, and paused briefly before continuing. Finally, we displayed the average frames per second (FPS) using the total time it took to run the animation.
