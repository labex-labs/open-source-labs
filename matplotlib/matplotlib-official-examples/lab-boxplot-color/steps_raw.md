# Python Matplotlib Tutorial: Creating Custom Fill Colors for Box Plots

## Introduction

This tutorial will guide you through the process of creating custom fill colors for box plots using Python Matplotlib. Box plots are a type of graph used to display the distribution of a set of data. They show the median, quartiles, and outliers of the data set. In this tutorial, we will use the `boxplot()` function in Matplotlib to create two types of box plots (rectangular and notched) and fill them with custom colors.

## Steps

### Step 1: Importing Required Libraries

We will start by importing the required libraries. In this example, we will be using `numpy` and `matplotlib.pyplot` libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating Random Test Data

Next, we will create random test data using the `numpy` library. We will generate 3 sets of data, each with a different standard deviation.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```

### Step 3: Creating Rectangular Box Plot

We will now create a rectangular box plot using the `boxplot()` function in Matplotlib. We will set the `patch_artist` parameter to `True` to fill the box with color.

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax1.set_title('Rectangular Box Plot')
```

### Step 4: Creating Notched Box Plot

We will now create a notched box plot with the `boxplot()` function. We will set the `notch` parameter to `True` to create a notched box plot.

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax2.set_title('Notched Box Plot')
```

### Step 5: Filling the Box Plots with Custom Colors

Next, we will fill the box plots with custom colors. We will create a list of colors and use a loop to fill each box with a different color.

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```

### Step 6: Adding Horizontal Grid Lines

Finally, we will add horizontal grid lines to the box plots using the `yaxis.grid()` function.

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Three Separate Samples')
    ax.set_ylabel('Observed Values')

plt.show()
```

## Summary

In this tutorial, we learned how to create custom fill colors for box plots using Python Matplotlib. We started by importing the required libraries, creating random test data, and then creating rectangular and notched box plots. We then filled the box plots with custom colors and added horizontal grid lines. Box plots are a useful visualization tool for displaying the distribution of data and custom fill colors can be used to make them more visually appealing.
