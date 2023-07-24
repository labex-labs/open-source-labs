# Python Matplotlib Tutorial: Creating a Multiple Dataset Plot with Parasite Axis

## Introduction

In this lab, we will learn how to create a multiple dataset plot using parasite axis in Python Matplotlib. We will use the `mpl_toolkits.axes_grid1.parasite_axes.host_subplot` and `mpl_toolkits.axisartist.axislines.Axes` to create a plot with multiple y-axes.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries. We will use `matplotlib.pyplot` for plotting and `mpl_toolkits` for creating parasite axis.

```python
import matplotlib.pyplot as plt
from mpl_toolkits import axisartist
from mpl_toolkits.axes_grid1 import host_subplot
```

### Step 2: Create Host and Parasite Axes

We will create a host axis and two parasite axes using the `host_subplot()` and `twinx()` functions. The `host_subplot()` function creates a host axis, and the `twinx()` function creates parasite axes that share the same x-axis with the host axis.

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```

### Step 3: Adjust Parasite Axis

We need to adjust the position of the parasite axes. The `new_fixed_axis()` function is used to create a new y-axis on the right side of the plot. The `toggle()` function is used to turn on all the ticks and labels of the right y-axis.

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```

### Step 4: Plot the Data

We will plot three datasets on the same plot: Density, Temperature, and Velocity. We will use the `plot()` function to plot the data.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
```

### Step 5: Set Axis Limits and Labels

We will set the x-axis and y-axis limits and labels for each axis using the `set()` function.

```python
host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```

### Step 6: Add Legend and Color

We will add a legend to the plot and color the labels of each axis to match the color of the corresponding dataset using the `legend()` and `label.set_color()` functions.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```

### Step 7: Display the Plot

Finally, we will display the plot using the `show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a multiple dataset plot using parasite axis in Python Matplotlib. We used the `mpl_toolkits.axes_grid1.parasite_axes.host_subplot` and `mpl_toolkits.axisartist.axislines.Axes` to create a plot with multiple y-axes. We also learned how to adjust the position of the parasite axes, plot the data, set the axis limits and labels, add legend and color to the plot, and display the plot.
