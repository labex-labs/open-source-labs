# Python Matplotlib Tutorial

## Introduction

This tutorial will show you how to create a plot with radians using the Python Matplotlib package. You will learn how to use the unit class to determine the tick locating, formatting, and axis labeling.

## Steps

### Step 1: Import necessary packages

First, import the necessary packages, including matplotlib.pyplot and numpy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create data

Create an array of values between 0 and 15 in increments of 0.01, and convert them to radians using the radians function from the basic_units package.

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```

### Step 3: Create a figure

Create a figure with two subplots using the subplots function from matplotlib.pyplot.

```python
fig, axs = plt.subplots(2)
```

### Step 4: Plot data in the first subplot

Plot the cosine of the x values in the first subplot using the plot function from matplotlib.pyplot. Use the xunits parameter to specify that the x-axis should be in radians.

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```

### Step 5: Plot data in the second subplot

Plot the cosine of the x values in the second subplot using the plot function from matplotlib.pyplot. Use the xunits parameter to specify that the x-axis should be in degrees.

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```

### Step 6: Add labels and adjust layout

Add a title and axis labels to the subplots using the title, xlabel, and ylabel functions from matplotlib.pyplot. Adjust the layout of the subplots using the tight_layout function.

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```

### Step 7: Display the plot

Display the plot using the show function from matplotlib.pyplot.

```python
plt.show()
```

## Summary

In this tutorial, you learned how to create a plot with radians using the Python Matplotlib package. You used the unit class to determine the tick locating, formatting, and axis labeling. You also learned how to create subplots, plot data, add labels, and adjust the layout of the plot.
