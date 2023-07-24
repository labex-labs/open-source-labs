# Log Axis Tutorial

## Introduction

This tutorial will guide you through how to assign a log scale for the x-axis using `matplotlib.axes.Axes.semilogx` in Python Matplotlib. A logarithmic scale is useful when the data you want to plot spans several orders of magnitude. In this tutorial, we will use an example of plotting exponential decay as a function of time.

## Steps

### Step 1: Import the necessary libraries

We will use `numpy` and `matplotlib` libraries in this tutorial.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate data

We will generate data for exponential decay function `np.exp(-t / 5.0)` using `numpy` library.

```python
dt = 0.01
t = np.arange(dt, 20.0, dt)
```

### Step 3: Create a plot and set x-axis to logarithmic scale

We create a figure and axes object using `subplots()` method. We then plot the exponential decay function using `semilogx()` method and set the x-axis to a logarithmic scale using `set_xscale()` method. We also add a grid to the plot using `grid()` method.

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```

### Step 4: Show the plot

We use `show()` method to display the plot.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to assign a logarithmic scale to the x-axis using `matplotlib.axes.Axes.semilogx` method. We also learned how to generate data for an exponential decay function and add a grid to the plot.
