# Python Matplotlib Tutorial Lab

## Creating Bar Chart with Color and Legend Entries

### Introduction

In this lab, we will learn how to create bar chart using Python's Matplotlib library. We will focus on how to control the color of the bars and the legend entries. This will help us create a visually appealing chart that is easy to read and understand.

### Steps

#### Import Matplotlib Library

First, we need to import the Matplotlib library. This can be done using the following code:

```python
import matplotlib.pyplot as plt
```

#### Define Data for the Chart

Next, we need to define the data that we want to use to create the chart. In this example, we will be creating a chart that shows the supply of different types of fruits. We will define the fruit names, the supply counts, the bar colors, and the legend labels as follows:

```python
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
```

#### Create the Bar Chart

Now, we can create the bar chart using the data that we defined in Step 2. We will use the `bar()` method of Matplotlib's `pyplot` module to create the chart. We will also pass in the `label` and `color` parameters to control the legend entries and the bar colors, respectively. The following code demonstrates how to create the bar chart:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```

#### Customize the Chart

We can customize the chart further by adding axis labels and a title. We can also change the color of the axis labels and the legend title. The following code demonstrates how to customize the chart:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```

### Summary

In this lab, we learned how to create bar chart using Python's Matplotlib library. We focused on how to control the color of the bars and the legend entries. We also learned how to customize the chart by adding axis labels and a title. By following these steps, we can create visually appealing charts that are easy to read and understand.
