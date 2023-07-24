# Python Matplotlib Tutorial

## Introduction

This tutorial demonstrates how to use Python's Matplotlib library to create a simple line plot with a shaded region representing the area under the curve. The plot includes a text label, axis labels, and custom tick placement and labels.

## Steps

### Step 1: Define the function

First, define the function that will be plotted. In this example, the function is (x - 3) _ (x - 5) _ (x - 7) + 85.

```python
def func(x):
    return (x - 3) * (x - 5) * (x - 7) + 85
```

### Step 2: Define the integral limits

Next, define the limits of the integral. In this example, the limits are a = 2 and b = 9.

```python
a, b = 2, 9
```

### Step 3: Create the x and y values

Generate a range of x values using the `numpy` `linspace` function. Then, use the function defined in step 1 to generate the corresponding y values.

```python
import numpy as np

x = np.linspace(0, 10)
y = func(x)
```

### Step 4: Create the plot

Create a figure and axis object using `subplots`. Plot the x and y values using `plot`. Set the y-axis limits to start at 0 using `set_ylim`.

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```

### Step 5: Create the shaded region

Create the shaded region using a `Polygon` patch. Generate x and y values for the region using `linspace` and the function defined in step 1. Then, define the vertices of the region as a list of tuples. Finally, create the `Polygon` object and add it to the axis using `add_patch`.

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```

### Step 6: Add the integral label

Add the integral label to the plot using `text`. The label should be centered at the midpoint between a and b and should be formatted using mathtext.

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```

### Step 7: Add axis labels and tick labels

Add the x and y-axis labels using `figtext`. Hide the top and right spines using `spines`. Set custom tick placement and labels using `set_xticks` and `set_yticks`.

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```

### Step 8: Show the plot

Use `show` to display the plot.

```python
plt.show()
```

## Summary

This tutorial demonstrated how to use Python's Matplotlib library to create a simple line plot with a shaded region representing the area under the curve. The plot included a text label, axis labels, and custom tick placement and labels. By following the steps outlined in this tutorial, you can create similar plots for your own data.
