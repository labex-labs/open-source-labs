# Python Matplotlib Tutorial

## Introduction

Matplotlib is a Python library used for creating static, animated, and interactive visualizations in Python. It is a powerful tool for data visualization, and it is widely used in the scientific community. In this lab, we will learn how to create a zoomed-in region in a Matplotlib plot.

## Steps

### Step 1: Import necessary libraries

The first step is to import the necessary libraries. We will be using NumPy and Matplotlib for this example.

```python
import numpy as np
from matplotlib import cbook
from matplotlib import pyplot as plt
```

### Step 2: Create the plot

Next, we will create a plot using some sample data. We will be using a bivariate normal distribution as our data source.

```python
fig, ax = plt.subplots()

# make data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z
extent = (-3, 4, -4, 3)

ax.imshow(Z2, extent=extent, origin="lower")
```

### Step 3: Add an inset plot

In this step, we will add an inset plot to the main plot. This inset plot will show a zoomed-in region of the main plot.

```python
# inset axes....
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9  # subregion of the original image
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.imshow(Z2, extent=extent, origin="lower")
```

### Step 4: Add a rectangle to show the zoomed-in region

In this step, we will add a rectangle to the main plot to show where the zoomed-in region is located.

```python
ax.indicate_inset_zoom(axins, edgecolor="black")
```

### Step 5: Display the plot

Finally, we will display the plot using the `plt.show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a zoomed-in region in a Matplotlib plot. We created a main plot using sample data, added an inset plot to show a zoomed-in region of the main plot, and added a rectangle to show where the zoomed-in region is located. We then displayed the plot using the `plt.show()` function.
