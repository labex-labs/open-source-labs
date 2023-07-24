# Python Matplotlib Tutorial

## Introduction

Matplotlib is a popular data visualization library in Python. It provides an easy-to-use interface for creating a wide range of visualizations, from simple line plots to complex heatmaps. In this lab, we will go through the basics of Matplotlib and create a simple line plot using the "fivethirtyeight" style sheet.

## Steps

### Step 1: Import Matplotlib and NumPy Libraries

The first step is to import the Matplotlib and NumPy libraries. NumPy is a fundamental package for scientific computing in Python that provides powerful arrays and linear algebra functions.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Set the Style to "fivethirtyeight"

The "fivethirtyeight" style sheet replicates the styles from the popular data-driven news website FiveThirtyEight.com. We will use this style sheet for our visualization.

```python
plt.style.use('fivethirtyeight')
```

### Step 3: Create Data for the Line Plot

In this step, we will create data for our line plot. We will use NumPy's `linspace` function to create an array of evenly spaced values between 0 and 10. We will also generate some random noise using NumPy's `random.randn` function.

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```

### Step 4: Create a Figure and Axes Objects

Next, we will create a figure and axes object using Matplotlib's `subplots` function. The figure object represents the entire figure and the axes object represents a single plot within the figure.

```python
fig, ax = plt.subplots()
```

### Step 5: Plot the Data

In this step, we will plot the data on the axes object using Matplotlib's `plot` function. We will plot six different lines with different slopes and random noise.

```python
ax.plot(x, np.sin(x) + x + noise)
ax.plot(x, np.sin(x) + 0.5 * x + noise)
ax.plot(x, np.sin(x) + 2 * x + noise)
ax.plot(x, np.sin(x) - 0.5 * x + noise)
ax.plot(x, np.sin(x) - 2 * x + noise)
ax.plot(x, np.sin(x) + noise)
```

### Step 6: Set the Title and Labels

In this step, we will set the title and labels for the plot using the axes object's `set_title`, `set_xlabel`, and `set_ylabel` methods.

```python
ax.set_title("'fivethirtyeight' style sheet")
ax.set_xlabel("x")
ax.set_ylabel("y")
```

### Step 7: Show the Plot

Finally, we will display the plot using Matplotlib's `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a simple line plot using the "fivethirtyeight" style sheet in Matplotlib. We covered the basics of creating a figure and axes object, plotting data, and setting the title and labels for the plot. With these skills, you can create a wide range of visualizations using Matplotlib.
