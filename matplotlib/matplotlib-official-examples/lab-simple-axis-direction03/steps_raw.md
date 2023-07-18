# Simple Axis Tick Label and Tick Directions Lab

## Introduction

This lab will guide you on how to create simple axis tick labels and tick directions using Matplotlib. The code will help you move the tick labels and ticks to inside the spines.

## Steps

### Step 1: Import Libraries

Import the necessary libraries to create the plot.

```python
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
```

### Step 2: Setup Axes Function

Create a function to set up the axes. This function will set the x and y tick values.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```

### Step 3: Create the Figure and Subplots

Create the figure and two subplots using the `setup_axes()` function.

```python
fig = plt.figure(figsize=(5, 2))
fig.subplots_adjust(wspace=0.4, bottom=0.3)

ax1 = setup_axes(fig, 121)
ax1.set_xlabel("ax1 X-label")
ax1.set_ylabel("ax1 Y-label")

ax2 = setup_axes(fig, 122)
ax2.set_xlabel("ax2 X-label")
ax2.set_ylabel("ax2 Y-label")
```

### Step 4: Move Tick Labels Inside the Spines

Move the tick labels to inside the spines for the first subplot using the `invert_ticklabel_direction()` method.

```python
ax1.axis[:].invert_ticklabel_direction()
```

### Step 5: Move Ticks Inside the Spines

Move the ticks to inside the spines for the second subplot using the `major_ticks.set_tick_out()` method.

```python
ax2.axis[:].major_ticks.set_tick_out(False)
```

### Step 6: Display the Plot

Display the plot using the `show()` method.

```python
plt.show()
```

## Summary

This lab has demonstrated how to create simple axis tick labels and tick directions using Matplotlib. By following the step-by-step instructions, you can easily move the tick labels and ticks to inside the spines of the plot.
