# Matplotlib ImageGrid Tutorial

## Introduction

This tutorial will demonstrate how to create a grid of images using Matplotlib's `ImageGrid`. We will create a 2x2 grid of images and explore various ways to add colorbars to the grid.

## Steps

### Step 1: Import necessary libraries and data

We first need to import the necessary libraries and data to create our grid. We will use `matplotlib.pyplot` for plotting, `cbook` to get a sample data set, and `ImageGrid` to create our grid.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Get sample data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
extent = (-3, 4, -4, 3)
```

### Step 2: Create a grid of 2x2 images with a single colorbar

Our first grid will be a 2x2 grid of images with a single colorbar. We will use the `ImageGrid` function to create the grid and specify the number of rows and columns we want. We will also specify the location of the colorbar and set `share_all` to `True` to share the colorbar across all images.

```python
# Create a grid of 2x2 images with a single colorbar
grid = ImageGrid(
    fig,  # Figure object
    141,  # Location of subplot
    nrows_ncols=(2, 2),  # Number of rows and columns
    axes_pad=0.0,  # Padding between axes
    label_mode="L",  # Label mode
    share_all=True,  # Share colorbar across all images
    cbar_location="top",  # Location of colorbar
    cbar_mode="single"  # Colorbar mode
)

# Plot images on grid
for ax in grid:
    im = ax.imshow(Z, extent=extent)

# Add colorbar to grid
grid.cbar_axes[0].colorbar(im)
for cax in grid.cbar_axes:
    cax.tick_params(labeltop=False)
```

### Step 3: Create a grid of 2x2 images with each image having its own colorbar

Our next grid will be a 2x2 grid of images with each image having its own colorbar. We will use the `ImageGrid` function again, but this time we will set `cbar_mode` to `"each"` to specify that each image should have its own colorbar.

```python
# Create a grid of 2x2 images with each image having its own colorbar
grid = ImageGrid(
    fig,  # Figure object
    142,  # Location of subplot
    nrows_ncols=(2, 2),  # Number of rows and columns
    axes_pad=0.1,  # Padding between axes
    label_mode="1",  # Label mode
    share_all=True,  # Share colorbar across all images
    cbar_location="top",  # Location of colorbar
    cbar_mode="each",  # Colorbar mode
    cbar_size="7%",  # Size of colorbar
    cbar_pad="2%"  # Padding between colorbar and images
)

# Plot images on grid and add colorbars
for ax, cax in zip(grid, grid.cbar_axes):
    im = ax.imshow(Z, extent=extent)
    cax.colorbar(im)
    cax.tick_params(labeltop=False)
```

### Step 4: Create a grid of 2x2 images with each image having its own colorbar and a different colorbar range

Our final grid will also be a 2x2 grid of images with each image having its own colorbar, but this time we will use a different colorbar range for each image. We will set the colorbar range using `vmin` and `vmax` when plotting each image.

```python
# Create a grid of 2x2 images with each image having its own colorbar and a different colorbar range
grid = ImageGrid(
    fig,  # Figure object
    143,  # Location of subplot
    nrows_ncols=(2, 2),  # Number of rows and columns
    axes_pad=(0.45, 0.15),  # Padding between axes
    label_mode="1",  # Label mode
    share_all=True,  # Share colorbar across all images
    cbar_location="right",  # Location of colorbar
    cbar_mode="each",  # Colorbar mode
    cbar_size="7%",  # Size of colorbar
    cbar_pad="2%"  # Padding between colorbar and images
)

# Plot images on grid and add colorbars
limits = ((0, 1), (-2, 2), (-1.7, 1.4), (-1.5, 1))  # Different colorbar ranges
for ax, cax, vlim in zip(grid, grid.cbar_axes, limits):
    im = ax.imshow(Z, extent=extent, vmin=vlim[0], vmax=vlim[1])
    cb = cax.colorbar(im)
    cb.set_ticks((vlim[0], vlim[1]))
```

## Summary

In this tutorial, we learned how to create a grid of images using Matplotlib's `ImageGrid`. We explored different ways to add colorbars to the grid, including using a single colorbar for all images, giving each image its own colorbar, and giving each image its own colorbar with a different colorbar range.
