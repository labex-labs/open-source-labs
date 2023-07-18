# Python Matplotlib Tutorial

## Introduction

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. Matplotlib was originally developed by John D. Hunter in 2003.

This tutorial will guide you on how to use the `.step()` and `.plot()` functions in Matplotlib.

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries, which are `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create data for the plot

Next, let's create some data that we will use to plot. We will use the `numpy.arange()` function to create an array of values from 0 to 14 and store it in the variable `x`. We will also use the `numpy.sin()` function to create an array of values that are the sine of each value in `x` divided by 2, and store it in the variable `y`.

```python
x = np.arange(14)
y = np.sin(x / 2)
```

### Step 3: Plot using `.step()`

We can use the `.step()` function to create piece-wise constant curves. The `where` parameter determines where the steps should be drawn. We will create three plots using different values for `where`.

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

The above code will create a plot with three piece-wise constant curves, each with a different value for `where`.

### Step 4: Plot using `.plot()`

We can achieve the same behavior as `.step()` by using the `drawstyle` parameter of the `.plot()` function. We will create three plots using different values for `drawstyle`.

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

The above code will create a plot with three piece-wise constant curves, each with a different value for `drawstyle`.

## Summary

In this tutorial, we learned how to use the `.step()` and `.plot()` functions in Matplotlib to create piece-wise constant curves. We also learned how to use the `where` and `drawstyle` parameters to determine where the steps should be drawn.
