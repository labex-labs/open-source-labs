# Matplotlib Tutorial: Creating Artists with Units

## Introduction

In this lab, you will learn how to create artists with units in Matplotlib. You will create different types of artists, such as a line, text, and patch, and add them to a plot. You will also set the units for the x and y axes, and learn how to convert units to scalars.

## Steps

### Step 1: Import Libraries

First, you need to import the necessary libraries. You will use `matplotlib.pyplot` for creating the plot, `numpy` for generating random data, and `matplotlib.collections`, `matplotlib.lines`, `matplotlib.patches`, and `matplotlib.text` for creating different types of artists.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.collections as collections
import matplotlib.lines as lines
import matplotlib.patches as patches
import matplotlib.text as text
```

### Step 2: Create the Figure and Axis

Next, you need to create the figure and axis objects. The figure object is the top-level container for all the plot elements, while the axis object represents the x and y axes of the plot.

```python
fig, ax = plt.subplots()
```

### Step 3: Set Units for the Axes

To use units for the x and y axes, you need to set the units for each axis using the `set_units` method. In this example, you will use centimeters as the unit.

```python
ax.xaxis.set_units('cm')
ax.yaxis.set_units('cm')
```

### Step 4: Generate Random Data

To create the line artist, you need to generate some random data. You will use `numpy.random` to generate 2 sets of x and y coordinates for the line.

```python
x = np.array([0, 1.5])
y = np.array([0, 2.5])
```

### Step 5: Create a Line Artist

Now, you can create the line artist using the `Line2D` class from `matplotlib.lines`. You can specify the x and y coordinates, line width, color, and axis object as arguments.

```python
line = lines.Line2D(x, y, lw=2, color='black', axes=ax)
```

### Step 6: Add the Artist to the Plot

To add the line artist to the plot, you need to call the `add_line` method of the axis object and pass the line artist as an argument.

```python
ax.add_line(line)
```

### Step 7: Create a Text Artist

Next, you will create a text artist using the `Text` class from `matplotlib.text`. You can specify the x and y coordinates, text label, horizontal and vertical alignment, and axis object as arguments.

```python
t = text.Text(3, 2.5, 'text label', ha='left', va='bottom', axes=ax)
```

### Step 8: Add the Artist to the Plot

To add the text artist to the plot, you need to call the `add_artist` method of the axis object and pass the text artist as an argument.

```python
ax.add_artist(t)
```

### Step 9: Set the Limits of the Plot

To set the limits of the plot, you need to call the `set_xlim` and `set_ylim` methods of the axis object and pass the minimum and maximum values for each axis.

```python
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 10)
```

### Step 10: Display the Plot

Finally, you can display the plot using the `show` method of `pyplot`.

```python
plt.show()
```

## Summary

In this lab, you learned how to create artists with units in Matplotlib. You learned how to set the units for the x and y axes, generate random data, create line and text artists, and add them to a plot. You also learned how to set the limits of the plot and display it.
