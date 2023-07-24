# Centered Spines with Arrows Tutorial

## Introduction

Matplotlib is a powerful data visualization tool in Python. In this tutorial, you will learn how to create a plot with centered spines and arrows using Matplotlib.

## Steps

### Step 1: Import necessary libraries

Before creating the plot, you need to import the necessary libraries. In this case, you need Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a figure and axis object

Next, you need to create a figure and axis object using the `subplots()` function. This function returns a tuple of `(figure, axis)`, which you can use to modify the plot.

```python
fig, ax = plt.subplots()
```

### Step 3: Move the spines

By default, the spines are drawn at the edges of the plot. In this case, you want to move the left and bottom spines to the center of the plot.

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```

### Step 4: Hide unnecessary spines

You also want to hide the top and right spines since they are not needed.

```python
ax.spines[["top", "right"]].set_visible(False)
```

### Step 5: Draw arrows at the end of the spines

To indicate the direction of the axes, you can draw arrows at the end of the spines.

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```

### Step 6: Add data to the plot

Finally, you can add some data to the plot to visualize it. In this case, you can use the `plot()` function to plot a sine wave.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```

### Summary

In this tutorial, you learned how to create a plot with centered spines and arrows using Matplotlib. You learned how to move the spines to the center of the plot, hide unnecessary spines, and draw arrows at the end of the spines. You also learned how to add data to the plot and visualize it.
