# Python Matplotlib Tutorial

## Introduction

Matplotlib is a data visualization library in Python that is used to create static, animated, and interactive visualizations in Python. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. In this lab, we will learn how to control view limits and sticky edges in Matplotlib using Python.

## Steps

### Step 1: Plotting with Margins

The `margins()` method in Matplotlib can be used to set margins in the plot instead of using `set_xlim()` and `set_ylim()` methods. In this step, we will learn how to zoom in and out of a plot using `margins()` method instead of `set_xlim()` and `set_ylim()` methods.

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

# create a subplot with margins
ax1 = plt.subplot(212)
ax1.margins(0.05) # default margin is 0.05, value 0 means fit
ax1.plot(t1, f(t1))

# create a subplot with zoomed out margins
ax2 = plt.subplot(221)
ax2.margins(2, 2) # values >0.0 zoom out
ax2.plot(t1, f(t1))
ax2.set_title('Zoomed out')

# create a subplot with zoomed in margins
ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25) # values in (-0.5, 0.0) zooms in to center
ax3.plot(t1, f(t1))
ax3.set_title('Zoomed in')

plt.show()
```

### Step 2: Sticky Edges

Some plotting functions in Matplotlib make the axis limits "sticky" or immune to the `margins()` method. For instance, `imshow()` and `pcolor()` expect the user to want the limits to be tight around the pixels shown in the plot. If this behavior is not desired, you need to set `use_sticky_edges` to `False`. In this step, we will learn how to work around sticky edges in Matplotlib.

```python
# create a grid
y, x = np.mgrid[:5, 1:6]

# define polygon coordinates
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# create subplots
fig, (ax1, ax2) = plt.subplots(ncols=2)

# use sticky edges for ax1 and turn off sticky edges for ax2
ax2.use_sticky_edges = False

# plot on both subplots
for ax, status in zip((ax1, ax2), ('Is', 'Is Not')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # sticky
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # not sticky
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} Sticky')

plt.show()
```

## Summary

In this lab, we learned how to control view limits and sticky edges in Matplotlib using Python. We learned how to zoom in and out of a plot using `margins()` method instead of `set_xlim()` and `set_ylim()` methods. We also learned how to work around sticky edges in Matplotlib using `use_sticky_edges` property.
