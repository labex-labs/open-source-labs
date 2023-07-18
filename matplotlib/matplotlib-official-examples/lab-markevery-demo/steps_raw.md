# Matplotlib Markevery Tutorial

## Introduction

This tutorial will guide you through the process of using the `markevery` property of `Line2D` to draw markers at a subset of data points in Matplotlib. We will cover various ways to specify the markers, including using integers, tuples, lists, slices, and floats. We will also explore how `markevery` behaves with linear and logarithmic scales, as well as with zoomed and polar plots.

## Steps

### Step 1: Define the Data Points

First, we define the data points that we will use for our plots. In this example, we use `numpy` to generate a set of x and y values for a sine wave.

```python
import matplotlib.pyplot as plt
import numpy as np

# define a list of markevery cases to plot
cases = [
    None,
    8,
    (30, 8),
    [16, 24, 32],
    [0, -1],
    slice(100, 200, 3),
    0.1,
    0.4,
    (0.2, 0.4)
]

# data points
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
```

### Step 2: Create Plots with Linear Scales

Next, we create a set of subplots to show how `markevery` behaves with linear scales. We iterate through the `cases` list and plot each case on a separate subplot. We use the `markevery` parameter to specify which data points to mark.

```python
# create plots with linear scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```

### Step 3: Create Plots with Logarithmic Scales

We repeat the previous step, but this time with logarithmic scales. We note that the logarithmic scale causes a visual asymmetry in the marker distance for integer-based subsampling, while fraction-based subsampling creates even distributions.

```python
# create plots with logarithmic scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```

### Step 4: Create Zoomed Plots

We create another set of subplots, this time to show how `markevery` behaves on zoomed plots. We note that integer-based subsampling selects points from the underlying data and is independent of the view, while float-based subsampling is related to the Axes diagonal and changes the displayed data range.

```python
# create zoomed plots
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```

### Step 5: Create Polar Plots

Finally, we create a set of subplots to show how `markevery` behaves on polar plots. We note that the behavior is similar to that on linear scales.

```python
# create polar plots
r = np.linspace(0, 3.0, 200)
theta = 2 * np.pi * r

fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained',
                        subplot_kw={'projection': 'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(theta, r, 'o', ls='-', ms=4, markevery=markevery)
```

## Summary

In this tutorial, we learned how to use the `markevery` property of `Line2D` to draw markers at a subset of data points in Matplotlib. We explored various ways to specify the markers, including using integers, tuples, lists, slices, and floats. We also saw how `markevery` behaves with linear and logarithmic scales, as well as with zoomed and polar plots.
