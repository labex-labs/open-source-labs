# Matplotlib Tutorial Lab

## Introduction

This lab will guide you through the process of creating figures with titles, subtitles, and global labels using the Matplotlib library in Python. You will learn how to create different types of oscillation plots and how to add a global x- or y-label to a figure.

## Steps

### Step 1: Create a damped and undamped oscillation plot

First, we will create a figure with two subplots, one for a damped oscillation and another for an undamped oscillation. We will use the `np.linspace()` function to create an array of time values and then plot the corresponding amplitude values for each type of oscillation using the `np.cos()` and `np.exp()` functions.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('damped')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('time (s)')
ax2.set_title('undamped')

fig.suptitle('Different types of oscillations', fontsize=16)

plt.show()
```

### Step 2: Add global x- and y-labels to a figure

Next, we will add global x- and y-labels to a figure showing the relative stock prices of different companies over time. We will use the `np.genfromtxt()` function to read in a CSV file containing stock price data and then plot the data for each company using subplots. We will use the `fig.supxlabel()` and `fig.supylabel()` methods to add global x- and y-labels to the figure.

```python
from matplotlib.cbook import get_sample_data

with get_sample_data('Stocks.csv') as file:
    stocks = np.genfromtxt(
        file, delimiter=',', names=True, dtype=None,
        converters={0: lambda x: np.datetime64(x, 'D')}, skip_header=1)

fig, axs = plt.subplots(4, 2, figsize=(9, 5), layout='constrained',
                        sharex=True, sharey=True)
for nn, ax in enumerate(axs.flat):
    column_name = stocks.dtype.names[1+nn]
    y = stocks[column_name]
    line, = ax.plot(stocks['Date'], y / np.nanmax(y), lw=2.5)
    ax.set_title(column_name, fontsize='small', loc='left')
fig.supxlabel('Year')
fig.supylabel('Stock price relative to max')

plt.show()
```

## Summary

In this lab, you learned how to create figures with titles and subtitles using the Matplotlib library in Python. You also learned how to add global x- and y-labels to a figure. These skills are useful for creating clear and informative visualizations of data.
