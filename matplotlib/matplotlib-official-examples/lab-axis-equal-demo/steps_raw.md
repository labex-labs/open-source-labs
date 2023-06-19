# Equal Axis Aspect Ratio Tutorial

## Introduction

In data visualization, it is important to present information in an accurate and visually appealing way. One way to achieve this is by setting equal axis aspect ratios in plots. This ensures that the x and y axes are scaled equally, resulting in a proportional representation of the data. In this tutorial, we will learn how to set and adjust plots with equal axis aspect ratios using Python's Matplotlib library.

## Steps

### Step 1: Import necessary libraries

We will begin by importing the necessary libraries for this tutorial. We will be using the Matplotlib library to create plots and the NumPy library to generate data.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Plot a circle with unequal axis aspect ratio

We will first plot a circle with unequal axis aspect ratio to demonstrate the importance of setting equal axis aspect ratios.

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

The resulting plot will show a circle that appears elongated due to the unequal axis aspect ratio.

### Step 3: Plot a circle with equal axis aspect ratio

To set the equal axis aspect ratio, we can use the `axis('equal')` function.

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)
```

The resulting plot will show a circle that is proportional and visually appealing.

### Step 4: Adjust plot limits while maintaining equal axis aspect ratio

We can also adjust the plot limits while maintaining the equal axis aspect ratio.

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)
```

The resulting plot will show a circle that is still proportional even after we change the limits.

### Step 5: Auto-adjust data limits for equal axis aspect ratio

We can also use the `set_aspect('equal', 'box')` function to auto-adjust the data limits for equal axis aspect ratio.

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('still a circle, auto-adjusted data limits', fontsize=10)
```

The resulting plot will show a circle that is still proportional and visually appealing.

## Summary

In this tutorial, we learned how to set and adjust plots with equal axis aspect ratios using Python's Matplotlib library. By setting equal axis aspect ratios, we can ensure that our plots are proportional and visually appealing, making it easier to interpret the data.
