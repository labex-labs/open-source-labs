# Scatter Masked Tutorial

## Introduction

This tutorial will guide you through creating a scatter plot with masked data points using the Python Matplotlib library. We will also add a line to demarcate the masked regions.

## Steps

### Step 1: Importing the Required Libraries and Setting Random Seed

We start by importing the necessary libraries and setting the random seed to ensure reproducibility.

```python
import matplotlib.pyplot as plt
import numpy as np

# Setting random seed for reproducibility
np.random.seed(19680801)
```

### Step 2: Generating Data for the Scatter Plot

Next, we generate data for the scatter plot. We create 100 data points with random x and y values between 0 and 0.9, and random radii between 0 and 10. The color of each data point is determined by the square root of its area.

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
```

### Step 3: Masking Data Points and Creating Scatter Plot

We mask the data points based on their distance from the origin. Data points with a distance less than `r0` are masked in `area1`, and those with a distance greater than or equal to `r0` are masked in `area2`. We then create a scatter plot of the masked data points with `marker='^'` and `marker='o'` for `area1` and `area2`, respectively.

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```

### Step 4: Adding a Line to Demarcate Masked Regions

Finally, we add a line to demarcate the masked regions. We create an array of theta values and plot a circle with radius `r0` using `np.cos(theta)` and `np.sin(theta)`.

```python
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```

### Step 5: Displaying the Scatter Plot

We display the scatter plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create a scatter plot with masked data points using the Python Matplotlib library. We also added a line to demarcate the masked regions. We started by importing the necessary libraries and setting the random seed. Next, we generated data for the scatter plot and masked the data points based on their distance from the origin. We then created a scatter plot of the masked data points and added a line to demarcate the masked regions. Finally, we displayed the scatter plot.
