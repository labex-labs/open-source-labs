# Matplotlib imshow Tutorial

## Introduction

This tutorial will guide you through the process of displaying images using Matplotlib's `imshow` function. You will learn how to use different interpolation methods to display images with Matplotlib.

## Steps

### Step 1: Import Required Libraries

The first step is to import the required libraries. In this tutorial, we will be using `Matplotlib` and `NumPy` libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Random Grid

The next step is to create a random grid of 4x4 using `NumPy` library.

```python
np.random.seed(19680801)
grid = np.random.rand(4, 4)
```

### Step 3: Define Interpolation Methods

Define the list of interpolation methods which we want to use to display images.

```python
methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']
```

### Step 4: Create Subplots

Create subplots to display the images using interpolation methods.

```python
fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9, 6),
                        subplot_kw={'xticks': [], 'yticks': []})
```

### Step 5: Display Images

Display the images using the `imshow` function and different interpolation methods.

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```

### Step 6: Show the Plot

Show the plot using the `show` function of `Matplotlib`.

```python
plt.tight_layout()
plt.show()
```

## Summary

In this tutorial, you learned how to use Matplotlib's `imshow` function to display images with different interpolation methods. You also learned how to create subplots and display images on them using `Matplotlib`.
