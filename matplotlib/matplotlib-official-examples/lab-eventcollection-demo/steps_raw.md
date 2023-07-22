# Matplotlib Line Plot with Data Points Lab

## Introduction

In this lab, we will learn how to create a line plot with data points using Matplotlib in Python. We will use the `EventCollection` class in Matplotlib to mark the locations of the x and y data points on the respective axes for each curve.

## Steps

### Step 1: Import necessary libraries

First, we need to import the required libraries. We will use `numpy` to create random data, `matplotlib.pyplot` to create the plot, and `EventCollection` from `matplotlib.collections` to mark the locations of data points.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import EventCollection
```

### Step 2: Create random data

We will create random data for two curves using `numpy.random.random()` function. We will generate two sets of 10 random numbers between 0 and 1 and store them in an array.

```python
# create random data
xdata = np.random.random([2, 10])
```

### Step 3: Sort the data

To make clean curves, we will sort the data using the `sort()` method.

```python
# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]
# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()
```

### Step 4: Create y data points

We will create some y data points for each curve by performing some mathematical operations on the sorted x data points.

```python
# create some y data points
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3
```

### Step 5: Create the plot

We will create the plot using `matplotlib.pyplot.plot()` function.

```python
# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')
```

### Step 6: Create the events

We will create the events marking the x and y data points using `EventCollection()` function.

```python
# create the events marking the x data points
xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)

# create the events marking the y data points
yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
                           orientation='vertical')
```

### Step 7: Add the events to the plot

We will add the events to the plot using `matplotlib.pyplot.add_collection()` function.

```python
# add the events to the axis
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)
```

### Step 8: Set the limits and add title

We will set the limits of the x and y axes and add a title to the plot using `matplotlib.pyplot.xlim()`, `matplotlib.pyplot.ylim()`, and `matplotlib.pyplot.title()` functions.

```python
# set the limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_title('line plot with data points')
```

### Step 9: Display the plot

Finally, we will display the plot using `matplotlib.pyplot.show()` function.

```python
# display the plot
plt.show()
```

## Summary

In this lab, we learned how to create a line plot with data points using Matplotlib in Python. We used the `EventCollection` class in Matplotlib to mark the locations of the x and y data points on the respective axes for each curve.
