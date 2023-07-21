# Python Matplotlib Tutorial Lab

## Introduction

This lab will guide you through generating a shaded and power-normalized rendering of the Mandelbrot set using Python's Matplotlib library.

## Steps

### Step 1: Import Required Libraries

First, we need to import the libraries we will be using: NumPy, Matplotlib, and Colors.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
```

### Step 2: Define the Mandelbrot Set Function

Next, we will define a function that generates the Mandelbrot set. The function takes in several parameters:

- `xmin`, `xmax`, `ymin`, `ymax`: the minimum and maximum values for the x and y axes
- `xn` and `yn`: the number of points to generate along each axis
- `maxiter`: the maximum number of iterations to perform for each point
- `horizon`: the maximum value at which to consider a point to be part of the set

```python
def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)
    C = X + Y[:, None] * 1j
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)
    for n in range(maxiter):
        I = abs(Z) < horizon
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0
    return Z, N
```

### Step 3: Generate the Mandelbrot Set

Now we will generate the Mandelbrot set by calling the `mandelbrot_set` function with our desired parameters. This will give us two arrays:

- `Z`: the final values of the complex numbers we iterated over
- `N`: the number of iterations performed for each point before it was determined to be part of the set

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```

### Step 4: Normalize the Data

In order to create a shaded and power-normalized rendering of the Mandelbrot set, we need to normalize our data. We will do this using the following formula:

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```

### Step 5: Create the Plot

Now that we have our normalized data, we can create the plot. We will use the `imshow` function to display the data as an image, and we will also add some text to the plot to indicate what we are looking at.

```python
dpi = 72
width = 10
height = 10*yn/xn
fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)

light = colors.LightSource(azdeg=315, altdeg=10)
M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,
                norm=colors.PowerNorm(0.3), blend_mode='hsv')
ax.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
ax.set_xticks([])
ax.set_yticks([])

year = time.strftime("%Y")
text = ("The Mandelbrot fractal set\n"
        "Rendered with matplotlib %s, %s - https://matplotlib.org"
        % (matplotlib.__version__, year))
ax.text(xmin+.025, ymin+.025, text, color="white", fontsize=12, alpha=0.5)

plt.show()
```

## Summary

In this lab, we learned how to generate a shaded and power-normalized rendering of the Mandelbrot set using Python's Matplotlib library. We accomplished this by defining a function to generate the set, normalizing the data, and creating a plot using the normalized data. This technique can be applied to other data sets to create visually appealing and informative images.
