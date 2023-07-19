# Python Matplotlib Tutorial

## Introduction

In this tutorial, you will learn how to use Matplotlib to create visualizations in Python. Matplotlib is a popular data visualization library in Python used to create a variety of charts and graphs. With Matplotlib, you can create line plots, scatter plots, bar plots, histograms, and many other types of visualizations.

## Steps

### Step 1: Import Matplotlib

Before creating any visualization, we need to import the Matplotlib library. We will also use the NumPy library to generate some sample data.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Sample Data

Let's create some sample data that we will use to create visualizations. We will generate four sets of data, each with 11 x,y data points.

```python
x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
```

### Step 3: Create a Figure with Subplots

Now we will create a figure with four subplots, one for each dataset. We will also set the x and y limits to be the same for all subplots.

```python
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.08})
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
```

### Step 4: Plot the Data

For each subplot, we will plot the x and y data points and add a linear regression line. We will also add a text box with some statistics about the data.

```python
datasets = {
    'I': (x, y1),
    'II': (x, y2),
    'III': (x, y3),
    'IV': (x4, y4)
}

for ax, (label, (x, y)) in zip(axs.flat, datasets.items()):
    ax.text(0.1, 0.9, label, fontsize=20, transform=ax.transAxes, va='top')
    ax.tick_params(direction='in', top=True, right=True)
    ax.plot(x, y, 'o')

    # linear regression
    p1, p0 = np.polyfit(x, y, deg=1)  # slope, intercept
    ax.axline(xy1=(0, p0), slope=p1, color='r', lw=2)

    # add text box for the statistics
    stats = (f'$\\mu$ = {np.mean(y):.2f}\n'
             f'$\\sigma$ = {np.std(y):.2f}\n'
             f'$r$ = {np.corrcoef(x, y)[0][1]:.2f}')
    bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=0.5)
    ax.text(0.95, 0.07, stats, fontsize=9, bbox=bbox,
            transform=ax.transAxes, horizontalalignment='right')

plt.show()
```

### Step 5: Interpret the Results

The resulting visualization is a set of four subplots, each showing a different dataset. The x and y limits are the same for all subplots. Each subplot contains the x and y data points as well as a linear regression line. The text box in the lower right corner of each subplot shows some statistics about the data, including the mean, standard deviation, and correlation coefficient.

## Summary

In this tutorial, you learned how to use Matplotlib to create visualizations in Python. You learned how to create a figure with subplots, plot data points, add a linear regression line, and add a text box with statistics about the data. With Matplotlib, you can create a wide variety of visualizations to explore and analyze your data.
