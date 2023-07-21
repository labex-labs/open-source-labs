# Creating Boxes from Error Bars using PatchCollection

## Introduction

In this lab, we will learn how to create box plots from error bars using PatchCollection. Box plots are useful for displaying the range and distribution of data. By adding a rectangle patch defined by the limits of the bars in both the x- and y-directions, we can make a more visually appealing error bar plot.

## Steps

### Step 1: Import Libraries

We will first import the necessary libraries, including `numpy` and `matplotlib`.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
```

### Step 2: Prepare Data

We will then prepare the data for our box plot. We will create some dummy data for the x and y values, as well as the error values.

```python
# Number of data points
n = 5

# Dummy data
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# Dummy errors (above and below)
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```

### Step 3: Create Function for Error Boxes

We will now create a function called `make_error_boxes` that will create the rectangle patch defined by the limits of the bars in both the x- and y-directions.

```python
def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
                     edgecolor='none', alpha=0.5):

    # Loop over data points; create box from errors at each point
    errorboxes = [Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
                  for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)]

    # Create patch collection with specified colour/alpha
    pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
                         edgecolor=edgecolor)

    # Add collection to axes
    ax.add_collection(pc)

    # Plot errorbars
    artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
                          fmt='none', ecolor='k')

    return artists
```

### Step 4: Create Figure and Axes

We will now create the figure and axes for our box plot using `plt.subplots()`.

```python
# Create figure and axes
fig, ax = plt.subplots(1)
```

### Step 5: Call Function to Create Error Boxes

We will now call the `make_error_boxes()` function to create the error boxes on our plot.

```python
# Call function to create error boxes
_ = make_error_boxes(ax, x, y, xerr, yerr)
```

### Step 6: Display the Plot

Finally, we will display the plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to create box plots from error bars using PatchCollection in Matplotlib. By adding a rectangle patch defined by the limits of the bars in both the x- and y-directions, we were able to create a more visually appealing error bar plot.
