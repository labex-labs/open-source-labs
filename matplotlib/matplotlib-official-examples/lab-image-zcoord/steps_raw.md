# Modifying Coordinate Formatter in Matplotlib

## Introduction

Matplotlib is a library used for data visualization in Python. It provides a wide range of tools for creating various types of plots, graphs, and charts. One of the useful features of Matplotlib is the ability to customize the coordinate formatter. In this lab, we will go through the steps of modifying the coordinate formatter in Matplotlib to report the image "z" value of the nearest pixel given x and y.

## Steps

### Step 1: Import necessary modules

To begin, we need to import the necessary modules. In this case, we will import `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a random matrix

Next, we will create a random matrix using numpy. We will use the `rand` method to create a 5x3 matrix with random values between 0 and 1. We will also set a random seed to ensure reproducibility of the results.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```

### Step 3: Create a plot

Now, we will create a plot of the matrix using `imshow` method of the Matplotlib `axes` class.

```python
fig, ax = plt.subplots()
ax.imshow(X)
```

### Step 4: Modify coordinate formatter

We will now modify the coordinate formatter to report the image "z" value of the nearest pixel given x and y. This can be achieved by customizing the `~.axes.Axes.format_coord` function.

```python
def format_coord(x, y):
    col = round(x)
    row = round(y)
    nrows, ncols = X.shape
    if 0 <= col < ncols and 0 <= row < nrows:
        z = X[row, col]
        return f'x={x:1.4f}, y={y:1.4f}, z={z:1.4f}'
    else:
        return f'x={x:1.4f}, y={y:1.4f}'

ax.format_coord = format_coord
```

### Step 5: Display the plot

Finally, we will display the plot using `plt.show()` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to modify the coordinate formatter in Matplotlib to report the image "z" value of the nearest pixel given x and y. We also learned how to create a plot of a random matrix using `imshow` method and customize the `~.axes.Axes.format_coord` function to modify the coordinate formatter.
