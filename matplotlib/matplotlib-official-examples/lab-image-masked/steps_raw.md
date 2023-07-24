# Python Matplotlib Tutorial

## Introduction

In this lab, we will learn how to use Matplotlib to create visualizations in Python. Matplotlib is a powerful library for data visualization and is commonly used to create plots, charts, and graphs. We will explore the different types of plots available in Matplotlib and learn how to customize them to create professional-looking visualizations.

## Steps

### Step 1: Importing Libraries

The first step is to import the necessary libraries. We will be using NumPy and Matplotlib for this tutorial. NumPy is a library for numerical computing and Matplotlib is a library for data visualization.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Creating Data

Next, we will create some data to use in our plots. For this tutorial, we will create a simple line plot.

```python
# Create the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
```

### Step 3: Customizing the Plot

Now that we have created a basic plot, let's customize it to make it more visually appealing. We can add a title, axis labels, and change the color and style of the line.

```python
# Add title and axis labels
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Change color and style of line
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```

### Step 4: Creating a Scatter Plot

In addition to line plots, Matplotlib also allows us to create scatter plots. Scatter plots are useful for visualizing the relationship between two variables.

```python
# Create the data
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.scatter(x, y)

# Add title and axis labels
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
```

### Step 5: Creating a Bar Chart

Another common type of plot is a bar chart. Bar charts are useful for comparing the values of different categories.

```python
# Create the data
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

# Create the bar chart
plt.bar(x, y)

# Add title and axis labels
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
```

## Summary

In this lab, we learned how to use Matplotlib to create different types of plots including line plots, scatter plots, and bar charts. We also learned how to customize our plots by adding titles, axis labels, and changing the color and style of the lines. Matplotlib is a powerful library for data visualization and is an essential tool for anyone working with data in Python.
