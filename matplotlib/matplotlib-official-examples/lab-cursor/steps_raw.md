# Matplotlib Cursor Tutorial

## Introduction

The `matplotlib.widgets.Cursor` is a useful tool for exploring the data plotted on a Matplotlib graph. It allows you to interactively display the x and y values of the data point under the cursor.

## Steps

### Step 1: Import Required Libraries

In this step, we import the required libraries: `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data

In this step, we generate random data points using numpy.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data points
x, y = 4*(np.random.rand(2, 100) - .5)
```

### Step 3: Create a Figure and Axes

In this step, we create a figure and axes object using `plt.subplots`.

```python
fig, ax = plt.subplots(figsize=(8, 6))
```

### Step 4: Plot Data Points

In this step, we plot the generated data points on the axes object.

```python
ax.plot(x, y, 'o')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
```

### Step 5: Create a Cursor

In this step, we create a cursor object using `Cursor` class and pass the axes object as an argument. We also specify the cursor color and line width.

```python
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
```

### Step 6: Display the Plot

In this step, we display the plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to use the `matplotlib.widgets.Cursor` to interactively display the x and y values of the data point under the cursor. We generated random data points using numpy, created a figure and axes object, plotted the data points, created a cursor object and displayed the plot using `plt.show()`.
