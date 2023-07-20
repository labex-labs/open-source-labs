# Step-by-Step Lab: Python Matplotlib Tutorial

## Introduction

This lab is a step-by-step tutorial on how to use Python Matplotlib library to create a histogram. A histogram is a graphical representation of the distribution of numerical data. It is an estimate of the probability distribution of a continuous variable.

## Steps

### Step 1: Import necessary libraries

In this step, we will import two libraries: numpy and matplotlib. Numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices. Matplotlib is a plotting library for the Python programming language.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Generate sample data

In this step, we will generate sample data using numpy. We will generate random data from a normal distribution with a mean of 100 and standard deviation of 15.

```python
np.random.seed(19680801)
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)
```

### Step 3: Create a histogram

In this step, we will create a histogram using matplotlib. We will set the number of bins to 50 and enable the density parameter to normalize bin heights so that the integral of the histogram is 1.

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```

### Step 4: Add a best fit line

In this step, we will add a best fit line to the histogram. We will calculate the y-values for the line and plot it on top of the histogram.

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```

### Step 5: Customize the histogram

In this step, we will customize the histogram by adding labels, title, and adjusting the layout.

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```

## Summary

In this lab, we learned how to use Python Matplotlib library to create a histogram. We generated sample data from a normal distribution and created a histogram using matplotlib. We also added a best fit line and customized the histogram by adding labels and a title.
