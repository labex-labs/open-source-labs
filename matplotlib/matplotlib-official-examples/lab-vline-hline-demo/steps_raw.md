# Matplotlib Hlines and Vlines Lab

## Introduction

In this lab, you will learn how to use hlines and vlines functions in Matplotlib. These functions are used to draw horizontal and vertical lines across a plot.

## Steps

### Step 1: Import Libraries

The first step is to import the libraries we need. In this lab, we will be using Matplotlib and NumPy libraries. Matplotlib is a data visualization library and NumPy is used for scientific computing with Python.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define Data

The next step is to define the data that we will be using in our plot. We will use NumPy's `arange` function to create an array of values from 0 to 5 with a step of 0.1. We will use this array as the x-axis. We will also define the y-axis by using the exponential function and sine function from NumPy.

```python
# Define the data
t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
```

### Step 3: Add Noise to Data

In this step, we will add some noise to the data to make it more realistic. We will use NumPy's `normal` function to generate random numbers with a mean of 0.0 and a standard deviation of 0.3.

```python
# Add noise to the data
nse = np.random.normal(0.0, 0.3, t.shape) * s
```

### Step 4: Create the Plot

Now, we will create the plot using Matplotlib's `subplots` function. We will create two subplots, one for vertical lines and one for horizontal lines. We will set the figure size to (12, 6) for better visibility.

```python
# Create the plot
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```

### Step 5: Add Vertical Lines

In this step, we will add vertical lines to the plot. We will use Matplotlib's `vlines` function to draw the vertical lines. We will also use the `transform` parameter to set the y-coordinates to be scaled from 0 to 1. We will draw two vertical lines at x=1 and x=2.

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```

### Step 6: Add Horizontal Lines

In this step, we will add horizontal lines to the plot. We will use Matplotlib's `hlines` function to draw the horizontal lines. We will draw horizontal lines at y=0.5, y=2.5, and y=4.5.

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```

### Step 7: Display the Plot

Finally, we will display the plot using Matplotlib's `show` function.

```python
# Display the plot
plt.show()
```

## Summary

In this lab, you learned how to use Matplotlib's `hlines` and `vlines` functions to draw horizontal and vertical lines across a plot. You also learned how to add noise to data and create subplots in a figure.
