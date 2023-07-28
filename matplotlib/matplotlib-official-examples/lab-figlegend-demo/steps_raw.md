# Matplotlib Tutorial: Creating Legends

## Introduction

In data visualization, legends help the viewer understand what they are looking at. Legends in Matplotlib are labels that describe the elements of a graph. This tutorial will show how to create legends for a Matplotlib figure.

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries - NumPy and Matplotlib. NumPy is a Python library that is used for working with arrays, while Matplotlib is a data visualization library.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating a Basic Plot

To create a basic plot, we need to define the x and y values and then plot them using `plt.plot()`. Here, we will plot two sine waves.

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```

### Step 3: Adding a Legend

To add a legend to the plot, we use the `plt.legend()` function. We can pass the labels for each line as a list of strings to the `labels` parameter of the function.

```python
plt.legend(labels=['sin(2pix)', 'sin(4pix)'])
```

### Step 4: Customizing the Legend

We can customize the legend by changing its position, font size, and other parameters. To change the position of the legend, we use the `loc` parameter. We can also change the font size using the `fontsize` parameter.

```python
plt.legend(labels=['sin(2pix)', 'sin(4pix)'], loc='lower right', fontsize='large')
```

### Step 5: Creating a Legend for Subplots

When creating subplots, we can create a legend for all the subplots by using the `fig.legend()` function. Here, we will create two subplots and plot two lines on each subplot.

```python
fig, axs = plt.subplots(1, 2)

x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.exp(-x)
l1, = axs[0].plot(x, y1)
l2, = axs[0].plot(x, y2, marker='o')

y3 = np.sin(4 * np.pi * x)
y4 = np.exp(-2 * x)
l3, = axs[1].plot(x, y3, color='tab:green')
l4, = axs[1].plot(x, y4, color='tab:red', marker='^')

fig.legend((l1, l2), ('Line 1', 'Line 2'), loc='upper left')
fig.legend((l3, l4), ('Line 3', 'Line 4'), loc='upper right')
```

### Step 6: Placing the Legend Outside the Axes

Sometimes, we may want the legend to be outside the axes. We can use the `loc` parameter to specify the location of the legend outside the axes.

```python
fig, axs = plt.subplots(1, 2, layout='constrained')

x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.exp(-x)
l1, = axs[0].plot(x, y1)
l2, = axs[0].plot(x, y2, marker='o')

y3 = np.sin(4 * np.pi * x)
y4 = np.exp(-2 * x)
l3, = axs[1].plot(x, y3, color='tab:green')
l4, = axs[1].plot(x, y4, color='tab:red', marker='^')

fig.legend((l1, l2), ('Line 1', 'Line 2'), loc='upper left')
fig.legend((l3, l4), ('Line 3', 'Line 4'), loc='outside right upper')
```

## Summary

In this tutorial, we have learned how to create legends for Matplotlib figures. We have seen how to create a basic plot, add a legend, customize the legend, create a legend for subplots, and place the legend outside the axes. Legends are an important aspect of data visualization, and knowing how to create them is an essential skill for any data scientist or analyst.
