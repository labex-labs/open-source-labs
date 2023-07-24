# Multiple Y-Axis Plotting with Matplotlib

## Introduction

In data visualization, it is often necessary to plot multiple variables with different units of measurement on the same graph. One common method to achieve this is by using multiple y-axes, where each y-axis corresponds to a different variable. In this lab, we will learn how to create a graph with multiple y-axes using Matplotlib.

## Steps

### Step 1: Import the necessary libraries

We start by importing the required libraries, Matplotlib and NumPy. Matplotlib is a data visualization library, and NumPy is a library for numerical computing in Python.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a figure and axes object

We create a figure and axes object, which represents a single plot in Matplotlib.

```python
fig, ax = plt.subplots()
```

### Step 3: Add a twin y-axis

We add a twin y-axis to the plot using the `twinx` method. This will create a new y-axis on the right side of the plot.

```python
twin1 = ax.twinx()
```

### Step 4: Set the position of the twin y-axis

We set the position of the twin y-axis using the `set_position` method. This will move the twin y-axis to the right of the original y-axis.

```python
twin1.spines.right.set_position(("axes", 1.2))
```

### Step 5: Add data to the plot

We add data to the plot using the `plot` method. We add three lines to the plot, each with a different y-axis.

```python
p1, = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
p2, = twin1.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")
p3, = twin2.plot([0, 1, 2], [50, 30, 15], "C2", label="Velocity")
```

### Step 6: Set the limits and labels for the axes

We set the limits and labels for each y-axis using the `set` method. We also set the color of the labels to match the color of the lines using the `set_color` method.

```python
ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
twin1.set(ylim=(0, 4), ylabel="Temperature")
twin2.set(ylim=(1, 65), ylabel="Velocity")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())
```

### Step 7: Set the tick colors

We set the tick colors for each y-axis to match the color of the labels.

```python
ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())
```

### Step 8: Add a legend to the plot

We add a legend to the plot using the `legend` method. We pass a list of line objects as the `handles` parameter.

```python
ax.legend(handles=[p1, p2, p3])
```

### Step 9: Display the plot

We display the plot using the `show` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a graph with multiple y-axes using Matplotlib. We created a figure and axes object, added a twin y-axis, set the position of the twin y-axis, added data to the plot, set the limits and labels for the axes, set the tick colors, added a legend to the plot, and displayed the plot. This technique can be useful when comparing variables with different units of measurement on the same graph.
