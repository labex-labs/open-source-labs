# Polar Plot with Legend - Step-by-Step Lab

## Introduction

In this lab, you will learn how to create a polar plot with a legend using Python Matplotlib. Polar plots are used to plot data in polar coordinates, which is useful when working with directional data. Legends are used to explain the meaning of the different lines or markers on a plot.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries. In this example, we will be using `numpy` and `matplotlib`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a Figure and Subplot

Next, we need to create a figure and subplot for our plot. We will be using the `projection` parameter of `add_subplot` to create a polar plot.

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```

### Step 3: Create Data

We need to create some data to plot on our polar plot. In this example, we will create two lines.

```python
r = np.linspace(0, 3, 301)
theta = 2 * np.pi * r
```

### Step 4: Plot Data

Now we can plot our data using the `plot` function. We will create two lines using the data we created in step 3.

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```

### Step 5: Customize Plot

We can customize our plot by changing the grid color and adding a legend. In this example, we will move the legend slightly away from the center of the plot to avoid overlap.

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2, .5 + np.sin(angle)/2))
```

### Step 6: Display Plot

Finally, we can display our plot using the `show` function.

```python
plt.show()
```

## Summary

In this lab, you learned how to create a polar plot with a legend using Python Matplotlib. You also learned how to customize the plot by changing the grid color and moving the legend. Polar plots are useful when working with directional data and legends are useful for explaining the meaning of the different lines or markers on a plot.
