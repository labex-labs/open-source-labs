# Python Matplotlib Stacked Bar Chart Lab

## Introduction

In this lab, we will learn how to create a stacked bar chart using the Matplotlib library in Python. We will use penguin data to create a stacked bar chart that shows the number of penguins with above average body mass.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries, including `numpy` and `matplotlib.pyplot`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define Data

We will define the data that we will use to create the stacked bar chart.

```python
species = (
    "Adelie\n $\\mu=$3700.66g",
    "Chinstrap\n $\\mu=$3733.09g",
    "Gentoo\n $\\mu=5076.02g$",
)
weight_counts = {
    "Below": np.array([70, 31, 58]),
    "Above": np.array([82, 37, 66]),
}
width = 0.5
```

### Step 3: Create a Stacked Bar Chart

We will create a stacked bar chart using `matplotlib.pyplot.bar` and loop through each weight category to stack the bars.

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")
```

### Step 4: Display the Chart

We will display the stacked bar chart using `matplotlib.pyplot.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a stacked bar chart using the Matplotlib library in Python. We started by importing the necessary libraries, defined the data that we will use to create the chart, and then created a stacked bar chart using `matplotlib.pyplot.bar`. Finally, we displayed the chart using `matplotlib.pyplot.show()`.
