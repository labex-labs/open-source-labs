# Matplotlib Tutorial - Customizing Plot Axes

## Introduction

In this tutorial, we will learn how to customize the background, labels, and ticks of a simple plot using Matplotlib.

## Steps

### Step 1: Importing necessary libraries

We will start by importing the necessary libraries that we will use in this tutorial.

```python
import matplotlib.pyplot as plt
```

### Step 2: Creating a figure and setting the background

We will create a figure using the `plt.figure()` method, which creates a `matplotlib.figure.Figure` instance. We will set the background color of the figure using the `rect.set_facecolor()` method.

```python
fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor('lightgoldenrodyellow')
```

### Step 3: Adding axes to the figure

We will add axes to the figure using the `fig.add_axes()` method. We will also set the background color of the axes using the `rect.set_facecolor()` method.

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```

### Step 4: Customizing the ticks and labels

We will customize the ticks and labels of the axes using the `ax1.tick_params()` method. We will set the color, rotation, and size of the x-axis label, and the color, size, and width of the y-axis ticks.

```python
ax1.tick_params(axis='x', labelcolor='tab:red', labelrotation=45, labelsize=16)
ax1.tick_params(axis='y', color='tab:green', size=25, width=3)
```

### Step 5: Displaying the plot

Finally, we will display the plot using the `plt.show()` method.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to customize the background, labels, and ticks of a simple plot using Matplotlib. We used the `plt.figure()`, `fig.add_axes()`, `ax1.tick_params()`, and `plt.show()` methods to create and display the plot.
