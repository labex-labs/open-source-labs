# Python Matplotlib Tutorial - Contourf and Log Color Scale

## Introduction

In this lab, we will learn how to use the `contourf` function in Matplotlib to create filled contour plots with a logarithmic color scale. We will use a dataset with positive and negative values to demonstrate this feature.

## Steps

### Step 1: Import the necessary libraries

We need to import the following libraries:

- `matplotlib.pyplot` for creating plots and visualizations
- `numpy` for generating the dataset

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate the dataset

We will generate a dataset with positive and negative values using `numpy`:

```python
N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)

X, Y = np.meshgrid(x, y)

# A low hump with a spike coming out.
# Needs to have z/colour axis on a log scale, so we see both hump and spike.
# A linear scale only shows the spike.
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
z = Z1 + 50 * Z2

# Put in some negative values (lower left corner) to cause trouble with logs:
z[:5, :5] = -1

# The following is not strictly essential, but it will eliminate
# a warning.  Comment it out to see the warning.
z = ma.masked_where(z <= 0, z)
```

### Step 3: Create the plot

We will use the `contourf` function to create a filled contour plot with a logarithmic color scale:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```

### Step 4: Customize the plot

We can customize the plot by adding labels, titles, and changing the color map:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.coolwarm)

ax.set_title('Contourf Plot with Log Color Scale')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

cbar = fig.colorbar(cs)

plt.show()
```

## Summary

In this lab, we learned how to use the `contourf` function in Matplotlib to create filled contour plots with a logarithmic color scale. We also learned how to customize the plot by adding labels, titles, and changing the color map.
