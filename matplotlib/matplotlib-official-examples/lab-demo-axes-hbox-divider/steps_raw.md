# Matplotlib Subplots Lab

## Introduction

In this lab, we will learn how to use Matplotlib to create subplots using the `HBoxDivider` and `VBoxDivider` classes. We will use a simple example to show how these classes can be used to arrange multiple subplots.

## Steps

### Step 1: Import Required Libraries

We begin by importing the required libraries - `matplotlib` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data

We create two numpy arrays to be used as the data for our subplots.

```python
arr1 = np.arange(20).reshape((4, 5))
arr2 = np.arange(20).reshape((5, 4))
```

### Step 3: Create Subplots Using `HBoxDivider`

We create two subplots side-by-side using the `HBoxDivider` class. We also adjust the axes' location so that they have equal heights while maintaining their aspect ratios.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(arr1)
ax2.imshow(arr2)

pad = 0.5  # pad in inches
divider = HBoxDivider(
    fig, 111,
    horizontal=[Size.AxesX(ax1), Size.Fixed(pad), Size.AxesX(ax2)],
    vertical=[Size.AxesY(ax1), Size.Scaled(1), Size.AxesY(ax2)])
ax1.set_axes_locator(divider.new_locator(0))
ax2.set_axes_locator(divider.new_locator(2))

plt.show()
```

### Step 4: Create Subplots Using `VBoxDivider`

We create two subplots one below the other using the `VBoxDivider` class. We adjust the axes' location so that they have equal widths while maintaining their aspect ratios.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.imshow(arr1)
ax2.imshow(arr2)

divider = VBoxDivider(
    fig, 111,
    horizontal=[Size.AxesX(ax1), Size.Scaled(1), Size.AxesX(ax2)],
    vertical=[Size.AxesY(ax1), Size.Fixed(pad), Size.AxesY(ax2)])

ax1.set_axes_locator(divider.new_locator(0))
ax2.set_axes_locator(divider.new_locator(2))

plt.show()
```

## Summary

In this lab, we learned how to use the `HBoxDivider` and `VBoxDivider` classes in Matplotlib to create subplots. We saw how to adjust the axes' location so that they have equal heights or widths while maintaining their aspect ratios. These classes can be useful when we need to arrange multiple subplots in a single figure.
