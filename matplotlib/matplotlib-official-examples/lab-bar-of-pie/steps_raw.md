# Python Matplotlib Tutorial: Creating a Bar of Pie Chart

## Introduction

In this tutorial, you will learn how to create a "Bar of Pie" chart using Python's Matplotlib library. A Bar of Pie chart is a combination of a Pie chart and a stacked bar chart, where the first slice of the pie is exploded into a bar chart with a further breakdown of its characteristics. This chart is useful when you want to show the distribution of a whole data set, while also highlighting specific categories.

## Steps

### Step 1: Import necessary libraries

Before we start creating the chart, we need to import the necessary libraries. In this case, we will be using `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the data for the chart

Next, we need to define the data that we will be using to create the chart. In this case, we will be using the following data:

```python
# pie chart parameters
overall_ratios = [.27, .56, .17]
labels = ['Approve', 'Disapprove', 'Undecided']
explode = [0.1, 0, 0]

# bar chart parameters
age_ratios = [.33, .54, .07, .06]
age_labels = ['Under 35', '35-49', '50-65', 'Over 65']
```

### Step 3: Create the pie chart

Now we can create the pie chart. We start by defining the figure and axis objects:

```python
# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)
```

Then we set the parameters for the pie chart and plot it:

```python
# rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode)
```

### Step 4: Create the bar chart

Next, we create the stacked bar chart. We start by defining the parameters for the chart:

```python
# bar chart parameters
bottom = 1
width = .2

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')
```

### Step 5: Connect the pie chart and bar chart

Finally, we connect the pie chart and bar chart using `ConnectionPatch`:

```python
# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
bar_height = sum(age_ratios)

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax2.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)
```

### Step 6: Display the chart

Finally, we display the chart:

```python
plt.show()
```

## Summary

In this tutorial, you learned how to create a "Bar of Pie" chart using Python's Matplotlib library. A Bar of Pie chart is useful when you want to show the distribution of a whole data set, while also highlighting specific categories. You also learned how to use `ConnectionPatch` to connect the pie chart and bar chart.
