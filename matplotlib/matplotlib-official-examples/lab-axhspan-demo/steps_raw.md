# Matplotlib Tutorial

## Introduction

In this tutorial, we will learn how to create lines and rectangles that span the axes in either the horizontal or vertical direction, and lines than span the axes with an arbitrary orientation using Matplotlib library in Python.

## Steps

### Step 1: Import Libraries

Firstly, we need to import the required libraries which are Matplotlib and NumPy. NumPy is used to generate the data.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data

We will use NumPy to generate data which we will use to plot the graph.

```python
t = np.arange(-1, 2, .01)
s = np.sin(2 * np.pi * t)
```

### Step 3: Create a Figure and Axes

We need to create a figure and axes object to plot the graph.

```python
fig, ax = plt.subplots()
```

### Step 4: Plot Data

Plot the data using the `plot()` function.

```python
ax.plot(t, s)
```

### Step 5: Add Horizontal Line

Add horizontal lines using the `axhline()` function.

```python
# Thick red horizontal line at y=0 that spans the xrange.
ax.axhline(linewidth=8, color='#d62728')
# Horizontal line at y=1 that spans the xrange.
ax.axhline(y=1)
```

### Step 6: Add Vertical Line

Add vertical lines using the `axvline()` function.

```python
# Vertical line at x=1 that spans the yrange.
ax.axvline(x=1)
# Thick blue vertical line at x=0 that spans the upper quadrant of the yrange.
ax.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')
```

### Step 7: Add Infinite Line

Add an infinite line going through (0, 0) to (1, 1) using the `axline()` function.

```python
# Infinite black line going through (0, 0) to (1, 1).
ax.axline((0, 0), (1, 1), color='k')
```

### Step 8: Add Rectangle

Add a rectangle using the `axhspan()` and `axvspan()` functions.

```python
# 50%-gray rectangle spanning the axes' width from y=0.25 to y=0.75.
ax.axhspan(0.25, 0.75, facecolor='0.5')
# Green rectangle spanning the axes' height from x=1.25 to x=1.55.
ax.axvspan(1.25, 1.55, facecolor='#2ca02c')
```

### Step 9: Show Plot

Finally, show the plot using the `show()` function.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create lines and rectangles that span the axes in either the horizontal or vertical direction, and lines than span the axes with an arbitrary orientation using Matplotlib library in Python. We learned how to import the required libraries, generate data, create a figure and axes, plot data, and add horizontal and vertical lines, infinite line, and rectangle to the graph.
