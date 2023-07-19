# Python Matplotlib Histogram Tutorial

## Introduction

In this tutorial, we will learn how to create a histogram using Matplotlib library. A histogram is a graphical representation of the distribution of a dataset. It is an estimate of the probability distribution of a continuous variable. To create a histogram, we need to split the entire range of values into a series of intervals or bins, and then count how many values fall into each interval.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries, which are NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate random data

We will generate two sets of random data using NumPy's `random.normal` function. These sets will be used to create histograms with different styles.

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```

### Step 3: Create a basic histogram

We will create a basic histogram using the `hist` function from Matplotlib. This histogram will have 10 equally sized bins.

```python
plt.hist(x, bins=10)
plt.show()
```

### Step 4: Change the number of bins

We can change the number of bins by specifying the `bins` parameter in the `hist` function. In this example, we will create a histogram with 20 bins.

```python
plt.hist(x, bins=20)
plt.show()
```

### Step 5: Change the histogram style

We can change the style of the histogram by specifying the `histtype` parameter in the `hist` function. In this example, we will create a histogram with a step curve that has a color fill.

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```

### Step 6: Create a histogram with custom bin widths

We can create a histogram with custom and unequal bin widths by providing a list of bin edges. In this example, we will create a histogram with unevenly spaced bins.

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```

### Step 7: Create two histograms with stacked bars

We can create two histograms with stacked bars by calling the `hist` function twice and setting the `histtype` parameter to `'barstacked'`. In this example, we will create two histograms with stacked bars.

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```

## Summary

In this tutorial, we learned how to create a histogram using Matplotlib library. We also learned how to change the number of bins, the style of the histogram, and how to create a histogram with custom bin widths and stacked bars.
