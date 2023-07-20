# Step-by-Step Lab: Masked Contour Plots with Matplotlib

## Introduction

In data visualization, contour plots are commonly used to display 3-dimensional data on a 2-dimensional plane. Matplotlib is a widely used plotting library in Python that provides functionalities to create different types of plots, including contour plots. In this lab, we will learn how to create masked contour plots using Matplotlib and how to illustrate the difference between corner masks being enabled and disabled.

## Steps

### Step 1: Importing Required Libraries

To create masked contour plots using Matplotlib, we need to import the following libraries:

- `numpy`: a library for the Python programming language that provides support for large, multi-dimensional arrays and matrices.
- `matplotlib.pyplot`: a collection of functions that provide a simple interface for creating different types of plots.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating Data for Plotting

In this step, we will create data to plot on a contour plot. We use the `np.meshgrid()` function to create a grid of points, and then calculate the `z` values using the sine and cosine functions.

```python
# Data to plot.
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```

### Step 3: Masking the Data

In this step, we will mask some of the `z` values using a Boolean mask. We create a `mask` array using the `np.zeros_like()` function, and then set some of the values to `True` to mask them.

```python
# Mask various z values.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```

### Step 4: Creating the Plot

In this step, we will create the masked contour plot using the `contourf()` function. We pass in the `x`, `y`, and `z` arrays to this function, along with the `corner_mask` argument set to `True` or `False` depending on the type of plot we want to create.

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indicate masked points with red circles.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```

### Step 5: Interpretation of Results

In this step, we will interpret the results of the masked contour plot. We can observe that the `corner_mask` parameter controls whether or not the corner points of the plot are masked. When `corner_mask` is set to `True`, the corners of the contour plot are masked, while when it is set to `False`, they are not masked. We can also see that the masked points are indicated by red circles.

## Summary

In this lab, we learned how to create masked contour plots using Matplotlib. We first imported the required libraries and then created the data to plot. We then masked some of the `z` values using a Boolean mask, and created the contour plot using the `contourf()` function. Finally, we interpreted the results and observed the difference between corner masks being enabled and disabled.
