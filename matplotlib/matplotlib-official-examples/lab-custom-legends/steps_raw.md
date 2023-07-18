# Composing Custom Legends

## Introduction

The Python Matplotlib library provides a flexible way to create and customize legends in a plot. Legends are an essential component of any plot, as they provide a clear and concise explanation of the data represented in the plot. This lab will guide you through the process of composing custom legends using Matplotlib objects.

## Steps

### Step 1: Plotting Lines

In this step, we will plot a set of lines using the Matplotlib library. First, we create some random data using NumPy. Next, we set the color cycle using the `cycler` function to specify the color map. Finally, we plot the data using the `plot` function and call `legend()` to generate the legend.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set random state for reproducibility
np.random.seed(19680801)

# Create random data
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# Set color cycle
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# Plot data and generate legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```

### Step 2: Composing Custom Legend

In this step, we will create a custom legend using Matplotlib objects. First, we import the `Line2D` class from the `matplotlib.lines` module. Next, we create a list of `Line2D` objects with custom color, width, and label attributes. Finally, we plot the data again using the `plot` function and call `legend()` with the custom lines and corresponding labels.

```python
# Import Line2D class
from matplotlib.lines import Line2D

# Create custom lines
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Plot data and generate custom legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```

### Step 3: Composing Custom Legend with Different Matplotlib Objects

In this step, we will create a custom legend using different Matplotlib objects, including `Line2D` and `Patch`. First, we import the `Patch` class from the `matplotlib.patches` module. Next, we create a list of `Line2D` and `Patch` objects with custom attributes. Finally, we call `legend()` with the custom objects and corresponding labels.

```python
# Import Line2D and Patch classes
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Create legend elements
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
                   Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Color Patch')]

# Plot data and generate custom legend
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```

## Summary

In this lab, we learned how to create custom legends using Matplotlib objects. We started by plotting a set of lines and generating a default legend. Next, we composed a custom legend using `Line2D` objects with custom attributes. Finally, we created a custom legend using different Matplotlib objects, including `Line2D` and `Patch`. By using custom legends, we can provide a clear and concise explanation of the data represented in a plot.
