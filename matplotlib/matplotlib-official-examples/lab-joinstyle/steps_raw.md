# Python Matplotlib Lab

## Introduction

This lab provides a step-by-step guide on how to use the `JoinStyle` module of Matplotlib in Python. `JoinStyle` controls how Matplotlib draws the corners where two different line segments meet. This lab is designed for users who are new to Matplotlib.

## Steps

### Step 1: Importing Required Libraries

In order to use the `JoinStyle` module, we need to import it from the `matplotlib._enums` library. We also need to import the `pyplot` module from `matplotlib` to create a graph.

```python
import matplotlib.pyplot as plt
from matplotlib._enums import JoinStyle
```

### Step 2: Creating a Graph

To create a graph, we first need to define the data that we want to plot. In this example, we will use the `numpy` library to generate some sample data.

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

Next, we create a new figure and axis using `plt.subplots()`. We will set the x and y limits of the graph and then plot the data using `plot()`.

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```

### Step 3: Setting JoinStyle

We can set the `JoinStyle` of the line using the `set_solid_joinstyle()` method of the `Line2D` object. We will create a new line object and set its join style to `JoinStyle.bevel`.

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```

### Step 4: Displaying the Graph

Finally, we display the graph using `plt.show()`.

```python
plt.show()
```

## Summary

This lab provided a step-by-step guide on how to use the `JoinStyle` module of Matplotlib in Python. We learned how to import required libraries, create a graph, set the `JoinStyle`, and display the graph. By adjusting the join style, we can change the appearance of corners where two different line segments meet in a graph.
