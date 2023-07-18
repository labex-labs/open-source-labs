# Python Matplotlib 3D Bar Chart Lab

## Introduction

In this lab, we will learn how to create a 3D bar chart using Python Matplotlib. We will use fake data to plot the chart with and without shading.

## Steps

### Step 1: Import Libraries and Set Up Figure

In the first step, we will import the necessary libraries and set up the figure and axes for the chart.

```python
import matplotlib.pyplot as plt
import numpy as np

# set up the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
```

### Step 2: Create Fake Data

In the second step, we will create fake data to use for the chart.

```python
# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1
```

### Step 3: Plot the Chart with Shading

In the third step, we will plot the 3D bar chart with shading.

```python
ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Shaded')
```

### Step 4: Plot the Chart without Shading

In the fourth step, we will plot the 3D bar chart without shading.

```python
ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
ax2.set_title('Not Shaded')
```

### Step 5: Display the Chart

In the final step, we will display the chart.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a 3D bar chart using Python Matplotlib. We used fake data to plot the chart with and without shading. We imported the necessary libraries, set up the figure and axes, created fake data, plotted the chart with and without shading, and then displayed the chart.
