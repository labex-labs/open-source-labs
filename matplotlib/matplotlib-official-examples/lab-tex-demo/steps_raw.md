# Python Matplotlib Tutorial Lab

## Introduction

In this lab, you will learn how to use Matplotlib library to create various plots. Matplotlib is a Python library used for visualizing data. It is built on top of the NumPy and SciPy libraries and allows you to create a wide range of visualizations such as line charts, scatter plots, and bar charts.

## Steps

### Step 1: Import Matplotlib and Numpy libraries

Before we can start creating plots, we need to import the Matplotlib and Numpy libraries. We can do this by running the following code:

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a Simple Line Plot

In this step, we will create a simple line plot using Matplotlib. We will start by generating some data to plot using the NumPy `linspace()` function and the `cos()` function. Then, we will use the `plot()` function to create the plot.

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```

### Step 3: Customize the Plot

In this step, we will customize the plot by adding labels to the x and y axes, and a title to the plot.

```python
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('Velocity (degrees/sec)')
plt.title('Cosine Wave')
plt.show()
```

### Step 4: Create a Scatter Plot

In this step, we will create a scatter plot using Matplotlib. We will start by generating some random data to plot using the NumPy `random()` function. Then, we will use the `scatter()` function to create the plot.

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```

### Step 5: Create a Bar Chart

In this step, we will create a bar chart using Matplotlib. We will start by generating some data to plot using the NumPy `random()` function. Then, we will use the `bar()` function to create the plot.

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```

## Summary

In this lab, you learned the basics of using Matplotlib to create various types of plots such as line plots, scatter plots, and bar charts. You also learned how to customize the plots by adding labels to the x and y axes, and titles to the plot. With these skills, you can now create your own plots to visualize your data.
