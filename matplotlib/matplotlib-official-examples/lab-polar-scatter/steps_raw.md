# Python Matplotlib Tutorial - Scatter Plot on Polar Axis

## Introduction

In this tutorial, we will learn how to create scatter plots on a polar axis using Matplotlib in Python. A polar plot is a graphical representation of data that is displayed in polar coordinates. It is useful when the data is cyclical or circular in nature, such as data measured over time or direction.

## Steps

### Step 1: Import necessary libraries

We need to import the Matplotlib and NumPy libraries to create the scatter plot on a polar axis. We will also set the random seed for reproducibility.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
```

### Step 2: Generate random data

We will generate random data for the scatter plot using NumPy. We will create 150 data points with random radius and angle values, and compute the area and color of each point.

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```

### Step 3: Create a scatter plot on a polar axis

We will create a scatter plot on a polar axis using the `plt.scatter()` function. We will set the `projection` parameter to `'polar'`, and pass in the radius, angle, color, and area values as parameters.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```

### Step 4: Create a scatter plot on a polar axis with offset origin

We can create a scatter plot on a polar axis with an offset origin by setting the `set_rorigin()` and `set_theta_zero_location()` methods of the `PolarAxes` object. We will set the origin radius to `-2.5` and the theta zero location to `'W'` with an offset of `10`.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```

### Step 5: Create a scatter plot on a polar axis confined to a sector

We can create a scatter plot on a polar axis confined to a sector by setting the `set_thetamin()` and `set_thetamax()` methods of the `PolarAxes` object. We will set the theta start and end limits to `45` and `135`, respectively.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```

## Summary

In this tutorial, we learned how to create scatter plots on a polar axis using Matplotlib in Python. We generated random data, created scatter plots on a polar axis, created scatter plots on a polar axis with an offset origin, and created scatter plots on a polar axis confined to a sector. Polar plots are useful for displaying cyclical or circular data, such as data measured over time or direction.
