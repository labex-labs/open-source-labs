# Matplotlib Multicursor Tutorial

## Introduction

This tutorial will show how to use the `matplotlib.widgets.MultiCursor` function to display a cursor on multiple plots simultaneously.

## Steps

### Step 1: Importing Libraries

The first step is to import the necessary libraries which are `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating Data

Next, we will create some data for our plots. In this example, we will create three sine waves with different frequencies.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)
```

### Step 3: Creating Plots

Now, we will create three subplots using the `plt.subplots` function. Two plots will be created in one figure, while the third plot will be created in a separate figure.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```

### Step 4: Adding MultiCursor

Finally, we will add the `MultiCursor` function to display a cursor on all three plots when hovering over a data point.

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```

## Summary

In this tutorial, we learned how to use the `matplotlib.widgets.MultiCursor` function to display a cursor on multiple plots simultaneously. We created three sine waves with different frequencies, created three subplots, and added the `MultiCursor` function to display a cursor on all three plots.
