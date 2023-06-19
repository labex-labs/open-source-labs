# Nested Pie Charts with Matplotlib

## Introduction

Pie charts are popular data visualization tools used to represent data in a circular form. However, there are times when you might want to create a nested version of the pie chart, known as the donut chart. This tutorial will guide you through creating nested pie charts using Matplotlib, a popular data visualization library in Python.

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries. In this case, we need `Matplotlib` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a nested pie chart using `ax.pie`

We can create a nested pie chart using `ax.pie` method. We will first generate some fake data, corresponding to three groups. In the inner circle, we'll treat each number as belonging to its own group. In the outer circle, we'll plot them as members of their original 3 groups.

```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```

### Step 3: Create a nested pie chart using `ax.bar`

We can also create a nested pie chart using `ax.bar` method on axes with a polar coordinate system. This may give more flexibility on the exact design of the plot.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
# Normalize vals to 2 pi
valsnorm = vals/np.sum(vals)*2*np.pi
# Obtain the ordinates of the bar edges
valsleft = np.cumsum(np.append(0, valsnorm.flatten()[:-1])).reshape(vals.shape)

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.bar(x=valsleft[:, 0],
       width=valsnorm.sum(axis=1), bottom=1-size, height=size,
       color=outer_colors, edgecolor='w', linewidth=1, align="edge")

ax.bar(x=valsleft.flatten(),
       width=valsnorm.flatten(), bottom=1-2*size, height=size,
       color=inner_colors, edgecolor='w', linewidth=1, align="edge")

ax.set(title="Pie plot with `ax.bar` and polar coordinates")
ax.set_axis_off()
plt.show()
```

### Step 4: Customize the Nested Pie Chart

We can customize the nested pie chart by changing the colors, adding labels, and adjusting the size.

```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

# Add labels
labels = ['Group 1', 'Group 2', 'Group 3']
ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'), labels=labels, labeldistance=0.7)

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

# Set the title
ax.set(aspect="equal", title='Nested Pie Chart')

plt.show()
```

### Step 5: Save the Nested Pie Chart

We can save the nested pie chart as an image in png, pdf, or svg format.

```python
fig.savefig('nested_pie_chart.png', dpi=300, bbox_inches='tight')
```

## Summary

In this tutorial, we have learned how to create nested pie charts in Matplotlib using two methods: `ax.pie` and `ax.bar`. We have also learned how to customize the nested pie chart by adding labels, changing colors, and adjusting the size. Finally, we have seen how to save the nested pie chart as an image in png, pdf, or svg format.
