# Step-by-Step Lab: Plotting Histograms with Matplotlib

## Introduction

Matplotlib is a popular data visualization library in Python. One of the most common ways to visualize data distributions is by using histograms. In this lab, we will learn how to create histograms with Matplotlib and explore different customization options.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries, including Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate sample data

Next, we will generate some sample data to use for the histogram. In this example, we will generate three sets of random data.

```python
np.random.seed(19680801)
n_bins = 10
x = np.random.randn(1000, 3)
```

### Step 3: Plot a basic histogram

We can create a basic histogram using the `hist` function in Matplotlib. This function takes in the data we want to plot and the number of bins we want to use.

```python
plt.hist(x, n_bins)
plt.show()
```

### Step 4: Add labels and a title

We can add labels to the x and y axes and a title to the plot using the `xlabel`, `ylabel`, and `title` functions.

```python
plt.hist(x, n_bins)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```

### Step 5: Customize the histogram

We can customize the histogram by changing the color, transparency, and edge color of the bars using the `color`, `alpha`, and `edgecolor` parameters.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```

### Step 6: Plot multiple histograms

We can plot multiple histograms on the same plot by passing in an array of data to the `hist` function.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.legend()
plt.show()
```

### Step 7: Plot stacked histograms

We can plot stacked histograms by setting the `stacked` parameter to `True`.

```python
plt.hist(x, n_bins, color=['green', 'blue', 'red'], alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'], stacked=True)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Stacked Histogram of Random Data')
plt.legend()
plt.show()
```

### Step 8: Plot step histograms

We can plot step histograms by setting the `histtype` parameter to `'step'`.

```python
plt.hist(x, n_bins, histtype='step', color=['green', 'blue', 'red'], label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Step Histogram of Random Data')
plt.legend()
plt.show()
```

## Summary

In this lab, we learned how to create histograms using Matplotlib. We explored different customization options, including changing the color, transparency, and edge color of the bars, plotting multiple histograms on the same plot, stacking histograms, and plotting step histograms. These tools can help us to better understand the distribution of our data.
