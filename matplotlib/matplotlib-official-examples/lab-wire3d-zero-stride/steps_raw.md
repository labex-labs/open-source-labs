# 3D Wireframe Plotting Lab

## Introduction

This lab is designed to show you how to create a 3D wireframe plot in Python using Matplotlib. A wireframe plot is a visual representation of a three-dimensional surface that displays the structure of the surface using lines. In this lab, we will show how to set the `rstride` and `cstride` parameters to control the density of the lines in the plot.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries. In this case, we will use Matplotlib and the `axes3d` module.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
```

### Step 2: Create a figure and two subplots

We will create a figure with two subplots using `subplots()` method. We will also set the projection to `'3d'` so that our subplots will be three-dimensional.

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```

### Step 3: Get the test data

We will use the `get_test_data()` method from `axes3d` module to get the test data.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```

### Step 4: Create the first subplot

We will create the first subplot with the `rstride` parameter set to `10` and `cstride` parameter set to `0`.

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```

### Step 5: Create the second subplot

We will create the second subplot with the `rstride` parameter set to `0` and `cstride` parameter set to `10`.

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```

### Step 6: Show the plot

We will show the plot using the `show()` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a 3D wireframe plot using Matplotlib. We used the `rstride` and `cstride` parameters to control the density of the lines in the plot. We created a figure with two subplots and used the `plot_wireframe()` method to create the wireframe plot in each subplot. Finally, we showed the plot using the `show()` method.
