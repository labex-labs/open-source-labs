# Matplotlib Fixed Size Axes Lab

## Introduction

In data visualization, it's important to have consistent axes sizes in order to make meaningful comparisons between different plots. The Matplotlib library provides a way to create fixed size axes for figures that do not change size. In this lab, we will learn how to create fixed size axes using Matplotlib.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Divider, Size
```

### Step 2: Create a Figure

Next, we will create a figure with a fixed size using the `plt.figure()` function.

```python
fig = plt.figure(figsize=(6, 6))
```

### Step 3: Define the Sizes of the Axes

We will define the size of the axes using the `Size` class. In this example, we will create an axes with a fixed physical size of 4.5 inches by 5 inches.

```python
h = [Size.Fixed(1.0), Size.Fixed(4.5)]
v = [Size.Fixed(0.7), Size.Fixed(5.)]
```

### Step 4: Create a Divider

We will create a `Divider` object that will divide the figure into the specified sizes.

```python
divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
```

### Step 5: Add Axes to the Figure

We will add the axes to the figure using the `add_axes()` function and passing in the position of the `Divider` object.

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```

### Step 6: Plot Data

We will plot some data on the axes using the `plot()` function.

```python
ax.plot([1, 2, 3])
```

### Step 7: Show the Plot

Finally, we will show the plot using the `plt.show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create fixed size axes using Matplotlib. By defining the sizes of the axes and creating a `Divider` object, we were able to create consistent axes sizes for our plot.
