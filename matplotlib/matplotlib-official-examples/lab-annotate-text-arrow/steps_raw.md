# Python Matplotlib Tutorial

## Introduction

This tutorial will guide you through creating an annotated scatter plot with a text arrow using Matplotlib in Python.

## Steps

### Step 1: Import libraries and generate random data

First, we need to import the necessary libraries and generate some random data for our scatter plot.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_aspect(1)

x1 = -1 + np.random.randn(100)
y1 = -1 + np.random.randn(100)
x2 = 1. + np.random.randn(100)
y2 = 1. + np.random.randn(100)

ax.scatter(x1, y1, color="r")
ax.scatter(x2, y2, color="g")
```

### Step 2: Add text annotations to the plot

Next, we'll add text annotations to the plot using the `ax.text()` function. We'll create two annotations, one for "Sample A" and one for "Sample B".

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```

### Step 3: Add a text arrow to indicate direction

To indicate the direction of the data, we'll add a text arrow using the `ax.text()` function and the `bbox` parameter with the `boxstyle` set to "rarrow".

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```

### Step 4: Set plot limits and show the plot

Finally, we'll set the x and y limits of the plot and show the plot using the `ax.set_xlim()`, `ax.set_ylim()`, and `plt.show()` functions.

```python
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

plt.show()
```

## Summary

In this tutorial, we learned how to create an annotated scatter plot with a text arrow using Matplotlib in Python. We used the `ax.text()` function to add annotations and a text arrow to the plot, and the `ax.set_xlim()`, `ax.set_ylim()`, and `plt.show()` functions to set plot limits and show the plot.
