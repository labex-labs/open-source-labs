# Python Matplotlib Tutorial - Customizing Box Plots

## Introduction

In this tutorial, we will learn how to customize box plots in Matplotlib. Box plots are a popular way to visualize the distribution of a dataset. They are also known as box-and-whisker plots and show the median, quartiles, and outliers of the data. We will go through various examples to learn how to customize box plots using Matplotlib.

## Steps

### Step 1: Import Required Libraries

We will start by importing the required libraries, which are Matplotlib and NumPy. We will also set a random seed for NumPy to ensure that our results are reproducible.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
```

### Step 2: Generate Data

We will generate some random data to use in our examples. We will use the NumPy function `random.lognormal()` to generate log-normal data with a mean of 1.5 and a standard deviation of 1.75. We will generate 37 samples of 4 variables, and we will store them in the `data` variable. We will also create a list of labels for each variable.

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```

### Step 3: Default Box Plot

We will start by creating a default box plot to visualize the data. We will use the Matplotlib function `boxplot()` and pass the data and labels as arguments. We will also set the title of the plot using the `set_title()` function.

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```

### Step 4: Remove Individual Components

We can remove individual components of the box plot using the various keyword arguments available in the `boxplot()` function. For example, we can remove the means by setting `showmeans` to False. We can also remove the box and whiskers by setting `showbox` and `showcaps` to False, respectively.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

axs[0, 1].boxplot(data, labels=labels, showmeans=False)
axs[0, 1].set_title('No Means')

axs[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axs[1, 0].set_title('No Box or Whiskers')

axs[1, 1].boxplot(data, labels=labels, showfliers=False)
axs[1, 1].set_title('No Outliers')

plt.show()
```

### Step 5: Customizing Box Plot Styles

We can also customize the styles of the box plot using the various keyword arguments available in the `boxplot()` function. For example, we can change the color and line style of the box by setting `boxprops`. We can also change the style of the median, mean, and mean line by setting `medianprops`, `meanprops`, and `meanlineprops`, respectively.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

boxprops = dict(linestyle='--', linewidth=2, color='red')
axs[0, 1].boxplot(data, labels=labels, boxprops=boxprops)
axs[0, 1].set_title('Custom Box')

medianprops = dict(linestyle='-', linewidth=2, color='blue')
meanprops = dict(marker='D', markeredgecolor='black', markerfacecolor='green')
meanlineprops = dict(linestyle='--', linewidth=2, color='red')
axs[1, 0].boxplot(data, labels=labels, medianprops=medianprops, meanprops=meanprops, meanline=True, meanlineprops=meanlineprops)
axs[1, 0].set_title('Custom Median, Mean, and Mean Line')

flierprops = dict(marker='o', markerfacecolor='red', markersize=8, markeredgecolor='none')
axs[1, 1].boxplot(data, labels=labels, flierprops=flierprops)
axs[1, 1].set_title('Custom Outliers')

plt.show()
```

## Summary

Box plots are a great way to visualize the distribution of a dataset. Matplotlib provides many customization options for box plots, such as removing individual components and customizing the styles of the components. By using these options, we can create box plots that effectively communicate the information we want to convey.
