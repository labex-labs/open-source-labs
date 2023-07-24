# Scatter Plot with Histograms

## Introduction

This lab will guide you on how to create a scatter plot with histograms using Matplotlib. A scatter plot with histograms is a great way to visualize the distribution of two variables and their relationship. The scatter plot displays the relationship between the two variables, while the histograms show the distribution of each variable independently.

## Steps

### Step 1: Import libraries

Before we can begin, we need to import the necessary libraries. In this lab, we will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate random data

We will generate some random data to use for the scatter plot and histograms.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.random.randn(1000)
y = np.random.randn(1000)
```

### Step 3: Define the scatter_hist function

We need to define the `scatter_hist` function, which takes in x and y data, as well as three axes, the main axes for the scatter plot, and two marginal axes. It will then create the scatter and histograms inside the provided axes.

```python
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # Remove labels from the histograms
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # Create the scatter plot
    ax.scatter(x, y)

    # Determine nice limits by hand
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')
```

### Step 4: Define the axes positions using a gridspec

We will now define a `gridspec` with unequal width- and height-ratios to achieve the desired layout. We will also create the axes and pass them to the `scatter_hist` function.

```python
# Start with a square Figure.
fig = plt.figure(figsize=(6, 6))
# Add a gridspec with two rows and two columns and a ratio of 1 to 4 between
# the size of the marginal axes and the main axes in both directions.
# Also adjust the subplot parameters for a square plot.
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
# Create the Axes.
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
# Draw the scatter plot and marginals.
scatter_hist(x, y, ax, ax_histx, ax_histy)
```

### Step 5: Define the axes positions using inset_axes

We can also use `inset_axes` to position the marginals _outside_ the main axes. The advantage of doing so is that the aspect ratio of the main axes can be fixed, and the marginals will always be drawn relative to the position of the axes.

```python
# Create a Figure, which doesn't have to be square.
fig = plt.figure(layout='constrained')
# Create the main axes, leaving 25% of the figure space at the top and on the right to position marginals.
ax = fig.add_gridspec(top=0.75, right=0.75).subplots()
# The main axes' aspect can be fixed.
ax.set(aspect=1)
# Create marginal axes, which have 25% of the size of the main axes.
# Note that the inset axes are positioned *outside* (on the right and the top) of the main axes,
# by specifying axes coordinates greater than 1.
# Axes coordinates less than 0 would likewise specify positions on the left and the bottom of the main axes.
ax_histx = ax.inset_axes([0, 1.05, 1, 0.25], sharex=ax)
ax_histy = ax.inset_axes([1.05, 0, 0.25, 1], sharey=ax)
# Draw the scatter plot and marginals.
scatter_hist(x, y, ax, ax_histx, ax_histy)
```

### Step 6: Display the plot

Finally, we can display the plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a scatter plot with histograms using Matplotlib. We defined the scatter_hist function, generated random data, defined the axes positions using a gridspec and inset_axes, and displayed the plot. Scatter plots with histograms are a great way to visualize the distribution of two variables and their relationship.
