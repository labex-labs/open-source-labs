# Python Matplotlib Boxplot Tutorial

## Introduction

Boxplots are a type of graph used to display the distribution of data based on five-number summary ("minimum", first quartile (Q1), median, third quartile (Q3), and "maximum"). They are commonly used in data analysis to identify and visualize outliers, as well as to compare the distribution of different groups of data. In this lab, you will learn how to create and customize boxplots in Python using the Matplotlib library.

## Steps

### Step 1: Import the necessary libraries

Before we start creating boxplots, we need to import the necessary libraries, including NumPy and Matplotlib:

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate the data

Next, we will generate some sample data to use in our boxplots. For this tutorial, we will use the following data:

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```

### Step 3: Create a basic boxplot

We can create a basic boxplot using the `boxplot()` function from Matplotlib. The `boxplot()` function takes in the data as the first argument and other optional parameters to customize the plot. Here is the code to create a basic boxplot:

```python
plt.boxplot(data)
plt.show()
```

### Step 4: Customize the boxplot

We can customize the boxplot by changing the appearance of the box, whiskers, and outliers. We can also create multiple boxplots on the same plot to compare different groups of data. Here are some examples of how to customize the boxplot:

```python
# Create a notched boxplot
plt.boxplot(data, notch=True)
plt.show()

# Change the outlier point symbols to green diamonds
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# Create horizontal boxplots
plt.boxplot(data, vert=False)
plt.show()

# Create multiple boxplots on one plot
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```

### Step 5: Add labels and titles

Finally, we can add labels and titles to our boxplot to make it more informative. We can add labels to the x and y axes, as well as a title to the plot. We can also change the font size and style of the labels and title. Here is an example of how to add labels and titles:

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Comparison of Three Groups')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
```

## Summary

In this lab, you learned how to create and customize boxplots in Python using the Matplotlib library. You learned how to generate sample data, create a basic boxplot, customize the appearance of the boxplot, and add labels and titles to the plot. Boxplots are a powerful tool for visualizing and comparing the distribution of data, and knowing how to create and customize them is an important skill for data analysts and scientists.
