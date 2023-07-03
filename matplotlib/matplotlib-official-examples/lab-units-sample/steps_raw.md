# Matplotlib Tutorial: Converting Units of Axis in Python

## Introduction

In data visualization, it is important to have the correct units of measurement on the axes of the plot. This tutorial demonstrates how to convert the units of the x and y axes in Matplotlib using Python.

## Steps

### Step 1: Import the Required Libraries

First, import the required libraries. In this example, we will use Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the Units

Next, define the units for the x and y axes. In this example, we will use centimeters and inches. We can use the `basic_units` library to define the units.

```python
from basic_units import cm, inch
```

### Step 3: Create Data

Now, create some data to plot. In this example, we will use `np.arange` to create an array of values from 0 to 8 in increments of 2.

```python
cms = cm * np.arange(0, 10, 2)
```

### Step 4: Create the Plot

Create a 2x2 grid of subplots using the `subplots` function. Then, use the `plot` function to plot the data on each subplot.

```python
fig, axs = plt.subplots(2, 2, layout='constrained')

axs[0, 0].plot(cms, cms)

axs[0, 1].plot(cms, cms, xunits=cm, yunits=inch)

axs[1, 0].plot(cms, cms, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(-1, 4)  # scalars are interpreted in current units

axs[1, 1].plot(cms, cms, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(3*cm, 6*cm)  # cm are converted to inches
```

### Step 5: Display the Plot

Finally, display the plot using the `show` function.

```python
plt.show()
```

## Summary

This tutorial demonstrated how to convert the units of the x and y axes in Matplotlib using Python. By using the `xunits` and `yunits` parameters of the `plot` function, we can easily convert the units and display the correct values on the axes.
