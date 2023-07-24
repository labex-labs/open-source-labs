# Python Matplotlib Horizontal Bar Chart Lab

## Introduction

In this lab, we will learn how to create a horizontal bar chart using the Python Matplotlib library. A horizontal bar chart is a chart that displays data as horizontal bars. It is useful for comparing data across different categories.

## Steps

### Step 1: Import Required Libraries

The first step is to import the required libraries. We will be using `numpy` and `matplotlib` libraries in this lab.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Set the Random Seed

Before creating the bar chart, we need to set the random seed to ensure that we get the same results every time we run the code.

```python
np.random.seed(19680801)
```

### Step 3: Create the Figure and Axes Objects

The next step is to create the figure and axes objects. The figure object is the window or the canvas where the chart is drawn, and the axes object is the actual chart.

```python
fig, ax = plt.subplots()
```

### Step 4: Prepare the Data

The data for the chart is prepared in this step. We will create a list of people's names, their performance, and the error rate.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```

### Step 5: Create the Bar Chart

Finally, we will create the horizontal bar chart using the `barh()` method of the axes object.

```python
ax.barh(y_pos, performance, xerr=error, align='center')
```

### Step 6: Customize the Chart

To make the chart more informative, we can customize it by adding labels, title, and by inverting the y-axis.

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```

### Step 7: Show the Chart

Finally, we will show the chart by calling the `show()` method of the `pyplot` object.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a horizontal bar chart using Python Matplotlib. We saw how to prepare data, create the figure and axes objects, and customize the chart. We also learned about the `barh()` method of the axes object and how to show the chart using the `show()` method of the `pyplot` object.
