# Python Matplotlib Tutorial: Plotting Sparsity Patterns

## Introduction

In this tutorial, we will learn how to plot sparsity patterns of arrays using Matplotlib. The sparsity pattern refers to the distribution of non-zero elements in an array. We will use the `spy` function in Matplotlib to plot the sparsity patterns.

## Steps

### Step 1: Importing Required Libraries

We will start by importing the required libraries which are NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating Random Array

Next, we will create a random array with dimensions (20, 20) using the `numpy.random.randn` function. We will also set a few elements to zero to create a sparse matrix.

```python
np.random.seed(19680801)
x = np.random.randn(20, 20)
x[5, :] = 0.
x[:, 12] = 0.
```

### Step 3: Creating Subplots

We will now create a 2x2 grid of subplots using the `subplots` function. This will give us four plots to visualize the sparsity pattern of the array.

```python
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
```

### Step 4: Plotting Sparsity Pattern

We will use the `spy` function to plot the sparsity pattern of the array. We will use different parameters such as `markersize` and `precision` to customize the plot.

```python
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)
```

### Step 5: Displaying the Plots

Finally, we will display the plots using the `show` function.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to plot sparsity patterns of arrays using Matplotlib. We used the `spy` function to visualize the sparsity pattern and customized the plot using different parameters. We also learned how to create subplots and display the plots using the `show` function.
