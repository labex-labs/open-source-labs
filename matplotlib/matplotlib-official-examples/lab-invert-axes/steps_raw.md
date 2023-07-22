# Inverting Axes of a Matplotlib Plot

## Introduction

Inverting axes in a Matplotlib plot can be useful when visualizing data with a non-linear relationship. This lab will guide you through the process of inverting the axes of a plot using Matplotlib in Python.

## Steps

### Step 1: Import Required Libraries

The first step is to import the required libraries. In this lab, we will be using Matplotlib and NumPy. Matplotlib is a popular plotting library in Python, and NumPy is a library for scientific computing in Python.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data

Next, we need to create some data to plot. In this example, we will create an array of values for time (`t`) and an array of values for voltage (`s`).

```python
t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
```

### Step 3: Create the Plot

Now, we can create the plot using Matplotlib. We will use the `plot` function to plot our data and set the limits of the x-axis using the `set_xlim` function.

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```

### Step 4: Invert the Axes

To invert the x-axis, we simply need to reverse the order of the limits using the `set_xlim` function. In this example, we set the x-axis limits from 5 to 0, which effectively reverses the x-axis.

```python
ax.set_xlim(5, 0)  # decreasing time
```

### Step 5: View the Inverted Plot

Finally, we can view the inverted plot using the `show` function.

```python
plt.show()
```

## Summary

Inverting the axes of a Matplotlib plot can be useful when visualizing data with a non-linear relationship. This lab provided a step-by-step guide on how to invert the x-axis of a plot using Matplotlib in Python. By reversing the order of the x-axis limits, we can effectively invert the x-axis of our plot.
