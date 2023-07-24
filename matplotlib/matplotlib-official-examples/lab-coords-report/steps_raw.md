# Python Matplotlib Tutorial

## Introduction

This step-by-step lab will guide you through using Python's Matplotlib library to create visualizations. Matplotlib is a data visualization library that allows users to create a wide range of visualizations, including line plots, scatter plots, and histograms. In this lab, we will create a simple scatter plot using Matplotlib.

## Steps

### Step 1: Import libraries

Before we start creating our visualization, we need to import the necessary libraries. In this example, we will be using numpy and matplotlib.pyplot.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create data

Next, we will create some random data to use in our visualization. In this example, we will create two arrays of random data using numpy.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.rand(20)
y = 1e7 * np.random.rand(20)
```

### Step 3: Create the plot

Now that we have our data, we can create our plot using Matplotlib. In this example, we will create a scatter plot using the plot() function.

```python
fig, ax = plt.subplots()
plt.plot(x, y, 'o')
```

### Step 4: Format the plot

To make our plot more readable, we can format it using Matplotlib's formatting functions. In this example, we will format the y-axis labels to display values in millions.

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```

### Step 5: Display the plot

Finally, we can display our plot using Matplotlib's show() function.

```python
plt.show()
```

## Summary

In this lab, we learned how to use Matplotlib to create a scatter plot. We also learned how to format the plot and display it. Matplotlib is a powerful library that can be used to create a wide range of visualizations.
