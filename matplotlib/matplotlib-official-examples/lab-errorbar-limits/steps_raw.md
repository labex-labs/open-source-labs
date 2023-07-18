# Python Matplotlib Errorbar Lab

## Introduction

Error bars are used in graphs and charts to show the potential error or uncertainty in a measurement or data point. Python Matplotlib is a popular data visualization library that provides different types of error bar plots. In this lab, we will learn how to create error bar plots with upper and lower limits using Matplotlib.

## Steps

### Step 1: Import Required Libraries

We will begin by importing the required libraries, including NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define Data

Next, we will define some example data to plot. Here, we will create an array of x-values, y-values, and their corresponding error values.

```python
x = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y = np.exp(-x)
xerr = 0.1
yerr = 0.2
```

### Step 3: Create Simple Error Bar Plot

We will create a simple error bar plot with standard error bars using the `errorbar` function. Here, we will set the x and y values along with their corresponding error values. We will also set the line style to dotted.

```python
fig, ax = plt.subplots(figsize=(7, 4))

# standard error bars
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```

### Step 4: Add Upper Limits

To add upper limits to the error bars, we will use the `uplims` parameter of the `errorbar` function. We will also add a constant value of 0.5 to the y-values to differentiate this plot from the previous one.

```python
# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```

### Step 5: Add Lower Limits

To add lower limits to the error bars, we will use the `lolims` parameter of the `errorbar` function. We will also add a constant value of 1.0 to the y-values to differentiate this plot from the previous ones.

```python
# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```

### Step 6: Add Upper and Lower Limits

To add both upper and lower limits to the error bars, we will use both the `uplims` and `lolims` parameters of the `errorbar` function. We will also add a marker to the plot to differentiate it from the previous ones.

```python
# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```

### Step 7: Add Limits to Both X and Y Axes

Finally, we will add limits to both the x and y axes. We will use the `xlolims` and `xuplims` parameters to add limits to the x-axis error bars.

```python
# Plot a series with lower and upper limits in both x & y
# constant x-error with varying y-error
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# mock up some limits by modifying previous data
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # only limited at this index
uplims[[3]] = True  # only limited at this index

# do the plotting
ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8, linestyle='none')
```

### Step 8: Display Plot

Finally, we will display the plot using the `show` function.

```python
# tidy up the figure
ax.set_xlim((0, 5.5))
ax.set_title('Errorbar upper and lower limits')
plt.show()
```

## Summary

In this lab, we learned how to create error bar plots with upper and lower limits using Matplotlib. We used the `errorbar` function to create different plots with upper and lower limits. We also learned how to add limits to both the x and y axes.
