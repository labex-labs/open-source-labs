# Matplotlib Simple Axisline3 Tutorial

## Introduction

In this tutorial, we will learn how to create a simple axis line using Matplotlib in Python.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Axes
```

### Step 2: Create Figure and Axes

Next, we will create a figure and axes object. We will use the `add_subplot` method to add the axes object.

```python
fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(axes_class=Axes)
```

### Step 3: Customize the Axes

We will now customize the axes by hiding the right and top axes lines.

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```

### Step 4: Display the Plot

Finally, we can display the plot using the `show` method.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create a simple axis line using Matplotlib in Python. We imported the necessary libraries, created a figure and axes object, customized the axes, and displayed the plot.
