# Exploring Normalizations

## Introduction

This lab explores various normalizations on a multivariate normal distribution using Python Matplotlib. In this lab, you will learn about linear normalization, power law normalization, and how to use Matplotlib to visualize the multivariate normal distribution.

## Steps

### Step 1: Import Libraries

In this step, you need to import the necessary libraries which are `Matplotlib`, `NumPy`, and `Multivariate_normal` from `NumPy.random`.

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import multivariate_normal
```

### Step 2: Set Random State

In this step, you need to set the random state for reproducibility.

```python
np.random.seed(19680801)
```

### Step 3: Create Data

In this step, you need to create data using `multivariate_normal()`. This function generates a random sample from a multivariate normal distribution.

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```

### Step 4: Create Histogram

In this step, you need to create a histogram using `hist2d()`. The `hist2d()` function is used to create a two-dimensional histogram.

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100)
```

### Step 5: Create Power Law Normalization

In this step, you need to create power law normalization using `PowerNorm()`.

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```

### Step 6: Create Subplots

In this step, you need to create subplots using `subplots()`.

```python
fig, axs = plt.subplots(nrows=2, ncols=2)
```

### Step 7: Create Linear Normalization

In this step, you need to create linear normalization.

```python
axs[0, 0].hist2d(data[:, 0], data[:, 1], bins=100)
```

### Step 8: Create Power Law Normalization

In this step, you need to create power law normalization with different gamma values.

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```

### Step 9: Set Title

In this step, you need to set the title of each plot.

```python
axs[0, 0].set_title('Linear normalization')

for ax, gamma in zip(axs.flat[1:], gammas):
    ax.set_title(r'Power law $(\gamma=%1.1f)$' % gamma)
```

### Step 10: Tight Layout

In this step, you need to adjust the spacing between subplots.

```python
fig.tight_layout()
```

### Step 11: Show Plot

In this step, you need to display the plot using `show()`.

```python
plt.show()
```

## Summary

This lab explored various normalizations on a multivariate normal distribution using Python Matplotlib. You learned about linear normalization, power law normalization, and how to use Matplotlib to visualize the multivariate normal distribution.
