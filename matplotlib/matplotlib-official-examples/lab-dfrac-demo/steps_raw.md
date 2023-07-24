# Matplotlib Tutorial: Differences between \dfrac and \frac

## Introduction

Matplotlib is a data visualization library in Python. In this tutorial, we will discuss the differences between \dfrac and \frac TeX macros when using Mathtex in Matplotlib.

## Steps

### Step 1: Import Matplotlib

To use Matplotlib, we first need to import it. We will also import numpy to generate some sample data for visualization.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Sample Data

We will create two arrays of sample data to plot.

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
```

### Step 3: Create a Figure and Axis

We will create a figure and axis object to plot our data on.

```python
fig, ax = plt.subplots()
```

### Step 4: Plot the Data with \frac

We will plot the data with the \frac TeX macro and display the resulting plot.

```python
ax.plot(x, y, label=r'$\frac{sin(x)}{x}$')
ax.legend()
plt.show()
```

### Step 5: Plot the Data with \dfrac

We will plot the data with the \dfrac TeX macro and display the resulting plot.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```

## Summary

In this tutorial, we discussed the differences between \dfrac and \frac TeX macros when using Mathtex in Matplotlib. We demonstrated how to plot data with both macros and display the resulting plots. By default, \frac produces a smaller, in-line style fraction, while \dfrac produces a larger, display style fraction.
