# Matplotlib Tutorial: Creating a Line Plot with Dual Axes

## Introduction

In this lab, we will learn how to create a line plot with dual axes using Matplotlib library in Python. We will plot two sets of data with different scales on the same graph. This is useful when we want to compare two related variables that have different units of measurement.

## Steps

### Step 1: Importing Libraries

We will start by importing the necessary libraries. We will need `matplotlib.pyplot` for creating the graph and `mpl_toolkits.axes_grid1` for creating the dual axes.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
```

### Step 2: Creating the Plot

Next, we will create the plot by defining the host axis and the parasite axis. The host axis will be used for the primary data and the parasite axis will be used for the secondary data.

```python
host = host_subplot(111)
par = host.twinx()
```

### Step 3: Setting Labels

We will set the labels for both axes and the title for the plot.

```python
host.set_xlabel("Distance")
host.set_ylabel("Density")
par.set_ylabel("Temperature")
plt.title("Density and Temperature vs Distance")
```

### Step 4: Adding Data

We will add the data to the plot by using the `plot` function. We will assign each line to a variable so that we can reference it later.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")
```

### Step 5: Formatting the Plot

We will format the plot by setting the legend, label colors, and line colors.

```python
host.legend()
host.yaxis.get_label().set_color(p1.get_color())
par.yaxis.get_label().set_color(p2.get_color())
```

### Step 6: Displaying the Plot

Finally, we will display the plot using the `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a line plot with dual axes using Matplotlib library in Python. We used the `host_subplot` and `twinx` functions to create the dual axes and added data using the `plot` function. We formatted the plot by setting the legend, label colors, and line colors. The resulting graph allows us to compare two related variables that have different units of measurement.
