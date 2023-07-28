# Matplotlib Tutorial

## Introduction

This tutorial will walk you through the process of creating an arrow style reference chart using Matplotlib in Python. The chart will display the different arrow styles available in `~.Axes.annotate`.

## Steps

### Step 1: Import Necessary Libraries

Import the necessary libraries to create the arrow style reference chart.

```python
import inspect
import itertools
import re

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches
```

### Step 2: Get Arrow Styles

Use `mpatches.ArrowStyle.get_styles()` to get all the arrow styles available in `~.Axes.annotate`.

```python
styles = mpatches.ArrowStyle.get_styles()
```

### Step 3: Set Up Figure

Set up the figure using `plt.figure()` and `add_gridspec()`. The figure will have a grid of 2 columns and n rows, where n is the number of arrow styles. Each cell in the grid will contain an arrow style and its default parameters.

```python
ncol = 2
nrow = (len(styles) + 1) // ncol
axs = (plt.figure(figsize=(4 * ncol, 1 + nrow))
       .add_gridspec(1 + nrow, ncol,
                     wspace=.7, left=.1, right=.9, bottom=0, top=1).subplots())
for ax in axs.flat:
    ax.set_axis_off()
for ax in axs[0, :]:
    ax.text(0, .5, "arrowstyle",
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="center", verticalalignment="center")
    ax.text(.35, .5, "default parameters",
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")
```

### Step 4: Plot Arrow Styles

Plot each arrow style in a cell of the grid, along with its default parameters. Use `ax.annotate()` to add the arrow style name and its default parameters to the cell.

```python
for ax, (stylename, stylecls) in zip(axs[1:, :].T.flat, styles.items()):
    l, = ax.plot(.25, .5, "ok", transform=ax.transAxes)
    ax.annotate(stylename, (.25, .5), (-0.1, .5),
                xycoords="axes fraction", textcoords="axes fraction",
                size="large", color="tab:blue",
                horizontalalignment="center", verticalalignment="center",
                arrowprops=dict(
                    arrowstyle=stylename, connectionstyle="arc3,rad=-0.05",
                    color="k", shrinkA=5, shrinkB=5, patchB=l,
                ),
                bbox=dict(boxstyle="square", fc="w"))
    # wrap at every nth comma (n = 1 or 2, depending on text length)
    s = str(inspect.signature(stylecls))[1:-1]
    n = 2 if s.count(',') > 3 else 1
    ax.text(.35, .5,
            re.sub(', ', lambda m, c=itertools.count(1): m.group()
                   if next(c) % n else '\n', s),
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")
```

### Step 5: Display Chart

Display the arrow style reference chart using `plt.show()`.

```python
plt.show()
```

## Summary

In this tutorial, you learned how to create an arrow style reference chart using Matplotlib in Python. You used `mpatches.ArrowStyle.get_styles()` to get all the arrow styles available in `~.Axes.annotate`, set up a figure using `plt.figure()` and `add_gridspec()`, plotted each arrow style in a cell of the grid, and displayed the chart using `plt.show()`.
