# Python Matplotlib Tutorial

## Introduction

This tutorial introduces the basic usage of Matplotlib library in Python, which is a popular data visualization tool in Python. Matplotlib is a library that allows users to create visualizations such as line plots, scatter plots, bar plots, and many more.

## Steps

### Step 1: Importing the Required Libraries

First, we will import the necessary libraries. We will be using the `pyplot` module of the `matplotlib` library to create visualizations.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating a Simple Line Plot

We will create a simple line plot with X-axis values ranging from 0 to 5 and corresponding Y-axis values. We will use the `plot` function provided by the `pyplot` module to create the line plot.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a line plot
plt.plot(x, y)

# Adding title and labels to the plot
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```

### Step 3: Creating a Scatter Plot

We will create a scatter plot with X-axis values ranging from 0 to 5 and corresponding Y-axis values. We will use the `scatter` function provided by the `pyplot` module to create the scatter plot.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a scatter plot
plt.scatter(x, y)

# Adding title and labels to the plot
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```

### Step 4: Creating a Bar Plot

We will create a bar plot with X-axis values ranging from 0 to 5 and corresponding Y-axis values. We will use the `bar` function provided by the `pyplot` module to create the bar plot.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a bar plot
plt.bar(x, y)

# Adding title and labels to the plot
plt.title('Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```

### Step 5: Creating a Pie Chart

We will create a pie chart with five slices representing different data points. We will use the `pie` function provided by the `pyplot` module to create the pie chart.

```python
# Creating data for the pie chart
data = [10, 20, 30, 25, 15]

# Creating labels for the pie chart
labels = ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5']

# Creating a pie chart
plt.pie(data, labels=labels)

# Adding title to the plot
plt.title('Pie Chart')

# Displaying the plot
plt.show()
```

## Summary

In this tutorial, we learned how to use Matplotlib library to create basic visualizations such as line plots, scatter plots, bar plots, and pie charts. We used the `pyplot` module of the `matplotlib` library to create these visualizations. Matplotlib is a powerful data visualization tool in Python and can be used to create a wide variety of visualizations.
