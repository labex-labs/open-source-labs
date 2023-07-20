# Matplotlib Colorbar Lab

## Introduction

Matplotlib is a Python library used for data visualization. In this lab, we will learn how to add a colorbar to a plot in Matplotlib. Colorbars are useful for indicating the range of values that a colormap represents.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries. We will be using Matplotlib's `pyplot` module, which provides an interface for creating plots.

```python
import matplotlib.pyplot as plt
```

### Step 2: Create a plot

Next, we will create a plot using Matplotlib's `imshow` function. This function displays an image on the plot. We will also create a figure with two subplots.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```

### Step 3: Add a colorbar to the plot

Now, we will add a colorbar to each subplot using Matplotlib's `make_axes_locatable` function. This function takes an existing axes, adds it to a new `AxesDivider` and returns the `AxesDivider`. The `append_axes` method of the `AxesDivider` can then be used to create a new axes on a given side ("top", "right", "bottom", or "left") of the original axes.

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```

### Step 4: Display the plot

Finally, we will display the plot using Matplotlib's `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to add a colorbar to a plot in Matplotlib. We used the `make_axes_locatable` function to add an additional axes to the plot and the `colorbar` function to create the colorbar. We also learned how to change the orientation and position of the colorbar.
