# Python Matplotlib Tutorial

## Introduction

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. This tutorial will guide you through the process of creating a plot using the ggplot style sheet in Matplotlib.

## Steps

### Step 1: Import Libraries and Set Style Sheet

First, we need to import the required libraries and set the ggplot style sheet.

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
```

### Step 2: Create a Scatter Plot

We will create a scatter plot with random data points.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Create random data points
x, y = np.random.normal(size=(2, 200))

# Create a scatter plot
plt.plot(x, y, 'o')
plt.show()
```

### Step 3: Create Sinusoidal Lines

We will create sinusoidal lines with colors from the default color cycle.

```python
# Create sinusoidal lines
L = 2*np.pi
x = np.linspace(0, L)
ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    plt.plot(x, np.sin(x + s), '-')
plt.margins(0)
plt.show()
```

### Step 4: Create Bar Graphs

We will create bar graphs with random data points.

```python
# Create bar graphs
x = np.arange(5)
y1, y2 = np.random.randint(1, 25, size=(2, 5))
width = 0.25

plt.bar(x, y1, width)
plt.bar(x + width, y2, width, color=list(plt.rcParams['axes.prop_cycle'])[2]['color'])
plt.xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
plt.show()
```

### Step 5: Create Circles

We will create circles with colors from the default color cycle.

```python
# Create circles
fig, ax = plt.subplots()
for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    xy = np.random.normal(size=2)
    ax.add_patch(plt.Circle(xy, radius=0.3, color=color['color']))
ax.axis('equal')
ax.margins(0)
plt.show()
```

## Summary

In this tutorial, we learned how to create a plot using the ggplot style sheet in Matplotlib. We created a scatter plot, sinusoidal lines, bar graphs, and circles with colors from the default color cycle. Matplotlib is a powerful tool for creating visualizations in Python.
