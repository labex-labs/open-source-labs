# Lab: Creating a Plot with Python Matplotlib

## Introduction

This lab will guide you through creating a plot with Python Matplotlib. Matplotlib is a plotting library for the Python programming language. In this lab, you will learn how to customize a plot's properties including colors, line widths, and more.

## Steps

### Step 1: Import necessary modules

First, we need to import the necessary modules. In this case, we need to import `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the property cycle and retrieve colors

Next, we need to define the property cycle and retrieve the colors from it.

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```

### Step 3: Define line widths

Now, we define the line widths for our plot.

```python
lwbase = plt.rcParams['lines.linewidth']
thin = lwbase / 2
thick = lwbase * 3
```

### Step 4: Create subplots

We create a 2x2 grid of subplots.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
```

### Step 5: Add horizontal and vertical lines

Now, we add horizontal and vertical lines to each subplot using the colors from the property cycle.

```python
for icol in range(2):
    if icol == 0:
        lwx, lwy = thin, lwbase
    else:
        lwx, lwy = lwbase, thick
    for irow in range(2):
        for i, color in enumerate(colors):
            axs[irow, icol].axhline(i, color=color, lw=lwx)
            axs[irow, icol].axvline(i, color=color, lw=lwy)
```

### Step 6: Customize subplots

We customize the subplots by setting the background color of the bottom subplots to black, setting the x-axis ticks, and adding a title to each subplot.

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```

### Step 7: Customize y-axis ticks

We customize the y-axis ticks for the leftmost subplots.

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```

### Step 8: Add title to plot

We add a title to the entire plot.

```python
fig.suptitle('Colors in the default prop_cycle', fontsize='large')
```

### Step 9: Display the plot

Finally, we display the plot.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a plot with Python Matplotlib. We customized the properties of the plot including colors and line widths. We also learned how to create subplots and customize their appearance.
