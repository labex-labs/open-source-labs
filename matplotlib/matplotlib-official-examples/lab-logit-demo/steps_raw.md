# Matplotlib Logit Scale Plotting Lab

## Introduction

In this lab, we will learn how to create plots with logit axes in Matplotlib. Logit axes are commonly used in probability plots to represent the cumulative distribution function (CDF) of a distribution. We will use the `math`, `numpy`, and `matplotlib.pyplot` libraries for this lab.

## Steps

### Step 1: Import the necessary libraries and set up the data

We will import the `math`, `numpy`, and `matplotlib.pyplot` libraries and set up the data for the plots.

```python
import math
import numpy as np
import matplotlib.pyplot as plt

xmax = 10
x = np.linspace(-xmax, xmax, 10000)
cdf_norm = [math.erf(w / np.sqrt(2)) / 2 + 1 / 2 for w in x]
cdf_laplacian = np.where(x < 0, 1 / 2 * np.exp(x), 1 - 1 / 2 * np.exp(-x))
cdf_cauchy = np.arctan(x) / np.pi + 1 / 2
```

### Step 2: Create a plot with logit scale and standard notation

We will create a plot with logit scale and standard notation. This can be done by setting the y-axis scale to logit using `set_yscale("logit")` and setting the y-axis limits using `set_ylim()`. We will also plot the cumulative distribution functions for the normal, Laplacian, and Cauchy distributions using `plot()` and add a legend using `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit")
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```

### Step 3: Create a plot with logit scale and survival notation

We will create a plot with logit scale and survival notation. This can be done by setting the y-axis scale to logit and setting the `one_half` parameter to `"1/2"` and `use_overline` parameter to `True` using `set_yscale("logit", one_half="1/2", use_overline=True)"`. We will also plot the cumulative distribution functions for the normal, Laplacian, and Cauchy distributions using `plot()` and add a legend using `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit", one_half="1/2", use_overline=True)
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```

### Step 4: Create a plot with linear scale

We will create a plot with linear scale. This can be done by simply plotting the cumulative distribution functions for the normal, Laplacian, and Cauchy distributions using `plot()` and add a legend using `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```

## Summary

In this lab, we learned how to create plots with logit axes in Matplotlib. We created plots with logit scale and standard notation, logit scale and survival notation, and linear scale. We used the `math`, `numpy`, and `matplotlib.pyplot` libraries for this lab.
