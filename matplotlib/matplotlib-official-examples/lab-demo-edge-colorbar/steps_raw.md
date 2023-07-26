# Matplotlib Image Grid Colorbars

## Introduction

This lab is about creating image grids with colorbars using Matplotlib. The example code provided shows how to use one common colorbar for each row or column of an image grid.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries to create the image grid with colorbars.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import AxesGrid
```

### Step 2: Define Image Data

We define a function that returns a sample image data and its extent.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```

### Step 3: Create a Grid with Bottom Colorbar

We create a grid of 2x2 images with a colorbar for each column.

```python
def demo_bottom_cbar(fig):
    grid = AxesGrid(fig, 121,  # similar to subplot(121)
                    nrows_ncols=(2, 2),
                    axes_pad=0.10,
                    share_all=True,
                    label_mode="1",
                    cbar_location="bottom",
                    cbar_mode="edge",
                    cbar_pad=0.25,
                    cbar_size="15%",
                    direction="column"
                    )

    Z, extent = get_demo_image()
    cmaps = ["autumn", "summer"]
    for i in range(4):
        im = grid[i].imshow(Z, extent=extent, cmap=cmaps[i//2])
        if i % 2:
            grid.cbar_axes[i//2].colorbar(im)

    for cax in grid.cbar_axes:
        cax.axis[cax.orientation].set_label("Bar")

    # This affects all axes as share_all = True.
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])
```

### Step 4: Create a Grid with Right Colorbar

We create a grid of 2x2 images with a colorbar for each row.

```python
def demo_right_cbar(fig):
    grid = AxesGrid(fig, 122,  # similar to subplot(122)
                    nrows_ncols=(2, 2),
                    axes_pad=0.10,
                    label_mode="1",
                    share_all=True,
                    cbar_location="right",
                    cbar_mode="edge",
                    cbar_size="7%",
                    cbar_pad="2%",
                    )
    Z, extent = get_demo_image()
    cmaps = ["spring", "winter"]
    for i in range(4):
        im = grid[i].imshow(Z, extent=extent, cmap=cmaps[i//2])
        if i % 2:
            grid.cbar_axes[i//2].colorbar(im)

    for cax in grid.cbar_axes:
        cax.axis[cax.orientation].set_label('Foo')

    # This affects all axes because we set share_all = True.
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])
```

### Step 5: Create the Figure and Call the Functions

Finally, we create the figure and call the functions to create the image grids with colorbars.

```python
fig = plt.figure()

demo_bottom_cbar(fig)
demo_right_cbar(fig)

plt.show()
```

## Summary

Matplotlib provides a simple way to create image grids with colorbars using the AxesGrid toolkit. This lab demonstrated how to create a grid of 2x2 images with a colorbar for each column and a grid of 2x2 images with a colorbar for each row. By following these steps, you can create image grids with colorbars for your own datasets.
