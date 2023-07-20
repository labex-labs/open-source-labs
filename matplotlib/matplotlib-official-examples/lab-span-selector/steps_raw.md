# Matplotlib Span Selector Lab

## Introduction

This lab will guide you through how to use the Matplotlib Span Selector to select a range on an axis and plot a detailed view of the selected range on another axis.

## Steps

### Step 1: Import Required Libraries

First, we need to import the required libraries - `numpy` and `matplotlib`.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Create Sample Data

We will now create some sample data to plot using `numpy`.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.arange(0.0, 5.0, 0.01)
y = np.sin(2 * np.pi * x) + 0.5 * np.random.randn(len(x))
```

### Step 3: Create Figure and Subplots

We will now create a figure with two subplots using `matplotlib`.

```python
fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))
```

### Step 4: Plot Data on First Subplot

We will plot the sample data on the first subplot.

```python
ax1.plot(x, y)
ax1.set_ylim(-2, 2)
ax1.set_title('Press left mouse button and drag '
              'to select a region in the top graph')
```

### Step 5: Define a Callback Function

We will define a callback function that will be called when a range is selected using the Span Selector.

```python
def onselect(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x) - 1, indmax)

    region_x = x[indmin:indmax]
    region_y = y[indmin:indmax]

    if len(region_x) >= 2:
        line2.set_data(region_x, region_y)
        ax2.set_xlim(region_x[0], region_x[-1])
        ax2.set_ylim(region_y.min(), region_y.max())
        fig.canvas.draw_idle()
```

### Step 6: Create a Span Selector

We will create a Span Selector object using `matplotlib.widgets.SpanSelector`.

```python
span = SpanSelector(
    ax1,
    onselect,
    "horizontal",
    useblit=True,
    props=dict(alpha=0.5, facecolor="tab:blue"),
    interactive=True,
    drag_from_anywhere=True
)
```

### Step 7: Plot Data on Second Subplot

We will plot the detailed view of the selected range on the second subplot.

```python
line2, = ax2.plot([], [])
```

### Step 8: Show Plot

We will now show the plot using `matplotlib.pyplot.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to use the Matplotlib Span Selector to select a range on an axis and plot a detailed view of the selected range on another axis. We also learned how to create a Span Selector object and define a callback function to handle the selected range.
