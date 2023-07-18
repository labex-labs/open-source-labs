# Python Matplotlib Tutorial - Axis Line Styles

## Introduction

In this lab, we will learn how to configure axis style in Matplotlib. We will be using the `mpl_toolkits.axisartist` axes classes to add arrows at the ends of each axis and to add X and Y-axis from the origin. We will also hide the borders of the plot.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import AxesZero
```

### Step 2: Create Figure and Subplot

Next, we will create a figure and a subplot.

```python
fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)
```

### Step 3: Configure Axis Style

We will now configure the axis style by adding arrows at the ends of each axis and adding X and Y-axis from the origin.

```python
for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")
    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

# hides borders
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```

### Step 4: Plot the Graph

We will now plot the graph using `np.linspace` and `np.sin`.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```

### Step 5: Display the Graph

Finally, we will display the graph using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to configure axis style in Matplotlib. We used the `mpl_toolkits.axisartist` axes classes to add arrows at the ends of each axis and to add X and Y-axis from the origin. We also hid the borders of the plot.
