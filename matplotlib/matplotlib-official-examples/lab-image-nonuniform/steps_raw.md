# Image Nonuniform Lab

## Introduction

This lab provides a step-by-step guide on how to use the NonUniformImage class in Python's Matplotlib library. NonUniformImage allows users to plot images with non-uniform pixel positions.

## Steps

### Step 1: Import Libraries

Before creating a NonUniformImage, we need to import the necessary libraries. In this example, we will be using numpy and matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.image import NonUniformImage
```

### Step 2: Create Linear and Nonlinear Arrays

We need to create two arrays, one with linear values and another with non-linear values. These arrays will be used to create our NonUniformImage.

```python
# Linear x array for cell centers:
x = np.linspace(-4, 4, 9)

# Highly nonlinear x array:
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```

### Step 3: Create Subplots and NonUniformImage

Now, we create subplots and add the NonUniformImage to each of them. We will create four subplots, two with 'nearest' interpolation and two with 'bilinear' interpolation. The interpolation keyword argument defines the type of interpolation used to display the image.

```python
# Create subplots
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')
fig.suptitle('NonUniformImage class', fontsize='large')

# Nearest Interpolation
ax = axs[0, 0]
im = NonUniformImage(ax, interpolation='nearest', extent=(-4, 4, -4, 4), cmap=cm.Purples)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title('nearest')

ax = axs[0, 1]
im = NonUniformImage(ax, interpolation='nearest', extent=(-64, 64, -4, 4), cmap=cm.Purples)
im.set_data(x2, y, z)
ax.add_image(im)
ax.set_xlim(-64, 64)
ax.set_ylim(-4, 4)
ax.set_title('nearest')

# Bilinear Interpolation
ax = axs[1, 0]
im = NonUniformImage(ax, interpolation='bilinear', extent=(-4, 4, -4, 4), cmap=cm.Purples)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title('bilinear')

ax = axs[1, 1]
im = NonUniformImage(ax, interpolation='bilinear', extent=(-64, 64, -4, 4), cmap=cm.Purples)
im.set_data(x2, y, z)
ax.add_image(im)
ax.set_xlim(-64, 64)
ax.set_ylim(-4, 4)
ax.set_title('bilinear')

plt.show()
```

### Step 4: Interpretation of Results

The subplots will display two different types of interpolation, 'nearest' and 'bilinear'. 'nearest' interpolation will display the pixel value of the nearest neighbor, while 'bilinear' interpolation will display the weighted average of the four nearest neighbors.

## Summary

NonUniformImage is a useful tool for plotting images with non-uniform pixel positions. This lab provided a step-by-step guide on how to use NonUniformImage in Python's Matplotlib library, including importing the necessary libraries, creating linear and nonlinear arrays, creating subplots and NonUniformImage, and interpreting the results.
