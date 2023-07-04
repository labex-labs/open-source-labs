# Matplotlib Tutorial

## Plotting Cumulative Distributions

### Introduction

This tutorial demonstrates how to plot the empirical cumulative distribution function (ECDF) of a sample and the theoretical CDF using Matplotlib. ECDFs are also known as "non-exceedance" curves in engineering, where the y-value for a given x-value gives the probability that an observation from the sample is below that x-value. Conversely, the empirical _complementary_ cumulative distribution function (the ECCDF, or "exceedance" curve) shows the probability y that an observation from the sample is above a value x.

### Steps

#### Import the necessary libraries

In this step, we will import the necessary libraries. We will be using the NumPy and Matplotlib libraries for this tutorial.

```python
import matplotlib.pyplot as plt
import numpy as np
```

#### Set the random seed and generate the data

In this step, we will set the random seed and generate the data. We will generate 100 data points from a normal distribution with a mean of 200 and a standard deviation of 25.

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```

#### Create the figure and subplots

In this step, we will create a figure with two subplots for the cumulative distributions. We will also set the figure size to 9x4.

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```

#### Plot the cumulative distributions

In this step, we will plot the cumulative distributions. We will use the `.ecdf` method to plot the ECDF and the complementary ECDF. We will also plot the theoretical CDF using a normal distribution with a mean of 200 and a standard deviation of 25.

```python
# Cumulative distributions
axs[0].ecdf(data, label="CDF")
n, bins, patches = axs[0].hist(data, 25, density=True, histtype="step",
                               cumulative=True, label="Cumulative histogram")
x = np.linspace(data.min(), data.max())
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (x - mu))**2))
y = y.cumsum()
y /= y[-1]
axs[0].plot(x, y, "k--", linewidth=1.5, label="Theory")

# Complementary cumulative distributions
axs[1].ecdf(data, complementary=True, label="CCDF")
axs[1].hist(data, bins=bins, density=True, histtype="step", cumulative=-1,
            label="Reversed cumulative histogram")
axs[1].plot(x, 1 - y, "k--", linewidth=1.5, label="Theory")
```

#### Label the figure

In this step, we will label the figure. We will add a title, gridlines, and labels for the x and y axes.

```python
fig.suptitle("Cumulative Distributions")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Annual rainfall (mm)")
    ax.set_ylabel("Probability of occurrence")
    ax.label_outer()

plt.show()
```

### Summary

In this tutorial, we learned how to plot the empirical cumulative distribution function (ECDF) and the theoretical CDF using Matplotlib. We also learned how to plot the empirical complementary cumulative distribution function (ECCDF) and the reversed cumulative histogram. By following the steps outlined in this tutorial, you should now be able to create your own cumulative distribution plots using Matplotlib.
