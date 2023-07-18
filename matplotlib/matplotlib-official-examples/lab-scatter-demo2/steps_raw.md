# Python Matplotlib Scatter Plot Tutorial

## Introduction

In this tutorial, we will learn how to create a scatter plot with varying marker colors and sizes using Python Matplotlib.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries, which are Matplotlib and Numpy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Load data

We will load a numpy record array from yahoo csv data with fields date, open, high, low, close, volume, adj_close from the mpl-data/sample_data directory. The record array stores the date as an np.datetime64 with a day unit ('D') in the date column.

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days
```

### Step 3: Calculate values for scatter plot

We will calculate delta1, volume, and close values for scatter plot.

```python
delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]
```

### Step 4: Create scatter plot

We will create a scatter plot with varying marker colors and sizes using the calculated values.

```python
fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()
```

## Summary

We have learned how to create a scatter plot with varying marker colors and sizes using Python Matplotlib. We started by importing the necessary libraries, then loading data, calculating values for scatter plot, and creating the scatter plot.
