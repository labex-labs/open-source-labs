# Custom Spines with Axisartist Tutorial

## Introduction

This tutorial will show you how to use the Matplotlib library to create custom spines at specific positions.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries for this tutorial. We will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import axisartist
```

### Step 2: Create Figure and Subplots

We will create a figure with two subplots using the `add_gridspec` method.

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```

### Step 3: Create Subplot 1

In the first subplot, we will create a new axis that passes through y=0 using `axisartist.Axes`. We will also make the other spines invisible.

```python
ax0 = fig.add_subplot(gs[0, 0], axes_class=axisartist.Axes)
ax0.axis["y=0"] = ax0.new_floating_axis(nth_coord=0, value=0, axis_direction="bottom")
ax0.axis["y=0"].toggle(all=True)
ax0.axis["y=0"].label.set_text("y = 0")
ax0.axis["bottom", "top", "right"].set_visible(False)
```

### Step 4: Create Subplot 2

In the second subplot, we will use `axisartist.axislines.AxesZero` to automatically create xzero and yzero axes. We will make the other spines invisible and set the xzero axis visible.

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```

### Step 5: Plot Data

Now that we have created our subplots, we can plot our data using `np.sin(x)`.

```python
x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))
```

### Step 6: Show Plot

Finally, we can display our plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create custom spines at specific positions using the Matplotlib library. We created a figure with two subplots and used `axisartist.Axes` and `axisartist.axislines.AxesZero` to create our spines. We also made the other spines invisible and set the xzero axis visible. Finally, we plotted our data and displayed our plot.
