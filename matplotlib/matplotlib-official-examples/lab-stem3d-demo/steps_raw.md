# 3D Stem Plot Lab

## Introduction

This lab demonstrates how to create a 3D stem plot using the Matplotlib library in Python. A stem plot is a way of plotting data points by drawing vertical lines from a baseline to the data point and placing a marker at the tip.

## Steps

### Step 1: Import the necessary libraries

In this step, we will import the Matplotlib and Numpy libraries using the import statement.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the data

In this step, we will define the data that we will use to create the 3D stem plot. We will create a linspace array for the angle, and use sine and cosine functions to calculate the x and y coordinates. We will also define the z coordinate as the angle.

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```

### Step 3: Create the 3D stem plot

In this step, we will create the 3D stem plot using the `stem` function from Matplotlib. We will pass the x, y, and z coordinates as arguments to the `stem` function.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```

### Step 4: Customize the plot

In this step, we will customize the 3D stem plot by changing the baseline using the `bottom` parameter and changing the format using the `linefmt`, `markerfmt`, and `basefmt` parameters.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```

### Step 5: Change the orientation of the plot

In this step, we will change the orientation of the plot using the `orientation` parameter. We will set the orientation to `'x'` so that the stems are projected along the x-direction and the baseline is in the yz-plane.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```

## Summary

In this lab, we learned how to create a 3D stem plot using the Matplotlib library in Python. We started by defining the data, then created the plot using the `stem` function. We also customized the plot by changing the format and orientation.
