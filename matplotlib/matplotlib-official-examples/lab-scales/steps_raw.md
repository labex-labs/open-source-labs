# Matplotlib Tutorial: Scale Transformations

## Introduction

Matplotlib is a Python library used for data visualization. It allows users to create a wide variety of charts, plots, and graphs. One of the key features of Matplotlib is its ability to apply scale transformations to axes. This allows for greater flexibility in presenting data, especially when dealing with very large or very small numbers. In this lab, we will learn how to apply various scale transformations to axes using Matplotlib.

## Steps

### Step 1: Import Libraries and Generate Data

First, we need to import the necessary libraries and generate some data to plot. In this example, we will use a normal distribution to generate data for the y-axis.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
```

### Step 2: Create a Linear Scale Plot

The first type of scale transformation we will explore is linear. This is the default scale used in Matplotlib. To create a linear scale plot, we use the `set_yscale()` method and pass in the string `'linear'`. We also add a title and grid to the plot.

```python
# linear
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear Scale')
plt.grid(True)
```

### Step 3: Create a Logarithmic Scale Plot

The next type of scale transformation we will explore is logarithmic. To create a logarithmic scale plot, we use the `set_yscale()` method and pass in the string `'log'`. We also add a title and grid to the plot.

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.grid(True)
```

### Step 4: Create a Symmetrical Logarithmic Scale Plot

The third type of scale transformation we will explore is symmetrical logarithmic. This type of scale is useful when dealing with data that contains both positive and negative values. To create a symmetrical logarithmic scale plot, we use the `set_yscale()` method and pass in the string `'symlog'`. We also set the `linthresh` parameter to `0.02` to specify the range of values around zero that will be linearly scaled. We also add a title and grid to the plot.

```python
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Symmetrical Logarithmic Scale')
plt.grid(True)
```

### Step 5: Create a Logit Scale Plot

The fourth type of scale transformation we will explore is logit. This type of scale is useful when dealing with data that is bounded by 0 and 1. To create a logit scale plot, we use the `set_yscale()` method and pass in the string `'logit'`. We also add a title and grid to the plot.

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit Scale')
plt.grid(True)
```

### Step 6: Create a Custom Scale Plot

The final type of scale transformation we will explore is custom. This allows us to define our own forward and inverse functions for the scale transformation. In this example, we will define a custom function to take the square root of the data. To create a custom scale plot, we use the `set_yscale()` method and pass in the string `'function'`. We also define the `forward()` and `inverse()` functions and pass them as arguments to the `functions` parameter. We also add a title and grid to the plot.

```python
# Function x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Custom Scale')
plt.grid(True)
```

### Step 7: Create a Mercator Transform Scale Plot

As a bonus, we will also create a plot using the Mercator transform function. This is not a built-in function in Matplotlib, but we can define our own forward and inverse functions to create a Mercator transform scale plot. In this example, we will define the `forward()` and `inverse()` functions for the Mercator transform. We also add a title and grid to the plot.

```python
# Function Mercator transform
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```

## Summary

In this lab, we learned how to apply various scale transformations to axes using Matplotlib. We explored linear, logarithmic, symmetrical logarithmic, logit, custom, and Mercator transform scale transformations. By applying these scale transformations, we can better visualize data that contains very large or very small numbers, as well as data that contains both positive and negative values.
