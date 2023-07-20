# Logarithmic Bar Chart Lab

## Introduction

In this lab, we will learn how to create a logarithmic bar chart using Python Matplotlib library. A logarithmic bar chart is useful when the values of the dataset are very different in size, and we want to visualize them in a more balanced way.

## Steps

### Step 1: Importing Libraries

First, we need to import the necessary libraries. In this case, we will be using the `matplotlib.pyplot` and `numpy` libraries. The `pyplot` library will allow us to create our bar chart, and the `numpy` library will help us to manipulate the data.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Defining the Data

Next, we need to define the data that we want to use for our bar chart. In this example, we will be using a tuple of tuples, where each inner tuple contains two values. The first value represents the x-axis value, and the second value represents the y-axis value.

```python
data = ((3, 1000), (10, 3), (100, 30), (500, 800), (50, 1))
```

### Step 3: Creating the Bar Chart

Now we are ready to create our bar chart. We will start by defining some variables that will help us to set the width of the bars and their position on the x-axis.

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

Next, we will create a figure and an axis object using the `subplots()` method. Then, we will use a for loop to iterate through each value in our dataset and create a bar for each one.

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

We set the `bottom` parameter to `0.001` to avoid having any bars with a height of 0, which is not compatible with a logarithmic scale.

### Step 4: Customizing the Chart

We can customize the appearance of our chart by adding labels to the x-axis and y-axis, and by setting the scale of the y-axis to logarithmic.

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```

### Step 5: Displaying the Chart

Finally, we can display our chart using the `show()` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a logarithmic bar chart using Python Matplotlib library. We started by importing the necessary libraries, defining the data, creating the bar chart, customizing it, and displaying it. A logarithmic bar chart is a useful way to visualize data that has a wide range of values, and it can help us to see the differences between them more clearly.
