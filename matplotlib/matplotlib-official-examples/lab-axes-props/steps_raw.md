# Matplotlib Lab

## Introduction

In this lab, you will learn how to customize the axis tick and grid properties in a Matplotlib plot using Python. Matplotlib is a data visualization library in Python that allows you to create a variety of charts and graphs. In this lab, we will focus on customizing the axis tick and grid properties of a line plot.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries. We will be using Matplotlib and NumPy in this lab. NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data

Next, we will create some data to plot. In this example, we will be using the sine function to generate a wave.

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
```

### Step 3: Create a Plot

Now, we will create a plot using the data we just created.

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```

### Step 4: Customize Axis Tick and Grid Properties

We can customize the axis tick and grid properties using the `grid()` and `tick_params()` functions. In this example, we will change the color and size of the tick labels and the width and style of the grid lines.

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```

### Step 5: Display the Plot

Finally, we will display the plot.

```python
plt.show()
```

## Summary

In this lab, you learned how to customize the axis tick and grid properties in a Matplotlib plot using Python. You can use the `grid()` function to control the visibility and style of the grid lines, and the `tick_params()` function to control the appearance of the tick labels. By customizing these properties, you can create more visually appealing and informative plots.
