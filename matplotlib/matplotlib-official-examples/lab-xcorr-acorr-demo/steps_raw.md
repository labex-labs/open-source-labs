# Python Matplotlib Lab

## Cross- and Auto-Correlation

### Introduction

The purpose of this lab is to demonstrate the use of cross-correlation and auto-correlation plots using the Python Matplotlib library. Cross-correlation and auto-correlation are mathematical tools used to measure the similarity between two signals. Cross-correlation measures the similarity between two different signals, while auto-correlation measures the similarity between a signal and a time-delayed version of itself. These tools are commonly used in signal processing, image analysis, and time series analysis.

### Steps

#### Import Libraries

First, we need to import the necessary libraries. In this lab, we will be using NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

#### Generate Random Data

Next, we will generate two arrays of random data using NumPy. We will use these arrays to demonstrate cross-correlation and auto-correlation.

```python
np.random.seed(19680801)
x, y = np.random.randn(2, 100)
```

#### Plot Cross-Correlation

We will now plot the cross-correlation between the two arrays using the `xcorr` function in Matplotlib.

```python
fig, ax = plt.subplots()
ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax.grid(True)
plt.show()
```

The `xcorr` function takes the following parameters:

- `x`: the first array of data
- `y`: the second array of data
- `usevlines`: boolean, whether to plot vertical lines from 0 to the correlation value
- `maxlags`: integer, the maximum number of lags to calculate the correlation for
- `normed`: boolean, whether to normalize the correlation values
- `lw`: integer, the line width for the plot

#### Plot Auto-Correlation

We will now plot the auto-correlation of the `x` array using the `acorr` function in Matplotlib.

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

The `acorr` function takes the following parameters:

- `x`: the array of data to calculate the auto-correlation for
- `usevlines`: boolean, whether to plot vertical lines from 0 to the correlation value
- `normed`: boolean, whether to normalize the correlation values
- `maxlags`: integer, the maximum number of lags to calculate the correlation for
- `lw`: integer, the line width for the plot

### Summary

In this lab, we learned how to use cross-correlation and auto-correlation plots in Python Matplotlib. We first imported the necessary libraries, then generated random data using NumPy. We then plotted the cross-correlation and auto-correlation of the data using the `xcorr` and `acorr` functions in Matplotlib. These tools are useful for measuring the similarity between two signals and are commonly used in signal processing, image analysis, and time series analysis.
