# Matplotlib ImageGrid Tutorial

## Introduction

This tutorial will demonstrate how to use Matplotlib's ImageGrid to create a grid of images with shared x and y axes. The tutorial will cover two demos:

- Demo 1 shows how to add a colorbar at each axis.
- Demo 2 shows how to add a shared colorbar.

## Steps

### Step 1: Import necessary libraries

We will use Matplotlib's ImageGrid to create the grid of images. We will also use numpy to generate sample data and cbook to access a sample dataset.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid
```

### Step 2: Define a function to add inner titles to the axes

The function `add_inner_title` will be used to add titles to the images.

```python
def add_inner_title(ax, title, loc, **kwargs):
    from matplotlib.offsetbox import AnchoredText
    from matplotlib.patheffects import withStroke
    prop = dict(path_effects=[withStroke(foreground='w', linewidth=3)],
                size=plt.rcParams['legend.fontsize'])
    at = AnchoredText(title, loc=loc, prop=prop,
                      pad=0., borderpad=0.5,
                      frameon=False, **kwargs)
    ax.add_artist(at)
    return at
```

### Step 3: Prepare the sample data

We will use the `get_sample_data` function from cbook to obtain sample data. We will then prepare the images to be displayed in the grid.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```

### Step 4: Demo 1 - Colorbar at each axis

We will create a grid of 3 images with a colorbar at each axis using the following code:

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Changing the colorbar ticks
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Image 1", "Image 2", "Image 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- We create a grid of 3 images using `ImageGrid`.
- We set the `cbar_mode` to "each" to add a colorbar at each axis.
- We set the `share_all` parameter to True to share the x and y axes across all the images.
- We set the `cbar_location` parameter to "top" to position the colorbars at the top.
- We set the `xticks` and `yticks` for the first image.
- We loop through each image and add the image to the axis using `imshow`.
- We add a colorbar to each axis using `ax.cax.colorbar`.
- We set the colorbar ticks for the second and third images.
- We add a title to each image using `add_inner_title`.

### Step 5: Demo 2 - Shared colorbar

We will create a grid of 3 images with a shared colorbar using the following code:

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# With cbar_mode="single", cax attribute of all axes are identical.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- We create a grid of 3 images using `ImageGrid`.
- We set the `cbar_mode` to "single" to add a shared colorbar.
- We set the `share_all` parameter to True to share the x and y axes across all the images.
- We set the `cbar_location` parameter to "right" to position the colorbar at the right.
- We set the `xticks` and `yticks` for the first image.
- We loop through each image and add the image to the axis using `imshow`.
- We set the `clim` parameter to ensure that all images use the same color scale.
- We add a shared colorbar to the axis using `ax.cax.colorbar`.
- We add a title to each image using `add_inner_title`.

### Step 6: Display the plot

We will use `plt.show()` to display the plot.

```python
plt.show()
```

## Summary

This tutorial demonstrated how to use Matplotlib's ImageGrid to create a grid of images with shared x and y axes. We covered two demos: Demo 1 showed how to add a colorbar at each axis, and Demo 2 showed how to add a shared colorbar.
