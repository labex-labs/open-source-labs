# Placing Text Boxes in Matplotlib

## Introduction

In data visualization, it is often necessary to add annotations to plots to provide additional information to the audience. One way to do this is by adding text boxes to a plot. In Matplotlib, it is possible to place text boxes in axes coordinates, so the text doesn't move around with changes in x or y limits. You can also use the `bbox` property of text to surround the text with a `~matplotlib.patches.Patch` instance.

In this lab, we will learn how to place text boxes in Matplotlib using Python.

## Steps

### Step 1: Import necessary libraries

Before we can start adding text boxes to our plots, we need to import the necessary libraries. In this example, we will be using `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create data

For this example, we will create a random dataset using `numpy.random.randn()`.

```python
np.random.seed(19680801)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
```

### Step 3: Create a histogram

Next, we will create a histogram of the data using `matplotlib.pyplot.hist()`.

```python
fig, ax = plt.subplots()
ax.hist(x, 50)
```

### Step 4: Create text for the text box

We will create a string containing the mean, median, and standard deviation of our data.

```python
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))
```

### Step 5: Create the text box properties

We will create a dictionary containing the properties for the text box. In this example, we will use a rounded box with a wheat-colored face and an alpha of 0.5.

```python
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
```

### Step 6: Add the text box to the plot

Finally, we will add the text box to the plot using `matplotlib.pyplot.text()`. We will specify the location of the text box in axes coordinates and use the `bbox` parameter to add the box properties.

```python
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
```

### Step 7: Display the plot

We will display the plot using `matplotlib.pyplot.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to add text boxes to a plot in Matplotlib using Python. We used the `matplotlib.pyplot.text()` function to add the text box and specified the location of the box in axes coordinates. We also used the `bbox` property to add a rounded box around the text and set the box properties using a dictionary. This technique can be used to add annotations to plots and provide additional information to the audience.
