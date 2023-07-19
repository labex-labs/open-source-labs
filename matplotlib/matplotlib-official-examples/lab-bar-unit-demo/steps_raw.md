# Step-by-Step Lab: Creating a Group Barchart with Units Using Matplotlib

## Introduction

In this lab, you will learn how to create a group barchart with units using Matplotlib. The barchart will display the cup height by group and beverage choice. The tutorial will walk you through the steps of creating the chart using Python code.

## Steps

### Step 1: Import the Necessary Libraries

The first step is to import the necessary libraries. We will be using NumPy and Matplotlib to create the barchart. The `cm` and `inch` units are defined in the `basic_units.py` file, which is used to convert the units.

```python
import matplotlib.pyplot as plt
import numpy as np
from basic_units import cm, inch
```

### Step 2: Define the Data

The next step is to define the data that we will use to create the barchart. We will create two sets of data - one for tea and one for coffee. Each set will have five values, one for each group. The height of the cups will be represented in centimeters.

```python
N = 5
tea_means = [15*cm, 10*cm, 8*cm, 12*cm, 5*cm]
tea_std = [2*cm, 1*cm, 1*cm, 4*cm, 2*cm]
coffee_means = (14*cm, 19*cm, 7*cm, 5*cm, 10*cm)
coffee_std = (3*cm, 5*cm, 2*cm, 1*cm, 2*cm)
```

### Step 3: Create the Figure and Axes Objects

The next step is to create the figure and axes objects. We will use the `subplots()` function to create the figure and axes objects.

```python
fig, ax = plt.subplots()
ax.yaxis.set_units(inch)
```

### Step 4: Define the Bar Chart Parameters

The next step is to define the parameters for the bar chart. We will define the x locations for the groups, the width of the bars, and the labels for the x-ticks.

```python
ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```

### Step 5: Create the Bar Chart

The next step is to create the bar chart. We will use the `bar()` function to create the chart. We will create two sets of bars, one for tea and one for coffee. We will also add error bars to the chart.

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```

### Step 6: Add Labels and Title to the Chart

The final step is to add labels and a title to the chart. We will add a title to the chart, a label for the x-axis, and a legend for the chart.

```python
ax.set_title('Cup height by group and beverage choice')
ax.set_xlabel('Group')
ax.legend()
ax.autoscale_view()
```

## Summary

In this lab, you learned how to create a group barchart with units using Matplotlib. You learned how to import the necessary libraries, define the data, create the figure and axes objects, define the bar chart parameters, create the bar chart, and add labels and a title to the chart. With this knowledge, you can create your own barcharts using Matplotlib.
