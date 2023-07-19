# Matplotlib Tutorial: Simple Plot

## Introduction

This tutorial will guide you through creating a simple plot using Python's Matplotlib library. Matplotlib is a data visualization library widely used in scientific computing to create static, animated, and interactive visualizations in Python.

## Steps

### Step 1: Import necessary libraries

Before we start creating the plot, we need to import the necessary libraries. In this case, we need to import `numpy` and `matplotlib.pyplot`.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Generate Data

We need to generate data for the plot. In this example, we will generate two arrays, `t` and `s`.

```python
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
```

### Step 3: Create the plot

Now that we have the data, we can create the plot. First, we create a figure and axis object using `plt.subplots()`. Then, we plot the data using `ax.plot()`.

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```

### Step 4: Add labels and title

We can add labels to the x and y axis, as well as a title to the plot using `ax.set()`.

```python
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
```

### Step 5: Add a grid

Finally, we can add a grid to the plot using `ax.grid()`.

```python
ax.grid()
```

### Step 6: Show the plot

We can use `plt.show()` to display the plot.

```python
plt.show()
```

## Summary

This tutorial has walked you through creating a simple plot using Matplotlib. We started by importing the necessary libraries, generated data for the plot, created the plot, added labels and a title, and added a grid. Matplotlib is a powerful library for creating visualizations in Python, and this tutorial is just the beginning of what you can do with it.
