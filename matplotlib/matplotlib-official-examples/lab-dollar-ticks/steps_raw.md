# Using Matplotlib to Add Dollar Signs to Y-Axis Labels

## Introduction

In this lab, we will learn how to use Matplotlib to format the y-axis labels of a plot to display dollar signs. This is particularly useful when working with financial data or any data that requires currency formatting.

## Steps

### Step 1: Import Necessary Libraries

First, we need to import the necessary libraries. We will be using `matplotlib.pyplot` to create our plot and format the y-axis labels.

```python
import matplotlib.pyplot as plt
```

### Step 2: Create the Plot

Next, let's create a simple plot to work with. We will use NumPy to generate some random data to plot.

```python
import numpy as np

# Generate random data
np.random.seed(19680801)
data = 100 * np.random.rand(20)

# Create the plot
fig, ax = plt.subplots()
ax.plot(data)
```

### Step 3: Format Y-Axis Labels with Dollar Signs

Now, let's format the y-axis labels to display dollar signs. We will use the `StrMethodFormatter` class from the `matplotlib.ticker` module to format the labels.

```python
import matplotlib.ticker as ticker

# Format y-axis labels with dollar signs
fmt = '${x:,.2f}'
tick = ticker.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
```

In the above code, we create a `StrMethodFormatter` object with the format string `'$ {x:,.2f}'`. This format string specifies that we want a dollar sign followed by a space, followed by a comma-separated number with two decimal places.

Next, we create a `Tick` object using the `StrMethodFormatter` object we just created. Finally, we set the y-axis major formatter to the `Tick` object.

### Step 4: Customize Tick Parameters

We can also customize the tick parameters to further adjust the appearance of our plot. In this example, we will change the color of the tick labels to green and move them to the right side of the plot.

```python
# Customize tick parameters
ax.tick_params(axis='y', which='major', labelcolor='green', labelright=True)
```

In the above code, we use the `tick_params` method to customize the y-axis tick parameters. We set the `axis` parameter to `'y'` to specify that we are customizing the y-axis, and the `which` parameter to `'major'` to specify that we are customizing the major ticks. We set the `labelcolor` parameter to `'green'` to change the color of the tick labels, and the `labelright` parameter to `True` to move the tick labels to the right side of the plot.

### Step 5: Display the Plot

Finally, we can display our plot using the `show` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to use Matplotlib to format y-axis labels with dollar signs. We used the `StrMethodFormatter` class from the `matplotlib.ticker` module to format the labels, and customized the tick parameters to further adjust the appearance of our plot.
