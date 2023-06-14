# Color by Y-Value

## Introduction

Matplotlib is a data visualization library in Python. It is a powerful tool for creating a wide range of graphs and charts. One of the features of Matplotlib is the ability to plot lines with different colors based on the y-value. This lab will demonstrate how to use masked arrays to plot a line with different colors by y-value.

## Steps

### Step 1: Import Required Libraries

In this step, we will import the required libraries for this lab.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data

In this step, we will create the data for our plot. We will create an array of values for t, and an array of values for s.

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
```

### Step 3: Create Masked Arrays

In this step, we will create three masked arrays: one for values greater than a certain threshold, one for values less than a certain threshold, and one for values between two thresholds.

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```

### Step 4: Create Plot

In this step, we will create the plot using the masked arrays created in the previous step. We will plot each masked array separately and use different colors for each.

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```

## Summary

In this lab, we have learned how to plot lines with different colors based on the y-value using masked arrays in Matplotlib. This technique can be useful when visualizing data with distinct regions of interest that require different colors for clarity.
