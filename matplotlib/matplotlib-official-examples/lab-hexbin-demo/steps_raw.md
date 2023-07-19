# Hexagonal Binned Plot Tutorial

## Introduction

This tutorial will guide you through creating a hexagonal binned plot using Matplotlib in Python. Hexagonal binned plots are 2D histogram plots in which the bins are hexagons and the color represents the number of data points within each bin. They are useful for visualizing the distribution of large datasets.

## Steps

### Step 1: Import Libraries

To create a hexagonal binned plot, we need to import the following libraries:

- `matplotlib.pyplot` for creating the plot
- `numpy` for generating random data

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data

We will generate 100,000 data points using `numpy.random.standard_normal()` and `numpy.random.standard_normal()`. `standard_normal()` generates random numbers from a standard normal distribution with a mean of 0 and a standard deviation of 1.

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```

### Step 3: Create the Hexagonal Binned Plot

We will create the hexagonal binned plot using `matplotlib.pyplot.hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

Here, we set the grid size to 50 and the color map to 'inferno'. We also add a color bar to show the count of data points within each hexagon.

### Step 4: Add a Logarithmic Color Scale

We can add a logarithmic color scale to the hexagonal binned plot by setting `bins='log'` in `hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("With a log color scale")

cb = fig.colorbar(hb, ax=ax, label='log10(N)')
```

### Step 5: Display the Plot

Finally, we display the plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create a hexagonal binned plot using `matplotlib.pyplot.hexbin()` in Python. We generated random data using `numpy.random.standard_normal()` and `numpy.random.standard_normal()`, created the hexagonal binned plot, added a logarithmic color scale, and displayed the plot using `plt.show()`.
