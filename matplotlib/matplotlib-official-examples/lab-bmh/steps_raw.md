# Python Matplotlib Tutorial

## Introduction

This lab provides a step-by-step guide on how to use Matplotlib to create histograms using the "bmh" style sheet.

## Steps

### Step 1: Import necessary modules

In this step, we import the necessary modules for creating the histograms.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

plt.style.use('bmh')
```

### Step 2: Define the function to plot beta distribution

In this step, we define the function to plot the beta distribution.

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```

### Step 3: Create the plot

In this step, we create the plot by calling the `plot_beta_hist()` function and passing the parameters.

```python
fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_title("'bmh' style sheet")

plt.show()
```

### Summary

In this lab, we learned how to use Matplotlib to create histograms using the "bmh" style sheet. We imported the necessary modules, defined the function to plot the beta distribution, and created the plot by calling the function and passing the parameters.
