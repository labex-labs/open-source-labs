# Step-by-Step Lab: Creating a Pie Chart with Matplotlib

## Introduction

In this lab, you will learn how to create a pie chart using the Matplotlib library in Python. A pie chart is a circular chart that is divided into slices to represent numerical proportions.

## Steps

### Step 1: Import Matplotlib

Before creating the pie chart, we need to import the Matplotlib library.

```python
import matplotlib.pyplot as plt
```

### Step 2: Define the Data

Next, we need to define the data that will be used to create the pie chart. The data should be in the form of a list of values and a list of labels.

```python
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
```

### Step 3: Create the Pie Chart

To create the pie chart, we will use the `pie()` function from Matplotlib.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
```

### Step 4: Add Labels to the Slices

We can add labels to the slices by passing a list of labels to the `labels` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```

### Step 5: Customize the Colors

We can customize the colors of the slices by passing a list of colors to the `colors` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown'])
```

### Step 6: Customize the Hatch Patterns

We can customize the hatch patterns of the slices by passing a list of hatch patterns to the `hatch` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```

### Step 7: Explode the Slices

We can explode one or more slices of the pie chart by passing a list of values to the `explode` parameter of the `pie()` function.

```python
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```

### Step 8: Control the Size

We can control the size of the pie chart by setting the `radius` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size': 'smaller'}, radius=0.5)
```

### Step 9: Modify the Shadow

We can modify the shadow of the pie chart by passing a dictionary of arguments to the `shadow` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle=90)
```

## Summary

In this lab, you learned how to create a pie chart using the Matplotlib library in Python. You learned how to define the data, create the chart, add labels, customize the colors and hatch patterns, explode the slices, control the size, and modify the shadow. With these skills, you can create informative and visually appealing pie charts to represent your data.
