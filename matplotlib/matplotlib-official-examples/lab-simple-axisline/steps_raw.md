# Simple Matplotlib Axisline Lab

## Introduction

In this lab, we will learn how to create a simple axis line using Matplotlib. We will use the mpl_toolkits.axisartist.axislines library to create an axis line with x and y axis labels, and a y2 axis label on the right side. We will also learn how to hide the top and right axes, and make the x axis line visible at y=0.

## Steps

### Step 1: Import Libraries

We start by importing the necessary libraries. We will be using Matplotlib and the mpl_toolkits.axisartist.axislines library.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import AxesZero
```

### Step 2: Create Figure and Subplot

Next, we create a figure and add a subplot with AxesZero. This creates an axis line with x and y axis labels, but no tick marks or grids.

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```

### Step 3: Hide Top and Right Axes

We will now hide the top and right axes, since we only need the left and bottom axes.

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```

### Step 4: Make X Axis Line Visible at Y=0

We will now make the x axis line visible at y=0. This is done by setting the xzero axis to visible.

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```

### Step 5: Set Axis Limits and Labels

We will now set the y axis limits to (-2, 4) and set the x and y axis labels.

```python
ax.set_ylim(-2, 4)
ax.set_xlabel("Label X")
ax.set_ylabel("Label Y")
```

### Step 6: Create Y2 Axis

Finally, we will create a new y2 axis on the right side of the plot with an offset of (20, 0) and label it.

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```

### Summary

We have learned how to create a simple axis line using Matplotlib. We first imported the necessary libraries, then created a figure and subplot with AxesZero. We then hid the top and right axes, made the x axis line visible at y=0, set the axis limits and labels, and finally created a new y2 axis on the right side of the plot.
