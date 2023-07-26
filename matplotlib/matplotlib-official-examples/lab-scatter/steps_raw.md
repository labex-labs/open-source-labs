# Matplotlib Scatter Plot Lab

## Introduction

In this lab, we will learn how to create a simple scatter plot using Python's Matplotlib library. A scatter plot is a type of plot that displays values for two variables as a collection of points. Each point represents the values of the two variables, and the position of the point represents the values of the two variables. Scatter plots are useful for identifying relationships between variables and for identifying outliers.

## Steps

### Step 1: Import the necessary libraries

In this step, we will import the necessary libraries for creating a scatter plot. We will be using the Matplotlib library for creating the plot and the NumPy library for generating random data.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate random data

In this step, we will generate random data for our scatter plot. We will be generating 50 data points for each variable using the NumPy library.

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```

### Step 3: Define the size and color of the points

In this step, we will define the size and color of the points in our scatter plot. We will be using the NumPy library to generate random values for the size and color of the points.

```python
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2
```

### Step 4: Create the scatter plot

In this step, we will create the scatter plot using the Matplotlib library. We will use the `scatter` function to create the plot and specify the size and color of the points.

```python
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
```

### Summary

In this lab, we learned how to create a simple scatter plot using Python's Matplotlib library. We generated random data for the plot using the NumPy library, defined the size and color of the points, and created the plot using the `scatter` function from the Matplotlib library. Scatter plots are useful for identifying relationships between variables and for identifying outliers.
