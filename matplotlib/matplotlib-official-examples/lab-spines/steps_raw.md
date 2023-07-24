# Matplotlib Spines Lab

## Introduction

In this lab, you will learn how to customize spines in Matplotlib. Spines are the lines that connect the axis tick marks and demarcate the boundaries of the data area. By default, Matplotlib displays spines on all four sides of the plot. However, you may want to customize these spines to better highlight your data.

## Steps

### Step 1: Import Matplotlib and NumPy

First, we need to import Matplotlib and NumPy libraries to create our plot. We will use NumPy to create sample data for our plot.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Sample Data

Next, we will create sample data for our plot using NumPy. We will generate 100 data points between 0 and 2π and compute their corresponding sine values.

```python
x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)
```

### Step 3: Create Subplots

We will create three subplots to demonstrate different spine customizations. We will use constrained layout to ensure that the labels do not overlap the axes.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```

### Step 4: Customize Spines for All Four Sides

In the first subplot, we will display spines on all four sides of the plot. We can access the spines of each subplot using the container `ax.spines`. We can then customize the spines using various methods.

```python
ax0.plot(x, y)
ax0.set_title('Normal Spines')
```

### Step 5: Customize Spines for Bottom and Left Sides

In the second subplot, we will display spines only on the bottom and left sides of the plot. We can hide the spines on the right and top sides of the plot using the `set_visible` method.

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```

### Step 6: Customize Spines with Bounds Limited to Data Range

In the third subplot, we will display spines with bounds limited to the data range. We can limit the extent of each spine to the data range using the `set_bounds` method.

```python
ax2.plot(x, y)
ax2.set_title('Spines with Bounds Limited to Data Range')

# Only draw spines for the data range, not in the margins
ax2.spines.bottom.set_bounds(x.min(), x.max())
ax2.spines.left.set_bounds(y.min(), y.max())
# Hide the right and top spines
ax2.spines.right.set_visible(False)
ax2.spines.top.set_visible(False)
```

### Step 7: Show the Plot

Finally, we will display the plot using the `show` method.

```python
plt.show()
```

## Summary

In this lab, you learned how to customize spines in Matplotlib. Specifically, you learned how to display spines on specific sides of the plot, hide spines on specific sides of the plot, and limit the extent of each spine to the data range. By customizing spines, you can create plots that better highlight your data and improve their overall readability.
