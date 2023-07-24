# Python Matplotlib Tutorial

## Introduction

In this lab, we will learn how to create a polar bar chart using Python Matplotlib library. We will create a chart that displays the distribution of values across different angles.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries. In this lab, we will use Numpy and Matplotlib.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Set random seed

We will set a random seed so that the results will be reproducible.

```python
np.random.seed(19680801)
```

### Step 3: Define data

We will define the data for the chart. We will generate 20 random values for radii and angles.

```python
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
colors = plt.cm.viridis(radii / 10.)
```

### Step 4: Create a polar bar chart

We will create a polar bar chart using the `projection='polar'` parameter.

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```

### Step 5: Display the chart

We will display the chart using the `plt.show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a polar bar chart using Python Matplotlib library. We used Numpy and Matplotlib libraries to generate random data and create a polar bar chart. We also learned how to display the chart using the `plt.show()` function.
