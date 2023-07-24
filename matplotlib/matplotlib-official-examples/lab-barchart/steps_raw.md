# Grouped Bar Chart with Labels using Python Matplotlib

## Introduction

In this lab, we will learn how to create a grouped bar chart and how to annotate bars with labels using Python Matplotlib. We will use data from the Palmer Penguins dataset to create a chart that displays penguin attributes by species.

## Steps

### Step 1: Import Required Libraries

We will begin by importing the necessary libraries to work with our data and create the chart.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Prepare Data

Next, we will prepare the data for our chart. We have three species of penguins and three attributes, so we will create a dictionary with the means for each attribute by species.

```python
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
```

### Step 3: Create a Grouped Bar Chart

Now, we can create our chart using the `bar` function from Matplotlib. We will create a loop that iterates through our attributes and creates a set of bars for each one. We will also adjust the width of the bars and the position of each set of bars.

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```

### Step 4: Add Labels to the Bars

We can add labels to the bars using the `bar_label` function from Matplotlib. This will add the value of each bar above it.

```python
ax.bar_label(rects, padding=3)
```

### Step 5: Customize the Chart

We can customize the chart by adding labels, a title, and adjusting the x-axis tick labels and legend. We will also set the y-axis limit to ensure that all of our data is visible.

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```

### Step 6: Show the Chart

Finally, we can show the chart using the `show` function from Matplotlib.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a grouped bar chart and how to annotate bars with labels using Python Matplotlib. We used data from the Palmer Penguins dataset to create a chart that displays penguin attributes by species. We also learned how to customize the chart by adding labels, a title, and adjusting the x-axis tick labels and legend.
