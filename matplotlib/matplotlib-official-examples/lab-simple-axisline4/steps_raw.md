# Simple Matplotlib Tutorial

## Introduction

This tutorial will guide you through the steps of creating a simple plot using Matplotlib, a Python library used for data visualization. We will be using the `host_subplot` module to create a plot with two y-axes.

## Steps

### Step 1: Import necessary modules

The first step is to import the necessary modules for our plot. We will be using `numpy` to generate our x and y data, `matplotlib.pyplot` to create the plot, and `mpl_toolkits.axes_grid1` to create the second y-axis.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
```

### Step 2: Generate data

Next, we need to generate our x and y data. We will be generating a sine wave for this example.

```python
xx = np.arange(0, 2*np.pi, 0.01)
yy = np.sin(xx)
```

### Step 3: Create the plot

Now we can create our plot using the `host_subplot` function. This function creates a subplot with two y-axes.

```python
ax = host_subplot(111)
ax.plot(xx, yy)
```

### Step 4: Create the second y-axis

To create the second y-axis, we need to create a new axis object using the `twin` function.

```python
ax2 = ax.twin()
```

### Step 5: Set tick labels for the second y-axis

We can set the tick labels for the second y-axis using the `set_xticks` function and passing in the tick locations and labels as arguments.

```python
ax2.set_xticks([0., .5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```

### Step 6: Hide tick labels for the right y-axis

We can hide the tick labels for the right y-axis using the `major_ticklabels.set_visible` function.

```python
ax2.axis["right"].major_ticklabels.set_visible(False)
```

### Step 7: Show tick labels for the top y-axis

We can show the tick labels for the top y-axis using the same `major_ticklabels.set_visible` function.

```python
ax2.axis["top"].major_ticklabels.set_visible(True)
```

### Step 8: Display the plot

Finally, we can display our plot using the `show` function.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create a simple plot with two y-axes using Matplotlib. We used the `host_subplot` module to create the plot and the `mpl_toolkits.axes_grid1` module to create the second y-axis. We generated our data using `numpy` and displayed the plot using `matplotlib.pyplot`.
