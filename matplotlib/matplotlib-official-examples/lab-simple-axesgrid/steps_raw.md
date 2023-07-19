# Matplotlib ImageGrid Tutorial

## Introduction

In this tutorial, we will learn how to use the `ImageGrid` function from the `mpl_toolkits.axes_grid1` module in Matplotlib. We will create a 2x2 grid of images and align them using the `ImageGrid` function.

## Steps

### Step 1: Import necessary libraries and create image arrays

We begin by importing the necessary libraries and creating four 10x10 image arrays using the `arange` and `reshape` functions from the NumPy library.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```

### Step 2: Create a figure and an ImageGrid object

Next, we create a `figure` object using the `plt.figure` function and pass in the `figsize` argument to set the size of the figure. We then create an `ImageGrid` object using the `ImageGrid` function and pass in the `figure`, `111` as the subplot argument, `(2, 2)` as the `nrows_ncols` argument to create a 2x2 grid of axes, and `0.1` as the `axes_pad` argument to set the padding between the axes.

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```

### Step 3: Iterate over the grid and plot the images

We then iterate over the `grid` object using the `zip` function to iterate over both the axes and the image arrays. We plot each image on its corresponding axis using the `imshow` function.

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```

### Step 4: Show the plot

Finally, we show the plot using the `plt.show` function.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to use the `ImageGrid` function from the `mpl_toolkits.axes_grid1` module in Matplotlib to align multiple images in a grid. We created a 2x2 grid of images and plotted them using the `imshow` function.
