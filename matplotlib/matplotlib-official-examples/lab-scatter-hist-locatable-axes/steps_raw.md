# Scatter Histogram Matplotlib Tutorial

## Introduction

In data visualization, scatter plots are used to show the relationship between two variables. Additionally, histograms are useful for showing the distribution of a single variable. In this tutorial, you will learn how to create a scatter plot with histograms using Python's Matplotlib library.

## Steps

### Step 1: Import Required Libraries

In this step, we will import the necessary libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
```

### Step 2: Create Random Data

In this step, we will create random data to use for the scatter plot.

```python
np.random.seed(19680801)
x = np.random.randn(1000)
y = np.random.randn(1000)
```

### Step 3: Create Scatter Plot

In this step, we will create a scatter plot using the random data from Step 2.

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```

### Step 4: Create Histograms

In this step, we will create histograms for the x and y variables using `make_axes_locatable` from `mpl_toolkits.axes_grid1`.

```python
divider = make_axes_locatable(ax)
ax_histx = divider.append_axes("top", 1.2, pad=0.1, sharex=ax)
ax_histy = divider.append_axes("right", 1.2, pad=0.1, sharey=ax)

ax_histx.xaxis.set_tick_params(labelbottom=False)
ax_histy.yaxis.set_tick_params(labelleft=False)

binwidth = 0.25
xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
lim = (int(xymax/binwidth) + 1)*binwidth
bins = np.arange(-lim, lim + binwidth, binwidth)

ax_histx.hist(x, bins=bins)
ax_histy.hist(y, bins=bins, orientation='horizontal')

ax_histx.set_yticks([0, 50, 100])
ax_histy.set_xticks([0, 50, 100])
```

### Step 5: Display Plot

In this step, we will display the scatter plot with histograms.

```python
plt.show()
```

## Summary

In this tutorial, you learned how to create a scatter plot with histograms using Python's Matplotlib library. You first imported the necessary libraries, then created random data for the scatter plot. Next, you created the scatter plot and histograms using `make_axes_locatable`. Finally, you displayed the plot.
