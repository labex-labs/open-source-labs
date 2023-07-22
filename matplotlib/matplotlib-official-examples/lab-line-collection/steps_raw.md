# Python Matplotlib LineCollection Tutorial

## Introduction

In this tutorial, we will learn how to use the `LineCollection` function in Matplotlib to efficiently draw multiple lines at once. We will see how to plot multiple lines with different colors and styles, and how to use a masked array to mask some values. We will also learn how to use the `ScalarMappable.set_array` function to map an array of values to colors.

## Steps

### Step 1: Import Libraries

Before we start, we need to import the necessary libraries. We will use `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data

Next, we need to create the data that we will use to plot the lines. We will use `numpy` to create a 2D array of `x` and `y` values.

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```

### Step 3: Create Line Collection

Now, we can create a `LineCollection` object with the `LineCollection` function. We can set the `linewidths`, `colors`, and `linestyle` parameters to customize the appearance of the lines.

```python
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

segs = np.zeros((50, 100, 2))
segs[:, :, 1] = ys
segs[:, :, 0] = x

segs = np.ma.masked_where((segs > 50) & (segs < 60), segs)

line_segments = LineCollection(segs, linewidths=(0.5, 1, 1.5, 2),
                               colors=colors, linestyle='solid')
```

### Step 4: Create Plot

We can now create a plot using `matplotlib` and add the `LineCollection` object to the plot using the `add_collection` method of the `Axes` object.

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```

### Step 5: Map Colors to Values

We can also map an array of values to colors using the `ScalarMappable.set_array` function. We will create a new set of data and a new `LineCollection` object with the `array` parameter set to the `x` values. We can then use the `colorbar` method of the `Figure` object to add a colorbar to the plot.

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)
plt.show()
```

## Summary

In this tutorial, we learned how to use the `LineCollection` function in Matplotlib to efficiently draw multiple lines at once. We saw how to plot multiple lines with different colors and styles, and how to use a masked array to mask some values. We also learned how to use the `ScalarMappable.set_array` function to map an array of values to colors.
