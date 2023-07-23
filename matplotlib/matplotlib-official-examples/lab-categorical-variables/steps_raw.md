# Python Matplotlib Tutorial

## Introduction

Matplotlib is a popular data visualization library in Python. It provides a variety of customizable plots and graphs for data exploration and presentation. In this lab, we will learn how to plot categorical variables using Matplotlib.

## Steps

### Step 1: Import Matplotlib

The first step is to import the Matplotlib library. We will also use the `numpy` library to generate some sample data.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Prepare Data

Next, we will prepare some sample data to plot. We will create a dictionary with the counts of different fruits, and then extract the keys and values into separate lists.

```python
data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())
```

### Step 3: Bar Plot

A bar plot is a good way to display categorical data. We can create a bar plot using the `bar` function.

```python
plt.bar(names, values)
plt.title('Fruit Counts')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```

### Step 4: Scatter Plot

We can also create a scatter plot to show the relationship between two categorical variables. In this case, we will use the same fruit data and add some random noise to the counts to create a second variable.

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```

### Step 5: Line Plot

A line plot can be used to show how a categorical variable changes over time. In this example, we will use data about the happiness levels of cats and dogs during different activities.

```python
cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]
plt.plot(activity, dog, label="dog")
plt.plot(activity, cat, label="cat")
plt.title('Happiness Levels')
plt.xlabel('Activity')
plt.ylabel('Happiness')
plt.legend()
plt.show()
```

## Summary

In this lab, we learned how to plot categorical variables using Matplotlib. We created bar plots, scatter plots, and line plots to visualize different types of categorical data. By customizing the axes labels, titles, and legends, we can create informative and visually appealing plots to communicate our data effectively.
