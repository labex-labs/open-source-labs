# Python Matplotlib Lab: Simple Colorbar

## Introduction

In this lab, we will learn how to add a simple colorbar to a Matplotlib plot. A colorbar is a useful tool for visualizing the range of values represented by colors in a plot. We will use the `imshow` function to create a simple 2D plot and then add a colorbar to it.

## Steps

### Step 1: Import libraries

To get started, we need to import the necessary libraries. We will use the `numpy` and `matplotlib.pyplot` libraries for this lab.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a 2D plot

Next, we will create a simple 2D plot using the `imshow` function.

```python
# Create a 2D array
data = np.random.rand(10, 10)

# Plot the array
plt.imshow(data)
```

### Step 3: Add a colorbar

Now we can add a colorbar to the plot using the `colorbar` function.

```python
# Add a colorbar to the plot
plt.colorbar()
```

### Step 4: Customize the colorbar

We can customize the appearance of the colorbar by using the `cmap` parameter. This parameter specifies the color map used to create the plot.

```python
# Customize the colorbar
plt.colorbar(cmap='viridis')
```

### Step 5: Add a label to the colorbar

We can add a label to the colorbar using the `label` parameter.

```python
# Add a label to the colorbar
plt.colorbar(cmap='viridis', label='Random Data')
```

## Summary

In this lab, we learned how to add a simple colorbar to a Matplotlib plot. We used the `imshow` function to create a 2D plot and then added a colorbar using the `colorbar` function. We also customized the appearance of the colorbar and added a label to it. Colorbars are a useful tool for visualizing the range of values represented by colors in a plot.
