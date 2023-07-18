# Density Estimation

## Introduction

In this lab, we will explore density estimation, which is a technique used to estimate the probability density function of a random variable. Specifically, we will focus on kernel density estimation, which is a non-parametric method for estimating the density.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the libraries that we will be using for density estimation. We will use the `KernelDensity` estimator from the `sklearn.neighbors` module, and the `numpy` library for data manipulation.

```python
from sklearn.neighbors import KernelDensity
import numpy as np
```

### Step 2: Generate some sample data

Next, we will generate some sample data to perform density estimation on. For the purpose of this lab, let's generate a 1-dimensional dataset with 100 points. We will use a normal distribution to generate the data.

```python
np.random.seed(0)
X = np.random.normal(0, 1, 100).reshape(-1, 1)
```

### Step 3: Fit a kernel density estimator

Now, we will create an instance of the `KernelDensity` estimator and fit it to our data. We can choose the type of kernel and bandwidth for the estimator. For example, we can use a Gaussian kernel and set the bandwidth to 0.2.

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```

### Step 4: Score the samples

After fitting the estimator, we can use the `score_samples` method to compute the log-likelihood of the samples under the estimated density function. This will give us a measure of how likely each sample is according to the density estimate.

```python
scores = kde.score_samples(X)
```

### Step 5: Visualize the density estimate

Finally, we can visualize the density estimate using a histogram and the estimated density function. We can plot the histogram of the original data as well as the estimated density function.

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogram')
plt.plot(X, np.exp(scores), color='red', label='Kernel Density Estimate')
plt.legend()
plt.show()
```

## Summary

In this lab, we learned how to perform kernel density estimation using the `KernelDensity` estimator from scikit-learn. Kernel density estimation is a powerful technique for estimating the probability density function of a random variable. By fitting a kernel density estimator to a dataset, we can estimate the underlying density and visualize it using a histogram and the estimated density function. This allows us to gain insights into the distribution of the data and make probabilistic predictions.
