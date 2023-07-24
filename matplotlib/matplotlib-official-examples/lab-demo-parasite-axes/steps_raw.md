# Python Matplotlib Lab

## Introduction

In this lab, you will learn how to create a parasite axes using the `mpl_toolkits.axes_grid1.parasite_axes.HostAxes` and `mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes` modules in Matplotlib. The parasite axes shares the x-scale with a host axes, but shows a different scale in y direction.

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries. In this lab, we will be using `matplotlib.pyplot` for plotting, `mpl_toolkits.axes_grid1.parasite_axes.HostAxes` and `mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes` for creating a parasite axes.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes
```

### Step 2: Create a figure and add host axes

We create a figure using `plt.figure()` method and add a host axes using `fig.add_axes()` method. Host axes shares the x-scale with parasite axes.

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```

### Step 3: Create parasite axes

We create two parasite axes using `host.get_aux_axes()` method. We set `viewlim_mode=None` to ensure that the parasite axes share the same x-scale with the host axes. We also set `sharex=host` to ensure that the x-scale is shared.

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```

### Step 4: Hide right y-axis of host axes

We hide the right y-axis of the host axes using `host.axis["right"].set_visible(False)` method.

```python
host.axis["right"].set_visible(False)
```

### Step 5: Show right y-axis of parasite axes 1

We show the right y-axis of the first parasite axes using `par1.axis["right"].set_visible(True)` method. We also set `par1.axis["right"].major_ticklabels.set_visible(True)` and `par1.axis["right"].label.set_visible(True)` to show the tick labels and label of the right y-axis.

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```

### Step 6: Add right y-axis to parasite axes 2

We add a right y-axis to the second parasite axes using `par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))` method.

```python
par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))
```

### Step 7: Plot data on all axes

We plot data on all axes using `plot()` method. We also set labels and limits for all axes using `set()` method.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")

host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```

### Step 8: Add legend and axis colors

We add a legend to the host axes using `host.legend()` method. We also set the color of the left y-axis label of the host axes, the right y-axis label of the first parasite axes, and the right y-axis label of the second parasite axes to match their respective lines using `host.axis["left"].label.set_color(p1.get_color())`, `par1.axis["right"].label.set_color(p2.get_color())`, and `par2.axis["right2"].label.set_color(p3.get_color())` methods.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```

### Step 9: Display the plot

We display the plot using `plt.show()` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a parasite axes using `mpl_toolkits.axes_grid1.parasite_axes.HostAxes` and `mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes` modules in Matplotlib. We also learned how to plot data on the parasite axes and share the x-scale with the host axes.
