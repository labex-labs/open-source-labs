# Python Matplotlib Tutorial

## Introduction

This tutorial will guide you through the step-by-step process of creating a bar graph using Python's Matplotlib library. The example in this tutorial shows how to use the default units of centimeters and inches, how to set the x and y units using various keywords, and how to set the x-limits using scalars or units.

## Steps

### Step 1: Import Required Libraries

In this step, we need to import the required libraries that we will use to create the bar graph. We will be using Matplotlib and numpy libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data for the Bar Graph

In this step, we need to create data for the bar graph. We will use the numpy library to create an array of values that we will use for the bar graph.

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```

### Step 3: Create the Bar Graph with Default Units

In this step, we will create the bar graph with default units using Matplotlib's `bar` method. We will use the `bottom` parameter to set the bottom of the bars to 0.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```

### Step 4: Set the x and y Units for the Bar Graph

In this step, we will set the x and y units for the bar graph using various keywords. We will use the `xunits` and `yunits` parameters to set the x and y units to centimeters and inches.

```python
axs[0, 1].bar(cms, cms, bottom=bottom, width=width, xunits=cm, yunits=inch)
```

### Step 5: Set the x-limits Using Scalars or Units

In this step, we will set the x-limits using scalars or units. We will use the `set_xlim` method to set the x-limits. We will set the x-limits to 2 and 6 using scalars in the current units for the bar graph in the second row and first column. We will set the x-limits to 2 cm and 6 cm using units for the bar graph in the second row and second column.

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```

### Step 6: Display the Bar Graph

In this step, we will display the bar graph using Matplotlib's `show` method.

```python
fig.tight_layout()
plt.show()
```

## Summary

In this tutorial, we have learned how to create a bar graph using Matplotlib library in Python. We have learned how to use the default units of centimeters and inches, how to set the x and y units using various keywords, and how to set the x-limits using scalars or units.
