# Matplotlib Subplots Lab

## Introduction

In data visualization, it is often necessary to plot multiple graphs in a single figure. Matplotlib allows us to achieve this using subplots. In this lab, we will learn how to create subplots in Matplotlib.

## Steps

### Step 1: Import Libraries

First, we need to import the required libraries. We will be using Matplotlib and NumPy. NumPy is used to generate some sample data.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Some Sample Data

We will generate some sample data that we will use to plot our graphs.

```python
# Create some fake data.
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
x2 = np.linspace(0.0, 2.0)
y2 = np.cos(2 * np.pi * x2)
```

### Step 3: Create Subplots Using `subplots()`

We will create subplots using `subplots()` function. We will create two subplots, one above the other.

```python
# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1)
```

### Step 4: Set Title and Axes Labels

We will set the title and axis labels for our subplots.

```python
# Set title and axis labels
fig.suptitle('A tale of 2 subplots')

ax1.set_ylabel('Damped oscillation')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Undamped')
```

### Step 5: Plot Data on Subplots

We will now plot our data on the subplots.

```python
# Plot data on subplots
ax1.plot(x1, y1, 'o-')
ax2.plot(x2, y2, '.-')
```

### Step 6: Display the Plots

Finally, we will display the plots using `plt.show()`.

```python
# Display the plots
plt.show()
```

## Summary

In this lab, we learned how to create subplots in Matplotlib. We used the `subplots()` function to create subplots and set the title, axis labels, and plot data on the subplots. By using subplots, we can display multiple graphs in a single figure, which is useful for data visualization.
