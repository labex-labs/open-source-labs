# Python Matplotlib Tutorial

## Introduction

Matplotlib is a data visualization library that is widely used in Python. It allows users to create a wide variety of visualizations, including line plots, scatter plots, bar charts, and more. In this lab, you will learn how to use the `symlog` axis scaling in Matplotlib to create symmetric log plots.

## Steps

### Step 1: Import Libraries

Before we can begin, we need to import the necessary libraries. In this lab, we will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data

Next, we need to generate some data to plot. In this example, we will create three arrays: one for the x-axis values, one for the y-axis values in the first plot, and one for the y-axis values in the third plot.

```python
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y1 = np.arange(0, 100.0, dt)
y3 = np.sin(x / 3.0)
```

### Step 3: Create Plots

Now that we have our data, we can create our plots. We will create three subplots, each with a different `symlog` axis scaling.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
```

### Step 4: Create Symlog Plot on x-axis

In the first subplot, we will create a `symlog` plot on the x-axis. We will also add a minor grid to the x-axis.

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```

### Step 5: Create Symlog Plot on y-axis

In the second subplot, we will create a `symlog` plot on the y-axis.

```python
ax1.plot(y1, x)
ax1.set_yscale('symlog')
ax1.set_ylabel('symlogy')
```

### Step 6: Create Symlog Plot on both x-axis and y-axis

In the third subplot, we will create a `symlog` plot on both the x-axis and y-axis. We will also set the `linthresh` parameter to 0.015.

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```

### Step 7: Display the Plots

Finally, we can display our plots using the `show()` method.

```python
plt.show()
```

## Summary

In this lab, you learned how to use the `symlog` axis scaling in Matplotlib to create symmetric log plots. Specifically, you learned how to create a `symlog` plot on the x-axis, on the y-axis, and on both the x-axis and y-axis.
