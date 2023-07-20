# Python Matplotlib 3D Histogram Lab

## Introduction

In this lab, you will learn how to create a 3D histogram of 2D data using Python Matplotlib. A histogram is a graphical representation of data that groups a range of values into bins, and the 3D histogram extends this concept by adding a third dimension to the visualization.

## Steps

### Step 1: Import Libraries

Before we can create the 3D histogram, we need to import the necessary libraries. In this case, we will be using NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data

Next, we will generate some random 2D data to use for the histogram. We will use NumPy's `random.rand()` function to generate 100 random values for both the x and y variables.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```

### Step 3: Create the Histogram

Now that we have our data, we can create the 3D histogram. We will use NumPy's `histogram2d()` function to create a 2D histogram of our data, and then use Matplotlib's `bar3d()` function to create a 3D bar graph of the histogram.

```python
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
```

### Step 4: Display the Histogram

Finally, we can display the histogram using Matplotlib's `show()` function.

```python
plt.show()
```

## Summary

In this lab, you learned how to create a 3D histogram of 2D data using Python Matplotlib. You also learned how to generate random data, create a 2D histogram, and create a 3D bar graph of the histogram. By following these steps, you can create your own 3D histograms to visualize your own data.
