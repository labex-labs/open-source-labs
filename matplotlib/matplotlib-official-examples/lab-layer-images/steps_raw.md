# Layer Images Tutorial

## Introduction

This is a step-by-step tutorial on how to layer images using alpha blending with Python Matplotlib.

## Steps

### Step 1: Import necessary libraries and define a function

Import the necessary libraries and define a function to create the first image.

```python
import matplotlib.pyplot as plt
import numpy as np

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))
```

### Step 2: Define the x and y variables

Define the x and y variables to create the meshgrid.

```python
dx, dy = 0.05, 0.05
x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)
```

### Step 3: Define the extent and create the first image

Define the extent and create the first image using the `imshow` function.

```python
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8)) % 2  # chessboard
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)
```

### Step 4: Create the second image

Create the second image using the `func3` function and the `imshow` function.

```python
Z2 = func3(X, Y)
im2 = plt.imshow(Z2, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear',
                 extent=extent)
```

### Step 5: Display the final image

Use the `show` function to display the final image.

```python
plt.show()
```

## Summary

This tutorial provided a step-by-step guide on how to layer images using alpha blending with Python Matplotlib. The process involved defining the necessary variables, creating the first and second images, and displaying the final image.
