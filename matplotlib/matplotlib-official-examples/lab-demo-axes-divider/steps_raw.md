# Matplotlib Image Plotting Lab

## Introduction

Matplotlib is a Python library that enables the creation of static, animated, and interactive visualizations in Python. It is widely used in scientific computing, data analysis, machine learning, and more. In this lab, you will learn how to plot images using Matplotlib and how to manipulate the location of axes and colorbars.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries that will be used in this lab. We will be using `matplotlib.pyplot` and `cbook` from `matplotlib` to get a sample image.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
```

### Step 2: Get Demo Image

In this step, we will define a function to get a demo image and its extent. We will be using `get_sample_data()` function from `cbook` to get a sample image.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```

### Step 3: Simple Image and Colorbar

In this step, we will create a simple image and its colorbar. We will be using `imshow()` function from `pyplot` to create the image, and `colorbar()` function to create the colorbar.

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```

### Step 4: Image and Colorbar with Draw-Time Positioning - A Hard Way

In this step, we will create an image and its colorbar with draw-time positioning in a hard way. We will be using `SubplotDivider` from `mpl_toolkits.axes_grid1` to create a divider for the axes and colorbar.

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # axes for image
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # axes for colorbar
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # main axes
        Size.Fixed(0.05),  # padding, 0.1 inch
        Size.Fixed(0.2),  # colorbar, 0.3 inch
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```

### Step 5: Image and Colorbar with Draw-Time Positioning - An Easy Way

In this step, we will create an image and its colorbar with draw-time positioning in an easy way. We will be using `make_axes_locatable` from `mpl_toolkits.axes_grid1` to create a divider for the axes and colorbar.

```python
def demo_locatable_axes_easy(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)

    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)

    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=False)
```

### Step 6: Two Images Side by Side with Fixed Padding

In this step, we will create two images side by side with fixed padding. We will be using `make_axes_locatable` from `mpl_toolkits.axes_grid1` to create a divider for the axes and colorbar.

```python
def demo_images_side_by_side(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    Z, extent = get_demo_image()
    ax2 = divider.append_axes("right", size="100%", pad=0.05)
    fig1 = ax.get_figure()
    fig1.add_axes(ax2)

    ax.imshow(Z, extent=extent)
    ax2.imshow(Z, extent=extent)
    ax2.yaxis.set_tick_params(labelleft=False)
```

### Step 7: Plotting

In this step, we will create a figure and add subplots for each image that we want to create.

```python
def demo():
    fig = plt.figure(figsize=(6, 6))

    # PLOT 1
    # simple image & colorbar
    ax = fig.add_subplot(2, 2, 1)
    demo_simple_image(ax)

    # PLOT 2
    # image and colorbar with draw-time positioning -- a hard way
    demo_locatable_axes_hard(fig)

    # PLOT 3
    # image and colorbar with draw-time positioning -- an easy way
    ax = fig.add_subplot(2, 2, 3)
    demo_locatable_axes_easy(ax)

    # PLOT 4
    # two images side by side with fixed padding.
    ax = fig.add_subplot(2, 2, 4)
    demo_images_side_by_side(ax)

    plt.show()
```

## Summary

In this lab, we learned how to plot images using Matplotlib and how to manipulate the location of axes and colorbars. We covered different ways of creating images and colorbars and how to position them in the figure. With the knowledge gained from this lab, you will be able to create more complex visualizations and manipulate them to suit your needs.
