# Matplotlib Tutorial: Multicolored Lines

## Introduction

In this lab, we will learn how to create multicolored lines in Matplotlib. We will use the `LineCollection` function to create a set of line segments and color them individually based on their derivative. We will also learn how to use a boundary norm to color the line segments.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries for this lab. We will import `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data

We will create a numpy array `x` containing 500 evenly spaced values between 0 and 3π. We will also create another numpy array `y` containing the sine of the values in `x`. Finally, we will create a numpy array `dydx` containing the first derivative of `y`.

```python
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))
```

### Step 3: Create Line Segments

We will create a set of line segments so that we can color them individually. We will use the numpy `concatenate` function to concatenate two arrays `points[:-1]` and `points[1:]` along the second axis. We will then reshape the resulting array to an N x 1 x 2 array so that we can stack points together easily to get the segments. The segments array for line collection needs to be (numlines) x (points per line) x 2 (for x and y).

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```

### Step 4: Create a Continuous Norm

We will create a continuous norm to map from data points to colors. We will use the `Normalize` function from `matplotlib.pyplot` to normalize the `dydx` values between its minimum and maximum. We will then use the `LineCollection` function to create a set of line segments and color them individually based on their derivative. We will use the `set_array` function to set the values used for colormapping.

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```

### Step 5: Create a Colorbar

We will create a colorbar to show the mapping between colors and `dydx` values. We will use the `colorbar` function from `matplotlib.pyplot` to create a colorbar.

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```

### Step 6: Use a Boundary Norm

We will use a boundary norm instead to color the line segments. We will create a `ListedColormap` containing three colors - red, green, and blue. We will then create a `BoundaryNorm` with boundaries -1, -0.5, 0.5, and 1, and the `ListedColormap`. We will use the `set_array` function to set the values used for colormapping.

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```

### Step 7: Create a Subplot

We will create a subplot to show the colored line segments. We will use the `subplots` function from `matplotlib.pyplot` to create a 2x1 grid of subplots, and the `sharex` and `sharey` parameters to share the x and y axes between the subplots.

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```

### Step 8: Set Axis Limits

We will set the x and y axis limits for the subplots.

```python
axs[0].set_xlim(x.min(), x.max())
axs[0].set_ylim(-1.1, 1.1)
```

### Step 9: Show the Plot

We will use the `show` function from `matplotlib.pyplot` to show the plot.

```python
plt.show()
```

## Summary

In this lab, we learned how to create multicolored lines in Matplotlib. We used the `LineCollection` function to create a set of line segments and color them individually based on their derivative. We also learned how to use a boundary norm to color the line segments. We used the `Normalize` function to normalize the `dydx` values between its minimum and maximum, and the `ListedColormap` function to create a colormap with three colors - red, green, and blue. We used the `BoundaryNorm` function to create a boundary norm with boundaries -1, -0.5, 0.5, and 1, and the `ListedColormap`. Finally, we used the `subplots` function to create a 2x1 grid of subplots, and the `sharex` and `sharey` parameters to share the x and y axes between the subplots. We then showed the plot using the `show` function.
