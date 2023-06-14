# Hatch Style Reference Lab

## Introduction

This lab will guide you through the process of adding hatches to most polygons in Matplotlib, including Axes.bar, Axes.fill_between, Axes.contourf, and children of patches.Polygon. You will learn how to create different hatching patterns, repeat them to increase density, and combine them to create additional patterns.

## Steps

### Step 1: Import the necessary libraries

To use Matplotlib, we must import the library and the necessary modules. We will use the pyplot module to create the subplots and the patches module to create the Rectangle object.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
```

### Step 2: Create the hatches_plot function

The hatches_plot function will create a rectangle with the specified hatching pattern and add it to the axis. It will also add a text with the hatching pattern.

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```

### Step 3: Create the subplots

We will create three sets of subplots with different hatching patterns.

```python
fig, axs = plt.subplots(2, 5, layout='constrained', figsize=(6.4, 3.2))
```

### Step 4: Create the first set of hatching patterns

We will create the first set of hatching patterns using the following list:

```python
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
```

We will then use a loop to create a rectangle with each hatching pattern and add it to a subplot.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```

### Step 5: Create the second set of hatching patterns

We will create the second set of hatching patterns by repeating each pattern twice to increase the density. We will use the following list:

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

We will use the same loop as before to create the rectangles.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```

### Step 6: Create the third set of hatching patterns

We will create the third set of hatching patterns by combining two patterns to create a new one. We will use the following list:

```python
hatches = ['/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-']
```

We will use the same loop as before to create the rectangles.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```

### Step 7: Display the plots

We will display the plots using the show() function.

```python
plt.show()
```

## Summary

In this lab, you learned how to add hatches to most polygons in Matplotlib, including Axes.bar, Axes.fill_between, Axes.contourf, and children of patches.Polygon. You learned how to create different hatching patterns, repeat them to increase density, and combine them to create additional patterns. You also learned how to use the add_patch() function to add a Rectangle object to an axis and how to use the text() function to add text to the plot.
