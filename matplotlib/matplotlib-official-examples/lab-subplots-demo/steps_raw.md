# Creating Subplots with Matplotlib

## Introduction

Matplotlib is a popular data visualization library in Python. It provides a variety of functions to create different types of plots. One of its key features is the ability to create subplots. This allows users to create multiple plots in the same figure, making it easier to compare different data sets or views of the same data. In this lab, we will walk through the process of creating subplots using Matplotlib.

## Steps

### Step 1: Creating a Figure with a Single Subplot

The simplest way to create a single subplot is by using the `subplots()` function without any arguments. This function returns a `Figure` object and a single `Axes` object.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

```

### Step 2: Stacking Subplots in One Direction

To create multiple subplots stacked vertically or horizontally, we can pass the number of rows and columns as arguments to the `subplots()` function. The returned `axs` object is a 1D numpy array containing the list of created `Axes`.

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```

### Step 3: Stacking Subplots in Two Directions

To create a grid of subplots, we can pass the number of rows and columns as arguments to the `subplots()` function. The returned `axs` object is a 2D NumPy array.

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```

### Step 4: Sharing Axes

By default, each `Axes` is scaled individually. To align the horizontal or vertical axis of subplots, we can use the `sharex` or `sharey` parameters.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```

### Step 5: Polar Axes

We can create a grid of polar `Axes` by passing the `projection='polar'` parameter to the `subplots()` function.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```

## Summary

In this lab, we learned how to create subplots using Matplotlib. We covered creating a figure with a single subplot, stacking subplots in one direction, stacking subplots in two directions, sharing axes, and creating polar axes. By using these techniques, we can create complex visualizations that allow us to compare and analyze multiple data sets at once.
