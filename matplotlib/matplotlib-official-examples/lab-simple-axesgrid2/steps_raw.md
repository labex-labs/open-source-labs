# Python Matplotlib ImageGrid Tutorial

## Introduction

In this tutorial, we will learn how to use `ImageGrid` from `mpl_toolkits.axes_grid1` in Matplotlib to align multiple images of different sizes.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries including Matplotlib, cbook and ImageGrid.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid
```

### Step 2: Create a Figure and ImageGrid

Next, we create a figure and ImageGrid with `nrows_ncols` parameter to define the number of rows and columns of the grid.

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```

### Step 3: Load the image data

We will use an example image data called `bivariate_normal.npy` from `cbook` to demonstrate the ImageGrid. We load the image data using `get_sample_data` function from `cbook`.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```

### Step 4: Display images in the ImageGrid

Finally, we display the images in the ImageGrid using `imshow` function and `zip` function to iterate through the axes in the grid.

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```

## Summary

In this tutorial, we have learned how to use `ImageGrid` in Matplotlib to align multiple images of different sizes. We first import the necessary libraries, then create a figure and ImageGrid, load the image data, and finally display the images in the ImageGrid.
