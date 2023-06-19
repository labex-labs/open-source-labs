# Python Matplotlib Tutorial: Creating Plots with Different Scales

## Introduction

In this lab, you will learn how to create plots with different scales in Python using Matplotlib. Specifically, you will learn how to create two plots on the same axes with different left and right scales.

## Steps

### Step 1: Import Required Libraries

Before we begin, let's import the required libraries. We will be using Matplotlib and NumPy for this tutorial.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Some Mock Data

Next, we will create some mock data to use for our plots. We will be using `numpy.arange` to create an array of values ranging from 0.01 to 10.0 with a step of 0.01. We will then use `numpy.exp` and `numpy.sin` to create two sets of data.

```python
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```

### Step 3: Create the Plot

Now that we have our data, we can create our plot. We will begin by creating an axes object using `matplotlib.pyplot.subplots()`. We will then plot our first set of data on this axes object and set the label color to red.

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

Next, we will instantiate a second axes object that shares the same x-axis as the first axes object using the `ax1.twinx()` method. We will then plot our second set of data on this new axes object and set the label color to blue.

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

Finally, we will adjust the layout of our plot using the `fig.tight_layout()` method and display it using `matplotlib.pyplot.show()`.

```python
fig.tight_layout()
plt.show()
```

### Step 4: Review the Plot

Take a moment to review the plot that was created. Notice how the two sets of data have different scales on the y-axis. The first set of data is plotted in red and has a scale on the left side of the plot, while the second set of data is plotted in blue and has a scale on the right side of the plot.

## Summary

Congratulations! You have learned how to create plots with different scales in Python using Matplotlib. Specifically, you have learned how to create two plots on the same axes with different left and right scales by using two different axes that share the same x-axis. You can use separate `matplotlib.ticker` formatters and locators as desired since the two axes are independent.
