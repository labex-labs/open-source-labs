# Python Matplotlib Tutorial: Simple Axis Direction

## Introduction

In this step-by-step lab, we will be learning how to create a simple axis direction in Python Matplotlib. Matplotlib is a data visualization library in Python that allows you to create static, animated, and interactive visualizations in Python programming. We will be using the library to create a simple axis direction diagram using the following steps.

## Steps

### Step 1: Import Libraries

First, we import the necessary libraries. In this case, we will be importing `matplotlib.pyplot` and `mpl_toolkits.axisartist`.

```python
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
```

### Step 2: Create the Figure and Axes

Next, we create the figure and axes objects using the `plt.subplots()` function. We specify the figure size using the `figsize` parameter.

```python
fig = plt.figure(figsize=(4, 2.5))
ax1 = fig.add_subplot(axes_class=axisartist.Axes)
```

### Step 3: Adjust the Subplot

We adjust the subplot using the `fig.subplots_adjust()` function to make room for the labels on the right side of the plot.

```python
fig.subplots_adjust(right=0.8)
```

### Step 4: Set the Axis Labels

We set the axis labels for the left and right sides of the plot using the `ax1.axis[]` function. We also set the direction of the tick labels using the `set_axis_direction()` function.

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Left label")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Right label")
ax1.axis["right"].label.set_axis_direction("left")
```

### Step 5: Show the Plot

Finally, we show the plot using the `plt.show()` function.

```python
plt.show()
```

## Summary

In this lab, we have learned how to create a simple axis direction diagram using Python Matplotlib. We started by importing the necessary libraries, creating the figure and axes objects, adjusting the subplot, setting the axis labels, and finally showing the plot.
