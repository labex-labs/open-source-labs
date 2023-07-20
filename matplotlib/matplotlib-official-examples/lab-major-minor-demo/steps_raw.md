# Major and Minor Ticks in Matplotlib

## Introduction

In a Matplotlib plot, ticks are used to mark the position of data points on the axis. Major ticks are the larger ticks that denote the values of the data points and minor ticks are the smaller ticks that are placed between the major ticks. This tutorial shows how to use major and minor ticks in Matplotlib.

## Steps

### Step 1: Import the necessary libraries and create data

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

First, we import the necessary libraries, i.e., Matplotlib and NumPy. Then we create data to plot. In this example, we create a numpy array "t" and calculate another numpy array "s" using t.

### Step 2: Plot the data

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```

Next, we create a figure and axis object and plot the data on the axis.

### Step 3: Set the major and minor locators

```python
# Set the major locator
ax.xaxis.set_major_locator(MultipleLocator(20))
# Set the major formatter
ax.xaxis.set_major_formatter('{x:.0f}')
# Set the minor locator
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

Here, we set the major locator to place ticks at multiples of 20, set the major formatter to label the major ticks with ".0f" formatting, and set the minor locator to place ticks at multiples of 5.

### Step 4: Display the plot

```python
plt.show()
```

Finally, we display the plot.

### Step 5: Automatic tick selection for major and minor ticks

```python
# Create data
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Plot the data
fig, ax = plt.subplots()
ax.plot(t, s)

# Set the minor locator
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Set the tick parameters
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Display the plot
plt.show()
```

In this step, we create new data and plot it. Then we set the minor locator to automatically select the number of minor ticks. After that, we set the tick parameters, i.e., the width and length of the ticks and their color, for both major and minor ticks. Finally, we display the plot.

## Summary

This tutorial showed how to use major and minor ticks in Matplotlib. We saw how to set the major and minor locators and formatters and how to automatically select the number of minor ticks. We also saw how to set the tick parameters, i.e., the width and length of the ticks and their color.
