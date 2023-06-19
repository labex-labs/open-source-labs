# Matplotlib Tutorial - Creating Subplots

## Introduction

Matplotlib is a Python library used for creating visualizations such as line plots, scatter plots, bar plots, and subplots, among others. In this lab, you will learn how to create a figure with two subplots using `.pyplot.subplot`.

## Steps

### Step 1: Import the necessary libraries

For this tutorial, we will be using the `pyplot` module from the Matplotlib library and the `numpy` library.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the data

We will define two sets of data that we will use to create our subplots.

```python
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
```

### Step 3: Create the subplots

We will create a figure with two subplots using `.pyplot.subplot`.

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

The `subplot()` function takes three arguments: the number of rows, the number of columns, and the index of the current plot. The index starts from 1 in the upper left corner and increases row-wise. In this example, we create a figure with two subplots: one on top and one on the bottom.

In the first subplot, we plot `t1` against `f(t1)` and `t2` against `f(t2)`. We set the color of the first plot to blue and add circular markers to each data point. We set the color of the second plot to black.

In the second subplot, we plot `t2` against the cosine function of `2*np.pi*t2`. We set the color of the plot to orange and the linestyle to dashed.

### Step 4: References

The use of the following functions, methods, classes, and modules is shown in this example:

- `matplotlib.pyplot.figure`
- `matplotlib.pyplot.subplot`

## Summary

In this lab, we learned how to create a figure with two subplots using `.pyplot.subplot`. We defined two sets of data and plotted them in two subplots using different colors and line styles. We also provided references to the functions and modules used in this example.
